# Merging Dragons Calculator
This calculator came about as a result of a question from a mobile gaming wife to her techie husband. She was playing a game called Merge Dragons and she wanted to know how she could calculate how many baubles she would need at level X if she was on X-Y (some lower level). She gave me a quick example:
*If I am level 1 and I combine 3 baubles, I get one bauble at level 2.*
*If I am level 1 and I combine 5 baubles, I get two baubles at level 2.*

This combination works going up throughout the levels, through level 9. So if you know you need 7 level 2 baubles, that is 3 groups of 5 and 1 group of 3 in level 1 (18 baubles).

While smarter people could have probably just built this in google sheets, I used the tool I knew the best and wrote it out in Python. Then my wife wanted an online version of it that she could use while playing the game and thus I've used Flask to take my Python code onto the web.

Sample version of Merging Dragons Calculator: https://hello-app-354216.uc.r.appspot.com/




