from tkinter import *
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
    global reps
    reps = 0
    check_marks.config(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 27, "bold"))
    label.config(text="Timer", fg=GREEN)
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text=f"00:00")
# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    #count_down(5 * 60)
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    reps += 1
    #if reps % 2 == 1:
    if reps % 8 == 0:
        count_down(long_break_sec)
        print(20)
        label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label.config(text="Break", fg=PINK)
        print(5)
    else:
        count_down(work_sec)
        label.config(text="Work", fg=GREEN)
    print(reps)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
import time
def count_down(thing):
    global timer
    global mark

    count_min = math.floor(thing / 60)
    count_sec = thing % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}") ####################
    if thing > 0:
        timer = window.after(1000, count_down, thing - 1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(reps / 2)):
            mark += "✓"
        check_marks.config(text=mark, fg=GREEN, bg=YELLOW, font=(FONT_NAME, 27, "bold"))


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
#window.minsize(width=300, height=200)
window.config(padx=100,pady=50, bg=YELLOW) #background is standard attribute widget


label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN)
label.grid(column=1, row=0)

#CHECK MARK
check_marks = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 27, "bold"))
check_marks.grid(column=1, row=3)

#text="✓"

#PHOTO AND TEXT
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img) #x and y position
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 27, "bold"))
canvas.grid(column=1, row=1)


#BUTTONS
stbutton = Button(text="Start", command=start_timer)
stbutton.grid(column=0, row=2)


rstbutton = Button(text="Reset", command=reset_timer)
rstbutton.grid(column=2, row=2)


#TIMER = LABEL fg=GREEN
#fg = FOREGROUND
#background


window.mainloop()