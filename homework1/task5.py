#Create a list of favorite book title with author
favBooks = ["Lord of the Rings by J.R.R Tolkien", "Miseducation of Cameron Post by Emily M. Danforth", 
"The Way of Kings by Brandon Sanderson", "Brain on Fire by Susannah Cahalan", "Priory of The Orange Tree by Samantha Shannon"]

#Use list slicing to print the first three books in the list.
keyWord = "by" 
indexNumber = 0

#This is testing list slicing using strings
while (indexNumber < 3):
    wholePortion = favBooks[indexNumber]
    justTitle = wholePortion.find(keyWord)

    justTitle = wholePortion[:justTitle].strip()
    print(justTitle)
    indexNumber +=1


firstThree = favBooks[0:3]
print(firstThree)

#Testing if the correct information was printed
def test_list():
    assert firstThree == ['Lord of the Rings by J.R.R Tolkien', 'Miseducation of Cameron Post by Emily M. Danforth', 'The Way of Kings by Brandon Sanderson']



#Create a dictionary that represents a basic student database
#Include: Student names, ID Number

student_database = {
    1001: "Alice Johnson",
    1002: "Bob Smith",
    1003: "Charlie Davis",
    1004: "Dana Lee",
    1005: "Ethan Brown",
    1006: "Fiona White",
    1007: "George Adams",
    1008: "Hannah Scott",
    1009: "Ian Cooper",
    1010: "Julia Martinez"
}

def test_studentDatabase():
    assert student_database[1001] == "Alice Johnson"
    assert student_database[1010] == "Julia Martinez"

def test_Database():
    assert student_database.get(1009) == "Ian Cooper"

