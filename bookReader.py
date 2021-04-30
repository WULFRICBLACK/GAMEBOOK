# -*- coding: utf-8 -*-
import json
import os

# %%
def openBook(fileName):
    with open(fileName, 'r', encoding='utf8') as f:
        book = json.load(f)
    return book

# %%
def iDontKnowWhatToCallYou():
    page = "0"
    while True:
        print(book['pages'][page]['content'])
        while True:
            targets = [option['target'] for option in book['pages'][page]['options']]
            for target, option in zip(targets, [option['description'] for option in book['pages'][page]['options']]):
                print(target, option)
            if book['pages'][page]['options'] != None:
                pass
                currentPage = input("Which page do you want to go to? ")
            if currentPage in targets:
                page = currentPage
                break
            else:
                print("This isn't part of the options\n")

# %%
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



# previous = 0
# cur = int(input("name the page: "))

# if cur in [option['target'] for option in book['pages'][str(previous)]['options']]:
#     print(book['pages'][str(cur)]['content'])
# else:
#     print("This isn't part of the options")

# previous = cur # store the pre value
