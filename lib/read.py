import os
import sys

def read(filename):
    is_sample = len(sys.argv) < 2 or sys.argv[1] != '1'
    sample_number = '' if len(sys.argv) < 2 or sys.argv[1] == '0' else sys.argv[1]
    full_path = os.path.realpath(filename)
    solution_dir = os.path.dirname(full_path)
    filename = os.path.split(full_path)[1]
    YEAR = solution_dir[-4:]
    DAY = filename[3:5]

    if is_sample:
        input_path = f'{solution_dir}/{DAY}_sample{sample_number}.txt'
    else:
        input_path = f'{solution_dir}/../input/{YEAR}/{DAY}_data.txt'

    f = open(input_path)
    txt = f.read().strip()
    f.close()
    lines = txt.split('\n')
    groups = txt.split('\n\n')

    return lines, groups
