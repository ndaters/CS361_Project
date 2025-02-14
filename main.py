import pyttsx3

import os
import time
import sys
import csv


def write_data(data):
    with open("To-Do.txt", "a") as file:
        file.write(data + "\n")


def read_data():
    if os.path.exists("To-Do.txt"):
        with open("To-Do.txt", "r") as file:
            print("Current To Do List: \n"
                  "------------------")
            for line in file:
                print(line.strip())
            return file.readlines()
    else:
        return []


def search_data(criteria):
    results = []
    for line in read_data():
        if criteria in line:
            results.append(line.strip())
    return results


def update_data( old_data, new_data):
    lines = read_data()
    with open("To-Do.txt", "w") as file:
        for line in lines:
            if old_data in line:
                file.write(new_data + "\n")
            else:
                file.write(line)


def delete_data(data_to_delete):
    with open("To-Do.txt", 'r') as f:
        lines = f.readlines()

    with open("To-Do.txt", 'w') as f:
        for line in lines:
            if data_to_delete not in line:
                f.write(line)


user_names_passwords = {"Joe": "joerules"}


def login_credentials():
    print("""
      ___________________   ___________________
  .-/|       ~~**~~      \ /      ~~**~~       |\-.
  ||||                    :                    ||||
  ||||   To Do:           :                    ||||
  ||||   Create To Do List:                    ||||
  ||||                    :                    ||||
  ||||                    :                    ||||
  ||||                    :                    ||||
  ||||                    :                    ||||
  ||||                    :                    ||||
  ||||                    :                    ||||
  ||||                    :                    ||||
  ||||                    :                    ||||
  ||||___________________ : ___________________||||
  ||/====================\:/====================\||
  `---------------------~___~--------------------''""")
    username = input('Enter Username: ')
    user_password = input('Enter Password: ')
    if str(username) in user_names_passwords:
        if user_names_passwords[username] == user_password:
            print("Welcome back " + username)
            return True
    print('Username and Password not recognized')
    return False


def header():
    print("***************** \nMy To Do List App \n*****************")


def tagline():
    print("Never Forget Anything Ever Again!")


def show_main_menu():
    header()
    tagline()
    print("""   
1: Add something to My To Do List
2: See Current To Do List
3: Delete something from My To Do List
4: About
5: Exit Program
6: Another way to see Current To Do List""")


def user_choice():
    choice = int(input("Select a choice: "))
    return choice


def about():
    print("""This program was design to help users keep track of their To Do List""")


def process_user_choice(choice):
    if choice == 1:
        data = input('Enter a task to add: ')
        double_check = input('Are you sure you want to add task: ' + data + "?\nreply yes or no")
        if double_check == "yes":
            print("Hold Please..")
            write_data(data)
            print('Your task has been added to your To Do List.\n'
                  'You can modify, complete or delete this task at any time')
        if double_check == "no":
            print("Task not added")
    elif choice == 2:
        read_data()
    elif choice == 3:
        data = input('Enter task to delete: ')
        print("Hold Please..")
        delete_data(data)
    elif choice == 4:
        about()
    elif choice == 5:
        sys.exit()
    elif choice == 6:
        read_data()


if __name__ == "__main__":
    header()
    time.sleep(1)
    tagline()
    time.sleep(1)
    login_credentials()
    filename = next(iter(user_names_passwords))
    while True:
        show_main_menu()
        choice = user_choice()
        process_user_choice(choice)
        time.sleep(2)
