import random

max_digits = 3
max_guesses = 10

def main():
    answer = generate_number()
    turn = 1
    game_running = True

    while game_running:
        guess = input(f"Turn {turn}: Guess a three digit number: ")
        game_running = check_guess(guess, answer)
        turn += 1
        if turn >= max_guesses+1 and game_running ==True:
            print(f"\nSorry, you failed to guess in {max_guesses} turns!\n Answer was {answer}")
            break
#####################################################################
#Generate the random number for the game
def generate_number():
    answer = ""
    for x in range(max_digits):
        while True:
            num = str(random.randint(0, 9))
            if num in answer:
                continue
            else:
                break
        answer += num
    return answer
#####################################################################
#Checks the guess and answer for the proper clues
def check_guess(guess, answer):
    clue = ""
    if guess == answer:
        print(f"\nCongrats, You guessed right!\nAnswer was {answer}")
        return False

    for x in range(max_digits):
        if guess[x] in answer:
            clue = 'Pico'

    for x in range(max_digits):
        if guess[x] == answer[x]:
            clue = 'Fermi'

    if clue != 'Pico' and clue != 'Fermi':
        clue = 'Bagels'

    print(clue)
    return True
#####################################################################
if __name__ == '__main__':
    main()