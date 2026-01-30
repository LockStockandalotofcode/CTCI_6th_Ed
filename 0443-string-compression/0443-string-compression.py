class Solution:
    def compress(self, chars: List[str]) -> int:
        s = ""
        i = 0

        while i in range(len(chars)):
            count = 0
            character = chars[i]
            
            current_index = i

            while current_index < len(chars) and chars[current_index] == character:
                count += 1
                current_index += 1

            s += character
            if count > 1:
                s += f"{count}"

            i = current_index
        
        for j in range(len(s)):
            chars[j] = s[j]
        return len(s)