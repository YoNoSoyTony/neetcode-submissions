class Solution:
    

    def encode(self, strs: List[str]) -> str:
        output = []
        for word in strs:
            output.append(f"{len(word)}|{word}")
        return "".join(output)

    def decode(self, s: str) -> List[str]:
        buildSize, buildWord = 1,2
        output = []


        word = ""
        wordSize = ""
        index = 0
        size = 0

        mode = buildSize

        while index < len(s):
            if mode == buildSize:
                if s[index] == "|":
                    size = int(wordSize)
                    word = ""
                    mode = buildWord
                if s[index].isnumeric():
                    wordSize += s[index]
            if mode == buildWord:
                for x in range(1,size+1):
                    word += s[index+x]
                index += size
                output.append(word)
                wordSize = ""
                mode = buildSize
            index += 1

        return output

                    

                


