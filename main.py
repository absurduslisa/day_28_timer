from tkinter import *
import time
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    marks = ''
    check_mark.config(text=marks)
    reps = 0
    title.config(text='Timer', fg=GREEN)



# ---------------------------- TIMER MECHANISM ------------------------------- # 


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def down_count_timer(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    count_text = f'{count_min}:{count_sec}'
    if count_sec < 10:
        count_text = f'{count_min}:0{count_sec}'
    print(count_text)
    canvas.itemconfig(timer_text, text=count_text)
    if count > 0:
        global timer
        timer = window.after(1000, down_count_timer, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            marks = ''
            work_sessions = math.floor(reps/2)
            for i in range(0, work_sessions):
                marks += '✔'
            check_mark.config(text=marks)



def start_timer():

    global reps
    print(reps)
    reps += 1
    work_sec = WORK_MIN * 60 #25*6 = 150
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_min = LONG_BREAK_MIN * 60
    if reps % 2 == 1:
        # timer = work_sec
        timer_amount = 10
        title.config(text='Work', fg=RED)
    elif reps % 8 == 0:
        # timer = long_break_min
        timer_amount = 15
        title.config(text='Break', fg=GREEN)
    elif reps % 2 == 0:
        # timer = short_break_sec
        timer_amount = 8
        title.config(text='Break', fg=PINK)
    # button_start.config(text='Stop')
    down_count_timer(timer_amount)


# for i in range(0, 5):
#     start_timer()
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

title = Label(text='Timer', font=(FONT_NAME, 50, 'normal'), fg=GREEN, background=YELLOW)
title.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)
tomato_png = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_png)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)
# down_count_timer(timer)

button_start = Button(text='Start', highlightthickness=0, width=6, command=start_timer)
button_start.grid(column=0, row=2)

button_reset = Button(text='Reset', highlightthickness=0, width=6, command=reset_timer)
button_reset.grid(column=2, row=2)

check_mark = Label(background=YELLOW, fg=GREEN)
check_mark.grid(column=1, row=3)

window.mainloop()


# timer
