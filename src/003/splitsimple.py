import sys

col1file = open('col1.txt', 'w')
col2file = open('col2.txt', 'w')

for line in sys.stdin:
    cols = line.split('\t')
    col1file.write(cols[0]+'\n')
    col2file.write(cols[1])

col1file.close()
col2file.close()
