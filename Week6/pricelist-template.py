"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 050358715
Name: An Cuong Nguyen
Email: cuong.nguyen@tuni.fi

Template for pricelist assignment.
"""

PRICES = {
    "milk": 1.09, "fish": 4.56, "bread": 2.10,
    "chocolate": 2.70, "grasshopper": 13.25,
    "sushi": 19.90, "noodles": 0.97, "beans": 0.87,
    "bananas": 1.05, "Pepsi": 3.15,  "pizza": 4.15,
}


def main():
    # TODO
    while True:
        productName = input("Enter product name: ").strip()
        if productName == '': break
        if productName in PRICES:
            print(f"The price of {productName} is {PRICES[productName]:.2f} e")
        else:
            print(f"Error: {productName} is unknown.")
    print("Bye!")

if __name__ == "__main__":
    main()
