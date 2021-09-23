"""
import sys


def print_to_stderr(*a):

    # Here is the array holding the objects
    # Passed as the argument of the function
    print(*a, file=sys.stderr)


print_to_stderr("Hello World")
"""

from __future__ import print_function

import sys


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


eprint("abc", "efg", "xyz", sep = "--" )