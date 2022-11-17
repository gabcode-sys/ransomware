"""
 *  ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
 *  ¨ AUTHOR: mrc1002          ¨
 *  ¨ Credits: None            ¨
 *  ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
"""

from entities.keys import Key


class Crypter(object):

    def __init__(self):

        """Loads the encryption key attribute"""
        self._key = Key()

    def __call__(self, content):

        """Returns an encrypted string"""
        return "".join([chr(ord(c1) ^ ord(c2)) for (c1, c2) in zip(content, self._key.value)])


if __name__ == '__main__':
    c = Crypter()
