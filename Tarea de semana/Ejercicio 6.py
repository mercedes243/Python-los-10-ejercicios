sentence = input("Enter a sentence: ")
vowel = input("Enter a vowel: ")

vowel = vowel.lower()

modified_sentence = sentence.replace(vowel, vowel.upper())

print("Modified sentence:" , modified_sentence)
