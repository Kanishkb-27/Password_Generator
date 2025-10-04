import random
import string
def new_password(length):
    char=string.ascii_letters+string.digits+string.punctuation
    password=''.join(random.choices(char,k=length))
    return password
user_len=int(input("Enter the length of the password you want"))
user_password=new_password(user_len)
print(f"New password suggestion: {user_password}")