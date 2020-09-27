"""
COMP.CS.100 Programming 1 code template
Fill in all TODOs in this file
"""

def main():
    nums = []
    print("Give 5 numbers:")
    for _ in range(5): nums += [int(input("Next number: "))]
    print("The numbers you entered that were greater than zero were:")
    for ele in nums:
        if ele > 0: print(f"{ele}")

if __name__=="__main__":
    main()