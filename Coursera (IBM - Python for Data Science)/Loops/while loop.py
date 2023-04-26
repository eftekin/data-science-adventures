PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
i = 0
rating = PlayListRatings[0]

while i < len(PlayListRatings) and rating >= 6:
    print(rating)
    i = i + 1
    rating = PlayListRatings[i]
