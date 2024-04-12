#psuedocode of the extended euclidean algorithm
extended_euclidean_alogorithm(num1, num2):
    #identify the base case of this algorithm
    #base case is that if num2 is 0 means that num1 is the GCD
    if num2 == 0:
        # it also means that the coefficients are 1 and 0
        return num1, 1, 0
    else:
        #recusively call the function to find the GCD, and the two coefficients
        #the two coefficients represent how the GCD of two numbers can be expressed as a combination of those numbers
        gdc, x, y = extended_euclidean_alogorithm(num2, num1%num2)
        #assign current value of y to x
        #calculate the new y using the formula
        #swap x and y
        x , y = y, x - (num1//num2) *y
        return gcd, z, i
