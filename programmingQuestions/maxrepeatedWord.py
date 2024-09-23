
str1 = "The line given here might be repeated but it seems to repeat is good for us because line is best"

dict1 = {}

for i in str1.split():
    if(i not in dict1.keys()):
        dict1[i] = 0
    dict1[i]+=1

print(max(dict1.items(), key=lambda x: x[1]))