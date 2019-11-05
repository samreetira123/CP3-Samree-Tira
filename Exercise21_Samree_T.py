from  tkinter import  *

def leftClick (event):
    Result = float(textBoxWeight.get()) / ((float(textBoxHeight.get()) / 100) ** 2)
    if Result >=30.0 :
        labelResult.configure(text = "คุณอ้วนมาก",font = 20,fg = "red")
    elif Result >=25.0 and Result <=29.9 :
        labelResult.configure(text = "คุณอ้วน",font = 20,fg = "Orange")
    elif Result >=23.0 and Result <=24.9 :
        labelResult.configure(text = "คุณน้ำหนักเกิน",font = 20,fg = "yellow")
    elif Result >=18.6 and Result <=22.9 :
        labelResult.configure(text = "คุณน้ำหนักปกติเหมาะสม",font = 20,fg = "green")
    else :
        labelResult.configure(text="คุณผอมเกินไป",font = 20,fg = "red")


mainWindows = Tk()
labelHeight = Label(mainWindows,text = "ส่วนสูง(เซนติเมตร)",font = 30)
labelHeight.grid(row=0,column=0)
textBoxHeight = Entry(mainWindows)
textBoxHeight.grid(row=0,column=1)
labelWeight = Label(mainWindows,text = "น้ำหนัก(กิโลกรัม)",font = 30)
labelWeight.grid(row=1,column=0)
textBoxWeight = Entry(mainWindows)
textBoxWeight.grid(row=1,column=1)
calculateButton = Button(mainWindows,text = "คำนวณ",font = 30)
calculateButton.bind('<Button-1>',leftClick)
calculateButton.grid(row =2,column = 0)
labelResult = Label(mainWindows,text = "ผลลัพธ์",font = 30)
labelResult.grid(row=2,column=1)
mainWindows.mainloop()