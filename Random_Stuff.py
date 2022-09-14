from string import ascii_letters as asc

alphabet = asc + "!@#$%^&*"

def CeaserCipher():
    message = str(input("Enter your message: "))
    shift = int(input("Enter the amount to shift: "))
    shifted = alphabet[shift:] + alphabet[:shift]
    for x in range(len(alphabet)):
        coded = ""
        letter = message[x]
        newLetter = shifted[letter]
    print(shifted)
    print(letter)


CeaserCipher()