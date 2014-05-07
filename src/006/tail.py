import sys
lines = sys.stdin.readlines()
for i in range(len(lines) - int(sys.argv[1]), len(lines)):
    print lines[i],
