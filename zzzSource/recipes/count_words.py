"""
Use a Counter to find the most common words in "The Wonderful Wizard of Oz" by
L. Frank Baum.

Available in plain text at:
https://ia700500.us.archive.org/2/items/thewonderfulwiza00055gut/wizoz10.txt

short link: http://bit.ly/thewonderfulwizard

Note: This code also counts the words in the header, so it's not a *realistic*
applicaton, but more of a demonstration of python's Counter.

Running this code should give you something like this:

    $ python count_words.py

    The Top 10 words
    the: 2808
    and: 1630
    to: 1143
    of: 869
    a: 819
    I: 597
    was: 502
    you: 486
    in: 476
    he: 408

"""

'''
from collections import Counter
import re
import urllib  # for more pleasant http, use http://bit.ly/python-requests


def main(n=10):

    # Download the content
    content = urllib.urlopen('http://bit.ly/thewonderfulwizard').read()

    # Clean the content a little
    content = re.sub('\s+', ' ', content)  # condense all whitespace
    content = re.sub('[^A-Za-z ]+', '', content)  # remove non-alpha chars
    words = content.split()

    # Start counting
    word_count = Counter(words)

    # The Top-N words
    print("The Top {0} words".format(n))
    for word, count in word_count.most_common(n):
        print("{0}: {1}".format(word, count))


if __name__ == "__main__":
    main()

'''