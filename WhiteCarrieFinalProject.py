"""
Weekly Meal Plan Generator
Carrie White
V4 Last Mod 12.14.21

This program generates a random list of recipes for a week and
then adds their ingredients into a grocery list.


"""
import random
from tkinter import *

root = Tk()
root.title("Weekly Meal Plan Generator")

#Define Meal Class
class Meal(object):
    def __init__(self,recipeName,ingred1,ingred2,ingred3,ingred4,ingred5):
        self.recipeName = recipeName
        self.ingred1 = ingred1
        self.ingred2 = ingred2
        self.ingred3 = ingred3
        self.ingred4 = ingred4
        self.ingred5 = ingred5


    def getRecipeName(self,recipeName):
        return self.recipeName


    def getIngredients(self,ingred1,ingred2,ingred3,ingred4,ingred5):
        return [self.ingred1,self.ingred2,sefl.ingred3,self.ingred4,self.ingred5]





#Meals list, Need to add more
recipe_1 = Meal('Tacos','ground beef','tortillas','cheddar cheese','taco seasoning','lettuce')
recipe_2 = Meal('Hamburgers','ground beef','hamburger buns','ketchup','sliced cheese','pickles')
recipe_3 = Meal('Fajitas','chicken breasts','yellow onion','bell pepper','lime','tortillas')
recipe_4 = Meal('Chicken salad','canned chicken','celery','apples','mayo','bread')
recipe_5 = Meal('Pork Chops','pork chops','fry seasoning','garlic cloves','canned biscuits','butter')
recipe_6 = Meal('Teriyaki','chicken breasts','rice','stir-fry veggies','soy sauce','mirin')
recipe_7 = Meal('Chicken Dumplings','canned chicken','canned biscuits','cream of chicken','milk','mashed potatoes')



#Randomize Meals button function
def randomize_meals():
    day1Meal = 'recipe_'+(str(random.randint(1,7)))
    day2Meal = 'recipe_'+(str(random.randint(1,7)))
    day3Meal = 'recipe_'+(str(random.randint(1,7)))
    day4Meal = 'recipe_'+(str(random.randint(1,7)))
    day5Meal = 'recipe_'+(str(random.randint(1,7)))
    day6Meal = 'recipe_'+(str(random.randint(1,7)))
    day7Meal = 'recipe_'+(str(random.randint(1,7)))

    
#Defines Meal Labels
    mealLabel1 = Label(root, text='day1Meal.getRecipeName()')
    mealLabel2 = Label(root, text='day2Meal.getRecipeName()')
    mealLabel3 = Label(root, text='day3Meal.getRecipeName()')
    mealLabel4 = Label(root, text='day4Meal.getRecipeName()')
    mealLabel5 = Label(root, text='day5Meal.getRecipeName()')
    mealLabel6 = Label(root, text='day6Meal.getRecipeName()')
    mealLabel7 = Label(root, text='day7Meal.getRecipeName()')

#Display Meal Labels
    mealLabel1.grid(row=2,column=1)
    mealLabel2.grid(row=3,column=1)
    mealLabel3.grid(row=4,column=1)
    mealLabel4.grid(row=5,column=1)
    mealLabel5.grid(row=6,column=1)            
    mealLabel6.grid(row=7,column=1)
    mealLabel7.grid(row=8,column=1)


#Generate List button function
def generate_list():
    listWindow = tk.toplevel(root)







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
button_randomize = Button(root, text="Randomize Meals", padx=20,command=randomize_meals)
#button_save_plan = Button(root, text="Save This Plan", padx=20)
button_generate_list = Button(root, text="Generate Grocery List", padx=10,command=generate_list)

#Display Buttons
button_randomize.grid(row=10, column=0)
#button_save_plan.grid(row=10, column=1)
button_generate_list.grid(row=10, column=1)



