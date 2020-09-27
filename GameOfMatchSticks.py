"""
COMP.CS.100 Programming 1
An Cuong Nguyen, cuong.nguyen@tuni.fi
"""

def main():
    totalSticks = 21
    turn = 1 # to decide wheather player 1 or 2 to play
    print("Game of sticks")
    while totalSticks > 0:
        if turn % 2 != 0:   player = 1          
        else:   player = 2       
        while True:
            numOfSticks = int(input(f"Player {player} enter how many sticks to remove: "))
            if numOfSticks <= 3 and numOfSticks > 0:    break
            print("Must remove between 1-3 sticks!")
        totalSticks -= numOfSticks
        if totalSticks > 0: print(f"There are {totalSticks} sticks left")
        turn += 1
    print(f"Player {player} lost the game!")



if __name__=="__main__":
    main()