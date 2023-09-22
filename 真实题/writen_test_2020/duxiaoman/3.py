

import sys
lines = sys.stdin.readlines()
lines = [line.strip() for line in lines]
win_dict = {'4 2', '2 4'}
for line in lines:
    if line in win_dict:
        print('WIN')
    else:
        print("LOSE")