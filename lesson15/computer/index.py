import paho.mqtt.client as mqtt
from datetime import datetime
import os, csv

#def record(r:list[str, str, int]):
def record(date:str, topic:str, value:int | float):
    '''
    # 檢查是否有data資料夾,沒有就建立data資料夾
    # 取得今天日期,並建立今天日期的csv檔
    # 將參數r的資料,儲存進入csv檔案內
    # parameters r:list -> 是list[日期字串, topic, 值]
    # parameters date:str->這是日期及時間
    # parameters topic:str->這是訂閱的topic
    # parameters value:int->這是訂閱的值 
    
    '''
    #os.path.realpath(__file__)
    root_dir = os.getcwd()
    data_dir = os.path.join(root_dir, 'data')
    #沒有目錄建立目錄
    if not os.path.isdir(data_dir):
        os.mkdir('data')

    
    # today = datetime.today()
    # filename = today.strftime('%Y-%m-%d') + '.csv'
    filename = date[0:10] + '.csv'
    #get_file_abspath
    full_path = os.path.join(data_dir, filename)
    #沒有這個檔,要建立檔案
    if not os.path.exists(full_path):
        with open(full_path, mode='w', newline='', encoding='utf-8') as file:
            file.write('時間,設備,值\n')

    with open(full_path, mode='a', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, topic, value])
def on_connect(client, userdata, flags, reason_code, properties):
    #連線bloker成功時,只會執行一次
    client.subscribe("SA-56/#")

def on_message(client, userdata, msg):
    global led_origin_value#變更為全域變數
    global temperature_origin_value
    topic = msg.topic
    value = msg.payload.decode()
    #print(f"Received message '{msg.payload.decode()}' on topic '{msg.topic}'")
    today = datetime.now()
    now_str = today.strftime('%Y-%m-%d %H:%M:%S')
    if topic =='SA-56/LED_LEVEL':
        led_value = int(value)
        if led_value != led_origin_value:
            led_origin_value = led_value
            print(f'led_value:{led_value}')
            
            #save_data = [now_str, 'SA-56/LED_LEVEL', led_value]
            record(now_str, topic, led_value)

    if topic == 'SA-56/TEMPERATURE':
        temperature_value = float(value)
        if temperature_value != temperature_origin_value:
            temperature_value = value
            print(f'溫度:{value}')
            record(now_str, topic, temperature_value)
    

def main():
    client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
    # 設定用戶名和密碼
    username = "pi"  # 替換為您的用戶名
    password = "raspberry"  # 替換為您的密碼
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.on_message = on_message 
    client.connect("192.168.0.252", 1883, 60)
    client.loop_forever()


if __name__ == "__main__":

    led_origin_value = 0
    temperature_origin_value = 0.0
    main()