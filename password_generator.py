import random
import string


letters = string.ascii_uppercase + string.ascii_lowercase
punctuation = "!@#&%?"
digits = string.digits

password_characters = letters + punctuation + digits

print("----PASSWORD GENERATOR----")

pass_length= int(input("What should be the length of your password? "))

password = ''.join(random.choice(password_characters) for _ in range(pass_length))
print("Generated password :" , password)















