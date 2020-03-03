"""
Playing with Python's `Counter`

- it's like a dictionary
- values can be positive/negative integers
- keys correspond to the things you want to count

"""
'''
>>> from collections import Counter
>>> c = Counter()  # Create a Counter
>>> c['widgets'] += 1  # start counting 'widgets'
>>> c
Counter({'widgets': 1})

# (most) regular dict methods are available
>>> c.keys()
['widgets']

>>> c.values()
[1]

>>> 'widgets' in c
True

# `update` will create new keys or adjust the counts for
# existing keys
>>> c.update({'foo': 1})
>>> c
Counter({'widgets': 1, 'foo': 1})

# calling `update` again will increment the value of 'foo'
>>> c.update({'foo': 1})
>>> c
Counter({'widgets': 1, 'foo': 2})

# You can create a Counter from an iterable
>>> c = Counter(['larry', 'moe', 'curly'])
>>> c
Counter({'larry': 1, 'curly': 1, 'moe': 1})

# Or you can pass in keyword args
>>> c = Counter(ravens=34, niners=31)
>>> c
Counter({'ravens': 34, 'niners': 31})

# `elements` gives you an iterator that yeilds a `key` for each
# `count`. (You can also create a counter from an iterable).
>>> colors = ['red', 'blue', 'yellow']
>>> c = Counter(colors)
>>> c
Counter({'blue': 1, 'yellow': 1, 'red': 1})

>>> c['red'] += 2  # Three 'red's
>>> c['blue'] += 1 # Two 'blues's
>>> c
Counter({'red': 3, 'blue': 2, 'yellow': 1})

>>> list(c.elements())
['blue', 'blue', 'yellow', 'red', 'red', 'red']

# Finding the N "most common" elements
>>> c.most_common(2)
[('red', 3), ('blue', 2)]

# Trick: Find the most common letters in a string:
>>> Counter('supercalifragilisticexpialidocious').most_common(3)
[('i', 7), ('a', 3), ('c', 3)]

# Subtracting counts
>>> money = {'gold': 1001, 'silver': 501, 'copper': 101}
>>> shield = {'gold': 25}
>>> sword = {'gold': 100, 'silver':50}

# initialize your bank
>>> c = Counter(money)
>>> c
Counter({'gold': 1001, 'silver': 501, 'copper': 101})

# Buy a shield
>>> c.subtract(shield)
>>> c
Counter({'gold': 976, 'silver': 501, 'copper': 101})

# Buy a sword
>>> c.subtract(sword)
Counter({'gold': 876, 'silver': 451, 'copper': 101})

# Buy a Castle!
>>> castle = {'gold': 50000, 'silver': 9999, 'copper': 350}
>>> c.subtract(castle)
>>> c
Counter({'copper': -249, 'silver': -9548, 'gold': -49124})
# oops!

# start over!
>>> c.clear()
Counter()
'''