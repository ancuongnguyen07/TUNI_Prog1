"""
COMP.CS.100 Programming 1
Code Template
"""
def longest_substring_in_order(mess):
    """
    Count "abba" in the string

    :param mess: string
    :return int: the number of appearance of "abba"
    """
    n = len(mess)
    start = end = 0
    for i in range(n):
        for k in range(i + 1,n):
            if mess[k - 1] > mess[k]:
                if k - i - 1> end - start:
                    start,end = i,k - 1
                break
            if k == n - 1:
                if k - i > end - start:
                    start,end = i,k
    return mess[start:end + 1]

#print(longest_substring_in_order("acdkbarstyefgioprtyrtyx"))
            
