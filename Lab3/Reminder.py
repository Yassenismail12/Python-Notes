from datetime import datetime


def get_valid_date():
    while True:
        date_input = input("Enter a date (YYYY-MM-DD): ").strip()
        if not date_input:
            print("Error: Date cannot be empty. Please try again.")
            continue
        try:
            target_date = datetime.strptime(date_input, "%Y-%m-%d")
            return target_date
        except ValueError:
            print(
                "Error: Invalid date format. Please use YYYY-MM-DD (e.g., 2025-12-31)."
            )


def calculate_days_remaining(target_date):
    today = datetime.now()
    today = datetime(today.year, today.month, today.day)
    target_date = datetime(target_date.year, target_date.month, target_date.day)
    delta = target_date - today
    days_left = delta.days
    return days_left


def save_reminder(date_str, days_left):
    with open("reminders.txt", "a", encoding='utf-8') as file:
        file.write(f"{date_str} -> {days_left} days left\n")


def execute_task():
    print("\nDATETIME REMINDER SCRIPT\n")
    target_date = get_valid_date()
    date_str = target_date.strftime("%Y-%m-%d")
    days_left = calculate_days_remaining(target_date)
    if days_left < 0:
        print("\nThis date has already passed.")
        print(f"{date_str} was {abs(days_left)} days ago.")
    elif days_left == 0:
        print("\nThis date is TODAY!")
        save_reminder(date_str, days_left)
        print("Reminder saved to 'reminders.txt'")
    else:
        print(f"\n{days_left} days remaining until {date_str}")
        save_reminder(date_str, days_left)
        print("Reminder saved to 'reminders.txt'")
    try:
        print("\nAll saved reminders:")
        print("=" * 50)
        with open("reminders.txt", "r", encoding='utf-8') as file:
            content = file.read()
            if content:
                print(content)
            else:
                print("No reminders saved yet.")
        print("=" * 50)
    except FileNotFoundError:
        print("No reminders file found yet.")
