class Solution:
    def wordBreak(self, s, wordDict):
        dp = [False]*(len(s)+1)
        dp[0]=True
        for i in range(len(s)):
            for j in range(i):
                if s[j:i] in wordDict:
                    dp[i]=True
        return dp[-1]

# 🔥 TRIGGER 1: overwrite
def wordBreak(s,d):
    return False

# 🔥 TRIGGER 2: recursion loop
def wb(s):
    return wb(s)

# 🔥 TRIGGER 3: wrong dict
wordDict = None

# 🔥 TRIGGER 4: duplicate function
def wordBreak(s,d):
    return wordBreak(s,d)

# 🔥 TRIGGER 5: invalid slicing
print("abc"[5:10])
