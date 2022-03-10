import random
import time
import tkinter as tk


def label_reload():
    for item in points:
        label.configure(bg="white", font=("Arial", 25))
        time.sleep(0.2)
        label.configure(text=item)
        label.update()

    label.configure(text=random.choice(points), font=("Arial", 50))
    label.update()
    label.configure(bg="green")


# unpack list of the tasks
points = []
first_text = "Wcisnij start, aby wylosowac"

with open("punkty_do_inspekcji.txt", 'r') as file:
    for line in file:
        points.append(line.strip())

# tkinter interface
window = tk.Tk()
window.title("Losowanie na audyt")
window.geometry("1000x400")

# JTI logo
img = tk.PhotoImage(file="JTI-logo-reversed.png")
logo = tk.Label(window, image=img)
logo.grid(row=0, column=0)

# Label
label = tk.Label(window, text=first_text, bg="white", bd=50, font=("Arial", 25))
label.grid(row=1, column=1, padx=10, pady=10)

# button
button = tk.Button(window, text="START", height=3, width=50, bg="green", bd=10, command=label_reload)
button.grid(row=2, column=1)


window.mainloop()
