file = open('Codingal.txt','r')
print(file.read())
file.close()

file_write = open('Codingal.txt', 'w')
print("File write mode -")
print(file_write.write("HI I am Lion, I am 3 yrs old"))
file_write.close()

file_append = open('Codingal.txt', 'a')
file_append.write("\n File append mode......")
file_append.write("Hi I am Lion, I am 3 yrs old")
file_append.close()

