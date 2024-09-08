# 20240907 homework BMI計算

height_cm = float(input("請輸入身高(公分):"))
weight_kg = float(input("請輸入體重(公斤):"))

height_m = round(height_cm/100, 2)

bmi_kg_m2 = round(weight_kg/(height_m**2), 2)

if bmi_kg_m2 >= 35 :
    print(f"您的BMI值是{bmi_kg_m2}\n您的體重重度肥胖")
elif bmi_kg_m2 >= 30 :
    print(f"您的BMI值是{bmi_kg_m2}\n您的體重中度肥胖")
elif bmi_kg_m2 >= 27 :
    print(f"您的BMI值是{bmi_kg_m2}\n您的體重輕度肥胖") 
elif bmi_kg_m2 >= 24 :
    print(f"您的BMI值是{bmi_kg_m2}\n您的體重過重")
elif bmi_kg_m2 >= 18.5 :
    print(f"您的BMI值是{bmi_kg_m2}\n您的體重正常範圍")
else :
    print(f"您的BMI值是{bmi_kg_m2}\n您的體重過輕") 
    