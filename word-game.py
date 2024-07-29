from tkinter import *
from random import *
from tkinter import messagebox
import time
ACCOUNTING_WORD = ['BTDE', 'RECITD', 'DTIAU', 'SOLO', 'FITROP',
'OCKTS', 'ISRK', 'XTA', 'ALABECN', 'CEIMNO', 'SSAET', 'AREHS', 'HACS',
'DEGTUB', 'UIYTEQ', 'EERCTPI', 'AASLRY', 'MENTDASTJU', 'LLYOPAR',
'TIGNSOP']
ACCOUNTING_ANSWER = ['DEBT', 'CREDIT', 'AUDIT', 'LOSS', 'PROFIT',
'STOCK', 'RISK', 'TAX', 'BALANCE', 'INCOME', 'ASSET','SHARE', 'CASH',
'BUDGET', 'EQUITY', 'RECEIPT', 'SALARY', 'ADJUSTMENT', 'PAYROLL',
'POSTING' ]
ran_num = randrange(0, ( len (ACCOUNTING_WORD)))
jumbled_rand_word = ACCOUNTING_WORD [ran_num]
points = 0

def main():

    def back():
        my_window.withdraw()

    def change():
        global ran_num
        ran_num = randrange(0, (len(ACCOUNTING_WORD)))
        word.configure(text=ACCOUNTING_WORD[ran_num])
        get_input.delete(0, END)
        ans_lab.configure(text="")

    def cheak():
        global points, ran_num
        user_word = get_input.get().upper()
        if user_word == ACCOUNTING_ANSWER[ran_num]:
            points += 5
            score.configure(text="Score:- " + str(points))
            messagebox.showinfo('correct',"Correct Answer.. Keep it Up!")
            ran_num = randrange(0, (len(ACCOUNTING_WORD)))
            word.configure(text=ACCOUNTING_WORD[ran_num])
            get_input.delete(0, END)
            ans_lab.configure(text="")
        else:
            messagebox.showerror("Error", "Inorrect Answer..Try your best!")
            get_input.delete(0, END)

    def show_answer():
        global points
        if points > 4:
            points -= 5
            score.configure(text="Score:- " + str(points))
            time.sleep(0.5)
            ans_lab.configure(text=ACCOUNTING_ANSWER[ran_num])
        else:
            ans_lab.configure(text='Not enough points')
            my_window = Tk()
            my_window.geometry("500x550+500+150")
            my_window.configure(background="LightBlue3")
            f=('Times New Roman',15,'bold')
            f1 = ('Courier',50,'italic')
            score =Label(my_window,text="Score:0",pady=10,bg="LightBlue3",fg="#000000",font=('Courier',30,'italic'))
            score.pack(anchor='n')
            word=Label(my_window,text=jumbled_rand_word,pady=10,bg="LightBlue3",fg="#000000",font=f1)
            word.pack()
            get_input = Entry(my_window,font="none 26 bold",borderwidth=10,justify='center')
            get_input.pack()
            submit=Button(my_window,text="Submit",width=18,borderwidth=8,font=f,fg="lavender",bg="blue4",command=cheak)
            submit.pack(pady=(10,20))
            change = Button(my_window,text="ChangeWord",width=18,borderwidth=8,fg="lavender",bg="blue4",font=f,command=change)

