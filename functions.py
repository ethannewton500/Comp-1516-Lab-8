# Lab 8 Ethan Newton partners are Erik and William
import data


def get_countries(substring):
    """
    This function sorts through all the countries in data.countries and if the country contains the substring it is
    written to MatchingCountries.txt
    :param substring: The substring that is searched for in data.countries
    :return: no return
    """
    f = open("MatchingCountries.txt", "w")
    for country in data.countries:
        if substring.lower() in country.lower():
            f.write(f"%s\n" % country)
    f.write("\n")
    f.close()


def get_capitals(substring):
    """
    This function sorts through all the capitals in data.capitals and if the country contains the substring it is
    written to MatchingCountries.txt
    :param substring: The substring that is searched for in data.capitals
    :return: No return
    """
    f = open("MatchingCountries.txt", "a")
    for capital in data.capitals:
        if substring.lower() in capital.lower():
            f.write(f"%s\n" % capital)
    f.close()


def get_file_data():
    """
    This function prints all lines from MatchingCountries.txt
    :return: No return
    """
    f = open("MatchingCountries.txt", "r")
    result = f.readlines()
    print(result)


def main():
    print("I should not be called")


if __name__ == '__main__':
    main()
