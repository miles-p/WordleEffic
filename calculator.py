from termcolor import colored
import csv
# Function to check if a letter at a specific position is green
def isGreen(letter, position, word):
    if letter == word[position]:
        return True
    else:
        return False

# Function to check if a letter at a specific position is grey
def isGrey(letter, position, word):
    if letter != word[position] and isYellow(letter, position, word) == False:
        return True
    else:
        return False

# Function to check if a letter at a specific position is yellow
def isYellow(letter, position, word):
    if isGreen(letter, position, word) == False and (isGreen(letter, (position + 1) % 5, word) or isGreen(letter, (position + 2) % 5, word) or isGreen(letter, (position + 3) % 5, word) or isGreen(letter, (position + 4) % 5, word)):
        return True
    else:
        return False

# Read the list of valid words from a file
wordlist = open("validwords.txt").read().split("\n")

result = []

for word in wordlist:
    # Initialize output and score variables
    output = ['light_grey', 'light_grey', 'light_grey', 'light_grey', 'light_grey']
    score_total = 0

    # Loop through each word in the wordlist
    for guess in wordlist:
        score = 0
        counter = 0

        # Loop through each letter in the current guess
        for letter in list(guess):
            # Check if the letter is green, yellow, or grey and update the output and score
            if isGreen(letter, counter, word):
                output[counter] = 'green'
                score += 3
            if isYellow(letter, counter, word):
                output[counter] = 'yellow'
                score += 2
            if isGrey(letter, counter, word):
                output[counter] = 'light_grey'
                score += 1
            counter += 1

        # Print the output with colored blocks and the score for the current guess
        #print(colored('█', output[0]) + colored('█', output[1]) + colored('█', output[2]) + colored('█', output[3]) + colored('█', output[4]), guess + " scores " + str(score))

        # Update the total score
        score_total += score

    # Print the average score across all words in the wordlist
    #print(score_total / len(wordlist))
    result.append([score_total / len(wordlist),word])
print(result)
with open('resultstable.txt', 'x') as f:
    write = csv.writer(f)
    write.writerows(result)