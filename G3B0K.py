import os
import sys
import time



os.system('clear')
time.sleep(1)
os.system(' figlet Bahan Termux')
print "=================================================="
print " AUTHOR : TH4UF4N"
print " TEAM   : ILUSION"
print " Github : https://github.com/G3B0K-ID"
print "=================================================="
print
time.sleep(2)
print "[+] Menu Pilihan [+]"
print "[1] Bahan Termux"
pilih = raw_input('[?] pilih : ')
if pilih == "1":
        os.system('pkg update && pkg upgrade')
        os.system('pkg install python')
        os.system('pkg install python2')
        os.system('pkg install pip')
        os.system('pkg install mechanize')
        os.system('pip2 install requests')
        print "[+] Penginstallan Selesai"
