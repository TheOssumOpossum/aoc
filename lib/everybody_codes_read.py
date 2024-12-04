import os
import sys

def read(filename):
    is_sample = len(sys.argv) < 2 or sys.argv[1] == '0'
    number = '1' if len(sys.argv) < 3 else sys.argv[2]
    full_path = os.path.realpath(filename)
    solution_dir = os.path.dirname(full_path)
    filename = os.path.split(full_path)[1]
    YEAR = solution_dir[-4:]
    DAY = filename[3:5]

    if is_sample:
        input_path = f'{solution_dir}/{DAY}_sample{number}.txt'
    else:
        input_path = f'{solution_dir}/../../input/everybody_codes/{YEAR}/{DAY}_data{number}.txt'

    f = open(input_path)
    txt = f.read().strip()
    f.close()
    lines = txt.split('\n')
    groups = txt.split('\n\n')

    return lines, groups
