from datetime import datetime


def calculate_age(birthday):
    today = datetime.today()
    age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
    return age


# 使用範例
birthday_str = input("請輸入出生日期 (格式為 yyyy/mm/dd): ")
birthday = datetime.strptime(birthday_str, '%Y/%m/%d')
age = calculate_age(birthday)
print("你的年齡為:", age)
