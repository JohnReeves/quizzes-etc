
jokes=\
  {
  "What is brown, hairy and wears sunglasses":"A coconut on vacation",
  "What did the Dalmation say after lunch":"That hit the spot",
  "Why did the kid cross the playground":"To get to the other slide",
  "How do you stop an astronaut's baby from crying":"You rocket",
  "What do you call a dinosaur that is sleeping":"A dino-snore",
  "What is fast loud and crunchy":"A rocket chip",
  "What did one plate say to the other plate":"Dinner is on me"
  #add more questions
}

# step through the dictionary of questions
# giving the question and answer at each line
# make your own dictionary of questions
# or make many, so you can choose the questions too

for question, answer in jokes.items():
  response = input("%s?\n>>" % question)
  if response.lower() != answer:
    print("No, %s? is %s :-)" % (question, answer))
  else:
    print("Yes, that's correct!")
    score+=1
