class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        result = []

        for str in strs:
            key = ''.join(sorted(str))
            anagrams[key] = anagrams.get(key, []) + [str]

        for k, v in anagrams.items():
            result.append(v)

        return result 
