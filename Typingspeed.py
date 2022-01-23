from tkinter import *
import random
import time
from pygame import mixer
import tkinter.messagebox as tkmsg
import threading


screen = Tk()
screen.title('TypingSpeed - by Aditya')
screen.geometry("500x600")

mixer.init()

words = ['Daenerys', "Jon", 'snow', 'Arya', 'Stark', "Tyrion", 'Lannister', 'Sansa', 'Khal', 'Drogo', 'Eddard', 'Ned',
         'Cersie', 'Clegane', 'Ramsay', 'Bolton', 'Joffrey', 'baratheon', 'Theon', 'Greyjoy', 'Robb', 'stark', 'Bran',
         'Daario', 'naharis', 'Malisandre', 'Tarth', 'Shae', 'Missandei', 'Oberyn', 'Martell', 'Tormund', 'Petyr',
         'Jamie', 'Margaery', 'Bronn', 'Jorah', 'Mormont', 'Varys', 'Hodor', 'Tommen', 'Samwell', 'Tarly', 'Gilly',
         'Gendry', 'Stannis', 'Rickon', 'jaqen', 'Jojen', 'Tywin', 'Robert', 'Roose', 'Walder', 'Frey', 'Grey', 'Worm',
         'Osha', 'Loras', 'High', 'Sparrow']


count = 0


def retry():
    global a
    global count
    global error
    global time_left
    global i
    global suggested_word
    global value

    time_left.set("60")
    a = 60
    count = 0
    error = 0
    i = 0
    suggested_word.set("Aditya")
    value.set("0")
    screen2.destroy()


def over():
    global screen2
    screen2 = Toplevel(screen)
    screen2.geometry("500x600")
    screen2.title("Results")
    screen2.config(bg = 'cyan', borderwidth = 5, relief = GROOVE)

    global count
    global error


    result_val = f"{count} words per minute"
    calculation = round(((count - error)*100)/count)
    accuracy_val = f"Accuracy = {calculation} %"

    result = StringVar()
    result.set(result_val)

    if count <= 30:

        Label(screen2, textvariable = result, font = "calibri 20 bold", pady = 20, fg = 'red', bg = "cyan").pack()
        Label(screen2, text="Need much work on speed :(", fg='red', font="calibri 15 bold", pady=20,
              bg="cyan").pack()

    elif 30 <= count <= 60:
        Label(screen2, textvariable=result, font="calibri 20 bold", pady=20, fg='orange', bg = "cyan").pack()
        Label(screen2, text="Good Speed :|", fg='orange', font="calibri 15 bold", pady=20,
              bg="cyan").pack()

    else:
        Label(screen2, textvariable=result, font="calibri 20 bold", pady=20, fg='green', bg = "cyan").pack()
        Label(screen2, text="God Level Speed :)", fg='green', font="calibri 15 bold", pady=20,
              bg="cyan").pack()

    accuracy = StringVar()
    accuracy.set(accuracy_val)

    if calculation >= 90:
        Label(screen2, text = "Welldone Buddy... Good Accuracy", fg = 'green', font = "calibri 15 bold", pady = 20, bg = "cyan").pack()
        Label(screen2, textvariable=accuracy, font="calibri 20 bold", fg = "green", pady = 20, bg = "cyan").pack()

    elif 50 <= calculation <= 90:
        Label(screen2, text="Good Work... Intermediate Accuracy", fg='orange', font="calibri 15 bold", pady=20, bg = "cyan").pack()
        Label(screen2, textvariable=accuracy, font="calibri 20 bold", fg="orange", pady=20, bg = "cyan").pack()

    else:
        Label(screen2, text="Need More Work... Poor Accuracy", fg='red', font="calibri 15 bold", pady=20, bg = "cyan").pack()
        Label(screen2, textvariable=accuracy, font="calibri 20 bold", fg="red", pady=20, bg = "cyan").pack()

    Button(screen2, text="Retry", bg="green", fg="white", font="calibri 18 bold", command = retry).pack(pady=20)

    Button(screen2, text="Exit", command=quit, bg="red", fg="white", font="calibri 18 bold", padx = 10).pack(pady=20)
    screen2.wm_iconbitmap('logo.ico')

a = 60


def playmusic():
    mixer.music.load('bgm.mp3')
    mixer.music.play()


def timer():
    global a
    global count
    global error
    global time_left
    global i
    global suggested_word
    global value
    global show_time

    time_left.set("60")
    a = 60
    count = 0
    error = 0
    i = 0
    suggested_word.set("Aditya")
    value.set("0")
    if a == 60:
        while a >= 1:
            time.sleep(1)
            a -= 1
            time_left.set(a)
            show_time = Label(screen, textvariable=time_left, font="calibri 10 bold", fg='red', bg = "cyan").update()
            if a == 0:

                over()

            else:
                pass
            if a == 15:
                t2 = threading.Thread(target=playmusic)
                t2.start()

            else:
                pass


    else:
        pass


def pretimer(event):
    t1 = threading.Thread(target=timer)
    t1.start()


error = 0

i = 0
def compare(event):
    global suggested_word
    global typed_word
    global space
    global words
    global value
    global count
    global error
    global i
    global warning_msg
    global warning

    count += 1
    typed = typed_word.get()
    suggested = suggested_word.get()
    suggested_word.set(random.choice(words))
    if typed == suggested:
        i += 1
        value.set(i)
        score_value = Label(screen, textvariable=value, font="calibri 10 bold", pady=20, fg = 'blue', bg = "cyan").update()
        warning_msg.set("Got it 😊")
        warning = Label(screen, textvariable = warning_msg, font="calibri 10 bold", pady=20, fg='green', bg = "cyan").update()

    else:
        error +=1
        warning_msg.set("Missed ☹")
        # warning = Label(screen, textvaiable = warning_msg, font="calibri 10 bold", pady=20, fg='red', bg = "cyan").update()

    space.delete(0, END)

def help1():
    tkmsg.showinfo("Help Center", 'This application is a fun purpose game which is very useful to determine and enhance '
                                  'your typing skills. You can practice typing with huge number of character names of '
                                  'Game of Thrones tv show. To start the Stopwatch drag your cursor to typing area,'
                                  ' timer will automatically start to test typing speed in WPM.    Thankyou...')

def abt():
    tkmsg.showinfo("About Us", "TypingSpeed is developed by Aditya Yadav")

menubar = Menu(screen)
helpmenu = Menu(menubar)
helpmenu.add_command(label = 'Help', command = help1)
helpmenu.add_command(label = 'About Us', command = abt)

menubar.add_cascade(label = 'Help', menu = helpmenu)
screen.config(menu = menubar)


Label(screen, text = "Wellcome, Test your typing speed here", fg = 'green', font = "calibri 20 bold", pady = 20, bg = "cyan").pack()
Label(screen, text = "*Hover on typing space to start stopwatch", fg = 'darkred', font = "calibri 10 bold", pady = 4, bg = "cyan").pack()


Label(screen, text = "Time Left", font = "calibri 15 bold", fg = "red", pady = 20, bg = "cyan").pack()

time_left = StringVar()
time_left.set("60")
show_time = Label(screen, textvariable = time_left, font = "calibri 25 bold", fg = 'red', bg = "cyan").pack()


suggested_word = StringVar()
suggested_word.set("Aditya")

Label(screen, textvariable = suggested_word, font = "calibri 15 bold", pady = 20, bg = "cyan").pack()

typed_word = StringVar()

Label(screen, text = "Enter given word here", font = "calibri 15 bold", fg = "blue", pady = 5, bg = "cyan").pack()

space = Entry(screen, font = "calibri 30 ", textvariable = typed_word, justify = "center")
space.pack(pady = 20)
space.focus_set()
space.bind("<Return>", compare)

value = StringVar()
value.set("0")

Label(screen, text = "Your Score", font = "calibri 15 bold", fg = "maroon", pady = 20, bg = "cyan").pack()

score_value = Label(screen, textvariable=value, font="calibri 10 bold", pady=20, bg = "cyan").pack()

warning_msg = StringVar()
warning_msg.set('Lets Go...')
warning = Label(screen, textvariable = warning_msg, font="calibri 10 bold", pady=20, fg='green', bg = "cyan").pack()

screen.config(bg = "cyan", borderwidth = 5, relief = GROOVE)

space.bind("<Enter>", pretimer)

screen.wm_iconbitmap('logo.ico')
screen.mainloop()
