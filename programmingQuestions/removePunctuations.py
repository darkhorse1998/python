import string

punctuations = string.punctuation

str1 = input("Enter string: ")

str2 = "".join([x for x in str1 if x not in punctuations])
print(str2)