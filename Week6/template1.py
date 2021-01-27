"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 050358715
Name: An Cuong Nguyen
Email: cuong.nguyen@tuni.fi

Template for sorting by price assignment.
"""

PRICES = {
    "milk": 1.09, "fish": 4.56, "bread": 2.10,
    "chocolate": 2.70, "grasshopper": 13.25,
    "sushi": 19.90, "noodles": 0.97, "beans": 0.87,
    "bananas": 1.05, "Pepsi": 3.15,  "pizza": 4.15,
}

def price(key):
    """
    Return the value-price of the key-food of PRICES dict
    :param :key-string
    :return :value-float
    """
    return PRICES[key]

def main():
    # TODO
    for food in sorted(PRICES,key=price):
        print(f"{food} {PRICES[food]:.2f}")


if __name__ == "__main__":
    main()
