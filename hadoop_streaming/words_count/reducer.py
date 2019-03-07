# coding=utf-8
import sys
from operator import itemgetter
from itertools import groupby

def read_mapper_output(files, separator='\t'):
    for line in files:
        yield line.strip().split(separator, 1)

def main():
    data = read_mapper_output(sys.stdin)
    for key, data in groupby(data, itemgetter(0)):
        count = 0
        for value in data:
            count += 1
        print "{word}\t{count}".format(word=key, count=count)

if __name__ == '__main__':
    main()
