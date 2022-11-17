"""
 *  ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
 *  ¨ AUTHOR: mrc1002          ¨
 *  ¨ Credits: None            ¨
 *  ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
"""

import win32api


class Dirs(object):

    def __init__(self, **args):

        """Search the installed disks"""
        # self._paths  = win32api.GetLogicalDriveStrings().split('\000')[:-1]
        self._paths = ['C:/testePadrao']

    @property
    def paths(self):
        return self._paths


if __name__ == '__main__':
    d = Dirs()
