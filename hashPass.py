import md5,time

outputfile = open("passwords_md5.csv","w+")
for line in open("passwords_plain.txt","r"):
    outputfile.write(md5.new(line.strip()).hexdigest() + "\n")

outputfile.close()
