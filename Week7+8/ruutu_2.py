"""
COMP.CS.100 Programming 1
Print a box with input error checking
"""
"""1 parameter, return number"""
def read_input(ques):
    """
    Read user's inputs according the request

    :param ques: prompt sentence
    :return string
    """
    #validValue = True
    while True:
        try:
            ans = int(input(ques))
            if  ans > 0: return ans
        except ValueError:
            continue

"""3 parameters, w:width, h:height, m:mark"""
def print_box(w, h, m):
    """
    Print the box with height(h) and width(w) filled with 
    marks(m)

    :param w,h,m: string
    """
    print()
    for _ in range(h):
        print(m*w)

def main():
    width = read_input("Enter the width of a frame: ")
    height = read_input("Enter the height of a frame: ")
    mark = input("Enter a print mark: ")


    print_box(width, height, mark)


if __name__ == "__main__":
    main()
