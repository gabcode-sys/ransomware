"""
 *  ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
 *  ¨ AUTHOR: mrc1002          ¨
 *  ¨ Credits: None            ¨
 *  ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
"""

from entities.extensions import Extensions
from entities.dirs import Dirs
import os


class Mapper(object):

    def __init__(self):

        """Load extensions and drives"""
        self._Extensions = Extensions()
        self._dirs = Dirs()

    def __call__(self):

        """yield files in directories"""
        for dirname in self._dirs.paths:

            for dirpath, dirs, files in os.walk(dirname):

                for i in files:
                    absolute_path = os.path.abspath(os.path.join(dirpath, i))
                    ext = absolute_path.split('.')[-1]

                    if ext in self._Extensions.extensions:
                        yield absolute_path


if __name__ == '__main__':
    m = Mapper()
