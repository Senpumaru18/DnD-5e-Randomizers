from string import ascii_letters as asc

alphabet = asc + "!@#$%^&*"

def CeaserCipher():
    message = str(input("Enter your message: "))
    shift = int(input("Enter the amount to shift: "))
    shifted = []
    for x in range(alphabet):
        

