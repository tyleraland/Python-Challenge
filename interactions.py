import string
import re

# Challenge 0
sol1 = 2**38

#challenge 1
clue1 = '''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'''
frm = string.ascii_lowercase
to = string.ascii_lowercase[2:] + 'ab'
string.translate(clue1, string.maketrans(frm,to)) # Directs user to apply
sol1 = 'ocr'

#challenge 2
clue2 = open('clue2').read()
string.translate(clue2, string.maketrans('',''), '!@#$%^&*()[]{}_+').replace('\n','') #equality

#challenge 3
clue3 = open('clue3').read()
ch3 = re.compile('(?<![A-Z])[A-Z][A-Z][A-Z][a-z][A-Z][A-Z][A-Z](?![A-Z])')
sol3 = "".join([letter[3] for letter in re.findall(ch3, clue3)])
print(sol3) # First attempt: try the first letter 'l'
