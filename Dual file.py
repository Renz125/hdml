file1 = open('Code.txt',
                        'r')
file2 = open('kitten.txt', 
                        'w')

for line in file1.readlines():

    if not(line.startswith('Coding')):

        print(line)

        file2.write(line)

file2.close()
file1.close()