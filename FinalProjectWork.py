"""
Weekly Meal Plan Generator
Carrie White
V1 11.28.21

This program generates a random list of recipes for a week and
then adds their ingredients into a grocery list.


"""

from tkinter import *

root = Tk()
root.title("Weekly Meal Plan Generator")



#Define Labels
titleLabel = Label(root, text="Weekly Meal Plan")
dayLabel1 = Label(root, text="Sunday")
dayLabel2 = Label(root, text="Monday")
dayLabel3 = Label(root, text="Tuesday")
dayLabel4 = Label(root, text="Wednesday")
dayLabel5 = Label(root, text="Thursday")
dayLabel6 = Label(root, text="Friday")
dayLabel7 = Label(root, text="Saturday")
blankLabel = Label(root, text=" ")

#Display Labels
titleLabel.grid(row=0, column=0, columnspan=2)
blankLabel.grid(row=1, column=0)
dayLabel1.grid(row=2, column=0)
dayLabel2.grid(row=3, column=0)
dayLabel3.grid(row=4, column=0)
dayLabel4.grid(row=5, column=0)
dayLabel5.grid(row=6, column=0)
dayLabel6.grid(row=7, column=0)
dayLabel7.grid(row=8, column=0)
blankLabel.grid(row=9, column=0)

#Define Buttons
button_randomize = Button(root, text="Randomize Meals", padx=20)
#button_save_plan = Button(root, text="Save This Plan", padx=20)
button_generate_list = Button(root, text="Generate Grocery List", padx=10)

#Display Buttons
button_randomize.grid(row=10, column=0)
#button_save_plan.grid(row=10, column=1)
button_generate_list.grid(row=10, column=1)





