class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words, w_to_p = s.split(' '), dict()
        print(set(pattern))
        print()
        
        if len(pattern) != len(words): 
            print(":False")
            return False
        if len(set(pattern)) != len(set(words)):
            print(":False")
            return False
        
        for i in range(len(words)):
            if words[i] not in w_to_p:
                w_to_p[words[i]] = pattern[i]
            elif w_to_p[words[i]] != pattern[i]:
                print(":False")
                return False
        print(":True")
        return True
        
            
b = Solution()
bb = b.wordPattern("abbc", "dog cat cat dog")