from tkinter import *

window = Tk()

# set parameters for the window:
window.title("Mile to Km Converter")
window.minsize(width = 500,height=300)
# adding padding
window.config(padx=10,pady=10)

# Is Equal Label
is_equal_to = Label(text="Is equal to",font=("Arial",24,"bold"))
is_equal_to.grid(column=1,row=2)

# input to convert
input = Entry(width=10)
input.grid(column=2,row=1)


# Miles Label

miles = Label(text="Miles",font=("Arial",24,"bold"))
miles.grid(column=3,row=1)

# Km Label

km = Label(text="Km",font=("Arial",24,"bold"))
km.grid(column=3,row=2)

# label converted
converted_value = Label(font=("Arial",24,"bold"))
converted_value.grid(column=2,row=2)

# Calculate Button
def action():

    get_value = input.get()
    result = round(float(get_value) * 1.6)
    converted_value.config(text=result)
    print("calculated")
