#write pseudocode for the Euclidean Algorithm
def gcd(num1, num2):
    #repeatedly loop until num 2 becomes 0 so that num 1 can hold the GCD
    while num2 != 0:
        #store the value of num2 into a temporary variable
        temp = num2
        #redefine num2 as the remainder of num1/num2
        num2 = num1 mod num2
        #redefine num1 as the previous value of num2 using the temp variable
        num1 = temp
    #when the iteration is done num1 will be the GCD
    return num1