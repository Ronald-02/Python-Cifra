def getDoubleAlphabet(alphabet):
    return alphabet + alphabet

def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage = ""
    for letter in message:
        if letter in alphabet:
            position = alphabet.index(letter)
            newPosition = (position + cipherKey) % len(alphabet)
            encryptedMessage += alphabet[newPosition]
        else:
            encryptedMessage += letter
    return encryptedMessage

def decryptMessage(encryptedMessage, cipherKey, alphabet):
    negativeCipherKey = -cipherKey
    decryptedMessage = encryptMessage(encryptedMessage, negativeCipherKey, alphabet)
    return decryptedMessage

def runCaesarCipherProgram():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet2 = getDoubleAlphabet(alphabet)
    print("Alphabet:", alphabet)
    print("Alphabet2:", alphabet2)

    message = input("Please enter a message to encrypt: ").upper()
    cipherKey = int(input("Please enter a key (whole number from 1-25): "))

    encryptedMessage = encryptMessage(message, cipherKey, alphabet2)
    print("Encrypted Message:", encryptedMessage)

    decryptedMessage = decryptMessage(encryptedMessage, cipherKey, alphabet2)
    print("Decrypted Message:", decryptedMessage)

if __name__ == "__main__":
    runCaesarCipherProgram()

    
    

    
    
    
    
    
    
    
    
    