score=0

jokes=\
  {
  "What is brown, hairy and wears sunglasses?":"A coconut on vacation :-)",
  "What did the Dalmation say after lunch?":"That hit the spot :-)",
  "Why did the kid cross the playground?":"To get to the other slide :-)",
  "How do you stop an astronaut's baby from crying?":"You rocket :-)"
  #add more questions
}

# step through the dictionary of questions
# giving the question and answer at each line
# make your own dictionary of questions
# or make many, so you can choose the questions too

for question, answer in jokes.items():
  response = input("What is the capital of %s?\n--->" % question)
  if response.capitalize() != answer:
    print("No, the capital of %s is %s." % (question, answer))
  else:
    print("Yes, that's correct!")
    score+=1

numberofquestions = len(jokes)
percent = ( 100 * score/numberofquestions )
print("You got %d%% out of %d!" % (percent, numberofquestions))
