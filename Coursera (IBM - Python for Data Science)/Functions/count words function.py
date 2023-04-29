def freq(string):
    words = string.split()
    Dict = {}

    for key in words:
        Dict[key] = words.count(key)

    print("The frequency of words is: ", Dict)


freq("Mary had a little lamb Little lamb, little lamb Mary had a little lamb.Its fleece was white as snow And "
     "everywhere that Mary went Mary went, Mary went Everywhere that Mary went The lamb was sure to go")
