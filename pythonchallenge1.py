#!/usr/bin/python

def transform(character):
	if ord(character)>=ord('a') and ord(character)<=ord('z'):
		return chr(((ord(character)-ord('a')+2)%26)+ord('a'))
	elif ord(character)>=ord('A') and ord(character)<=ord('Z'):
		return chr(((ord(character)-ord('A')+2)%26)+ord('Z'))
	else:
		return character

def decode(message):
	return "".join(map(transform,message))


print decode("g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.")
