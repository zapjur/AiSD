#musiałem usunąć plik zadanie2.csv z foldera, poniewaz był za duzy :()
f = open('zadanie2.csv', 'r')
txt = f.read()
txt = txt.lower()
txt = txt.splitlines()
txt = [l.split(',',1) for l in txt]
f.close()

for line in txt:
    if line[1] == '':
        line.pop(0)
        line.pop()

newTxt = []
for i in txt:
    if i != []:
        newTxt.append(i)

def sortTxt(newTxt):
    for i in range(len(newTxt)):
        for j in range(len(newTxt)- i - 1):
            try: 
                if int(newTxt[j][0]) > int(newTxt[j+1][0]):
                    bufor = newTxt[j]
                    newTxt[j] = newTxt[j+1]
                    newTxt[j+1] = bufor
            except ValueError:
                if newTxt[j][0] == 'id':
                    pass

sortTxt(newTxt)

def checkIfFixed(list):
    for i in range(1, len(list)):
        if list[i-1][0] == list[i][0]:
            return False
    return True

while True:
    for i in range(1, len(newTxt)):
        try:
            if newTxt[i-1][0] == newTxt[i][0]:
                newTxt[i][0] = str(int(newTxt[i][0])+1)
            elif int(newTxt[i-1][0]) > int(newTxt[i][0]):
                bufor = newTxt[i-1]
                newTxt[i-1] = newTxt[i]
                newTxt[i] = bufor
        except ValueError:
            if newTxt[i][0] == 'id':
                pass
    if checkIfFixed(newTxt) == True:
        break

for i in newTxt:
    print(i)
