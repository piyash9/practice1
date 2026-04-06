
f = open("my_file.txt", 'w')
f.write("this is my new file")
f.close()

f1 = open("my_file.txt", 'r')

print(f1.read())
f1.close()

f3 = open("my_file.txt", 'w')
