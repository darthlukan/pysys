import sys

stringFile = open(sys.argv[1], 'r')

for line in stringFile:
    print(max(line.split(), key=len))

stringFile.close()
sys.exit(0)
