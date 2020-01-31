def ceasarCipher(str, key):
    newLetterCharacter = []
    newKey = key % 26
    for letter in str:
        newLetterCharacter.append(getNewLetter(letter, newKey))
    return "".join(newLetterCharacter)

def getNewLetter(letter, key):

    newLetterCode = ord(letter) + key
    return chr(newLetterCode) if newLetterCode <=122 else chr(96 + newLetterCode % 122)


print(ceasarCipher('madam', 2))

