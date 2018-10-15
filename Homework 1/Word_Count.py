file=open("kjvdat.txt","r+")
wordcount = []
i = 0
for line in file:
   #print(line)
   l = line.split()
   p = i / 31102
   if((p % 10) == 0):
       print("{0}%".format(p))
   i += 1
   for w in l:
    isInList = False
    for cw in wordcount:
        if w == cw[0]:
            cw[1] = cw[1] + 1
            isInList = True
    if isInList == False:
        wordcount.append([w, 1])
file.close()
def sort_key(row):
    return row[1]
wordcount.sort(key = sort_key, reverse = True)
print("{:<20}{:^5}".format("WORD", "COUNT"))
print("-----------------------------------")
for c in wordcount:
    print("{:<20}{:^5}".format(c[0], c[1]))