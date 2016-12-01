#!/usr/bin/env python

import sys
import threading
import profile


alphabet = "abcdefghijklmnopqrstuvwxyz"


threadLock = threading.Lock()


if len(sys.argv) != 4:
    print  (" HATA! Kullanim soyle olmali : pyhton caeser_thread.py s n l")
    sys.exit(0)
else:
    s = int(sys.argv[1]) #ne kadar kayacak
    n = int(sys.argv[2]) # kac thread olusucak
    l = int(sys.argv[3]) # blok uzunlugu

#thread classi ;
class myThread(threading.Thread):

    def __init__(self, threadID, name,order):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.order = order
    def run(self):
        caesar_chip(self)


# anahtar olusturma;

def shiftAlphabet():
    encryptedText = ""
    for i in alphabet:
        encryptedText += alphabet[(alphabet.index(i) + s) % 26]

    return encryptedText

# sifreleme;
def encrypt(text):
    encryptedText = ""
    for i in text:
        if i in alphabet:
            encryptedText += keyalphabet[alphabet.index(i)]
        else:
            encryptedText += ""
    return encryptedText

#metinden okuma ve yazma v
def caesar_chip(thread):
    control = True
    while control:
        threadLock.acquire()
        myText = myInputText.read(l)
        if myText == '':

            control = False

        threadLock.release()
        myText = encrypt(myText)

        threadLock.acquire()

        myOutputText.write(myText)
        threadLock.release()

def main():
    global myInputText, myOutputText, keyalphabet
    myInputText = open('metin.txt', 'r')
    outputFile =  "crypted_" + str(s) + "_" + str(n) + "_" + str(l) + ".txt"
    myOutputText = open(outputFile, 'w')

    my_thread = []
    keyalphabet = shiftAlphabet()

    for j in range(0, n):
        thread = myThread(j,"thread" + 'j',0)
        thread.start()
        my_thread.append(thread)

    for k in my_thread:
        k.join()

    myInputText.close()
    myOutputText.close()

    print ("Sifreleme tamamlandi")
    print ("Sifreleme sonucu cikan metin bu dosyada: " +outputFile)
if __name__ == '__main__':
     main()
