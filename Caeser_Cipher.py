def main():
    get_user_input()

def get_user_input():
    while True:
        temp_str = input('Would you like to (e)ncrypt or (d)ecrypt?')
        if temp_str.lower() != 'e' and temp_str.lower() != 'd':
            print('Invalid input. Try again.')
            continue
        else:
            if temp_str.lower() == 'e':
                temp_str = input('What would you like to encrypt?: ')
                temp_val = int(input('What value would you like to shift by?: '))
                print(encrypt(temp_str, temp_val))
                break
            else:
                temp_str = input('What would you like to decrypt?: ')
                decrypt(temp_str)
                break

def encrypt(phrase: str, shift_val: int):
    encrypted_phrase = ''
    for char in phrase:
        if ord(char) not in range(ord('a'), ord('z')):
            if char == ' ': temp = ord(' ')
            else: continue
        else: temp = ord(char) + shift_val

        if temp > ord('z'): temp -= 26
        encrypted_phrase = encrypted_phrase + chr(temp)
    return encrypted_phrase

def decrypt(phrase: str):
    for shift_val in range(0,25):
        print(f'key {shift_val}: {encrypt(phrase, shift_val)}')

if __name__ == '__main__':
    main()