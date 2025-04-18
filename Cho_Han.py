import random

def main():
    #Tracks the users current cash
    coffer : int = 5000

    #run the program until the user runs out of money
    while coffer > 0:
        bet = int(input(f'\nYou have ${coffer}, how much would you like to bet?: '))
        if bet > coffer:
            print(f'Sorry, you do not have enough money!')
            continue

        #Random roll the dice
        die1, die2 = random.randint(1,6), random.randint(1,6)
        while True:
            #Have the user guess the even or odd
            guess = input('The dice have been rolled, is the total even or odd?: ')
            if guess.lower() != 'even' and guess.lower() != 'odd':
                print('Please enter a valid input.')
                continue
            else:
                break

        #Return the dice values and whether they read even or odd
        print(f'The dice read:\n\t{die1} - {die2}\n The roll is {check_even(die1, die2)}')
        if guess.lower() ==  check_even(die1, die2).lower():
            print('You win!')
            coffer += bet
        else:
            print('You lose!')
            coffer -= bet

#Returns a value to tell if the total is even or odd
def check_even(d1: int, d2 : int):
    if (d1 + d2) % 2 == 0:
        return 'Even'
    else:
        return 'Odd'

if __name__ == '__main__':
    main()