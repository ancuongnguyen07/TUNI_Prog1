"""
COMP.CS.100 Programming 1
Code template for  tourist dictionary.
"""

def main():
    wordDict = {}
    print("Enter rows of text for word counting. Empty row to quit.")
    while True:
        mess = input()
        if mess == '': break
        for word in mess.lower().split(' '):
            if word in wordDict: wordDict[word] += 1
            else: wordDict[word] = 1

    print()
    for word in sorted(wordDict):
        print(f"{word} : {wordDict[word]} times")

if __name__ == "__main__":
    main()