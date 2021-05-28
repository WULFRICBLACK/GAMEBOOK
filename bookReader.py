# -*- coding: utf-8 -*-
import json
import os

# %%
def openBook(fileName):
    with open(fileName, 'r', encoding='utf8') as f:
        book = json.load(f)
    return book

# %%
def saveBook(fileName, book):  # saveState(page)
    # print(json.dumps(book, indent=2, ensure_ascii=False))
    print("saving…")
    with open(fileName, 'w+', encoding ='utf8') as f:
        json.dump(book, f, indent=2, ensure_ascii=False)

# %%
def saveTxt(book):
    visitedPages = book['meta']['visitedPages']
    while True:
        choice = input("What name do you want to give this txt file? (or exit) ")
        if choice == "exit":
            return
        try:
            with open(choice+'.txt', 'x') as f:
                f.writelines(book['pages'][page]['content']+"\n\n" for page in visitedPages)
            break
        except FileExistsError:
            print("A file with this name alreay exists.")
    print("Your file "+choice+".txt was saved successfully.")

# %%
def bookPlayer(continuePlaying, book):
    visitedPages = book['meta']['visitedPages']
    if continuePlaying:
        page = str(visitedPages[-1])
    else:
        visitedPages.clear()
        page = "0"
    while True:
        print(book['pages'][page]['content'])
        try:
            if visitedPages[-1] != page:
                raise Exception
        except Exception:  # InedxError (raised when the list is empty) is part of Exception
            visitedPages.append(page)
            saveBook(fileName, book)
        while True:
            targets = [option['target'] for option in book['pages'][page]['options']]
            if not book['pages'][page]['options']:  # if no options => end of book
                choice = input("\nYou reached the end of this gamebook! Do you want to save your storyline as a txt file (y)? ")
                if choice == "y" or choice == "yes":
                    saveTxt(book)
                visitedPages.clear()
                saveBook(fileName, book)
                return
            elif len(book['pages'][page]['options']) == 1:
                for option in [option['description'] for option in book['pages'][page]['options']]:
                    print(option)
                _ = input("[enter]\n")
                page = str(targets[0])
                break
            else:
                for target, option in zip(targets, [option['description'] for option in book['pages'][page]['options']]):
                    print(target, option)
                currentPage = input("Which page do you want to go to? ")
            if currentPage in [str(i) for i in targets]:  # or if any(currentPage in str(i) for i in tartets):
                page = currentPage
                break
            else:
                print("This isn't part of the options.\n")

# %%
while True:
    while True:
        title = input("What is the gamebook's filename (without extention)? ")
        fileName = title+".json"
        if not os.path.isfile(fileName):  # check if the file exists
            print("No such file in directory.")
        else:
            book = openBook(fileName)
            break

    print("\n", "Title: "+book['meta']['title'], "Author: "+book['meta']['author'], book['meta']['summary'], "\n", sep="\n")

    if book['meta']['checked'] == True:
        if book['meta']['visitedPages']:
            choice = input("Do you want to continue with the save on page "+book['meta']['visitedPages'][-1]+" (y)? ")
            bookPlayer(choice == "y" or choice == "yes", book)
        else:
            bookPlayer(False, book)
        exit = False
        while True:
            choice = input("\nDo you want to:\n'play' the gamebook again,\n'run' another gamebook,\nor 'exit' the program?\n")
            if choice == "play":
                bookPlayer(False, book)
            elif choice== 'run':
                break
            elif choice=='exit':
                exit = True
                break
            else:
                print("You must type 'play', 'run' or 'exit'.")
        if exit:
            break
    else:
        print("The book hasn't been checked for errors go to the bookCreator and check it!")
