import tkinter as tk
from tkinter import messagebox as msg
import re
import datetime


class BMICalculatorGUI:

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.win = tk.Tk()

        self.lab0 = tk.Label(self.win, text="BMI", font=12)
        self.lab0.grid(row=0, columnspan=2, padx=10, pady=10)

        self.lab1 = tk.Label(self.win, text="姓名", font=12)
        self.lab1.grid(row=1, column=0, padx=10, pady=10)
        self.lab2 = tk.Label(self.win, text="出生年月日\nYYYY-MM-DD", font=12)
        self.lab2.grid(row=2, column=0, padx=10, pady=10)

        self.lab3 = tk.Label(self.win, text="身高(cm)", font=12)
        self.lab3.grid(row=3, column=0, padx=10, pady=10)
        self.lab4 = tk.Label(self.win, text="體重(kg)", font=12)
        self.lab4.grid(row=4, column=0, padx=10, pady=10)

        self.nam = tk.StringVar()
        self.bir = tk.StringVar()

        self.ent1 = tk.Entry(self.win, textvariable=self.nam)
        self.ent1.grid(row=1, column=1, padx=10, pady=10)
        self.ent2 = tk.Entry(self.win, textvariable=self.bir)
        self.ent2.grid(row=2, column=1, padx=10, pady=10)

        self.hei = tk.DoubleVar()
        self.wei = tk.DoubleVar()

        self.ent3 = tk.Entry(self.win, textvariable=self.hei)
        self.ent3.delete(0, tk.END)
        self.ent3.grid(row=3, column=1, padx=10, pady=10)
        self.ent4 = tk.Entry(self.win, textvariable=self.wei)
        self.ent4.delete(0, tk.END)
        self.ent4.grid(row=4, column=1, padx=10, pady=10)

        self.res = tk.StringVar()

        def calBMI():
            try:
                dateReg = re.compile(r"^\d\d\d\d-\d\d-\d\d$")
                inp_bir_str = self.bir.get()
                if dateReg.match(inp_bir_str) is None:
                    raise Exception
                cur_date = datetime.date.today()
                bir_date = datetime.date(int(inp_bir_str[0:4]), int(
                    inp_bir_str[5:7]), int(inp_bir_str[8:]))
                diff = datetime.date(1, 1, 1) + (cur_date - bir_date)
                diff = diff.isoformat()

                bmi = self.wei.get()/(self.hei.get()/100)

                self.tex6.configure(state=tk.NORMAL)
                self.tex6.delete('1.0', tk.END)
                self.tex6.insert(tk.END, f"{self.nam.get()} 您好\n")
                self.tex6.insert(
                    tk.END, f"您的年齡: {int(diff[0:4])-1}年{int(diff[5:7])-1}月{int(diff[8:])-1}日\n")
                self.tex6.insert(tk.END, f"您的 BMI: {round(bmi, 2)}\n")
                self.tex6.insert(tk.END, f"參考訊息: {self.bmiInfo(bmi)}")
                self.tex6.configure(state=tk.DISABLED)
            except:
                self.ent1.delete(0, tk.END)
                self.ent2.delete(0, tk.END)
                self.ent3.delete(0, tk.END)
                self.ent4.delete(0, tk.END)
                self.tex6.configure(state=tk.NORMAL)
                self.tex6.delete('1.0', tk.END)
                self.tex6.configure(state=tk.DISABLED)
                msg.showerror("輸入錯誤", "輸入錯誤")

        self.btn0 = tk.Button(self.win, text="計算", command=calBMI, font=12)
        self.btn0.grid(row=5, column=0, padx=5, pady=5)

        def clear():
            self.ent1.delete(0, tk.END)
            self.ent2.delete(0, tk.END)
            self.ent3.delete(0, tk.END)
            self.ent4.delete(0, tk.END)
            self.tex6.configure(state=tk.NORMAL)
            self.tex6.delete('1.0', tk.END)
            self.tex6.configure(state=tk.DISABLED)

        self.btn1 = tk.Button(self.win, text="清除", command=clear, font=12)
        self.btn1.grid(row=5, column=1, padx=5, pady=5)

        self.tex6 = tk.Text(self.win, height=5, width=35, font=12)
        self.tex6.insert(tk.END, "歡迎使用")
        self.tex6.configure(state=tk.DISABLED)
        self.tex6.grid(row=6, columnspan=2, padx=5, pady=5)

    def mainloop(self):
        self.win.mainloop()

    def bmiInfo(self, bmi):
        if bmi < 18.5:
            return "「體重過輕」，需要多運動，均衡飲食，以增加體能，維持健康！"
        if 18.5 <= bmi < 24:
            return "恭喜！「健康體重」，要繼續保持！"
        if 24 <= bmi < 27:
            return "「體重過重」了，要小心囉，趕快力行「健康體重管理」！"
        if 27 <= bmi:
            return "啊～「肥胖」，需要立刻力行「健康體重管理」囉！"


def main() -> None:
    bmical = BMICalculatorGUI()
    bmical.win.resizable(width=False, height=False)
    bmical.mainloop()


if __name__ == "__main__":
    main()
