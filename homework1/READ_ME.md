Explanations: 
Task 1:

message = "Hello, World!"
print(message)

def test_output():
    assert message == "Hello, World!"

 Here I just created a variable that contained the appropriate message, then I used pytest to ensure the message was exactly as intended.

Task 2: 
For task two, I used various datatypes, such as int, string, and float.

For the int portion, i added two numbers:
    intTest = 4 + 4
Then, I tested in within a pytest, i know the answer SHOULD be 8: 
    assert intTest == 8

Next, for floating points I added an integer from the previous calculations and a float.
    floatingPointTest = 4.0 + intTest
I know the answer should be a float, thus the pytest is as follows. 
    assert floatingPointTest == 12.0
    NOTE: This did not work when using floatingPointTest == 12

For Strings, i created a variable, then used the singular character in the word to try something new. 
    stringTest = "hello"

    assert "h" in stringTest
    assert "e" in stringTest
    assert "l" in stringTest
    assert "l" in stringTest
    assert "o" in stringTest


The function check_number(numberGiven) evaluates the input and returns:
    "The number is positive" if greater than 0.
    "The number is negative" if less than 0.
    "The number is 0" if exactly 0.

The pytest test case ensures that the function behaves as expected:
    assert check_number(10) == "The number is positive"
    assert check_number(-5) == "The number is negative"
    assert check_number(0) == "The number is 0"

Then, I created a function getPrimes(maxNum) to generate the first maxNum prime numbers.
This function generates the first maxNum prime numbers and returns them in a list.

    Initialize an empty list (primeList) to store prime numbers.
    Use counter to track how many primes have been found, starting at 1.
    Start checking numbers from 2 (currentNum = 2).
    Loop until counter reaches maxNum:
    Assume currentNum is prime (isPrime = True).
    Check divisibility by all numbers up to sqrt(currentNum).
    If any number evenly divides currentNum, it is not prime (isPrime = False).
    If isPrime remains True, add the number to primeList and increment counter.
    Increment currentNum and continue the loop until maxNum primes are found
    
    I tested this using pytest by creating a list I knew was correct:
        firstTenPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    Then was able to assert and test if the list i created was right. 


Next was the sum loop
Explanation:
This function calculates the sum of numbers from 1 to num using a while loop.

    Initialize sum = 0 to store the cumulative total.
    Start a counter at 1.
    Loop until counter exceeds num:
    Add counter to sum.
    Increment counter by 1.
    Return the total sum.

This was then tested in pytest by utilizing python
    realSum = sum(range(1, 101))
    assert sumLoop(100) == realSum
When done like this, I can test without room for potential calculation errors, I also checked this with a quick google search.


Task 4: 
def calculate_discount(price, discount):
    Takes a product's price and discount percentage.
    Computes the discounted price using:
        Final Price=Price×(1−Discount/100)
    Uses round(finalPrice, 2) to ensure currency formatting.

I did some checking with both integers and floats by calculating by hand and hardcoding this information:
    # Testing Integers
    def test_discountInt():
        assert calculate_discount(100, 20) == 80
        assert calculate_discount(50, 10) == 45

    # Testing Floats
    def test_discountFloat():
        assert calculate_discount(36.0, 15.0) == 30.60
        assert calculate_discount(45.0, 10.0) == 40.50


Task 5: 
Here, i created a list of my favorite books, for slicing i know i could just use firstThree = favBooks[:3]. 

However, I was curious and couldn't remember the exact syntax on how to split just the title (strings sliving). Thus, I used ChatGpt, which seemed to have an issue with understanding what I was asking but I was able to connect the dots.
    Link to chat here: https://chatgpt.com/share/67b50f4a-26d0-8012-83b5-6105361f2e43

This was not relevant to the project, thus i stuck with firstThree = favBooks[:3].

I used pytest here by manually inserting the first three in the list and seeing it the slicing worked. 
    def test_list():
    assert firstThree == ['Lord of the Rings by J.R.R Tolkien', 'Miseducation of Cameron Post by Emily M. Danforth', 'The Way of Kings by Brandon Sanderson']

Then came the database portion, which i used the key as the student id.
To test, i ensured the correct key was with the correct student:
     assert student_database[1001] == "Alice Johnson"
I also used a different method using .get:
    assert student_database.get(1009) == "Ian Cooper"


Task 6: 
Dynamically Resolving the File Path
    Uses os.path.abspath(__file__) to get the script's directory.
    Constructs the full path to "task6_read_me.txt" using os.path.join(BASE_DIR, "task6_read_me.txt").
    Ensures the file can be accessed correctly, no matter where the script is executed.
        (NOTE: THIS WAS IT CAN BE RAN THROUGH A CONTAINER)
Counting Words in a File
    Opens the file in read mode ("r") with UTF-8 encoding.
    Uses .split() to separate words by whitespace.
    Returns the total word count.
    If the file doesn’t exist, raises a FileNotFoundError 
Metaprogramming for Dynamic Test Function Creation
    Defines generate_test(filename, expectedCount), which:
    Creates and returns a function that checks if countWords(filename) matches expectedCount.
    Generates a unique function name dynamically based on the filename (test_task6_read_me).
    Uses globals() to register the generated test function, so pytest can automatically detect and execute it.


Task 7: 
This is explained through the comments in the code! 