import re 

txt =  "Lorem ipsum dolor sit amet, consectetur adipiscing elit"
x = re.findall("am", txt)

print(x)

#['am']