# Author: Jessica Strait
# This project reads a list of names and their popularity. It takes a name as input and interprets its popularity from this file.
# Our program will find a name's popularity based on a list derived from a file. 

#First, open up the girls' name file and get ready to read. We can create a list using a "while" loop. 
#We use "rstrip" to remove the new line symbol. Once all names are on our list, close the file.

girls = open(r'C:\users\jessl\Desktop\GirlNames.txt', 'r')
girlName = girls.readline()

girls_list = []
while girlName != "":
    girlName = girlName.rstrip('\n')
    girls_list.append(girlName)
    girlName = girls.readline()

girls.close()

# We can repeat the same process to create a list from the boys' file.

boys = open(r'C:\users\jessl\Desktop\BoyNames.txt', 'r')
boyName = boys.readline()

boys_list = []
while boyName != "":
    boyName = boyName.rstrip('\n')
    boys_list.append(boyName)
    boyName = boys.readline()

boys.close()

# We are ready for input. We will tell the user to pick "name" or stop. We must prompt the user to do this with each iteration of our "while" loop. The easiest way to account for any "name"
#(girls' name but not boys, vice versa, both, neither) is with a "while" loop and nested "if" statements. We should look in both lists, and use the index function to identify the location.

name = input("Enter a name to see its popularity, or enter stop to end the program.")

while name != "stop":
    if name in girls_list:
        print(name, "is a popular girls' name and it is ranked:", girls_list.index(name)+1)
        if name in boys_list:
            print(name, "is a popular boys' name and it is ranked:", boys_list.index(name)+1)
            name = input("Enter a name to see its popularity, or enter stop to end the program.")
        else:
            print(name, "is not a popular boys' name.")
            name = input("Enter a name to see its popularity, or enter stop to end the program.")
    elif name in boys_list:
        print(name, "is not a popular girls' name.")
        print(name, "is a popular boys' name and it is ranked:", boys_list.index(name)+1)
        name = input("Enter a name to see its popularity, or enter stop to end the program.")
    else:
            print(name, "is not a popular girls' or boys' name.")
            name = input("Enter a name to see its popularity, or enter stop to end the program.")