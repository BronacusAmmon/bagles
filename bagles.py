import random

NUM_DIGITS = 3 
GUESS_MAX = 10 


def main():
    print(f'''Bagles, a deductive Logic game.
            I am thinking of a {NUM_DIGITS}-digit number with no repeated digits.
            Here are some clues:
            When I say:     That means:
            Pico    One digit is correct, but in the wrong position.
            Fermi   One digit is correct and is in the correct position.
            Bagles  No digit is correct''')
    while True:
            secretNum = getSecretNum()
            print("I have thought up a number")
            print(f"You have {GUESS_MAX} guesses to get it")

            numGuesses = 1
            while numGuesses <= GUESS_MAX:
                guess = ''
                while len(guess) != NUM_DIGITS or not guess.isdecimal():
                    print(f"Guess #{numGuesses}")
                    guess = input('> ')
                
                clues = getClues(guess, secretNum)
                print(clues)
                numGuesses += 1

                if guess == secretNum:
                    break
                if numGuesses > GUESS_MAX:
                        print("You ran out of guesses")
                        print(f'The answer was {secretNum}')

            print("do you want to play again (yes or no)")
            if not input('> ').lower().startswith('y'):
                break
    print('Thanks for playing')

def getSecretNum():
        numbers = list('0123456789')
        random.shuffle(numbers)

        secretNum = ""
        for i in range(NUM_DIGITS):
            secretNum += str(numbers[i])
        return secretNum
def getClues(guess, secretNum):
        if guess == secretNum:
            return 'you got it'
        
        clues = []

        for i in range(len(guess)):
            if guess[i] == secretNum[i]:
                clues.append("Fermi")
            elif guess[i] in secretNum:
                clues.append("Pico")
        if len(clues) == 0:
            return "Bagles"
        else:
            clues.sort()
            return " ".join(clues)

        

if __name__ == '__main__':
    main()