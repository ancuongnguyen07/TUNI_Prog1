"""
COMP.CS.100 Programming 1
Code Template
"""
def count_abbas(mess):
    """
    Count "abba" in the string

    :param mess: string
    :return int: the number of appearance of "abba"
    """
    count = 0
    for i in range(len(mess) - 3):
        if mess[i:i + 4] == "abba": count += 1
    return count

#print(str(count_abbas("abbabbabba")))