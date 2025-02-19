import os

# Dynamically generate the absolute path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "task6_read_me.txt")

# Function to count words in a file
def countWords(filename):
    if not os.path.exists(filename):
        raise FileNotFoundError(f"File '{filename}' not found. Check your file path!")

    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()
        words = text.split()
        return len(words)

if __name__ == "__main__":
    wordCount = countWords(FILE_PATH)
    print(f"The file {FILE_PATH} contains {wordCount} words.")

# Implement metaprogramming techniques to dynamically generate function names for test cases
def generate_test(filename, expectedCount):
    def test_function():
        assert countWords(filename) == expectedCount
    return test_function

# Expected word count from task6_read_me.txt
EXPECTED_WORD_COUNT = 127

# Generate test function name correctly
test_func_name = f"test_{os.path.splitext(os.path.basename(FILE_PATH))[0]}"
globals()[test_func_name] = generate_test(FILE_PATH, EXPECTED_WORD_COUNT)

