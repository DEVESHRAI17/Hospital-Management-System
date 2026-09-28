def get_positive_int(prompt):
    while True:
        try:
            val = int(input(prompt))
            if val <= 0:
                print("Error: Value must be a positive integer.")
                continue
            return val
        except ValueError:
            print("Error: Invalid input. Please enter a number.")

def get_positive_float(prompt):
    while True:
        try:
            val = float(input(prompt))
            if val < 0:
                print("Error: Amount cannot be negative.")
                continue
            return val
        except ValueError:
            print("Error: Invalid input. Please enter a valid decimal number.")

def get_non_empty_string(prompt):
    while True:
        val = input(prompt).strip()
        if not val:
            print("Error: Input cannot be empty.")
            continue
        return val