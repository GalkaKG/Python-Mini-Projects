from tkinter import *


def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.689)
    kilometer_results_label.config(text=f"{km}")


window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(350, 250)
window.config(padx=20, pady=20)

miles_input = Entry()
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

kilometer_results_label = Label(text="0")
kilometer_results_label.grid(column=1, row=1)

kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()
