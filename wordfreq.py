
def tokenize(lines):
    words = []
#    word = "{} är {}"
    for line in lines:
        start = 0
        while start < len(line):
            if not line[start].isspace():
                if line[start].isalpha():
#                    words.append(word.format(line[start], "en bokstav"))
                    end = start 
                    while end < len(line):
                        print(line[start:end])
                        if line[end].isalpha():
                            end += 1
                        else:
                            words.append(line[start:end].lower())
                            start = end
                elif line[start].isdigit():
                    pass
#                    words.append(word.format(line[start], "en siffra"))
                else:
                    pass
#                    words.append(word.format(line[start], "en symbol"))    
            else:
                pass
            start += 1
    return words
print(tokenize("Grön 15salami!"))