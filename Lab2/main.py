import random


def sort_numbers():
    nums = []
    print("5 numbers:")
    while len(nums) < 5:
        try:
            n = float(input(f"Number {len(nums) + 1}: "))
            nums.append(n)
        except ValueError:
            print("Enter a good number")
    print("Ascending:", sorted(nums))
    print("Descending:", sorted(nums, reverse=True))


def sequence():
    while True:
        try:
            length = int(input("Enter sequence length: "))
            start = int(input("Enter start number: "))
            break
        except ValueError:
            print("values must be integers")
    sequence = list(range(start, start + length))
    print("sequence:", sequence)

def good_or_done():
    nums = []
    while True:
        val = input("Enter a number: (Done to exit) ").strip().lower()
        if val == "done" or val == "Done":
            break
        try:
            nums.append(float(val))
        except ValueError:
            print("enter a good number or 'done'")
    if nums:
        total = sum(nums)
        count = len(nums)
        avg = total / count
        print(f"Total: {total}, Count: {count}, Average: {avg:.2f}")
    else:
        print("No good numbers entered")

def no_doubles():
    while True:
        vals = input("Enter numbers separated by spaces: ").split()
        try:
            nums = [float(v) for v in vals]
            break
        except ValueError:
            print("Please enter numbers only")
    unique_sorted = sorted(set(nums))
    print("No duplicates, sorted:", unique_sorted)

def word_count():
    str = input("Enter a sentence: ").lower()
    words = str.split()
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    print("Word counts:")
    for word, count in counts.items():
        print(f"{word}: {count}")

def grade_book():
    students = {}
    while len(students) < 5:
        name = input(f"Enter student {len(students) + 1} name: ").strip()
        try:
            score = float(input(f"Enter {name}'s score: "))
            students[name] = score
        except ValueError:
            print("enter a number")
    scores = list(students.values())
    print("Highest score:", max(scores))
    print("Lowest score:", min(scores))
    print("Average score:", sum(scores) / len(scores))

def shopping():
    cart = {}
    while True:
        print("\nShopping Cart options:")
        print("1. Add item")
        print("2. Remove item")
        print("3. View items")
        print("4. Checkout")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            name = input("Enter item name: ").strip()
            try:
                price = float(input("Enter item price: "))
                cart[name] = price
            except ValueError:
                print("price be a number")
        elif choice == "2":
            name = input("Enter item name to remove: ").strip()
            if name in cart:
                del cart[name]
                print(f"{name} removed")
            else:
                print("item not found in cart")
        elif choice == "3":
            if cart:
                for item, price in cart.items():
                    print(f"{item}: {price}")
            else:
                print("Cart is empty")
        elif choice == "4":
            total = sum(cart.values())
            print(f"Total cost: {total}")
            break
        else:
            print("select options from: 1, 2, 3, 4.")

def guessing():
    target = random.randint(1, 20)
    attempts = 0
    print("Guess the number (between 1 and 20)")
    while True:
        try:
            guess = int(input("Your guess: "))
            attempts += 1
            if guess < target:
                print("Too low!")
            elif guess > target:
                print("Too high!")
            else:
                print(f"Correct guess, The number was {target}. Attempts: {attempts}")
                break
        except ValueError:
            print(" enter an integer only")

def main():
    tasks = {
        "1": sort_numbers,
        "2": sequence,
        "3": good_or_done,
        "4": no_doubles,
        "5": word_count,
        "6": grade_book,
        "7": shopping,
        "8": guessing,
    }

    while True:
        print("\nLab 2")
        for k in sorted(tasks.keys(), key=int):
            print(f"{k}: Task {k}")
        print("0: Exit")

        choice = input("Choose a task number: ").strip()
        if choice == "0":
            print("Exiting..")
            break
        elif choice in tasks:
            tasks[choice]() 
        else:
            print("select a valid task number")

main()
