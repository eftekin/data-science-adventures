def countOccurrences(fileName, word):
    count = 0
    with open(fileName, 'r') as f:
        for line in f:
            count += line.count(word)
    return count


fileName = "notes.txt"
word = "the"
occurrences = countOccurrences(fileName, word)

print(occurrences)
