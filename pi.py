text = """
    How I want a drink, alcoholic of course, after the heavy chapters involving
    quantum mechanics. All of thy geometry, Herr Planck, is fairly hard.
"""

# TODO
text = text.replace(",", "")
text = text.replace(".", "")
word = text.split()
print(word)
word_length = list(map(len, word))
print(word_length)
type(word_length)

result = "".join(map(str, word_length))
print(result)
