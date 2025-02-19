"""
# PRIOR TO RUNNING:
# Before executing this program, install the required packages by running the following command in the terminal:
# pip install numpy pytest --break-system-packages
#
# NumPy (Numerical Python) is a package used for working with arrays and performing mathematical operations.
# Pytest is used for writing test cases to verify that our functions work correctly.
"""

# Import required packages
import numpy as np  # NumPy helps with numerical computations, such as matrix operations.

# Function to generate a random matrix
def generate_random_matrix(rows, cols):
    """
    Creates a matrix (2D array) of shape (rows, cols) filled with random numbers between 0 and 1.
    
    Parameters:
    rows (int): The number of rows in the matrix.
    cols (int): The number of columns in the matrix.

    Returns:
    numpy.ndarray: A NumPy array (matrix) with random values.
    """
    return np.random.rand(rows, cols)  # Generates a matrix filled with random floating-point numbers.

# Function to calculate the sum of all elements in a matrix
def matrix_sum(matrix):
    """
    Returns the sum of all elements in the given matrix.

    Parameters:
    matrix (numpy.ndarray): A NumPy array (matrix) containing numbers.

    Returns:
    float: The sum of all numbers in the matrix.
    """
    return np.sum(matrix)  # np.sum() adds up all the values in the matrix and returns the total.

# The main part of the script that runs when we execute it directly
if __name__ == "__main__":
    # Generates a 3x3 random matrix (3 rows, 3 columns)
    matrix = generate_random_matrix(3, 3)
    
    # Computes the sum of all elements in the generated matrix
    total = matrix_sum(matrix)

    # Displays the generated matrix and its total sum
    print("Generated Matrix:")  
    print(matrix)  # Prints the matrix as a 2D array
    print("\nSum of all elements:", total)  # Displays the sum of all numbers in the matrix

# TEST CASES (These are used to verify that our functions work correctly)
def test_matrix_shape():
    """
    Test to ensure that the generated matrix has the correct shape.

    This function checks whether `generate_random_matrix(rows, cols)`
    actually creates a matrix with the given number of rows and columns.

    Expected outcome:
    - If rows=3, cols=3, then matrix.shape should be (3,3).
    """
    rows, cols = 3, 3  
    matrix = generate_random_matrix(rows, cols)  #
    assert matrix.shape == (rows, cols)  

def test_matrix_sum():
    """
    Test to ensure that the sum function correctly computes the total sum.

    This function creates a fixed 2x2 matrix with known values and checks
    if `matrix_sum(matrix)` correctly returns the expected total.

    Expected outcome:
    - For the matrix [[1, 2], [3, 4]], the sum should be 10.
    """
    matrix = np.array([[1, 2], [3, 4]])  
    expected_sum = 10  
    assert matrix_sum(matrix) == expected_sum  

