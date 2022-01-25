s = 'paypalishiring'
n = len(s)
numRows = 3

alphabets = [[] for _ in range(numRows)]
counter = 0

for i in range(n):
    if counter == (numRows-1):
        val = -1
    if counter == 0:
        val = 1
        
    alphabets[counter].append(s[i])
    counter = counter + val



result = "".join(["".join(k) for k in alphabets])

rst = ["".join(k) for k in alphabets]
