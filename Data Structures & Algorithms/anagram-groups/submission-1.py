class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        hashOut = {}
        res = []

        for string in strs:

            hashIn = {}
            for char in string:
                hashIn[char] = hashIn.get(char, 0) + 1

            key = tuple(sorted(hashIn.items()))

            if key in hashOut:
                res[hashOut[key]].append(string)
            else:
                hashOut[key] = len(res)
                res.append([string])

        return res


            

        