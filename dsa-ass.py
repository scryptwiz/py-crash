# most repeated text in a sentence
sentence = "This is a common interview question"

char_freq = {}
for char in sentence:
    if char in char_freq:
        char_freq[char] += 1
    else:
        char_freq[char] = 1

print(char_freq)
