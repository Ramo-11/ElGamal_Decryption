import textwrap

def get_word_from_num(num):
    """
    Decrypts a number to the original word.
    """
    # Define a dictionary to map numbers to letters
    letters = {i: chr(i+97) for i in range(26)}

    # Calculate the letters
    c = num % 26
    num //= 26
    b = num % 26
    num //= 26
    a = num % 26

    # Convert the letters to the original word
    word = letters[a] + letters[b] + letters[c]
    return word

def mod_inv(x, p):
    """
    Calculates the modular inverse of x modulo p using Fermat's Little Theorem.
    """
    return pow(x, p-2, p)

def mod_exp(y, a, p):
    """
    Calculates y^a mod p
    """
    res = 1
    while a > 0:
        if a % 2 == 1:
            res = (res * y) % p
        y = (y * y) % p
        a //= 2
    return res

def calc_mod(y1, y2, a, p):
    """
    Calculates y2*(y1^a)^-1 mod p given y1, y2, a, and p.
    """
    y1_a_inv = mod_inv(mod_exp(y1, a, p), p)
    return (y2 * y1_a_inv) % p

with open('ciphertext.txt', 'r') as file:
    ciphertext = file.read()

a = 7899
p = 31847
plaintext = ""
for cipher in ciphertext.split('\n'):
    y1, y2 = map(int, cipher.split())
    result = calc_mod(y1, y2, a, p)
    plaintext += get_word_from_num(result)

plaintext = textwrap.fill(plaintext, width=70)
file = open("plaintext.txt", "w")
file.write(plaintext)
file.close()