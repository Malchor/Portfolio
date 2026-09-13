from tkinter import Tk, Frame, Label, Entry, Button, StringVar
import tkinter as tk

def temperature_converter():

    def convert_to_fahrenheit():
        celsius = float(celsius_entry.get())
        fahrenheit = (celsius * 9/5) + 32
        fahrenheit_entry.insert(0, fahrenheit)

    def convert_to_celsius():
        fahrenheit = float(fahrenheit_entry.get())
        celsius = (fahrenheit - 32) * 5/9
        celsius_entry.insert(0, celsius)

    window = tk.Tk()
    window.title("Temperature Converter")

    tk.Label(window, text="Fahrenheit").pack()
    fahrenheit_entry = tk.Entry(window)
    fahrenheit_entry.pack()

    tk.Label(window, text="Celsius").pack()
    celsius_entry = tk.Entry(window)
    celsius_entry.pack()

    tk.Button(window, text="Convert to Fahrenheit", command=convert_to_fahrenheit).pack()

    tk.Button(window, text="Convert to Celsius", command=convert_to_celsius).pack()

    window.mainloop()



def what_to_do_today():

    def recommend():
        temp = float(temp_entry.get())

        if temp >= 30:
            result_label.config(text="Go swimming")
        elif temp >= 20:
            result_label.config(text="Go for a walk")
        elif temp >= 10:
            result_label.config(text="Read a book")
        else:
            result_label.config(text="Stay inside")

    window = tk.Tk()
    window.title("What To Do Today")

    tk.Label(window, text="Enter today's temperature").pack()

    temp_entry = tk.Entry(window)
    temp_entry.pack()

    tk.Button(window, text="Recommend Activity",command=recommend).pack()

    result_label = tk.Label(window, text="")
    result_label.pack()

    window.mainloop()



def truth_table():

    def check_answers():
        score = 0

        if entry1.get() == "1":
            score = score + 1

        if entry2.get() == "1":
            score = score + 1

        if entry3.get() == "1":
            score = score + 1

        if entry4.get() == "0":
            score = score + 1

        percentage = (score / 4) * 100
        result_label.config(text="Score: " + str(percentage) + "%")

    window = tk.Tk()
    window.title("Truth Table - OR")

    tk.Label(window, text="Enter 1 for True, 0 for False").pack()

    tk.Label(window, text="True OR True").pack()
    entry1 = tk.Entry(window)
    entry1.pack()

    tk.Label(window, text="True OR False").pack()
    entry2 = tk.Entry(window)
    entry2.pack()

    tk.Label(window, text="False OR True").pack()
    entry3 = tk.Entry(window)
    entry3.pack()

    tk.Label(window, text="False OR False").pack()
    entry4 = tk.Entry(window)
    entry4.pack()

    tk.Button(window, text="Submit", command=check_answers).pack()

    result_label = tk.Label(window, text="")
    result_label.pack()

    window.mainloop()



file_name = "login_details.txt"

def sign_up():

    def save_user():
        username = username_entry.get()
        password = password_entry.get()

        if len(password) < 5:
            message_label.config(text="Password must be at least 5 characters",fg="red")
            return

        has_letter = False
        has_number = False

        for char in password:
            if char.isalpha():
                has_letter = True
            if char.isdigit():
                has_number = True

        if has_letter == False or has_number == False:
            message_label.config(text="Password must contain letter and number",fg="red")
            return

        file = open(file_name, "a")
        file.write(username + "," + password + "\n")
        file.close()

        window.destroy()
        login_window()

    def toggle_password():
        if show_var.get() == 1:
            password_entry.config(show="")
        else:
            password_entry.config(show="*")

    window = tk.Tk()
    window.title("Sign Up")

    message_label = tk.Label(window, text="Create Account", fg="black")
    message_label.pack()

    tk.Label(window, text="Username").pack()
    username_entry = tk.Entry(window)
    username_entry.pack()

    tk.Label(window, text="Password").pack()
    password_entry = tk.Entry(window, show="*")
    password_entry.pack()

    show_var = tk.BooleanVar()
    tk.Checkbutton(window, text="Show Password", variable=show_var, command=toggle_password).pack()

    tk.Button(window, text="Sign Up", command=save_user).pack()

    window.mainloop()

def login_window():

    def login():
        username = username_entry.get()
        password = password_entry.get()

        file = open(file_name, "r")

        for line in file:
            data = line.strip().split(",")
            saved_user = data[0]
            saved_pass = data[1]

            if username == saved_user and password == saved_pass:
                result_label.config(text="Login Successful", fg="green")
                file.close()
                return

        result_label.config(text="Login Failed", fg="red")
        file.close()

    window = tk.Tk()
    window.title("Login")

    tk.Label(window, text="Username").pack()
    username_entry = tk.Entry(window)
    username_entry.pack()

    tk.Label(window, text="Password").pack()
    password_entry = tk.Entry(window, show="*")
    password_entry.pack()

    tk.Button(window, text="Login", command=login).pack()

    result_label = tk.Label(window, text="")
    result_label.pack()

    window.mainloop()

temperature_converter()
what_to_do_today()
#truth_table()
#sign_up()


