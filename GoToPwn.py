#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# GoToPwn - MD5 Decrypt Fast
#
# By Jonatas Fil
#


import sys
import re
import urllib

BLUE = '\033[94m'
GREEN = '\033[92m'
END = '\033[0m'

def menu():
    print GREEN + "\nGoToPwn - Decrypt MD5 hash\n" + END
    print BLUE + "     by Jonatas Fil" + END
    sys.stderr.write(BLUE+ "\nUso: GoToPwn.py" + GREEN + " hash\n" + END.format(sys.argv[0]))
    sys.exit(1)

try:
    url = "http://md5decoder.org/" + sys.argv[1]

except IndexError:
       menu()

request = urllib.urlopen(url).read()

if re.search("Decrypted", request):
      decrypt = re.findall(r'Decrypted (.*?),', request)
      print BLUE + "\nCracked !!! => "+ GREEN + str(decrypt) + END + "\n"
else:
      print(BLUE + "\nFail :(" + END + "\n")
