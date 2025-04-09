def main():
    user_entry, shift_val = get_user_input()
    print(encrypt(user_entry.lower(), shift_val))

def get_user_input():
    temp_str = input('What would you like to encrypt?')
    temp_val = int(input('What value would you like to shift by?'))
    return temp_str, temp_val

def encrypt(phrase: str, shift_val: int):
    encrypted_phrase = ''
    for char in phrase:
        temp = ord(char) + shift_val
        if temp > ord('z'):
            temp -= 26
        encrypted_phrase = encrypted_phrase + chr(temp)
    return encrypted_phrase

if __name__ == '__main__':
    main()