def show(array):
    for i in array:
        print(i)
        
def lcs_dp(word1, word2):
    max=0
    index=0
    
    letters=[[0 for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]
    for i in range(len(word1)):
        for j in range(len(word2)):
            if word1[i]==word2[j]:
                letters[i+1][j+1]=1+letters[i][j]
            if max < letters[i+1][j+1]:
                max=letters[i+1][j+1]
                index=i+1
    return word1[index-max:index]

    
    

print(lcs_dp('abcde', 'cdefab'))