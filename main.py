
from tkinter import *
from tkinter.messagebox import *
import tkinter as tk
import time
import math

#Digital clock

def openWindow1():

    def update_clock():
        hours = time.strftime("%I")
        minutes = time.strftime("%M")
        seconds = time.strftime("%S")
        am_or_pm = time.strftime("%p")
        time_text = hours + ":" + minutes + ":" + seconds + " " + am_or_pm
        digital_clock_lbl.config(text=time_text)
        digital_clock_lbl.after(1000, update_clock)


    new_wind1=Toplevel(root)
    new_wind1.resizable(False, False)
    new_wind1.config(bg="#2F3C7E")
    new_wind1.title("Digital Clock")
    digital_clock_lbl = tk.Label(new_wind1, text="00:00:00", font="Helvetica 72 bold")
    digital_clock_lbl.pack()

    update_clock()

#Analog clock

def openWindow2():

    def update_clock2():
        hours = int(time.strftime("%I"))
        minutes = int(time.strftime("%M"))
        seconds = int(time.strftime("%S"))

        # updating seconds hand
        seconds_x = seconds_hand_len * math.sin(math.radians(seconds * 6)) + center_x
        seconds_y = -1 * seconds_hand_len * math.cos(math.radians(seconds * 6)) + center_y
        canvas.coords(seconds_hand, center_x, center_y, seconds_x, seconds_y)

        # updating minutes hand
        minutes_x = minutes_hand_len * math.sin(math.radians(minutes * 6)) + center_x
        minutes_y = -1 * minutes_hand_len * math.cos(math.radians(minutes * 6)) + center_y
        canvas.coords(minutes_hand, center_x, center_y, minutes_x, minutes_y)

        # updating hours hand
        hours_x = hours_hand_len * math.sin(math.radians(hours * 30 + 0.5 * minutes + 0.008 * seconds)) + center_x
        hours_y = -1 * hours_hand_len * math.cos(math.radians(hours * 30 + 0.5 * minutes + 0.008 * seconds)) + center_y
        canvas.coords(hours_hand, center_x, center_y, hours_x, hours_y)

        new_wind2.after(1000, update_clock2)

    new_wind2 = Toplevel(root)
    new_wind2.geometry("400x400")
    new_wind2.resizable(False, False)
    new_wind2.title("Analog Clock")

    canvas = tk.Canvas(new_wind2, width=400, height=400, bg="black")
    canvas.pack(expand=True, fill='both')

    # create background

    canvas._photo = photo = tk.PhotoImage(file='clock_400.png')
    canvas.create_image(200, 200, image=photo)

    # create clock hands
    # seconds hand
    center_x = 200
    center_y = 200

    seconds_hand_len = 95
    minutes_hand_len = 80
    hours_hand_len = 60

    seconds_hand = canvas.create_line(200, 200, 200 + seconds_hand_len, 200 + seconds_hand_len, width=1.5, fill='red')
    # minutes hand
    minutes_hand = canvas.create_line(200, 200, 200 + minutes_hand_len, 200 + minutes_hand_len, width=2, fill='white')
    # hours hand
    hours_hand = canvas.create_line(200, 200, 200 + hours_hand_len, 200 + hours_hand_len, width=4, fill='white')

    update_clock2()


#Countdown Timer

def openWindow3():

    #start function of the Countdown Timer
    def Start_Timer():
        times = int(float(hours.get())) * 3600 + int(float(minutes.get())) * 60 + int(float(seconds.get()))

        while times > -1:
            minute, second = (times // 60, times % 60)

            hour = 0
            if minute > 60:
                hour, minute = (minute // 60, minute % 60)

            seconds.set(second)
            minutes.set(minute)
            hours.set(hour)

            root.update()
            time.sleep(1)
            times -= 1

        showinfo("Countdown Timer", "Time is up!")

    # stop function of the Countdown Timer
    def Stop_Timer():
        seconds.set("00")
        minutes.set("00")
        hours.set("00")

    hours = StringVar()
    minutes = StringVar()
    seconds = StringVar()

    new_wind3=Toplevel(root)
    new_wind3.geometry("450x450")
    new_wind3.title("Countdown Timer")
    new_wind3.config(bg="#2F3C7E")
    new_wind3.resizable(False, False)
    heading = Label(new_wind3, text="Timer", font="arial 30 bold", bg="#2F3C7E", fg="#FBEAEB", padx=5, pady=5)
    heading.pack(pady=10)

    Entry(new_wind3, textvariable=hours, width=2, font="arial 50", bg="#FBEAEB", fg="#000", bd=0).place(x=30, y=155)
    hours.set("00")

    minutes = StringVar()
    Entry(new_wind3, textvariable=minutes, width=2, font="arial 50", bg="#FBEAEB", fg="#000", bd=0).place(x=150, y=155)
    minutes.set("00")

    seconds = StringVar()
    Entry(new_wind3, textvariable=seconds, width=2, font="arial 50", bg="#FBEAEB", fg="#000", bd=0).place(x=270, y=155)
    seconds.set("00")

    Label(new_wind3, text="hours", font="arial 8", bg="#2F3C7E", fg="#000").place(x=105, y=200)
    Label(new_wind3, text="minutes", font="arial 8", bg="#2F3C7E", fg="#000").place(x=225, y=200)
    Label(new_wind3, text="seconds", font="arial 8", bg="#2F3C7E", fg="#000").place(x=345, y=200)

    button1 = Button(new_wind3, text="Start", bg="#FBEAEB", fg="#000", width=20, height=2, font="arial 10 bold",
                     command=Start_Timer)
    button1.pack(padx=15, pady=5, side=LEFT)

    button2 = Button(new_wind3, text="Stop", bg="#FBEAEB", fg="#000", width=20, height=2, font="arial 10 bold",
                     command=Stop_Timer)
    button2.pack(padx=15, pady=5, side=RIGHT)


#StopWatch

hr = 00
second = 00
min = 00
stop = 0

def openWindow4():

    # start function of the StopWatch
    def Start_watch():
        global second, hr, min

        time.sleep(1)
        second += 1
        if second == 60:
            second = 00
            min += 1
        if min == 60:
            min = 00
            hr += 1
        if stop == 0:
            label = tk.Label(new_wind4, text=f"{hr}:{min}:{second}", width=15, font="arial 20 bold", fg="white", bg="#2F3C7E")
            label.after(1000, Start_watch)
            label.place(x=80, y=100)

    # stop function of the StopWatch
    def Stop_watch():
        global stop
        stop = 1

    # reset function of the StopWatch
    def Reset_watch():
        global counter, hr, second, min, stop
        stop = 0
        second = 0
        min = 0
        hr = 0

    new_wind4 = Toplevel(root)
    new_wind4.geometry("450x450")
    new_wind4.title("StopWatch")
    new_wind4.config(bg="#2F3C7E")
    new_wind4.resizable(False, False)
    heading = Label(new_wind4, text="StopWatch", font="arial 30 bold", bg="#2F3C7E", fg="#FBEAEB", padx=5, pady=5)
    heading.pack(pady=10)

    button1 = tk.Button(new_wind4, text="Start", bg="#FBEAEB", fg="#000", height=2, width=20, font="arial 10 bold",
                        command=Start_watch)
    button1.pack(padx=5, pady=5, side=LEFT)

    button2 = tk.Button(new_wind4, text="Stop", bg="#FBEAEB", fg="#000", width=20, height=2, font="arial 10 bold",
                        command=Stop_watch)
    button2.pack(padx=5, pady=5, side=RIGHT)

    button3 = tk.Button(new_wind4, text="Reset", bg="#FBEAEB", fg="#000", width=20, height=2, font="arial 10 bold",
                        command=Reset_watch)
    button3.pack(padx=5, pady=5, side=RIGHT)


root = Tk()
root.geometry("600x300")
root.title("Clock Project")
root.config(bg="#2F3C7E")
root.resizable(False, False)
icon = tk.PhotoImage(file="alarm-clock.png")
root.wm_iconphoto(True, icon)
btn1=Button(root, text='Digital clock',font="arial 15 bold",bg="#FBEAEB",fg="black", command=openWindow1)
btn1.pack(side=LEFT, padx=0, pady=20)

btn2=Button(root, text='Analog clock',font="arial 15 bold",bg="#FBEAEB",fg="black", command=openWindow2)
btn2.pack(side=LEFT, padx=15, pady=20)

btn3=Button(root, text='Countdown',font="arial 15 bold",bg="#FBEAEB",fg="black", command=openWindow3)
btn3.pack(side=RIGHT, padx=15, pady=20)

btn4=Button(root, text='StopWatch',font="arial 15 bold",bg="#FBEAEB",fg="black", command=openWindow4)
btn4.pack(side=RIGHT, padx=15, pady=20)

root.mainloop()