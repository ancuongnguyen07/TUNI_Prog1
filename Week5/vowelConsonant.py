"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Name:       An Cuong Nguyen
Email:      cuong.nguyen@tuni.fi
Student Id: 050358715

Count vowels and consonents
"""
VOWELS = "UEOAI"

def main():
    word = input("Enter a word: ")
    vowelCount = 0
    for letter in word.upper():
        if letter in VOWELS: vowelCount += 1
    print(f"The word {word} contains {vowelCount} vowels and {len(word) - vowelCount} consonants")

if __name__ == "__main__":
    main()