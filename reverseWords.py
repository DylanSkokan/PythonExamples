# create a function to reverse words in a sentence
def reverse_sentence(words):
    word_list = words.split()
    reversed_list = ""
    for i in range(len(word_list) - 1, -1, -1):
        reversed_list += word_list[i] + " "

    return reversed_list


user_sentence = input("Enter a sentence for reversal:")
print(reverse_sentence(user_sentence))

