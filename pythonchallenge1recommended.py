#!/usr/bin/python

from string import maketrans

intab='abcdefghijklmnopqrstuvwxyz'
outtab='cdefghijklmnopqrstuvwxyzab'
transtab=maketrans(intab,outtab)

message="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

print message.translate(transtab)


