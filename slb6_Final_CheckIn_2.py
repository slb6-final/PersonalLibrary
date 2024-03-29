import csv
# import json


# function for Yes/No question, Boolean response
def yes_no(choice):
    yes = set(['yes', 'y', 'Yes', 'Y', 'YES', ''])
    no = set(['no', 'n', 'No', 'N', 'NO'])

    if choice in yes:
        return True
    elif choice in no:
        return False
    else:
        print("Please respond with 'yes' or 'no'")


# # function for simplifying adding entries into dictionaries
# def add_dict(dictionary, key, value):
#     if key in dictionary:
#         dictionary[key].append()
#     else:
#         dictionary[key] = [value]
#     return


def add_entry(condition):
    # empty list for library
    # library = []

    outfile = open('PersonalLibrary.csv', 'r+', encoding='utf-8', newline='')
    csvout = csv.writer(outfile)
    # Headers for CSV file
    csvout.writerow(['Title', 'Author', 'ISBN', 'Copyright', 'Publisher', 'Series', '# in Series'])

    # While loop to continuously prompt for entry.
    condition = yes_no(input("Would you like to add an entry? "))
    while condition:
        # empty dictionary for each entry
        metadata = {}
        title = input("Enter title: ")
        # Prompts for value input for manual entry of metadata.
        author = input("Enter author: ")
        isbn = input("Enter ISBN: ")
        copyright_date = input("Enter copyright year: ")
        publisher = input("Enter publisher: ")
        series_quest = yes_no(input("Is this book in a series? "))
        if series_quest is True:
            series = input("Enter series : ")
            num_series = input("Enter number in series: ")
        else:
            series = ''
            num_series = ''

        # title = input("Enter title: ")
        # add_dict(metadata, 'Title', title)
        #
        # author = input("Enter author: ")
        # add_dict(metadata, 'Author', author)
        #
        # isbn = input("Enter ISBN: ")
        # add_dict(metadata, 'ISBN', isbn)
        #
        # copyright_date = input("Enter copyright year: ")
        # add_dict(metadata, 'Copyright Date', copyright_date)
        #
        # publisher = input("Enter publisher: ")
        # add_dict(metadata, 'Publisher', publisher)
        #
        # series_quest = yes_no(input("Is this book in a series? "))
        # if series_quest is True:
        #     series = input("Enter series : ")
        #     add_dict(metadata, 'Series', series)
        #
        #     num_series = input("Enter number in series: ")
        #     add_dict(metadata, 'Number in Series', num_series)
        # library.append(metadata)

        row = [title, author, isbn, copyright_date, publisher, series, num_series]
        csvout.writerow(row)

        print("Would you like to add another entry? ")
        condition = yes_no(input("Enter 'Y' for yes or 'N' for no: "))
        #print(condition)

    # print("your library has ", len(library), " entries.")
    # for entry in library:
    #     # initiate txt file for metadata of Personal Library
    #     print(entry)
    #     file = open('PersonalLibrary.json', 'a', encoding='utf-8', newline='')
    #     file.write(json.dumps(library, indent=3)
    #     file.close()
    return condition

def remove_entry():
    # FUNCTION TO REMOVE PREVIOUS ENTRIES FROM CSV FILE
    library = list()
    title = input("Please enter a title to be deleted: ")
    with open('PersonalLibrary.csv', 'r') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            library.append(row)
            for field in row:
                if field == title:
                    library.remove(row)
                    print("The title ", title, " has been removed from your library.")
    with open('PersonalLibrary.csv', 'w', encoding='utf-8', newline='') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(library)


# function for main interface.
def main():
    print("Would you like to ADD an entry?")
    condition = yes_no(input("Enter 'Y' for yes or 'N' for no: "))
    if condition is True:
        add_entry(condition)
    print("Would you like to REMOVE an entry?")
    condition = yes_no(input("Enter 'Y' for yes or 'N' for no: "))
    if condition is True:
        remove_entry()

    print("You have finished your personal library file.")

main()
