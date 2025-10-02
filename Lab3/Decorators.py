import time
import functools
from datetime import datetime

def log_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] Function '{func.__name__}' executed in {execution_time:.4f} seconds\n"
        with open('execution_log.txt', 'a', encoding='utf-8') as file:
            file.write(log_entry)
        return result
    return wrapper

@log_time
def example_fast_function():
    time.sleep(0.1)
    return "Fast function completed"

@log_time
def example_slow_function():
    time.sleep(0.5)
    return "Slow function completed"

def display_execution_log():
    try:
        print("\nExecution Log Contents:")
        print("="*70)
        with open('execution_log.txt', 'r', encoding='utf-8') as file:
            content = file.read()
            if content:
                print(content)
            else:
                print("No log entries yet.")
        print("="*70)
    except FileNotFoundError:
        print("\nNo execution log file found yet.")
        print("The log will be created when decorated functions are executed.")

def clear_execution_log():
    with open('execution_log.txt', 'w', encoding='utf-8') as file:
        file.write("")
    print("Execution log cleared")

def execute_task():
    print("\nDECORATORS TASK - Execution Time Logger\n")
    print("This decorator logs the execution time of functions.")
    print("It has been applied to:")
    print("  - Task 1: Math Automation (process_numbers_and_save)")
    print("  - Task 2: Regex Log Cleaner (process_logs)")
    print("\nRunning test functions to demonstrate the decorator...\n")
    print("Running example_fast_function()...")
    result1 = example_fast_function()
    print(f"{result1}")
    print("\nRunning example_slow_function()...")
    result2 = example_slow_function()
    print(f"{result2}")
    print("\nBoth functions executed and logged!")
    display_execution_log()
    print("\nTip: Run Task 1 or Task 2 to see the decorator in action!")
    print("The execution times will be automatically logged.")
