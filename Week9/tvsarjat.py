"""
COMP.CS.100 Programming 1
Read genres and tv-series from a file into a dict.
Print a list of the genres in alphabetical order
and list tv-series by given genre on user's command.
"""

def read_file(filename):
    """
    Reads and saves the series and their genres from the file.

    TODO: comment the parameter and the return value.
    :para :filename-string
    :return : a dict with key is genre and values are names of movies
    """

    # TODO initialize a new data structure
    movieDict = {}

    try:
        file = open(filename, mode="r")

        for row in file:

            # If the input row was correct, it contained two parts:
            # · the show name before semicolon (;) and
            # · comma separated list of genres after the semicolon.
            # If we know that a function (method split in this case)
            # returns a list containing two elements, we can assign
            # names for those elements as follows:
            name, genres = row.rstrip().split(";")

            genres = genres.split(",")

            # TODO add the name and genres data to the data structure
            for g in genres:
                if g not in movieDict:
                    movieDict[g] = [name]
                    continue
                movieDict[g].append(name)

        file.close()
        return  movieDict
        # TODO return the data structure

    except ValueError:
        print("Error: rows were not in the format name;genres.")
        return None

    except IOError:
        print("Error: the file could not be read.")
        return None


def main():
    filename = input("Enter the name of the file: ")

    genre_data = read_file(filename)

    # TODO print the genres
    print(f"Available genres are: {(', '.join(sorted(genre_data.keys())).rstrip())}")

    while True:
        genre = input("> ")

        if genre == "exit":
            return

        # TODO print the series belonging to a genre.

        if genre not in genre_data or len(genre_data[genre]) == 0:
            continue
        else:
            print(('\n'.join(sorted(genre_data[genre]))).rstrip())


if __name__ == "__main__":
    main()
