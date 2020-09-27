"""
COMP.CS.100 Programming 1 code template
Fill in all TODOs in this file
"""

def main():
    nums = []
    print("Give 5 numbers:")
    for _ in range(5): nums += [int(input("Next number: "))]
    print("The numbers you entered, in reverse order:")
    for i in range(len(nums)-1,-1,-1):
        print(f"{nums[i]}")

if __name__=="__main__":
    main()