# search the string to see if it starts with
# "the" and ends with "spain"

import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$",txt)

if x:
    print("YES , we have a match")

else:
    print("not macth")

#  ^ -----	Starts with
#  .  ------	Any character (except newline character)
#  *  -------	Zero or more occurrences
#  $ ------	Ends with