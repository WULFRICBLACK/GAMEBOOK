# -*- coding: utf-8 -*-
import json
import os

# %%
def openBook(fileName):
    with open(fileName, 'r', encoding='utf8') as f:
        book = json.load(f)
    return book

# %%
def saveBook(fileName, book):
    # print(json.dumps(book, indent=2, ensure_ascii=False))
    print("saving…")  # for debug purpose only! or not after all.
    book['meta']['checked'] = checkReadability(book)
    with open(fileName, 'w+', encoding='utf8') as f:
        json.dump(book, f, indent=2, ensure_ascii=False)

# %%
def checkNumber(question):
    while True:
        try:
            i = int(input(question))
            if i >= 0:
                return i
            else:
                print("There is no such thing as negative pages in a book.")
        except Exception:
            print("This is not a number.")


# %%
def checkReadability(book):
    pages = [page for page in book['pages']]
    for page in pages:
        for option in book['pages'][page]['options']:
            if not str(option['target']) in pages:
                return False
    return True

# %%
def start():
    print("Remember that at any point you can type 'exit' to go back to a lower level question or to exit the program.")
    while True:
        choice = input("Do you want to create a new gamebook (1) or edit one (2)? ")
        if choice == "1":
            createBook()
            break
        elif choice == "2":
            while True:
                title = input("What is the gamebook's filename? ")
                fileName = title+".json"
                if not os.path.isfile(fileName):  # check if the file exists
                    print("No such file in directory.")
                else:
                    editBook(fileName, False)
                    return
        else:
            print("This is not 1 or 2.")

# %%
def createBook():
    while True:
        while True:
            title = input("What is the gamebook's title? ")
            if any((char in set('<|:>/"?*\\')) for char in title):
                print('These characters cannot be used for filenames: \\ / : * ? " < > |')
            else:
                break
        fileName = title+".json"
        if not os.path.isfile(fileName):  # check if the file exists
            break
        else:
            print("A file with this name already exists.")
            break  # remove this line for final project, so that books cannot be overwritten (debug)
    book = {}
    book['meta'] = {}
    book['meta']['title'] = title
    book['meta']['author'] = input("Who is the gamebook's author? ")
    book['meta']['summary'] = input("What is the gamebook's summary? ")
    book['meta']['checked'] = False
    book['pages'] = {}

    saveBook(fileName, book)
    editBook(fileName, True)

# %%
def addPage(book):
    while True:
        pageNumber = 0
        while True:
            if not str(pageNumber) in book['pages']:
                break
            pageNumber += 1
        # print("page"+str(pageNumber))
        content = input("What is the content of page "+str(pageNumber)+"(or exit)? ")
        if content == "exit":
            return book

        options = []
        for ordinalNumeral in ["1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th"]:
            optionDescription = input("What is option "+str(pageNumber)+"'s "+ordinalNumeral+" description (or next)? ")
            if optionDescription == "next":
                if ordinalNumeral == "1st":
                    print("This will be considered as one ending of the gamebook.")
                break
            target = checkNumber("What is the "+ordinalNumeral+" option leading to? ")
            options.append({"description": optionDescription, "target": target})

        book['pages'][str(pageNumber)] = {}
        book['pages'][str(pageNumber)]['content'] = content
        book['pages'][str(pageNumber)]['options'] = options
        print(json.dumps(book, indent=2, ensure_ascii=False))  # for debug purpose only!
        return book

# %%
def editPage(book, fileName):
    while True:
        page = input("Which page do you want to edit? ")
        if page in book['pages']:
            while True:
                choice = input("Do you want to edit page "+page+"'s content (1), it's options (2) or delete it (3)? ")
                if choice == "1":
                    info = input("Here is the old content of page "+page+":\n"+book['pages'][page]['content']+"\nWhat do you want to replace it with ?\n")
                    if not info == "exit":
                        book['pages'][page]['content'] = info
                elif choice == "2":
                    options = book['pages'][page]['options']
                    if options:  # if list options not empty
                        print("\nHere are the options:") if len(options) >= 2 else print("\nHere is the option:")
                        for option in options:
                            print(option['target'], option['description'])
                        while True:
                            if len(options) >= 2:
                                choice = input("Do you want to edit the existing option (1), delete it (2) or add new ones (3)? ")
                                pass
                            else:
                                choice = input("Do you want to edit one of the existing options (1), delete one of them (2) or add new ones (3)? ")
                                pass
                    else:
                        pass
                elif choice == "3":
                    confirm = input("Are you certain you want to delete page "+page+" (y)? ")
                    if confirm == "y" or confirm == "yes":
                        del book['pages'][page]
                        saveBook(fileName, book)
                        print("Page "+page+" was successfuly deleted.")
                        break
                elif choice == "exit":
                    break
                else:
                    print("Try again.")
        elif page == "exit":
            break
        else:
            print("This page isn't part of the gamebook.")

# %%
def editBook(fileName, goToAddPage):
    book = openBook(fileName)
    while True:
        if goToAddPage:
            saveBook(fileName, addPage(book))

        choice = input("Do you want to:\n(1) Add new pages to this gamebook,\n(2) edit a specific page\n(3) or change it's title, author or summary\n")
        if choice == "1":
            book = addPage(book)
        elif choice == "2":
            editPage(book, fileName)
        elif choice == "3":
            while True:
                choice = input("Do you want to edit the 'title', the 'author' or the 'summary' of the gamebook ? ")
                if choice == 'title' or choice == 'author' or choice == 'summary':
                    info = input("Here is the old "+choice+":\n"+book['meta'][choice]+"\nWhat do you want to replace it with ?\n")
                    book['meta'][choice] = info
                    break
                elif choice == 'exit':
                    break
                else:
                    print("Try again.")
        elif choice == "exit":
            if not book['meta']['checked']:
                saveBook(fileName, book)
            return
        else:
            print("This is not a 1, 2, 3 or exit.")
            continue
        saveBook(fileName, book)


# book = openBook("book.json")
# print(editPage(book, "book.json"))
start()
