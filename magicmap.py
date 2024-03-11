# Please excuse my noob-ness. This is a quick and dirty way to
# produce the magic numbers needed to know what the 'visible'
# characters of a View are.

magicmap = [
'       a',
'    abcdefg',
'   abcdefghi',
'  abcdefghijk',
' abcdefghijklm',
' abcdefghijklm',
' abcdefghijklm',
'abcdefghijklmno',
' abcdefghijklm',
' abcdefghijklm',
' abcdefghijklm',
'  abcdefghijk',
'   abcdefghi',
'    abcdefg',
'       a'
]

line = '['
for i in range(0,len(magicmap)):
    for j in range(0,len(magicmap[i])):
        if not magicmap[i][j].isspace():
            line += "[{},{}],".format(i,j)
line += ']'
line.replace(",]","]")
print(line)
