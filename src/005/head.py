import sys

num = int(sys.argv[1])
i = 0

for line in sys.stdin:
    print line,
    i = i + 1
    if i >= num:
        break
