mountains = [
    ['Makalu', 8485],
    ['Lhotse', 8516],
    ['Kanchendzonga', 8586],
    ['K2', 8611],
    ['Everest', 8848]
]
highest_mountains = list(filter(lambda m: m[1] > 8600, mountains))
print(highest_mountains)