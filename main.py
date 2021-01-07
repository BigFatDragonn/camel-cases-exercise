word = input()
word_1 = (word.title())[0].lower() + (word.title())[1:]
print("".join(word_1.split()))