Introduction=input("Write you Inrtoduction ")
count=1
characterCount=0
for i in Introduction:
    characterCount=characterCount+1
    if (i==" "):
        count=count+1
        characterCount=characterCount-1
print(count)
print(characterCount)