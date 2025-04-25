import os
import random
from time import sleep

def main():
    array = fill_array()
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')       #clear the screen in between print statements
        print_array(array)      #print the new data to the screen
        array = check_life(array)      #check to see if the next data lives or dies
        sleep(0.5)  #delay for half a second

def fill_array():   #Function used to fill the array with random 1's and 0's
    array = [0] * 20
    for i in range(0,len(array)):
        row = [0] * 79
        for j in range(0,len(row)):
            row[j] = random.randint(0,1)
        array[i] = row
    return array

def print_array(array):     #Function used to print the data to the terminal
    for i in range(0,len(array)):
        row = ''
        for j in range(0,len(array[i])):
            if array[i][j] == 1:
                row = row + 'O'
            else:
                row = row + ' '
        print(row)

def check_life(arr):    #checks to see if the data in each cell is alive or dead based on neighboring cells
    array = []      #empty array to store the new data
    for i in range(0,len(arr)):
        row = []
        for j in range(0,len(arr[i])):      #iterate through the whole array and check neighbors for life
            count = 0
            try:
                if arr[i-1][j] == 1:    #Upper cell check
                    count += 1
                if arr[i-1][j+1] == 1:    #Upper-right cell check
                    count += 1
                if arr[i][j+1] == 1:    #Right cell check
                    count += 1
                if arr[i+1][j+1] == 1:    #Lower-right cell check
                    count += 1
                if arr[i+1][j] == 1:    #Lower cell check
                    count += 1
                if arr[i+1][j-1] == 1:    #Lower-left cell check
                    count += 1
                if arr[i][j-1] == 1:    # Left cell check
                    count += 1
                if arr[i-1][j-1] == 1:    #Upper-left cell check
                    count += 1
            except IndexError:
                pass
            if arr[i][j] == 1:      #assign the cell value based on the neighbors
                if count == 2 or count == 3 : row.append(1)
                else: row.append(0)
            elif arr[i][j] == 0:
                if count == 3: row.append(1)
                else: row.append(0)
        array.append(row)       #add each row to the newly created array
    return array

if __name__ == '__main__':
    main()