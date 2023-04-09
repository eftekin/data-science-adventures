import re

sentence = "The legendary developer was known for revolutionizing the tech industry with their groundbreaking " \
           "innovations. "
wordToSearch = "the"
result = re.findall(wordToSearch, sentence)
print(result)
