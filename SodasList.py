'''
Scores List
Pawelski
11/6/2023
Introduction to Computer Science

Instructions:
Read through the code and predict the
output of the program. Check your prediction
by running the code.
Add the following code to the program and try
running the program.
print(drinks[23])

You should notice that the program produces an
error! Why? What is an IndexError?
'''

drinks = ["Coca Cola", "Diet Coke", "Sprite", "Mr. Pibb"]

print(drinks)
drinks[0] = "Pepsi"
drinks[3] = "Pibb Xtra"
print(drinks)

index = 1
drinks[index] = "Cherry Pepsi"
print(drinks)