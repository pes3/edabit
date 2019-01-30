original = input("Input Sentence Here: ")

x = 0
completeList = []

for letter in original:
    if x%2 ==0:
        makecap = letter.upper()
        completeList.append(makecap)
    else:
        completeList.append(letter)
    x +=1
    s = ''.join(completeList)

print(s)
