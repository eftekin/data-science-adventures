even_or_odd = lambda num: "even" if num % 2 == 0 else "odd"

print(even_or_odd(10))
print(even_or_odd(5))


multiple_of_three = (
    lambda num: "multiple of three" if num % 3 == 0 else "not a multiple"
)

print(multiple_of_three(9))
print(multiple_of_three(10))


rate_movie = (
    lambda rate: "I liked this movie."
    if rate > 8.5
    else "This movie was not very good."
)

print(rate_movie(9.2))
print(rate_movie(7.2))


ones_place = lambda num: num % 10

print(ones_place(123))
print(ones_place(4))


double_square = lambda num: 2 * (num**2)

print(double_square(5))
print(double_square(3))


import random

add_random = lambda num: num + (random.randint(1, 10))

print(add_random(5))
print(add_random(100))
