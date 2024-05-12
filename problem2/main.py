def caesar(offset, input_str):
    shifted_chars = [chr((ord(char) - ord('a' if char.islower() else 'A') + offset) % 26 + ord('a' if char.islower() else 'A')) if char.isalpha() else char for char in input_str]
    return ''.join(shifted_chars)


if __name__ == '__main__':
    print(caesar(3, "abc")) # def
    print(caesar(2, "alta")) # cnvc
    print(caesar(10, "alterraacademy")) # kvdobbkkmknowi
    print(caesar(1, "abcdefghijklmnopqrstuvwxyz")) # bcdefghijklmnopqrstuvwxyza
    print(caesar(1000, "abcdefghijklmnopqrstuvwxyz")) # mnopqrstuvwxyzabcdefghijkl