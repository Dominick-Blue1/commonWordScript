#  The purpose of this script is to pull in a text file and output the most common words used within the file.

#  Collections Module
#  The collection Module in Python provides different types of containers.
#  A Container is an object that is used to store different objects and,
#  provide a way to access the contained objects and iterate over them.

#  re Module
#  This module provides regular expression matching operations similar to those found in Perl.

import collections
import re

#  Make sure you place the correct file name here in 'words'
words = re.findall(r'\w+', open('words2.txt').read().lower())

#  The number placed here will give the top n most common words.
most_common = collections.Counter(words).most_common(10)
print(most_common)