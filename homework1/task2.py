#Use various data types

#Integer test
intTest = 4 + 4

def test_int():
    assert intTest == 8


#Floating point test
floatingPointTest = 4.0 + intTest

def test_fp():
    assert floatingPointTest == 12.0

#Strings test
stringTest = "hello"

def test_string():
    assert "h" in stringTest
    assert "e" in stringTest
    assert "l" in stringTest
    assert "l" in stringTest
    assert "o" in stringTest


#Boolean Test
isFloatMath = isinstance(floatingPointTest,float)

def test_bool():
    assert isFloatMath is True
    assert isinstance(stringTest, str)


