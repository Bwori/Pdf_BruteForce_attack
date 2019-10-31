import PyPDF2 as pd

filename = input('path to the file:')
file = open(filename, 'rb')
pdfReader = pd.PdfFileReader(file)

tried = 0

if not pdfReader.isEncrypted:
    print('The file is not encrypted! you can open successfully')

else:
    # NOTE
    # word.txt has less word and in small letters if in caps change the code ie.lower() to .Upper()
    # if the password is in digits change dictionary.txt to code.txt
    # Code.txt is 4 digit code but you can generate more from the generate.py code

    wordListFile = open('dictionary.txt', 'r')
    body = wordListFile.read().lower()
    words = body.split('\n')

    for i in range(len(words)):
        word =words[i]
        print('Trying decryption by :{}'.format(word))
        result = pdfReader.decrypt(word)
        if result ==1:
            print('Success! the password is : '+ word)
            break
        elif result == 0:
            tried += 1
            print ('Passwords tried: '+ str(tried))
            continue