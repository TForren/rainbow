import md5,time

outputfile = open("dictionary_rainbow.csv","w+")
for line in open("words.txt","r"):
    hexstr = md5.new(line.strip()).hexdigest()
    outputfile.write(line.strip() + " " + hexstr + "\n")

outputfile.close()
