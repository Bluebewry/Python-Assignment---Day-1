#Exercise 1 

num_list =[]

for number in range(1,11):
    cubed_number = number**3
    num_list.append(cubed_number)

print(num_list)

#Exercise 2

prime = []

for i in range(1,101):
    if i % 2 == 1:
        prime.append(i)

print(prime)

#Exercise 3

# Exercise 3 <br>
user_input = int(input("How old are you?: "))

if user_input > 65:
    print("seniors")
elif user_input >= 18:
    print("adults")
elif user_input < 18:
    print("kids")
