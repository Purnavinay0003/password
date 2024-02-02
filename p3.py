import string
import random

plen = int(input("Enter password length:\n"))
lowercase_letters = int(input("Enter the number of lowercase letters:\n"))
uppercase_letters = int(input("Enter the number of uppercase letters:\n"))
digits = int(input("Enter the number of digits:\n"))
symbols = int(input("Enter the number of symbols (punctuation):\n"))

if __name__ == "__main__":
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation

    s = []
    s.extend(random.choices(s1, k=lowercase_letters))
    s.extend(random.choices(s2, k=uppercase_letters))
    s.extend(random.choices(s3, k=digits))
    s.extend(random.choices(s4, k=symbols))

    random.shuffle(s)

    if len(s) >= plen:
        password = "".join(s[:plen])
        print("Your password is:", password)
    else:
        print("Insufficient characters to generate the password.")
