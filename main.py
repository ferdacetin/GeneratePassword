import random
import string

def generate_password(length, level, output=[]):
    chars = string.ascii_letters
    if level > 1:
        chars = "{}{}".format(chars, string.digits)
    if level > 2:
        chars = "{}{}".format(chars, string.punctuation)

    for i in range (length):
        output.append(random.choice(chars))

    return "".join(output)
print(("-"*30) + "Password Generator" + ("-"*30))

password_length = int(input("Length : "))
password_level = int(input("Level :"))

password = generate_passaword(password_length, password_level)
print("Your password is : {}".format (password))