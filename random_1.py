import random
import string

def generate_random_name():
    first_names =  [
        "Aarav", "Ananya", "Kabir", "Avni", "Vihaan", "Advik", "Aanya", "Shaurya", "Diya", "Aadi",
        "Aaradhya", "Ishaan", "Navya", "Aryan", "Saisha", "Reyansh", "Anika", "Arjun", "Riya", "Samarth",
        "Myra", "Kabir", "Ananya", "Rudra", "Pari", "Vihaan", "Aadya", "Vivaan", "Aanya", "Kian",
        "Avni", "Aarush", "Kiara", "Arnav", "Aashi", "Aryan", "Saanvi", "Aarav", "Avani", "Aadi",
        "Neha", "Kabir", "Anika", "Aarav", "Anaya", "Veer", "Ishika", "Aarush", "Aadhya", "Shaurya",
        "Navya", "Arjun", "Vihaan", "Anvi", "Advik", "Myra", "Aahana", "Vivaan", "Anaya", "Arnav",
        "Aarav", "Diya", "Aryan", "Saanvi", "Reyansh", "Ananya", "Kabir", "Aaradhya", "Avni", "Vihaan",
        "Aadya", "Advik", "Aanya", "Aarush", "Shaurya", "Anika", "Arjun", "Riya", "Samarth", "Myra",
        "Kabir", "Ananya", "Rudra", "Pari", "Vihaan", "Aadya", "Vivaan", "Aanya", "Kian", "Avni",
        "Aarush", "Kiara", "Arnav", "Aashi", "Aryan", "Saanvi", "Aarav", "Avani", "Aadi", "Neha"
    ]

    last_names =  [
        "Mehta", "Chauhan", "Verma", "Sharma", "Reddy", "Patel", "Singh", "Gupta", "Malhotra", "Khanna",
        "Bajaj", "Sinha", "Deshmukh", "Joshi", "Gandhi", "Rawat", "Pillai", "Rao", "Nair", "Iyer",
        "Shah", "Menon", "Kumar", "Saxena", "Rastogi", "Chopra", "Balaji", "Sarin", "Prasad", "Gupta",
        "Das", "Srivastava", "Venkat", "Iyer", "Choudhury", "Bose", "Acharya", "Ranganathan", "Rajagopal", "Vaidya",
        "Sharma", "Malik", "Narayan", "Rao", "Krishnan", "Kulkarni", "Reddy", "Thakur", "Shah", "Kumar",
        "Sengupta", "Chakraborty", "Bhat", "Gupta", "Singhania", "Venkatesh", "Menon", "Dixit", "Chandra", "Mukherjee",
        "Naidu", "Sharma", "Rangan", "Vaid", "Reddy", "Prakash", "Dutta", "Krishnamurthy", "Kapoor", "Soni",
        "Goswami", "Trivedi", "Verma", "Narang", "Pandey", "Rathore", "Gupta", "Sarin", "Chopra", "Verma",
        "Malhotra", "Rajput", "Mehra", "Dewan", "Bajaj", "Khatri", "Nair", "Chopra", "Shah", "Srivastava",
        "Iyer", "Choudhury", "Bhatia", "Narayan", "Sengupta", "Iyer", "Chakraborty", "Krishnan", "Mukherjee", "Naidu"
    ]

    return f"{random.choice(first_names)} {random.choice(last_names)}"

def generate_random_insurance_number():
    return ''.join(str(random.randint(1,100000)))
# Example usage:
name = generate_random_name()
insurance_number = generate_random_insurance_number()
print(name, insurance_number)
