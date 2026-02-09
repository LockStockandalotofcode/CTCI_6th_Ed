class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}

        # technique - Hashing
        for s in strs:
            key = "".join(sorted(s))
            if key not in result:
                result[key] = []
            result[key].append(s)

        return list(result.values())