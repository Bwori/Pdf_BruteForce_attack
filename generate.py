# Print into a txt file
# from 0 to 1000

final = '1000'
initail = 0
test = '0000'
fout = open('Code.txt', 'w')
print(test)
while initail < 10:
    code = "\n000"+ str(initail)
    fout.write(code)
    initail +=1
while initail < 100:
    code = "\n00"+ str(initail)
    fout.write(code)
    initail +=1
while initail < 1000:
    code = "\n0"+ str(initail)
    fout.write(code)
    initail +=1
while initail < 10000:
    code = "\n"+ str(initail)
    fout.write(code)
    initail +=1
fout.close()
print("End")