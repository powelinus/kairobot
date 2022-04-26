import re
from subprocess import Popen, PIPE

word = "myword"
p = Popen(["some", "command", "here"], 
          stdout=PIPE, universal_newlines=True)
for line in p.stdout: 
    if word in line:
       for _ in range(re.findall(r"\w+", line).count(word)):
           print("something something")