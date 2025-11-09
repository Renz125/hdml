outputFile = open('Unique.txt','w')
inputFile = open('Repeated.txt','r')

lines_seen_so_far = set()
print("Eliminatiing duplicate items.......")
for line in inputFile:

    if line not in lines_seen_so_far:
        outputFile.write(line)
        lines_seen_so_far.add(line)

outputFile.close()
inputFile.close()