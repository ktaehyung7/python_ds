def lcs(i, j):
    if i==word1_length or j == word2_length:
        return 0
    if word1[i]==word2[j]:
        return 1+lcs(i+1, j+1)
    else:
        return max(lcs(i+1, j), lcs(i, j+1))
    
word1='abcde'
word2='cdefab'
word1_length=len(word1)
word2_length=len(word2)
print(lcs(0,0))