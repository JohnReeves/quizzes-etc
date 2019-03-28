score=0

questions=\
  {
  "England":"London",
  "Spain":"Madrid",
  "France":"Paris",
  "Portugal":"Lisbon",
  "Germany":"Berlin",
  "Italy":"Rome",
  "Poland":"Warsaw",
  "Russia":"Moscow",
  "Australia":"Canberra",
  "Austria":"Vienna"
  #add more questions
}

# step through the dictionary of questions
# giving the question and answer at each line
# make your own dictionary of questions
# or make many, so you can choose the questions too

for question, answer in questions.items():
  response = input("What is the capital of %s?\n--->" % question)
  if response.capitalize() != answer:
    print("No, the capital of %s is %s." % (question, answer))
  else:
    print("Yes, that's correct!")
    score+=1

numberofquestions = len(questions)
percent = ( 100 * score/numberofquestions )
print("You got %d%% out of %d!" % (percent, numberofquestions))
