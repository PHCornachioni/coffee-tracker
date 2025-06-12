from tkinter import *

BACKGROUND_COLOR = "#AB886D"
track = 0

def reset():
    global track
    track = 0
    tracker_label.config(text=track)
    canvas.itemconfig(coffee, image=coffee_1_image)
    with open("data/data.txt", "w") as data:
        data.write(f"{track}")


def add():
    global track
    track += 1
    tracker_label.config(text=track)
    with open("data/data.txt", "w") as data:
        data.write(f"{track}")
    if track < 9:
        coffee_face_update()

def subtract():
    global track
    if track > 0:
        track -= 1
        tracker_label.config(text=track)
        with open("data/data.txt", "w") as data:
            data.write(f"{track}")
        if track < 9:
            coffee_face_update()


def coffee_face_update():
    if track == 1:
        canvas.itemconfig(coffee, image=coffee_2_image)
    elif track == 2:
        canvas.itemconfig(coffee, image=coffee_3_image)
    elif track == 3:
        canvas.itemconfig(coffee, image=coffee_4_image)
    elif track == 5:
        canvas.itemconfig(coffee, image=coffee_5_image)
    elif track == 6:
        canvas.itemconfig(coffee, image=coffee_6_image)
    elif track == 7:
        canvas.itemconfig(coffee, image=coffee_7_image)
    elif track >= 8:
        canvas.itemconfig(coffee, image=coffee_8_image)


try:
    with open("data/data.txt", "r") as data:
        track = int(data.readline())
except (FileNotFoundError, ValueError):
    with open("data/data.txt", "w") as data:
        data.write("0")

window = Tk()
window.title("Coffee Tracker")
window.config(width=800, height=600, padx=50, pady=50, bg=BACKGROUND_COLOR)

#tracker
coffees_label = Label(text="Coffees", bg=BACKGROUND_COLOR, fg="#D7C0B3", font=("Arial", 70, "bold"))
coffees_label.grid(row=0, column=0, columnspan=4)
tracker_label = Label(text=track, bg=BACKGROUND_COLOR, fg="#D7C0B3", font=("Arial", 80, "bold"))
tracker_label.grid(row=1, column=1, columnspan=2)

#coffees
canvas = Canvas(width=534, height=562, bg=BACKGROUND_COLOR, highlightthickness=0)
coffee_1_image = PhotoImage(file="images/coffee_1.png")
coffee_2_image = PhotoImage(file="images/coffee_2.png")
coffee_3_image = PhotoImage(file="images/coffee_3.png")
coffee_4_image = PhotoImage(file="images/coffee_4.png")
coffee_5_image = PhotoImage(file="images/coffee_5.png")
coffee_6_image = PhotoImage(file="images/coffee_6.png")
coffee_7_image = PhotoImage(file="images/coffee_7.png")
coffee_8_image = PhotoImage(file="images/coffee_8.png")
coffee = canvas.create_image(267, 281, image=coffee_1_image)
canvas.grid(row=2, column=0, columnspan=4)

#buttons
subtract_image = PhotoImage(file="images/button_subtract.png")
add_button = Button(image=subtract_image, highlightthickness=0, borderwidth=0, activebackground=BACKGROUND_COLOR, background=BACKGROUND_COLOR, command=subtract)
add_button.grid(row=1, column=0)

reset_image = PhotoImage(file="images/button_reset.png")
reset_button = Button(image=reset_image, highlightthickness=0, borderwidth=0, activebackground=BACKGROUND_COLOR, background=BACKGROUND_COLOR, command=reset)
reset_button.grid(row=4, column=0, columnspan=4)

add_image = PhotoImage(file="images/button_add.png")
add_button = Button(image=add_image, highlightthickness=0, borderwidth=0, activebackground=BACKGROUND_COLOR, background=BACKGROUND_COLOR, command=add)
add_button.grid(row=1, column=3)

coffee_face_update()

window.mainloop()