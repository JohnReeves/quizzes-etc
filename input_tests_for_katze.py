
# 'greetings' is a variable
greetings="hello katze"

# 'x' is a loop counter
# 'range' is a function to count to 3 or any other amount
for x in range(3):
   print(greetings)

   # 'for' is a loop in python
   # 'letter' is a variable holding each letter in greetings
   for letter in greetings:
     print(letter)

# 'input' is a function for getting a response from the user
# 'response' is a variable for storing the value of the response
# you could call it *anything*
response = input(greetings)
for x in range(4):
   print(response)

# just to prove you can call it 'anything'
anything = input("tell me anything")
for x in range(20):
  print(anything)

