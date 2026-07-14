class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for word in strs:
            signature = self.findSignature(word)
            print(signature)
            result[signature] = result.get(signature, [])
            result[signature].append(word)
        return list(result.values())
    
    def findSignature(self, word:List[str]) -> str:
        count  = [0] * 26
        for letter in word:
            count[ord(letter)-ord('a')] += 1
        return tuple(count)
