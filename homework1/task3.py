# Function to check if a number is positive, negative, or zero
def check_number(numberGiven):
    if numberGiven > 0:
        return "The number is positive"
    elif numberGiven < 0:
        return "The number is negative"
    else:
        return "The number is 0"

# Function to get prime numbers
def getPrimes(maxNum):
    primeList = []
    counter = 1
    currentNum = 2

    while counter < maxNum + 1:
        isPrime = True
        for i in range(2, int(currentNum**0.5) + 1):
            if currentNum % i == 0:
                isPrime = False  
        
        if isPrime:
            primeList.append(currentNum)
            counter += 1  

        currentNum += 1

    return primeList

#Adds a numbers together
def sumLoop (num):
    counter = 1
    sum = 0
    while(counter <= num):
        sum += counter
        counter += 1
    return sum    

    


if __name__ == "__main__":
    try:
        userInput = int(input("Please enter any number: "))
        print(check_number(userInput))
    except ValueError:
        print("Please enter a number only")

    # Print first 10 prime numbers
    print("First 10 Prime Numbers:", getPrimes(10))

    #Printing sum of numbers from 1-100
    print("Added sum of 1-100:", sumLoop(100))


#Testing functionality of pos/neg number check
def test_check_number():
    assert check_number(10) == "The number is positive"
    assert check_number(-5) == "The number is negative"
    assert check_number(0) == "The number is 0"

#Testing functionality if prime numbers are correct for first 10
def test_primes():
    firstTenPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    assert getPrimes(10) == firstTenPrimes

#Testing functionality of sum loop 
def test_sum():
    realSum = sum(range(1, 101))
    assert sumLoop(100) == realSum


