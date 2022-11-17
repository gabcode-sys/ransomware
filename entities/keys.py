"""
 *  ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
 *  ¨ AUTHOR: mrc1002          ¨
 *  ¨ Credits: None            ¨
 *  ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
"""

import string
import random
import sys


class Key(object):

    def __init__(self, **args):

        """Set encryption key"""
        self._value = ''.join(random.choice(
            string.ascii_lowercase + string.ascii_uppercase + string.digits + r'^!\$%&/()=?{[]}+~#-_.:,;<>|\\') for _ in
                              range(20000))

    @property
    def value(self):
        return self._value


if __name__ == '__main__':
    k = Key()
