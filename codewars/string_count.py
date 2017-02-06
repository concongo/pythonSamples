_word = "(( @)"
_word = _word.lower() #.lower makes all text lowercase. There is .upper() as well

_wordtemp = ""
for i in range(0,len(_word)):
    if _word.count(_word[i]) > 1:
        _wordtemp = _wordtemp + ')'
    else:
        _wordtemp = _wordtemp + '('
        
print("ans ", _wordtemp)
print("ans ",_word.count("e"))
