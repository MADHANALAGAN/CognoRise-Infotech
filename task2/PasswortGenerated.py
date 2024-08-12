import random 
import string


def generated_password(length): 
    characters=string.ascii_letters + string.digits + string.punctuation
    password="".join(random.choice(characters)for i in range(length))
    print("generated password is :",password)

def check():
    try:
        length=int(input("Enter length of password : "))
        if length < 1:
            print("Invalid input! Please enter integer values")
        else:
          return generated_password(length)
        
    except ValueError:
        print("Invalid input! Please enter numeric values")
if __name__=="main":
    check()
