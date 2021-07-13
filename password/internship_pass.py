import random
import string

def get_random_password(n):
    #少なくとも小文字・大文字・数字・特殊文字は一つ入るように
    random_source = string.ascii_lowercase + string.digits
                    #+ string.punctuation
    password = random.choice(string.ascii_lowercase)
    #password += random.choice(string.ascii_uppercase)
    password += random.choice(string.digits)
    #password += random.choice(string.punctuation)

    for i in range(n-4):
        password += random.choice(random_source)

    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)
    return password

print("Random Password is ", get_random_password(10))
