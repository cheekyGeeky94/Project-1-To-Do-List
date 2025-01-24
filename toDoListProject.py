def welcome_user():
    print("Hello! Welcome to the List App!")                                                                        #This will be the first line of code when the program starts

welcome_user()                                                                                                      #I have the function called so that it is the first line of code

my_tasks = []                                                                                                       #This is the empty list that is created

def main_menu():
    print("Main Menu:")                                                     #This function has the main menu list the choices and the user has to enter one of the numbers to select
    print("*************************")                                                                              #I just wanted to make it look good lol
    print("1. Add Tasks")                                                                                           #What they want to do/where they want to go in the program
    print("2. View Tasks")
    print("3. Delete Tasks")
    print("0. Quit Application")                                                                                    #I will be calling the "main menu" "MM" for short

    
main_menu()

choice = input("Enter a number from the menu to choose your option: ")                                              #This line allows the user to enter a number from the MM


def option_add():
    while True:
        task = input("Enter the task you would like to add to your list. If you are done, type 'done': ")           #This allows the user to enter a task
        if (task == "done") or (task == "Done") or (task == "DONE"):                                                                                          #This condition will break and send the user to the MM
            break                                                                                                   #This breaks the loop and starts you back to the MM
        my_tasks.append(task)                                                                                       #I wanted to notify the user that a task has been added
        print(f"Task '{task}' has been added!")

def option_view():
    print(f"Here are your list of tasks thus far: {my_tasks}")
    if my_tasks == []:
        print("You have not added any tasks 🤷‍♀️")                                                                   #If no tasks were added the user will be notified

def option_delete():
        while True:                                                                                                #Yes, another loop. I wanted to get my practice in
            if my_tasks == []:
                print("You have no tasks to delete 🤷‍♀️")                                                            #User gets notified if there are no tasks, sent to MM
                break
            task = input("Enter the task you would like to remove from your list. If you are done, type 'done': ")  #The user has to enter their task to delete
            if (task == "done") or (task == "Done") or (task == "DONE"):
                break                                                                                               #This condition will berak the loop and start you back to the MM
            try:
                my_tasks.remove(task)                                                                               #If nothing in the list is entered by the user, the code will break
            except:
                print("🚫 This task does not exist. Please try again. 🚫")                                         #This exception will give this error instead of the code breaking
            else:
                print(f"{task} has been removed ❌.")                                                               #if there are no other exceptions the code will run as normal
            finally:
                print(f"This is your list: {my_tasks}")                                                             #Display the list to show it was deleted, will display even after error


def option_choose(choice):
    while choice != "0":                                                                                            #I have created so many loops I know, but it works 😂
        if choice == "1":                                                                                           #Anyway, the user must choose 1, 2, or 3 and the
            option_add()                                                                                            #corresponding function will be called
        elif choice == "2":
            option_view()
        elif choice == "3":
            option_delete()
        else:
            print("Invalid option. Please try again!")                                                              #This will happen if you don't enter 0, 1, 2, or 3
        print()                                                                                                     #This is just an empty print statement to have gaps
        main_menu()                                                                                                 #You go back to the MM if an invalid option is entered
        choice = input("Enter a number from the menu to choose your option: ")                                      #Entered this again because it is not in a function 😁
    print("You have quit the application. Goodbye!🙋‍♀️")                                                             #This prompts when you enter 0 and the program ends
option_choose(choice)
