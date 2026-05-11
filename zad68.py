from typing import List


class Solution:
    def calculateWords(self, words: List[str], maxWidth: int) -> int:
        digits = 0
        int_words = 0
        for i in words:
            if digits+len(i)<=maxWidth:
                digits += len(i) + 1
                int_words+=1
            else: break
        return int_words

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        output = []
        while words:
            words_in_line = self.calculateWords(words, maxWidth)
            line = ""
            digits = 0

            for i in range(words_in_line):
                digits+=len(words[i])

            if words_in_line == len(words):
                for i in range(words_in_line):
                    if i + 1 != words_in_line:
                        line+=words[i] + " "
                    else: 
                        line+=words[i]
                        line+=" "*(maxWidth-digits-(words_in_line-1))
            elif words_in_line == 1:
                line+=words[0]+ " "*(maxWidth - len(words[0]))
            else: 
                spaces_left = maxWidth - digits
                places_left = words_in_line - 1
                for i in words[0:words_in_line]:
                    line+=i
                    if spaces_left and spaces_left % places_left==0:
                        line+= " "*int(spaces_left//places_left)
                        spaces_left -= spaces_left/places_left
                        places_left -= 1
                    elif spaces_left:
                        line+= " "*(spaces_left//places_left + 1)
                        spaces_left -= (spaces_left//places_left + 1)
                        places_left -= 1
            output.append(line)
            words = words[words_in_line:]
        return output
    
sol = Solution()
print(sol.fullJustify(["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"],20))



["What   must   be","acknowledgment  ","shall be         "]
["What   must   be","acknowledgment  ","shall be        "]