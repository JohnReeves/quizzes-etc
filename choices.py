
names="josh, katia, hannah, sam, helen, mrs biggs, hawking, pizza"
sports="rugby, football, badminton, ice skating,\
 sleep-time, netball, arts-crafts-time"
numbers="6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17"
siblings="0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11"


questions=\
{
  "what do you want to eat":[names,"nom nom %s was tasty"],
  "what do you want to do":[sports,"%s sounds nice"],
  "what's your favourite number":[numbers,"I like %s too!"],
  "how many siblings do you have":[siblings,"I have %s too!"]
}

for question, answer in questions.items():
  response = input("%s: \n%s?\n--->" % (question, answer[0]))
  if response not in (answer[0]).split(", "):
    print("no")
  else:
    print(answer[1] % response)
  
