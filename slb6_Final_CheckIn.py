# Shannon Buchanan
# Final Project Check-In

import csv


# function for Yes/No question, Boolean response
def yes_no(choice):
    yes = set(['yes', 'y', ''])
    no = set(['no', 'n'])

    if choice in yes:
        return True
    elif choice in no:
        return False
    else:
        print("Please respond with 'yes' or 'no'")


def add_entry(condition):
    # initiate CSV file for metadata of Personal Library
    outfile = open('PersonalLibrary.csv', 'w+', encoding='utf-8', newline='')
    csvout = csv.writer(outfile)
    # Headers for CSV file
    csvout.writerow(['Title', 'Author', 'ISBN', 'Copyright', 'Publisher', 'Series', '# in Series', 'Goodreads URL'])

    # TO GO HERE: IF/ELSE STATEMENT FOR DETERMINING WHETHER ISBN OR TITLE WAS ENTERED FOR WEB-SCRAPING PURPOSES
    # While loop to continuously prompt for entry.

    while condition:

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

        # add rows to CSV file
        row = [title, author, isbn, copyright_date, publisher, series, num_series]
        csvout.writerow(row)

        # prompt to add another entry
        print("Would you like to add another entry?")
        condition = yes_no(input("Enter 'Y' for yes or 'N' for no: "))
        if condition is False:
            break
        else:
            continue
        break
    # RETURN TO MAIN FUNCTION WHY WON'T IT STOP AND GO BACK TO THE MAIN FUNCTION! HELP!
    else:
        return condition


def remove_entry(condition):
    # FUNCTION TO REMOVE PREVIOUS ENTRIES FROM CSV FILE

    with open("testData.csv")    as csvfile:
        reader = csv.DictReader(csvfile)

        with open("testData.csv", 'w+', newline='') as csvfile:
            fieldnames = ['Title', 'Author', 'ISBN', 'Copyright Year', 'Publisher'
                , 'Series', 'Number in Series', 'Goodreads URL']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            print("Delete an entry")
            deletion = input("Enter title to delete: ")

        for row in reader:
            if deletion != row['Title']:
                writer.writerow(row)  # write all non-matching rows
        else:
            print("Library Record Deleted")  # nothing to write

    # RETURN TO MAIN FUNCTION
    return


def main():
    # MAIN FUNCTION TO PROMPT FOR ADDING OR REMOVING ENTRIES FROM CSV FILE.
    print("Would you like to add an entry?")
    condition = yes_no(input("Enter 'Y' for yes or 'N' for no: "))
    while condition:
        add_entry(condition)
    else:
        print("Would you like to remove an entry?")
        condition = yes_no(input("Enter 'Y' for yes or 'N' for no: "))
        if condition is True:
            remove_entry(condition)
        else:
            # Once file is written
            print("You have finished your personal library file.")

main()

'''SWITCH FROM CSV TO LIST OF DICTIONARIES THAT PRINTS TO CSV AT END?'''
