import random
import string

def generate_random_name():
    first_names = ["John", "Jane", "Alice", "Bob"]
    last_names = ["Smith", "Doe", "Johnson", "Brown"]
    return f"{random.choice(first_names)} {random.choice(last_names)}"

def generate_random_insurance_number():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

# Example usage:
name = generate_random_name()
insurance_number = generate_random_insurance_number()
print(name, insurance_number)
