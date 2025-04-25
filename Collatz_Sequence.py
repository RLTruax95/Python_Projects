def main():
    while True:
        num = input("Enter a number greater than 0 or 'Q' to quit: ")
        if num.lower == 'q':
            break
        elif int(num) <= 0:
            continue
        else:
            output = ''
            num = int(num)
            output = output + str(num)
            while num >= 1:
                if num % 2 == 0:
                    num = num / 2
                elif num == 1:
                    break
                else:
                    num = 3 * num + 1
                output += f', {int(num)}'
            print(output)

if __name__ == '__main__':
    main()