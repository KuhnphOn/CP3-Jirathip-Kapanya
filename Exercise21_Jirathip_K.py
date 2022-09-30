from tkinter import *


def bmiResult(bmi):
    if bmi <= 18.5:
        {labelResult.configure(text="ผอมเกินไป",font="Leelawadee")}
    elif bmi >= 18.6 and bmi <= 22.9:
        {labelResult.configure(text="น้ำหนักปกติ เหมาะสม",font="Leelawadee")}
    elif bmi > 23 and bmi <= 24.9:
        {labelResult.configure(text="น้ำหนักเกิน",font="Leelawadee")}
    elif bmi >= 25 and bmi <=29.9:
        {labelResult.configure(text="อ้วน",font="Leelawadee")}
    elif bmi > 30:
        {labelResult.configure(text="อ้วนมาก",font="Leelawadee")}
    else:
        {labelResult.configure(text="Error, Please try again")}


def bmiCalc(event):
    try:
        h = float(textBoxH.get())
        w = float(textBoxW.get())
        bmi = w/((h/100)**2)
    except:
        h = "null"
        w = "null"
        bmi = 0
    print("Height:", h, "cm")
    print("Weight:", w, "kg")
    print("BMI:", bmi, "\n")
    bmiResult(bmi)


main = Tk()
labelHeight = Label(main, text="ส่วนสูง (cm.)",
                    font=("Niramit")).grid(row=0, column=0)
textBoxH = Entry(main)
textBoxH.grid(row=0, column=1)

labelWeight = Label(main, text="น้ำหนัก (kg.)",
                    font=("Niramit")).grid(row=1, column=0)
textBoxW = Entry(main)
textBoxW.grid(row=1, column=1)

calculateButton = Button(main, text="คำนวณ", font=("Niramit", 36))
calculateButton.bind('<Button-1>', bmiCalc)
calculateButton.grid(row=2, column=0)

labelResult = Label(main, text="BMI:")
labelResult.grid(row=2, column=1)

main.mainloop()
