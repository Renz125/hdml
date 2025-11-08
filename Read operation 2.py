file_read = open('Code.txt', 'r')
print("File in read mode")
print(file_read.read())
file_read.close()

file_write = open('Code.txt', 'w')
file_write.write("File in write mode")
file_write.write("Hi! I am  a penguin and I am 2 years old")
file_write.close()

file_append = open('Code.txt', 'w')
file_append.write("\n File in append mode")
file_append.write("Hi! I am a penguin and I am 2 years old")
file_append.close()
