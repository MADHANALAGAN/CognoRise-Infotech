from arithmetic_operator import *


def calculator():
        print("*"*35)
        print("Welcome to the simple calculator!")
        print("*"*35)
        print("Addition as 1")
        print("Subtraction as 2")
        print("Multiplication as 3")
        print("Division as 4")
        print("Floor division as 5")
        print("Modulo as 6")
        print("Exponentiation as 7")
        print(" ")
        choice=int(input("Enter you choice(1 to 7) :"))

        
        if choice not in (1,2,3,4,5,6,7):
            print("."*20)
            print("GIVE PROPER CHOICE ")
            print("."*20)
            print(" ")
            return calculator()
            
        else:
        
            try:
                number1=float(input("Enter number1 :"))
                number2=float(input("Enter number2 :"))
            except ValueError:
                print("."*35)
                print("Invalid input! Please enter numeric values.")
                print("."*35)
                print(" ")
                return calculator()  
        
        
        if choice == 1:
                print(f"Addition of {number1} and {number2} is :{addition(number1,number2)}")
        elif choice == 2:
                print(f"Subtraction of {number1} and {number2} is :{subtraction(number1,number2)}")
        elif choice == 3:
                print(f"Multiplication of {number1} and {number2} is :{multiplication(number1,number2)}")
        elif choice == 4:
                print(f"Division of {number1} and {number2} is :{division(number1,number2)}")
        elif choice == 5:
            print(f"Floor division of {number1} and {number2} is :{floordivision(number1,number2)}")
        elif choice == 6:
            print(f"modulo of {number1} and {number2} is : {modulo(number1,number2)}")
        else:
            print(f"Exponentiation of {number1} and {number2} is : {exponentiation(number1,number2)}")
        print(" ")
        return again_calculator()


def again_calculator():
    again=input("Do you want again_calculator say(yes/no) :").lower()
    if again =="yes":
          return calculator()
    else:
          print("THANK YOU ! for using the calculator.")
 
if __name__=="__main__":
      calculator()
       
      

