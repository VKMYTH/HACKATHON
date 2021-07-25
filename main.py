import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Carbo Complex")
root.geometry("600x1000")
root.configure(bg="light green")
s = ttk.Style(root)
s.configure('TNotebook', tabposition='n')

tk.Label(root, text="Carbo Complex, The Carbon Footprint Evaluator", bg="light green", font=('bold')).pack(side="top")

# setting up ^^

annual_household = 0.0

def add_household(var):
    global annual_household


tabControl = ttk.Notebook(root)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)
tab4 = ttk.Frame(tabControl)
tab5 = ttk.Frame(tabControl)

tabControl.add(tab1, text="Introduction")
tabControl.add(tab2, text='Household')
tabControl.add(tab3, text='Transportation')
tabControl.add(tab4, text='Food')
tabControl.add(tab5, text='Analysis')
tabControl.pack(expand=1, fill="both")

# setting up the tabs ^^

def start_quiz():
    annual_household = 0.00
    tabControl.select(tab2)

tk.Label(tab1, text="A Carbon Footprint is the amount of carbon compounds emitted because of fossil fuels from a person or group. Carbon Footprints are important to know because they can show how you are impacted the world with just day to day tasks such as turning on the TV. When gasses are emitted it impacts our enviornment in a harmful way by changing the climate. If you want to see what your carbon footprint is, take the Carbon Footprint test below which calculates your carbon footprint and gives you tips based on your score.", bg="light green", wraplength=500, justify="center", bd=20).pack(side="top")

tk.Button(tab1, text="Begin your quiz", command=start_quiz).pack()

# all of the info on the first tab ^^

ttk.Label(tab2, text="How many people live in your home?").pack()
people_count_buttons = []
people_count = tk.DoubleVar()
people_count.set(-1)

ttk.Radiobutton(tab2, text="1", variable=people_count, value=0.07, command=lambda: add_household(people_count.get())).pack()
ttk.Radiobutton(tab2, text="2", variable=people_count, value=0.13, command=lambda: add_household(people_count.get())).pack()
ttk.Radiobutton(tab2, text="3", variable=people_count, value=0.23, command=lambda: add_household(people_count.get())).pack()
ttk.Radiobutton(tab2, text="4", variable=people_count, value=0.43, command=lambda: add_household(people_count.get())).pack()
ttk.Radiobutton(tab2, text="5", variable=people_count, value=0.82, command=lambda: add_household(people_count.get())).pack()
ttk.Radiobutton(tab2, text="6", variable=people_count, value=1.63, command=lambda: add_household(people_count.get())).pack()

ttk.Label(tab2, text="What type of home do you live in?").pack()

housing_type = tk.DoubleVar()
housing_type.set(-1)

ttk.Radiobutton(tab2, text="An Apartment", variable=housing_type, value=0.43, command=lambda: add_household(housing_type.get())).pack()
ttk.Radiobutton(tab2, text="A Townhouse", variable=housing_type, value=0.83, command=lambda: add_household(housing_type.get())).pack()
ttk.Radiobutton(tab2, text="A house", variable=housing_type, value=1.63, command=lambda: add_household(housing_type.get())).pack()

ttk.Label(tab2, text="How much of your household is air-conditioned").pack()

total_rooms = tk.DoubleVar()
total_rooms.set(-1)

ttk.Radiobutton(tab2, text="0", variable=total_rooms, value=0.00, command=lambda: add_household(total_rooms.get())).pack()
ttk.Radiobutton(tab2, text="1-3 rooms", variable=total_rooms, value=0.77, command=lambda: add_household(total_rooms.get())).pack()
ttk.Radiobutton(tab2, text="4 or all rooms", variable=total_rooms, value=3.05, command=lambda: add_household(total_rooms.get())).pack()

ttk.Label(tab2, text="Does your household recycle cans?").pack()

recycle_cans = tk.DoubleVar()
recycle_cans.set(-1)

ttk.Radiobutton(tab2, text="Yes", variable=recycle_cans, value=0.00, command=lambda: add_household(recycle_cans.get())).pack()
ttk.Radiobutton(tab2, text="No", variable=recycle_cans, value=0.28, command=lambda: add_household(recycle_cans.get())).pack()
ttk.Radiobutton(tab2, text="Not Sure", variable=recycle_cans, value=0.13, command=lambda: add_household(recycle_cans.get())).pack()

ttk.Label(tab2, text="Do you recycle plastic?").pack()

recycle_plastic = tk.DoubleVar()
recycle_plastic.set(-1)


ttk.Label(tab2, text="Does your household recycle paper products such as magazines and newspapers")

recycle_paper = tk.DoubleVar()
recycle_paper.set(-1)

ttk.Radiobutton(tab2, text="Yes", variable=recycle_paper, value=0.00, command=lambda: add_household(recycle_paper.get())).pack()
ttk.Radiobutton(tab2, text="No", variable=recycle_paper, value=0.11, command=lambda: add_household(recycle_paper.get())).pack()
ttk.Radiobutton(tab2, text="Not Sure", variable=recycle_paper, value=0.08, command=lambda: add_household(recycle_paper.get())).pack()

ttk.Label(tab2, text="How many hours each day does your household play video games?").pack()

video_hours = tk.DoubleVar()
video_hours.set(-1)

ttk.Radiobutton(tab2, text="0-2", variable=video_hours, value=0.04, command=lambda: add_household(video_hours.get())).pack()
ttk.Radiobutton(tab2, text="3-4", variable=video_hours, value=0.05, command=lambda: add_household(video_hours.get())).pack()
ttk.Radiobutton(tab2, text="5-6", variable=video_hours, value=0.08, command=lambda: add_household(video_hours.get())).pack()
ttk.Radiobutton(tab2, text="7 or more", variable=video_hours, value=0.09, command=lambda: add_household(video_hours.get())).pack()

ttk.Label(tab2, text="Does your household turn off video game consoles when they are not in use?").pack()

video_off = tk.DoubleVar()
video_off.set(-1)

ttk.Radiobutton(tab2, text="Yes", variable=video_off, value=0.00, command=lambda: add_household(video_off.get())).pack()
ttk.Radiobutton(tab2, text="No", variable=video_off, value=0.14, command=lambda: add_household(video_off.get())).pack()

ttk.Label(tab2, text="Does your household turn off the TV when they are not watching it?").pack()

tv_off = tk.DoubleVar()
tv_off.set(-1)

ttk.Radiobutton(tab2, text="Yes", variable=tv_off, value=0, command=lambda: add_household(tv_off.get())).pack()
ttk.Radiobutton(tab2, text="No", variable=tv_off, value=0.05, command=lambda: add_household(tv_off.get())).pack()

ttk.Label(tab2, text="Does everyone in your household turn off the lights when they leave a room empty?").pack()

lights_off = tk.DoubleVar()
lights_off.set(-1)

ttk.Radiobutton(tab2, text="Yes", variable=lights_off, value=0.00, command=lambda: add_household(lights_off.get())).pack()
ttk.Radiobutton(tab2, text="No", variable=lights_off, value=0.13, command=lambda: add_household(lights_off.get())).pack()

# all of the info, questions and radiobuttons on tab2 (questions)

ttk.Label(tab3, text='How do you get to school each day?').pack()

school = tk.DoubleVar()
school.set(-1)

ttk.Radiobutton(tab3, text="Walk, Bike, Scooter, Or SkateBoard", variable=school, value=0.00, command=lambda: add_household(school.get())).pack()
ttk.Radiobutton(tab3, text="Ride the Bus", variable=school, value=0.14, command=lambda: add_household(school.get())).pack()
ttk.Radiobutton(tab3, text="Car", variable=school, value=0.29, command=lambda: add_household(school.get())).pack()

ttk.Label(tab3, text='How many times a week does your household use a car?').pack()

car_w = tk.DoubleVar()
car_w.set(-1)

ttk.Radiobutton(tab3, text="Never", variable=car_w, value=0.00, command=lambda: add_household(car_w.get())).pack()
ttk.Radiobutton(tab3, text="5 times", variable=car_w, value=1.73, command=lambda: add_household(car_w.get())).pack()
ttk.Radiobutton(tab3, text="10 times", variable=car_w, value=3.45, command=lambda: add_household(car_w.get())).pack()
ttk.Radiobutton(tab3, text="15 times", variable=car_w, value=5.18, command=lambda: add_household(car_w.get())).pack()
ttk.Radiobutton(tab3, text="16 times or more", variable=car_w, value=6.21, command=lambda: add_household(car_w.get())).pack()

ttk.Label(tab3, text='How many times have you flown in an airplane in the past year?').pack()

airplane = tk.DoubleVar()
airplane.set(-1)

ttk.Radiobutton(tab3, text="Never", variable=airplane, value=0.00, command=lambda: add_household(airplane.get())).pack()
ttk.Radiobutton(tab3, text="5 times", variable=airplane, value=1.83, command=lambda: add_household(airplane.get())).pack()
ttk.Radiobutton(tab3, text="10 times", variable=airplane, value=3.67, command=lambda: add_household(airplane.get())).pack()
ttk.Radiobutton(tab3, text="15 times", variable=airplane, value=5.50, command=lambda: add_household(airplane.get())).pack()

ttk.Label(tab3, text='What kind of car(s) does your household drive and how many of each?').pack()

hybrid = tk.DoubleVar()
hybrid.set(-1)

ttk.Label(tab3, text="Small Car or Hybrid?").pack()
ttk.Radiobutton(tab3, text="0", variable=hybrid, value=0.00, command=lambda: add_household(hybrid.get())).pack()
ttk.Radiobutton(tab3, text="1", variable=hybrid, value=1.33, command=lambda: add_household(hybrid.get())).pack()
ttk.Radiobutton(tab3, text="2", variable=hybrid, value=2.66, command=lambda: add_household(hybrid.get())).pack()

midsize = tk.DoubleVar()
midsize.set(-1)

ttk.Label(tab3, text="Midsize").pack()
ttk.Radiobutton(tab3, text="0", variable=midsize, value=0.00, command=lambda: add_household(midsize.get())).pack()
ttk.Radiobutton(tab3, text="1", variable=midsize, value=2.33, command=lambda: add_household(midsize.get())).pack()
ttk.Radiobutton(tab3, text="2", variable=midsize, value=4.60, command=lambda: add_household(midsize.get())).pack()

large = tk.DoubleVar()
large.set(-1)
ttk.Label(tab3, text="Large SUV/Truck").pack()
ttk.Radiobutton(tab3, text="0", variable=hybrid, value=0.00, command=lambda: add_household(hybrid.get())).pack()
ttk.Radiobutton(tab3, text="1", variable=hybrid, value=3.37, command=lambda: add_household(hybrid.get())).pack()
ttk.Radiobutton(tab3, text="2", variable=hybrid, value=6.75, command=lambda: add_household(hybrid.get())).pack()

# all of the info, questions and radiobuttons on tab3 (questions)

ttk.Label(tab4, text="How many individual servings of wrapped food does your household eat each day? (Such as chips, cookies, candy and pretzels)").pack()

servings = tk.DoubleVar()
servings.set(-1)

ttk.Radiobutton(tab4, text="None", variable=hybrid, value=0.00, command=lambda: add_household(hybrid.get())).pack()
ttk.Radiobutton(tab4, text="3 times", variable=hybrid, value=0.39, command=lambda: add_household(hybrid.get())).pack()
ttk.Radiobutton(tab4, text="6 times", variable=hybrid, value=0.78, command=lambda: add_household(hybrid.get())).pack()
ttk.Radiobutton(tab4, text="7 or more", variable=hybrid, value=1.57, command=lambda: add_household(hybrid.get())).pack()

ttk.Label(tab4, text='What kind of food does your household eat?').pack()

food = tk.DoubleVar()
food.set(-1)

ttk.Radiobutton(tab4, text="Just Vegetables (vegan)", variable=food, value=0.19, command=lambda: add_household(food.get())).pack()
ttk.Radiobutton(tab4, text="Vegetables, eggs, and dairy (vegetarian)", variable=food, value=1.22, command=lambda: add_household(food.get())).pack()
ttk.Radiobutton(tab4, text="Everything", variable=food, value=6.72, command=lambda: add_household(food.get())).pack()

ttk.Label(tab4, text='How many times a week does your household eat at a fast food restaurant?').pack()

kind = tk.DoubleVar()
kind.set(-1)

ttk.Radiobutton(tab4, text="Never", variable=kind, value=0.00, command=lambda: add_household(kind.get())).pack()
ttk.Radiobutton(tab4, text="Once A week", variable=kind, value=0.39, command=lambda: add_household(kind.get())).pack()
ttk.Radiobutton(tab4, text="Twice a week", variable=kind, value=0.78, command=lambda: add_household(kind.get())).pack()
ttk.Radiobutton(tab4, text="More than twice a week", variable=kind, value=1.57, command=lambda: add_household(kind.get())).pack()

# all of the info, questions and radiobuttons on tab4 (questions)

def quiz_end():
    global annual_household
    if people_count.get() != -1:
        annual_household += people_count.get()
    if housing_type.get() != -1:
        annual_household += housing_type.get()
    if total_rooms.get() != -1:
        annual_household += total_rooms.get()
    if recycle_plastic.get() != -1:
        annual_household += recycle_plastic.get()
    if recycle_paper.get() != -1:
        annual_household += recycle_paper.get()
    if recycle_cans.get() != -1:
        annual_household += recycle_cans.get()
    if video_hours.get() != -1:
        annual_household += video_hours.get()
    if video_off.get() != -1:
        annual_household += video_off.get()
    if tv_off.get() != -1:
        annual_household += tv_off.get()
    if lights_off.get() != -1:
        annual_household += lights_off.get()
    if school.get() != -1:
        annual_household += school.get()
    if car_w.get() != -1:
        annual_household += car_w.get()
    if airplane.get() != -1:
        annual_household += airplane.get()
    if hybrid.get() != -1:
        annual_household += hybrid.get()
    if midsize.get() != -1:
        annual_household += midsize.get()
    if large.get() != -1:
        annual_household += large.get()
    if servings.get() != -1:
        annual_household += servings.get()
    if food.get() != -1:
        annual_household += food.get()
    if kind.get() != -1:
        annual_household += kind.get()
    tk.Label(tab5, text="Your quiz is over, and you don't need to answer any more questions.", font=5, wraplength=500).pack()
    tk.Label(tab5, text=f"Your final Carbon Footprint is {annual_household}", font=5, wraplength=500).pack()
    if annual_household >= 20.9:
        tk.Label(tab5, text="Your Carbon Footprint is above average, and that's not very good.", font=5, wraplength=500).pack()
        tk.Label(tab5, text=" - Choose organic and local foods that are in season.", fg="red", font=4, wraplength=500).pack()
        tk.Label(tab5, text=" - Buy less stuff! And buy used or recycled items whenever possible.", fg="red", font=4, wraplength=500).pack()
        tk.Label(tab5,
                 text=" - Switch lights off when you leave the room and unplug your electronic devices when they are not in use.", fg="red", font=4, wraplength=500).pack()
        tk.Label(tab5,
                 text=" - Take care of your car. Keeping your tires properly inflated can increase your fuel efficiency by three percent; and ensuring that your car is properly maintained can increase it by four percent. Remove any extra weight from the car.", fg="red", font=4, wraplength=500).pack()
        tk.Label(tab5, text="To retake the quiz, restart the application", font=4, wraplength=500).pack()
    elif annual_household < 20.9:
        tk.Label(tab5,
                 text="Your Carbon Footprint is below average, and that's helping the environment positively, so for that thank you!", font=3, wraplength=500).pack()
        tk.Label(tab5,
                 text=" - Maintain your current strategy/day to day activities, and if you can, lower the standards that are on the questions", fg="green", font=4, wraplength=500).pack()
        tk.Label(tab5, text="To retake the quiz, restart the application", font=4, wraplength=500).pack()
    else:
        raise ValueError("Something went wrong... Restart the application.")
    tk.Label(tab5, text="Thank you for using the Carbon Footprint Calculator", font=3, wraplength=500)
    tabControl.select(tab5)
    # when the end button is clicked all of this code will run

ttk.Button(tab4, text="Click this button once you've answered the questions and to end your quiz", command=quiz_end).pack()

root.mainloop()

# ends the program^^
