# Shannon Buchanan
# Final Project Submission

import csv


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

# FUNCTION FOR ADDING NEW ENTRIES TO THE LIBRARY
def add_entry(condition):
    outfile = open('PersonalLibrary.csv', 'r+', encoding='utf-8', newline='')
    csvout = csv.writer(outfile)
    # Headers for CSV file
    csvout.writerow(['Title', 'Author', 'ISBN', 'Copyright', 'Publisher', 'Series', '# in Series'])

    # While loop to continuously prompt for entry.
    condition = yes_no(input("Would you like to add an entry? "))
    while condition:

        title = input("Enter title: ")
        # Prompts for value input for manual entry of metadata.
        author = input("Enter author: ")
        isbn = input("Enter ISBN: ")
        copyright_date = input("Enter copyright year: ")
        publisher = input("Enter publisher: ")
        
        # since not all books are a part of a series, the following questions are optional. 
        series_quest = yes_no(input("Is this book in a series? "))
        if series_quest is True:
            series = input("Enter series : ")
            num_series = input("Enter number in series: ")
        else:
            series = ''
            num_series = ''
        
        # write the metadata for this particular entry to the CSV file.
        row = [title, author, isbn, copyright_date, publisher, series, num_series]
        csvout.writerow(row)

        # prompt for adding more entries to teh library
        print("Would you like to add another entry? ")
        condition = yes_no(input("Enter 'Y' for yes or 'N' for no: "))
    # return back to the main function.
    return condition

# FUNCTION TO REMOVE PREVIOUS ENTRIES FROM CSV FILE
def remove_entry():
    # blank list to write the csv file to.
    library = list()
    # title of entry that user wants to delete
    title = input("Please enter a title to be deleted: ")
    
    # opens file, reads it, and then writes each row from the file into the library list
    with open('PersonalLibrary.csv', 'r') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            library.append(row)
            # checks if the the title the user wants to remove is in each field.
            for field in row:
                # if the title is in a field, the row that field resides in is removed from the list.
                if field == title:
                    library.remove(row)
                    print("The title ", title, " has been removed from your library.")
    # opens file and writes the library list to the file. 
    with open('PersonalLibrary.csv', 'w', encoding='utf-8', newline='') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(library)


# FUNCTION FOR MAIN INTERFACE
def main():
    print("Welcome to your personal library.")
    # prompt for adding entry
    print("Would you like to ADD an entry?")
    condition = yes_no(input("Enter 'Y' for yes or 'N' for no: "))
    if condition is True:
        # jumps to add_entry function
        add_entry(condition)
    # prompt for removing an entry
    print("Would you like to REMOVE an entry?")
    condition = yes_no(input("Enter 'Y' for yes or 'N' for no: "))
    if condition is True:
        # jumps to remove_entry function
        remove_entry()
    # completes program by stating the personal library file is complete.
    print("You have finished your personal library file.")
main()
