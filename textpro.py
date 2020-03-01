def sentence_maker(phrase):
    interrogratives = ("how", "what", "why")
    capitalized = phrase.capitalize()
    if phrase.startswith(interrogratives):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)


results = []
while True:
    user_input = input("Say something: ")
    if user_input == "\end":
        break
    else:
        results.append(sentence_maker(user_input))

print(" ".join(results))  