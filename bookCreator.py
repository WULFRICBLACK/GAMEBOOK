import json
import os

# %%
def openBook(fileName):
    with open(fileName, 'r') as f:
        book = json.load(f)
    return book


# %%
def saveBook(fileName, book):
    # print(json.dumps(book, indent=2, ensure_ascii=False))
    print("saving…")
    with open(fileName, 'w+') as f:
        json.dump(book, f, indent=2, ensure_ascii=False)

# %%
def start():
    while True:
        start = input("Do you want to create a new gamebook (1) or edit (2) one? ")
        if start == "1":
            createBook()
            break
        elif start == "2":
            while True:
                title = input("What is the gamebook's filename? ")
                fileName = title+".json"
                ex = False
                if title == "exit":
                    break
                elif not os.path.isfile(fileName):  # check if the file exists
                    print("No such file in directory.")
                else:
                    editBook(fileName)
                    ex = True
                    break
            if ex:
                break
        else:
            print("This is not 1 or 2.")

# %%
def createBook():
    while True:
        title = input("What is the gamebook's title? ")
        fileName = title+".json"
        #%% if not os.path.isfile(fileName):  # check if the file already exists
        #     break
        # else:
        #     print("A file with this name already exists.")
        break # removed line and add comments to the code at the end of the project
    # %%
    book = {}
    book['meta'] = {}
    book['meta']['title'] = title
    book['meta']['author'] = input("Who is the gamebook's author? ")
    book['meta']['summary'] = input("What is the gamebook's summary? ")
    book['pages'] = {}

    saveBook(fileName, book)
    editBook(fileName)

# %%
def editBook(fileName):
    while True:
        book = openBook(fileName)
        pageNumber = 0
        while True:
            if not str(pageNumber) in book['pages']:
                break
            pageNumber += 1
        content = input("What is the content of page "+str(pageNumber)+"? ")
        options = []
        for ordinalNumeral in ["1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th"]:
            optionDescription = input("What is option "+str(pageNumber)+"'s "+ordinalNumeral+" description (or exit)? ")
            if optionDescription == "exit":
                if ordinalNumeral == "1st":
                    print("This will be considered as one ending of the gamebook.")
                break
            target = checkNumber("What is the "+ordinalNumeral+" option leading to? ")
            options.append({"description": optionDescription, "target": target})

        book['pages'][str(pageNumber)] = {}
        book['pages'][str(pageNumber)]['content'] = content
        book['pages'][str(pageNumber)]['options'] = options
        print(json.dumps(book, indent=2, ensure_ascii=False))
        saveBook(fileName, book)
        break

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


start()

# while True:
#     input("what is the description of page "+pageNumber+"?")
#     while True:
#         input("how many output options do you want for this page (number)?")
#         if numberOfOptions == "coin":
#             for i in ["first", "second"]:  # alternatively ["heads", "tails"]
#                 tryPageNumber(where is the "i" option leading to?)
#                 input("what is the description of the "i" option?")
#             break
#         else:
#             white True:
#                 try:
#                     numberOfOptions = int(numberOfOptions)
#                     if 1 = < numberOfOptions = < 3:
#                         for i in numberOfOptions:
#                             tryPageNumber(what is page "i" leading to?)
#                             what is the description of page "i"?
#                         break
#                     else:
#                         it should be between 1 and 3 exits
#                 except Exception:
#                     this is not in the options, try again!
