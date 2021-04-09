import json
import os

def openBook(fileName):
    with open(fileName, 'r') as f:
        book = json.load(f)
    return book

# %%
def i():
    page = 0
    while True:
        print(book['pages'][str(page)]['content'])
        while True:
            targets = [option['target'] for option in book['pages'][str(page)]['options']]
            for target, option in zip(targets, [option['description'] for option in book['pages'][str(page)]['options']]):
                print(target, option)

            currentPage = int(input("Whih page do you want to go to? "))
            if currentPage in targets:
                page = currentPage
                break
            else:
                print("This isn't part of the options\n")



while True:
    title = input("What is the gamebook's filename? ")
    fileName = title+".json"
    if not os.path.isfile(fileName):  # check if the file exists
        print("No such file in directory.")
    else:
        book = openBook(fileName)
        break

print("\n", "Title: " + book['meta']['title'],  "Author: " + book['meta']['author'], book['meta']['summary'], "\n", sep="\n")

if book['meta']['checked'] == True:
    i()
else:
    print("the book hasn't been checked for errors go to the bookCreator and check it!")








# previous = 0
# cur = int(input("name the page: "))

# for option in book['pages']['0']['options']:
#     if cur == option['target']:
#         print(book['pages'][str(cur)]['content'])
#         break
# # cannot easily add else outside of loop


# # however, using lists comprehension
# if cur in [option['target'] for option in book['pages'][str(previous)]['options']]:
#     print(book['pages'][str(cur)]['content'])
# else:
#     print("This isn't part of the options")

# previous = cur # store the pre value
