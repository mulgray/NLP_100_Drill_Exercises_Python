col1lines = open('../003/col1.txt').readlines()
col2lines = open('../003/col2.txt').readlines()

concatfile = open('concat.txt', 'w')

for index in range(0, len(col1lines)):
    concatfile.writelines(col1lines[index][:-1]+'\t'+col2lines[index])

concatfile.close()
