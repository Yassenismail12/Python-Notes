import Math_automation
import Regex
import Reminder
import Transformer
import FileManager
import Randomizer
import Decorators

def display_menu():
    """Display the task menu to the user."""
    print("\n" + "="*50)
    print("Select a task to execute")
    print("="*50)
    print("1. Math Automation")
    print("2. Regex Log Cleaner")
    print("3. Datetime Reminder Script")
    print("4. Product Data Transformer")
    print("5. OS File Manager")
    print("6. Random Data Generator")
    print("7. Decorators Task")
    print("0. Exit")
    print("="*50)

def get_valid_choice():
    """Get and validate user's menu choice"""
    while True:
        try:
            choice = input("\nEnter task number (0-7): ").strip()
            choice_num = int(choice)
            if 0 <= choice_num <= 7:
                return choice_num
            else:
                print("Please enter a number between 0 and 7")
        except ValueError:
            print("Invalid input. Please enter a valid number")

def run_selected_task(choice):
    """Execute the selected task."""
    print("\n" + "-"*50)
    
    if choice == 1:
        print("Running Task 1: Math Automation")
        print("-"*50)
        Math_automation.execute_task()
    elif choice == 2:
        print("Running Task 2: Regex Log Cleaner")
        print("-"*50)
        Regex.execute_task()
    elif choice == 3:
        print("Running Task 3: Datetime Reminder Script")
        print("-"*50)
        Reminder.execute_task()
    elif choice == 4:
        print("Running Task 4: Product Data Transformer")
        print("-"*50)
        Transformer.execute_task()
    elif choice == 5:
        print("Running Task 5: OS File Manager")
        print("-"*50)
        FileManager.execute_task()
    elif choice == 6:
        print("Running Task 6: Random Data Generator")
        print("-"*50)
        Randomizer.execute_task()
    elif choice == 7:
        print("Running Task 7: Decorators Task")
        print("-"*50)
        Decorators.execute_task()
    
    print("-"*50)

if __name__ == "__main__":
    print("\n Day 3 Lab")
    
    while True:
        display_menu()
        choice = get_valid_choice()
        
        if choice == 0:
            print("\nExiting..")
            break
        
        run_selected_task(choice)
        
        continue_choice = input("\nWould you like to run another task? (y/n): ").strip().lower()
        if continue_choice != 'y':
            print("\nExiting...")
            break