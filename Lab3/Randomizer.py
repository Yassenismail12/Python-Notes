import random
import csv

def get_valid_count():
    while True:
        user_input = input("How many random numbers would you like to generate? ").strip()
        if not user_input:
            print("Error: Input cannot be empty. Please try again.")
            continue
        try:
            count = int(user_input)
            if count <= 0:
                print("Error: Please enter a positive number.")
                continue
            if count > 1000000:
                print("Warning: Generating more than 1 million numbers may take time.")
                confirm = input("Continue? (y/n): ").strip().lower()
                if confirm != 'y':
                    continue
            return count
        except ValueError:
            print("Error: Invalid input. Please enter a valid integer.")

def generate_random_numbers(count):
    print(f"Generating {count} random numbers...")
    numbers = [random.randint(1, 1000) for _ in range(count)]
    print(f"Generated {count} random numbers")
    return numbers

def save_to_csv(numbers):
    filename = 'random_numbers.csv'
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['index', 'value'])
        for index, value in enumerate(numbers, start=1):
            writer.writerow([index, value])
    print(f"Saved numbers to '{filename}'")

def calculate_statistics(numbers):
    total_count = len(numbers)
    average = sum(numbers) / total_count if total_count > 0 else 0
    minimum = min(numbers) if numbers else 0
    maximum = max(numbers) if numbers else 0
    return {
        'count': total_count,
        'average': average,
        'min': minimum,
        'max': maximum
    }

def display_statistics(stats):
    print("\n" + "="*60)
    print("RANDOM NUMBERS STATISTICS")
    print("="*60)
    print(f"Total Count: {stats['count']}")
    print(f"Average: {stats['average']:.2f}")
    print(f"Minimum: {stats['min']}")
    print(f"Maximum: {stats['max']}")
    print("="*60)

def display_sample(numbers, sample_size=10):
    if len(numbers) <= sample_size:
        print("\nAll generated numbers:")
        sample = numbers
    else:
        print(f"\nSample of first {sample_size} numbers:")
        sample = numbers[:sample_size]
    print("   " + ", ".join(map(str, sample)))
    if len(numbers) > sample_size:
        print(f"   ... and {len(numbers) - sample_size} more")

def execute_task():
    print("\nRANDOM DATA GENERATOR\n")
    count = get_valid_count()
    numbers = generate_random_numbers(count)
    save_to_csv(numbers)
    stats = calculate_statistics(numbers)
    display_statistics(stats)
    display_sample(numbers)
