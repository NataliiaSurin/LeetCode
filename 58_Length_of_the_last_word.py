string = " N b b b"
string = string.strip()
if " " in string:
    i = -1
    space_index = list(())
    for char in string:
        i += 1
        if char == " ":
            space_index.append(i)
    print(len(string[space_index[len(space_index)-1]+1:len(string)]))
else:
    print(len(string))



