import string

from random import*
characters = string.ascii_letters + string.punctuation + string.digits
password = "".join(choice(characters)for x in range(randint(8,8)))
print("Password Generator")
print()
print("Your new password is: " + password)
