debug = False # True to find out what's happening

# dictionary of morse code letters
# huffman encoding of english letter frequencies
# https://en.wikipedia.org/wiki/Morse_code#/media/File:Morse_code_tree3.png
morse_code=\
{
  # single key: e & t
  "e":".", "t":"-",

  # double key: i,a,n & m
  "i":"..","a":".-","n":"-.","m":"--",
  
  # triple key: s,u,r,w,d,k,g,o
  "s":"...","u":"..-","r":".-.","w":".--",
  "d":"-..","k":"-.-","g":"--.","o":"---",

  # quartle key: 
  "h":"....","v":"...-","f":"..-.","l":".-..",
  "c":".-.-","p":".--.","j":".---",
  "b":"-...","x":"-..-","y":"-.--","z":"--..","q":"--.-"

}

if debug:
  print("%d letters encoded" % len(morse_code))
  print(sorted(morse_code))

# 'input' is a function to input anything
# 'anything' is a variable, a named thing
# 'lower' is a string method to make everything lowercase
anything = input("tell me anything!\n>>").lower()

# find out what happens if you don't declare
# the morse code string outside the loop!

word = ""
for letter in anything:
  if letter in morse_code:
    word += morse_code[letter]+" "
  elif letter == " ":
    word += "   "

print(word)
