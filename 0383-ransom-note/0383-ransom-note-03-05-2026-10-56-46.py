class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_dict = {}
        for ch in magazine:
            mag_dict[ch] = mag_dict.get(ch,0) + 1
        
        for ch in ransomNote:
            mag_dict[ch] = mag_dict.get(ch, 0) - 1
            if mag_dict[ch] == -1:
                return False
            
        return True