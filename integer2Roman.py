class Solution:
    def int2Roman(self, num):
        romanPieces = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX' 
                       ,'', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'
                       ,'', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'
                       ,'', 'M', 'MM', 'MMM', 'MMMM']
        return romanPieces[num//1000+30] + romanPieces[(num//100)%10+20] + romanPieces[(num//10)%10+10] + romanPieces[num%10]
    
a=Solution()
aa = a.int2Roman(3)