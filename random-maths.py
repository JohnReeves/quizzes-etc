import random

score=0
questions=int(input("how many questions do you want? "))

for x in range(questions):
  number1 = random.randint(0,12)
  number2 = random.randint(0,12)

  answer=int(input("what is %d X %d \n>> " % (number1, number2)))

  if answer == (number1 * number2):
    print("brilliant")
    score += 1
  else:
    print("try again")

print("your score is %d out of %d" % (score, questions))
