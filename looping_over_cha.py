letters = input ("Please enter some text")
for character in letters:
    print(f"You typed {character}")


word = "Hello"
for index in range(len(word)):
    letter = word[index]
    next_letter = ""
    next_index = index + 1
    if next_index < len(word):
        next_letter = word[next_index]
    print(f'"The letter {letter} is at index {index}, followed by {next_letter}"')
