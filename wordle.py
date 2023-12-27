from termcolor import colored
import random
def isGreen(letter, position, word):
    if letter == word[position]:
        return True
    else:
        return False
def isGrey(letter, position, word):
    if letter != word[position] and isYellow(letter, position, word) == False:
        return True
    else:
        return False
def isYellow(letter, position, word):
    if isGreen(letter, position, word) == False and (isGreen(letter, (position + 1) % 5, word) or isGreen(letter, (position + 2) % 5, word) or isGreen(letter, (position + 3) % 5, word) or isGreen(letter, (position + 4) % 5, word)):
        return True
    else:
        return False

wordlist = open("validwords.txt").read().split("\n")
#for word in wordlist:
#    counter = 0
#    for letter in list(word):
#        print(isGreen(letter,counter,word))
#        counter += 1
#print(isYellow('l',2,'llama'))
word = wordlist[random.randint(0,len(wordlist))]
hasReached = False
for i in range(5):
    guess = input("> ")
    counter = 0
    output = ['light_grey', 'light_grey', 'light_grey', 'light_grey', 'light_grey']
    if guess == word:
        hasReached = True
        print("You got it! The word was "+word)
        exit()
    for letter in list(guess):
        if isGreen(letter, counter, word):
            output[counter] = 'green'
        if isYellow(letter, counter, word):
            output[counter] = 'yellow'
        if isGrey(letter, counter, word):
            output[counter] = 'light_grey'
        counter += 1
    print(colored(guess[0], output[0])+colored(guess[1], output[1])+colored(guess[2], output[2])+colored(guess[3], output[3])+colored(guess[4], output[4]))
    #print(colored('█', 'green'))
    #print(colored('█', 'yellow'))
    #print(colored('█', 'light_grey'))
print("Better luck next time! The word was "+word)