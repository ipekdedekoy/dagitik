import sys,profile
from multiprocessing import Process, Queue, Lock ,Array

alphabet = "abcdefghijklmnopqrstuvwxyz"

if len(sys.argv) != 4:
    print  (" HATA! Kullanim soyle olmali : pyhton caeser_thread.py s n l")
    sys.exit(0)
else:
    s = int(sys.argv[1])
    n = int(sys.argv[2])
    l = int(sys.argv[3])

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





def caesar_chip(workQueue, queueLock, output):

    while  True:
        workQueue.acquire()
        myText = myInputText.read(l)
        workQueue.release()
        myText = encrypt(myText)

        queueLock.acquire()
        myOutputText = open(output, 'a')
        myOutputText.write(myText)
        myOutputText.close()
        queueLock.release()



def main():
    global keyAlphabet
    global  outputText
    queue_lock = Queue()
    processes = []
    work_queue = Queue()


    outputText = "crypted" + str(s) +'_' + str(n) + '_' +str(l)

    myInputText = open('metin.txt', 'r')
    myOutPutText = open(outputText, 'w')
    myOutPutText.close()

    keyAlphabet = shiftAlphabet()

    for i in range(0,n):
        p = Process(target=caesar_chip(), args= (work_queue,queue_lock,outputText)) #burada arguman hatasi yasiyorum ??
        p.start()
        processes.append(p)


    for p in processes:
        p.join()


    myInputText.close()
if __name__ == '__main__':
    main()