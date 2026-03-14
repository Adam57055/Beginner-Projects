#Following the pythagorean theorem, sides will be squared when inputted by user
while True:
    side_1 = int(input("Enter a side: ")) ** 2
    side_2 = int(input("Enter another side: ")) ** 2
    side_3 = int(input("Enter another side: ")) ** 2
#Statements from outcomes are outlined
    statement = "\nThis is a pythagorean triple."
    not_statement = "\nThis is not a pythagorean triple."
#Hypotenuse is determined as the largest side
    triangle = [side_1, side_2, side_3]
    hypotenuse = max(triangle)
#Hypotenuse is taken out to determine the sum of the other two sides
    triangle.remove(hypotenuse)
#If two sides equal hypotenuse, this scenario represents a pythagorean triple
    if sum(triangle) == hypotenuse:
        print(statement)
#If two sides do not equal hypotenuse, this scenario does not represent a pythagorean triple
    else:
        print(not_statement)
#If user wishes to continue the program goes on; if not, it ends
    count = input("\nWould you like to go again? (y/n) ")
    if count == 'n':
        break
#Program's print statement when discontinued
print("\nGoodbye!")
