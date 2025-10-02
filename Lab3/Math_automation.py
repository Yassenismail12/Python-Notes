import math
from Decorators import log_time

def get_valid_numbers():
    """Get and validate comma-separated numbers from user."""
    while True:
        user_input = input("Enter multiple numbers separated by commas: ").strip()
        
        if not user_input:
            print("Please try again with no empty fields")
            continue
        
        try:
            numbers = [float(num.strip()) for num in user_input.split(',')]
            
            if len(numbers) == 0:
                print("No valid numbers entered, Please try again.")
                continue
            
            return numbers
        except ValueError:
            print("Please enter valid numbers separated by commas")

def calculate_math_operations(number):
    """Calculate floor, ceil, sqrt, and circle area for a given number."""
    result = {
        'number': number,
        'floor': math.floor(number),
        'ceil': math.ceil(number),
        'sqrt': math.sqrt(abs(number)) if number >= 0 else None,  
        'circle_area': math.pi * (number ** 2) if number >= 0 else None
    }
    return result

@log_time
def process_numbers_and_save(numbers):
    """Process all numbers and save results to file."""
    results = []
    
    for num in numbers:
        results.append(calculate_math_operations(num))
    
    with open('math_report.txt', 'w' , encoding='utf-8') as file:
        file.write("="*60 + "\n")
        file.write("MATH AUTOMATION REPORT\n")
        file.write("="*60 + "\n\n")
        
        for result in results:
            file.write(f"Number: {result['number']}\n")
            file.write(f"  Floor: {result['floor']}\n")
            file.write(f"  Ceil: {result['ceil']}\n")
            
            if result['sqrt'] is not None:
                file.write(f"  Square Root: {result['sqrt']:.4f}\n")
                file.write(f"  Circle Area (πr²): {result['circle_area']:.4f}\n")
            else:
                file.write("  Square Root: N/A (negative number)\n")
                file.write("  Circle Area: N/A (negative number)\n")
            
            file.write("-"*60 + "\n")
    
    return results

def display_file_content():
    """Read and display the content of math_report.txt."""
    print("\nContent of math_report.txt:")
    print("="*60)
    with open('math_report.txt', 'r', encoding='utf-8') as file:
        content = file.read()
        print(content)
    print("="*60)

def execute_task():
    """Main execution function for Task 1."""
    print("\nMATH AUTOMATION\n")
    numbers = get_valid_numbers()
    print(f"\nProcessing {len(numbers)} numbers...")
    results = process_numbers_and_save(numbers)
    
    print("File 'math_report.txt' created successfully!")
    print(f"Processed {len(results)} numbers")
    display_file_content()