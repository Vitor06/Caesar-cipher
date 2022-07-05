from operator import mod
import string
KEY= 23
def scheme():
    letters = list(string.ascii_lowercase)
    values = [i for i in range(0,26)]
    scheme = dict(zip(letters,values))

    return scheme

def encrypt(text,scheme,key):
    letters =list(text)

    Encrypt =  lambda x : mod((x+key),26) if x is not  None else  ' '
    search_value = lambda letter : scheme.get(letter)
    search_key = lambda num : [key for key,value in scheme.items() if value==num][0] if num!=' ' else ' '

    letter_to_num = list(map(search_value,letters))
    text_num= list(map(Encrypt,letter_to_num))
    text_output =list(map(search_key,text_num))
    
    return text_output
    
def decrypt(text,scheme,key):
    return encrypt(text,scheme,-key)
    

def main():
   
    sc= scheme()

    with open('textInput.txt','r+') as f:
        text_input = f.read().strip().lower()
        encrypt_text = ''.join(encrypt(text_input,sc,KEY))
        decrypt_text = ''.join(decrypt(encrypt_text,sc,KEY))
        f.seek(0)
        f.write(encrypt_text)
        print('Original : ' + text_input)
        print('Encrypt : ' + encrypt_text.upper())

    with open('textOutPutDecrypt.txt','w') as f:
        f.write(decrypt_text)

       
main()