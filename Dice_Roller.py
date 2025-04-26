import random

def main():
    entry = input('Enter any number of dice to roll (ie. 2d6, 5d3, 2d12, etc): ')
    modifier = entry[entry.find('/' or '*' or '-' or '+')+1:]
    dice_count = int(entry[:entry.find('d')])
    sides = entry[entry.find('d')+1:]

    print(f'roll {dice_count} d{sides} ({modifier})')

if __name__ == '__main__':
    main()