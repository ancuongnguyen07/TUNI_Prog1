def increase(a):
    a += 1

def addEle(arr):
    arr += [1,2,4,5]

def main():
    a = 5
    arr = [1]
    increase(a)
    addEle(arr)


    # -------------- check if any variable changed
    print(a)
    print(arr)
    # list variable changed

if __name__=='__main__':
    main()