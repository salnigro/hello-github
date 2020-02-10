# three data types at input

# string

phrase = input("Enter a string ")
print("You said " + phrase)
print(f"You said {phrase}")


someFloat = float(input("Enter a float: "))
print("You entered float: " +str(someFloat))
print(f"You entered float: {someFloat}")

someInt = float(input("Enteer an int: "))
print("You Entered int: " + str(someInt))
print(f"You entered int: {someInt}")

print(f"Do Python inline, like this: {someFloat} * {someInt} = {someFloat * someInt}")
