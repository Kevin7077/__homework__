import tkinter as tk
from datetime import datetime


def calculate_bmi():
    # Get input values
    name = name_entry.get()
    birthdate_str = birthdate_entry.get()
    height_str = height_entry.get()
    weight_str = weight_entry.get()

    # Validate inputs
    if not name:
        result_text.set("姓名不能為空")
        return
    try:
        birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
    except ValueError:
        result_text.set("出生年月日格式不正確（應為YYYY-MM-DD）")
        return
    try:
        height = float(height_str)
    except ValueError:
        result_text.set("身高格式不正確（應為數字）")
        return
    try:
        weight = float(weight_str)
    except ValueError:
        result_text.set("體重格式不正確（應為數字）")
        return

    # Calculate BMI
    height_m = height / 100
    bmi = weight / (height_m ** 2)
    bmi = round(bmi, 1)

    # Set result text
    result_text.set(f"{name}的BMI是{bmi:.1f}")


root = tk.Tk()
root.title("BMI 計算器")

frame1 = tk.Frame(root)
frame1.pack(side=tk.TOP, pady=10)
name_label = tk.Label(frame1, text="姓名：")
name_label.pack(side=tk.LEFT, padx=10)
name_entry = tk.Entry(frame1)
name_entry.pack(side=tk.LEFT)

frame2 = tk.Frame(root)
frame2.pack(side=tk.TOP, pady=10)
birthdate_label = tk.Label(frame2, text="出生年月日（YYYY-MM-DD）：")
birthdate_label.pack(side=tk.LEFT, padx=10)
birthdate_entry = tk.Entry(frame2)
birthdate_entry.pack(side=tk.LEFT)

frame3 = tk.Frame(root)
frame3.pack(side=tk.TOP, pady=10)
height_label = tk.Label(frame3, text="身高（cm）：")
height_label.pack(side=tk.LEFT, padx=10)
height_entry = tk.Entry(frame3)
height_entry.pack(side=tk.LEFT)
weight_label = tk.Label(frame3, text="體重（kg）：")
weight_label.pack(side=tk.LEFT, padx=10)
weight_entry = tk.Entry(frame3)
weight_entry.pack(side=tk.LEFT)

frame4 = tk.Frame(root)
frame4.pack(side=tk.TOP, pady=10)
result_text = tk.StringVar()
result_label = tk.Label(frame4, textvariable=result_text)
result_label.pack()

frame5 = tk.Frame(root)
frame5.pack(side=tk.TOP, pady=10)
calculate_button = tk.Button(frame5, text="計算BMI", command=calculate_bmi)
calculate_button.pack()

root.mainloop()
