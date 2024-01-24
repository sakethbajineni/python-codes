# RegEx stands for regular expression 
# it is a sequence of characters that forms a search operation
# iwe can check whether the string contains our input or not

import re
word="the next generation totally depends on AI"

searching=re.search("^the.*AI$",word)

if searching:
    print("yes there is match")
else:
    print("there is no match")


