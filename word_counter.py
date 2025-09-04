# step1: Open text file to read the message

with open("sample.txt", "r") as file:
    text= file.read()

print(text)

# step2: split the text into word

words= text.split()

# step3: count words using dictionaries

word_count= {}

for word in words:
    word= word.lower()   # Makes lowercase to avoid Hello v/s hello
    word= word.strip(".,!?")    #Removes punctuation mark

    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# step4: Print the output

print("Number of frequency count: \n")
for word, count in word_count.items():
    print(f"{word}: {count}")