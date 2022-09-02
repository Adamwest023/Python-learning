# have a python dictionary that has a key/value pair that represents a word and its definition
# collect input from the use, input is a word
# check if the word is in the dictionary
# print the word

from PyDictionary import PyDictionary

dictionary = PyDictionary("eyes","indentation", "head")

print(dictionary.getMeanings())

# while True:
#     word = input("Enter your word: ")
#     if word == "":
#         break
    
#     print(dictionary.meaning(word))



# def main():
#     word_dictionary = {
#         'hi': 'a way of greeting',
#         'eyes': ' an organ for seeing',
#         'earth': 'a habitable planet in space',
#     }
#     while True:
#         word = input("Enter a word: ")
#         if word == "":
#             break   
#         if word in word_dictionary:
#             print(word, ":", word_dictionary[word])
# main()