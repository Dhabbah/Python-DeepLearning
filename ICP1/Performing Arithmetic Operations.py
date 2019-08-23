#This function is to do perfprm arithmetic operations on the given numbers by the user
def operations(num1, num2):
    print("You have entered the number %s and %d" % (Enumber1, Enumber2))
    print("The addition of these two numbers is: " + str(Enumber1 + Enumber2))
    print("The subtraction of these two numbers is: " + str(Enumber1 - Enumber2))
    print("The multiplication of these two numbers is: " + str(Enumber1 * Enumber2))
    print("The division of these two numbers is: " + str(Enumber1 / Enumber2))
    print("The Quotient is " + str(int(Enumber1 / Enumber2)) + " and the remainder is " + str(int(Enumber1 % Enumber2)))

#To enter two numbers by the user
Enumber1 = float(input("Please type the first number:"))
Enumber2 = float(input("Please type the first number:"))
#Calling the function
operations(Enumber1, Enumber2)