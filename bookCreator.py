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
            number = int(input(question))
            if number >= 0:
                return number
            else:
                print("There is no such thing as negative pages in a book.")
        except Exception:
            print("This is not a number.")


# %%
def checkReadability(book):
    pages = [pageNumber for pageNumber in book['pages']]
    for pageNumber in pages:
        for option in book['pages'][pageNumber]['options']:
            if not str(option['target']) in pages:
                return False
    return True

# %%
def start():
    print("\nRemember that at any point you can type 'exit' to go back to a lower level question or to exit the program.")
    while True:
        choice = input("(1) Create a new gamebook\n(2) or edit one ?\n ")
        if choice == "1":
            createBook()
            break
        elif choice == "2":
            while True:
                try:
                    title = input("What is the gamebook's filename? ")
                    fileName = title+".json"
                    editBook(fileName, False)
                    return
                except Exception:
                    print("No such file in directory.")

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
def addOptions(book, pageNumber):
    options = book['pages'][pageNumber]['options']
    for index, ordinalNumeral in enumerate(["1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th"]):
        if len(options) > index:
            continue
        optionDescription = input("What is option "+pageNumber+"'s "+ordinalNumeral+" description (or next)? ")
        if optionDescription == "next":
            if ordinalNumeral == "1st":
                print("This will be considered as one ending of the gamebook.")
            return book
        target = checkNumber("Which page is the "+ordinalNumeral+" option leading to? ")
        options.append({"description": optionDescription, "target": target})

    print(book['pages'][pageNumber]['options'])
    return book

# %%
def addPage(book):
    while True:
        intPageNum = 0
        while True:
            if not str(intPageNum) in book['pages']:
                break
            intPageNum += 1
        pageNumber = str(intPageNum)
        content = input("What is the content of page "+pageNumber+"(or exit)? ")
        if content == "exit":
            return book

        book['pages'][pageNumber] = {}
        book['pages'][pageNumber]['content'] = content
        book = addOptions(book, pageNumber)
        print(json.dumps(book, indent=2, ensure_ascii=False))  # for debug purpose only!
        return book

# %%
def deleteOption(fileName, book, pageNumber, optionIndex, name):
    confirm = input("Are you certain you want to delete "+name+" (y)? ")
    if confirm == "y" or confirm == "yes":
        del book['pages'][pageNumber]['options'][optionIndex]
        saveBook(fileName, book)
        print(name.capitalize()+" was successfuly deleted.")
    return book

# %%
def printOptions(options):
    if options:
        print("\nHere is the option:") if len(options) == 1 else print("\nHere are the options:")
        for option in options:
            print(option['target'], option['description'])

# %%
def editPage(book, fileName):
    while True:
        pageNumber = input("Which page do you want to edit? ")
        if pageNumber in book['pages']:
            while True:
                choice = input("(1) Edit page "+pageNumber+"'s content,\n(2) it's options\n(3) or delete it?\n ")
                if choice == "1":
                    info = input("Here is the old content of page "+pageNumber+":\n"+book['pages'][pageNumber]['content']+"\nWhat do you want to replace it with ?\n")
                    if not info == "exit":
                        book['pages'][pageNumber]['content'] = info
                elif choice == "2":
                    options = book['pages'][pageNumber]['options']
                    if options:  # if options not empty
                        printOptions(options)
                        while True:
                            if len(options) == 1:
                                choice = input("(1) Edit the existing option,\n(2) delete it\n(3) or add new ones?\n ")
                            else:
                                choice = input("(1) Edit one of the options,\n(2) delete one\n(3) or add new ones?\n ")
                            if choice == "1" or choice == "2":
                                if len(options) == 1:
                                    optionIndex = 0
                                    name = "this remaining option with target "+str(options[0]['target'])
                                else:
                                    while True:
                                        try:
                                            choosenTarget = int(input("What is the taget of the option you want to "+("edit" if choice == "1" else "delete")+"? "))
                                            for index, option in enumerate(options):
                                                if choosenTarget == option['target']:
                                                    optionIndex = index
                                                    name = "option "+str(choosenTarget)
                                                    break
                                            if choosenTarget == option['target']:
                                                break
                                            print("This is not part of the options.")
                                        except Exception:
                                            print("This is not a number.")
                                if choice == "2":
                                    book = deleteOption(fileName, book, pageNumber, optionIndex, name)
                                    if not options:  # if there is no more options
                                        break
                                else:  # edit option
                                    while True:
                                        choice = input("Edit the 'description' or the 'target' page ? ")
                                        if choice == "description":
                                            description = input("Here is the old description:\n"+options[optionIndex]['description']+"\nWhat do you want to replace it with ?\n")
                                            if not description == "exit":
                                                options[optionIndex]['description'] = description
                                                saveBook(fileName, book)
                                                printOptions(options)
                                            break
                                        elif choice == "target":
                                            options[optionIndex]['target'] = checkNumber("What do you want to replace target "+str(choosenTarget)+" with? ")
                                            saveBook(fileName, book)
                                            printOptions(options)

                                            break
                                        elif choice == "exit":
                                            break
                                        else:
                                            print("This is not 'description', 'target' or 'exit'.")
                            elif choice == "3":
                                book = addOptions(book, pageNumber)
                                printOptions(options)
                            elif choice == "exit":
                                break
                            else:
                                print("This is not a 1, 2, 3 or 'exit'.")
                    else:
                        book = addOptions(book, pageNumber)
                elif choice == "3":
                    if pageNumber != "0":
                        confirm = input("Are you certain you want to delete page "+pageNumber+" (y)? ")
                    if confirm == "y" or confirm == "yes":
                        del book['pages'][pageNumber]
                        saveBook(fileName, book)
                        print("Page "+pageNumber+" was successfuly deleted.")
                        printOptions(options)
                        break
                    else:
                        print("You can't delete page 0.")
                elif choice == "exit":
                    break
                else:
                    print("Try again.")
        elif pageNumber == "exit":
            break
        else:
            print("This isn't part of the gamebook's pages.")

# %%
def editBook(fileName, goToAddPage):
    book = openBook(fileName)
    while True:
        if goToAddPage:
            book = addPage(book)
            saveBook(fileName, book)

        choice = input("(1) Add new pages to this gamebook,\n(2) edit a specific page\n(3) or change it's title, author or summary?\n ")
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
                elif choice == "exit":
                    break
                else:
                    print("Try again with 'title', 'author', 'summary' or 'exit'.")
        elif choice == "exit":
            if not book['meta']['checked']:
                saveBook(fileName, book)
            return
        else:
            print("This is not a 1, 2, 3 or 'exit'.")
            continue
        saveBook(fileName, book)


# book = openBook("book.json")
# print(editPage(book, "book.json"))
start()
