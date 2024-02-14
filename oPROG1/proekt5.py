import pymorphy3
morph = pymorphy3.MorphAnalyzer()

word1 = input()
word2 = input()
word3 = input()
word4 = input()

w1 = morph.parse(word1)[0].inflect({"ablt"})

if w1.tag.gender == "masc":
    pr = 'он'
elif w1.tag.gender == "femn":
    pr = 'она'
else:
    pr = 'оно'

w2 = morph.parse(word2)[0].inflect({"plur", "gent"})
w4 = morph.parse(word4)[0].inflect({"accs"})
A = {"accs", "sing", w4.tag.gender}
w3 = morph.parse(word3)[0].inflect(A)

print(f"Плохого человека {w1.word.title()} не назовут. Имея множество {w2.word}, {pr} может создать {w3.word} {w4.word}")


# word = input("Введите слово: \n")
# word = word.inflect({"plur", "gent"})
# text = text.format(word=word.word)
# if "masc" in word.tag:
#     text = text.format(pronoun='он')
# if "femn sign" in word.tag:
#     text = text.format(pronoun='она')

# for i in range(0, 4):
#     word = morph.parse(input("Введите слово: \n"))[0]
#     print(word)
#     if "NOUN" in word.tag:
#         word = word.inflect({"plur", "gent"})
#     if "VERB" in word.tag or "INFN" in word.tag:
#         word = word.inflect({""})
#     if "ADJF" in word.tag:
#         A = {"sing", "accs"}
#
#         word = word.inflect(A)
#
#

# input_words = []
# pronoun = morph.parse('он')
# print("Введите 4 слова")
# for i in range(0, 4):
#     input_words.append(input())
#
# for item in input_words:
#     word = morph.parse(item)[0]
#     print(word)
#     if ("VERB" in word.tag):
#         text = text.format(verb = word.word)
#     elif ("ADJF" in word.tag):
#         text = text.format(adj = word.word)
#     elif ("NOUN" in word.tag):
#         text = text.format(noun = word.word)
#         if ("masc" in word.tag):
#             text = text.format(pronoun = pronoun.word)
#         elif ("fem" in word.tag):
#             pronoun = pronoun.inflect({"femn sing"})
#             text = text.format(pronoun = pronoun.word)