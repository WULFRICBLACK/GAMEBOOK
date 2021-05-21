# -*- coding: utf-8 -*-
import json
import os

# %%
def openBook(fileName):
    with open(fileName, 'r', encoding='utf8') as f:
        book = json.load(f)
    return book


def saveBook(fileName, book):
    # print(json.dumps(book, indent=2, ensure_ascii=False))
    print("saving…") # for debug purpose only!
    with open(fileName, 'w+', encoding ='utf8') as f:
        json.dump(book, f, indent=2, ensure_ascii=False)

# %%
<<<<<<< HEAD
def bookPlayer():
=======
def iDontKnowWhatToCallYou():
>>>>>>> 0d7dc7e968a5132ca59ca2115040b344b9019c24
    page = "0"
    while True:
        print(book['pages'][page]['content'])
        while True:
            targets = [option['target'] for option in book['pages'][page]['options']]
            for target, option in zip(targets, [option['description'] for option in book['pages'][page]['options']]):
                print(target, option)
<<<<<<< HEAD
                saveBook(filename,book)
=======
>>>>>>> 0d7dc7e968a5132ca59ca2115040b344b9019c24
            if not book['pages'][page]['options']:  # if no options => end of book
                return
            elif len(book['pages'][page]['options']) == 1:
                _ = input("Clic enter to go to the next page.\n")
                page = str(target)
                break
            else:
                currentPage = input("Which page do you want to go to? ")
            if currentPage in str(targets):
                page = currentPage
                break
            else:
                print("This isn't part of the options.\n")

# %%
<<<<<<< HEAD
while True:   
    while True:
        title = input("What is the gamebook's filename? ")
        fileName = title+".json"
        if not os.path.isfile(fileName):  # check if the file exists
            print("No such file in directory.")
        else:
            book = openBook(fileName)
            break

    print("\n", "Title: "+book['meta']['title'], "Author: "+book['meta']['author'], book['meta']['summary'], "\n", sep="\n")

    if book['meta']['checked'] == True:
        bookPlayer()
        exit = False
        while True:
            choice = input("Do you wish to play the gamebook again (Type play ) or run another gamebook(Type restart) or exit the program(Type exit)")
            if choice =="play":
                bookPlayer()
            elif choice== 'restart':
                break
            elif choice=='exit':
                exit=True
                break
            else:
                print("Not valid option among play restart and exit")
        if exit:
            break    

                  
    else:
        print("The book hasn't been checked for errors go to the bookCreator and check it!")

=======
while True:
    title = input("What is the gamebook's filename? ")
    fileName = title+".json"
    if not os.path.isfile(fileName):  # check if the file exists
        print("No such file in directory.")
    else:
        book = openBook(fileName)
        break

print("\n", "Title: "+book['meta']['title'], "Author: "+book['meta']['author'], book['meta']['summary'], "\n", sep="\n")

if book['meta']['checked'] == True:
    iDontKnowWhatToCallYou()
else:
    print("The book hasn't been checked for errors go to the bookCreator and check it!")



>>>>>>> 0d7dc7e968a5132ca59ca2115040b344b9019c24
# previous = 0
# cur = int(input("name the page: "))

# if cur in [option['target'] for option in book['pages'][str(previous)]['options']]:
#     print(book['pages'][str(cur)]['content'])
# else:
#     print("This isn't part of the options")

# previous = cur # store the pre value
