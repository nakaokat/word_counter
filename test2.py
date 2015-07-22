# -*- coding: utf-8 -*-
__author__ = 'nakaokataiki'

import main


example = "alice. in, the: wonderland;"
collect = "alice in the wonderland"



result = main.main(example, main.no_ignore)
print(result)

if __name__ == '__main__':
    if main.remove_mark(example) == collect:
        print(main.remove_mark(example))
        print("okay")
    else:
        print(main.remove_mark(example))
        print("not okay")

