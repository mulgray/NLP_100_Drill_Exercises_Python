import sys

col1 = []
col2 = []

for line in sys.stdin:
    cols = line.split('\t')
    col1.append(cols[0]+'\n')
    col2.append(cols[1])

col1file = open('col1.txt', 'w')
col1file.writelines(col1)
col1file.close()

col2file = open('col2.txt', 'w')
col2file.writelines(col2)
col2file.close()
