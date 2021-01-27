"""
COMP.CS.100 Programming 1
Code template for  tourist dictionary.
"""

def main():
    english_spanish = {"hey": "hola", "thanks": "gracias", "home": "casa"}
    spanish_english = {}
    for pairs in english_spanish.items():
        spanish_english[pairs[1]] = pairs[0]

    print("Dictionary contents:")
    print(', '.join(sorted(english_spanish)).rstrip())

    while True:
        command = input("[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: ")

        if command == "W":

            word = input("Enter the word to be translated: ")
            if word in english_spanish:
                print(f"{word} in Spanish is {english_spanish[word]}")
            else:
                print("The word", word, "could not be found from the dictionary.")

        elif command == "A":
            englishWord = input("Give the word to be added in English: ")
            spanishWord = input("Give the word to be added in Spanish: ")

            english_spanish[englishWord] = spanishWord
            spanish_english[spanishWord] = englishWord

            print("Dictionary contents:")
            print(', '.join(sorted(english_spanish)).rstrip())

        elif command == "R":
            word = input("Give the word to be removed: ")
            if word in english_spanish:
                del english_spanish[word]
            else: print(f"The word {word} could not be found from the dictionary.")

        elif command == "Q":
            print("Adios!")
            return
        elif command == "P":
            print("\nEnglish-Spanish")
            for key in sorted(english_spanish):
                print(f"{key} {english_spanish[key]}")

            print("\nSpanish-English")
            for key in sorted(spanish_english):
                print(f"{key} {spanish_english[key]}") 
            print()
        elif command == "T":
            mess = input("Enter the text to be translated into Spanish: ")
            print("The text, translated by the dictionary:")

            translatedMess = []
            for w in mess.split(' '):
                if w in english_spanish:
                    translatedMess.append(english_spanish[w])
                else: translatedMess.append(w)
            print(' '.join(translatedMess).rstrip())
        else:
            print("Unknown command, enter W, A, R, P, T or Q!")

if __name__ == "__main__":
    main()
