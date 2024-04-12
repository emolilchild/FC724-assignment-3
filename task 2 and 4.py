#convert my psuedocode into python syntax
def euclidean_algorithm(num1, num2):
    # repeatedly loop until num 2 becomes 0 so that num 1 can hold the GCD
    while num2 != 0:
        # store the value of num2 into a temporary variable
        temp = num2
        # redefine num2 as the remainder of num1/num2
        num2 = num1 % num2
        # redefine num1 as the previous value of num2 using the temp variable
        num1 = temp
    # when the iteration is done num1 will be the GCD
    return num1
#task 4 accept keyboard inputs
def inputs():
    #ask for inputs
    n1 = int(input("enter the first non-negative number:"))
    n2 = int(input("enter the next non_negative number:"))
    #ensure that inputs are valid
    if n1 < 0 or n2 < 0:
        print("you have entered an invalid input")
        #make the entire code into a function so that i can call this recursively if input is invalid
        return inputs()
    else:
        #return the values if input is valid
        return n1, n2

#prompt user to enter inputs
values = inputs()
#will return inputs as a tuple
#get the values using the index of the tuple
num1 = values[0]
num2 = values[1]
#save GDC inside a variable
GDC = euclidean_algorithm(num1, num2)
#return results
print(f"the GDC is {GDC}")
