import os
import random

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        array = fill_array()
        print_array(array)
        check_life(array)
        input()

def fill_array():   #Function used to fill the array with random 1's and 0's
    array = [0] * 10
    for i in range(0,len(array)):
        row = [0] * 30
        for j in range(0,len(row)):
            row[j] = random.randint(0,1)
        array[i] = row
    return array

def print_array(array):     #Function used to print the data to the terminal
    for i in range(0,len(array)):
        row = ''
        for j in range(0,len(array[i])):
            if array[i][j] == 1:
                row = row + 'O '
            else:
                row = row + '  '
        print(row)

def check_life(arr):
    array = []
    for i in range(0,len(arr)):
        row = []
        for j in range(0,len(arr[i])):
            count = 0
            try:
                if j != 0 and arr[i][j-1] == 1:     #Left boundary check
                    count += 1
                if j+1 != len(arr[i]) and arr[i][j+1] == 1:   #Right boundary check
                    count += 1
                if i != len(arr) and arr[i+1][j] == 1:    #Lower boundary check
                    count += 1
                if i != 0 and arr[i-1][j] == 1: #Upper boundary check
                    count += 1
            except IndexError:
                pass
            if arr[i][j] == 1:
                if count > 1: row.append(1)
                else: row.append(0)
            elif arr[i][j] == 0:
                if count == 3: row.append(1)
                else: row.append(0)
        array.append(row)
    return array

if __name__ == '__main__':
    main()