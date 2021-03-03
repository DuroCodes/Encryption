import pandas as pd
from os import system as sys
from termcolor import colored as c
import time

print(c("███████╗███╗   ██╗ ██████╗██████╗ ██╗   ██╗██████╗ ████████╗██╗ ██████╗ ███╗   ██╗", "red"))
print(c("██╔════╝████╗  ██║██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║", "yellow"))
print(c("█████╗  ██╔██╗ ██║██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║   ██║██║   ██║██╔██╗ ██║", "green"))
print(c("██╔══╝  ██║╚██╗██║██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║   ██║██║   ██║██║╚██╗██║", "cyan"))
print(c("███████╗██║ ╚████║╚██████╗██║  ██║   ██║   ██║        ██║   ██║╚██████╔╝██║ ╚████║", "blue"))
print(c("╚══════╝╚═╝  ╚═══╝ ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝", "magenta"))
time.sleep(1)
sys("clear")

encryptionkey = pd.read_csv(r"decodekeynew.csv",
                            sep=',', names=['Character', 'Byte'], header=None, skiprows=[0])

df = pd.DataFrame(data=encryptionkey)

df['Character'] = df['Character'].astype(str)
df['Byte'] = df['Byte'].astype(str)

def split(message):
    return [char for char in message]

choice = input("Please choose one of the following:\n  1. Encrypt a key\n  2. Decrypt a key\n[1/2]: ")
sys("clear")

if(choice.lower() in ["1", "one", "encrypt"]):
  message = input("Input the string you wish to encrypt: ")
  sys("clear")
  message_split = split(message)
  def code_message():
    coded_message = ""

    for i in range(len(message_split)):
        j = message_split[i]
        try:
            coded_char = encryptionkey.loc[encryptionkey['Character'] == j, 'Byte'].iloc[0]

        # To handle if character is not in our decryption list
        except:
            print('unrecognized character')
            coded_char = '@@@'

        coded_message = coded_message + coded_char
    return coded_message
  
  coded_message = code_message()
  print('Your coded message:', code_message(), '\n')

# ---------------------------------------------------------------------------------------------------#

if(choice.lower() in ["2", "two", "decrypt"]):
  coded_message = input("Input the string you wish to decrypt: ")
  sys("clear")
  
  def decode_message(message):
    new_word = ''
    decoded_message = []

    for i in range(0, len(message), 2):
        j = message[i:i + 2]
        index_nb = df[df.eq(j).any(1)]

        df2 = index_nb['Character'].tolist()

        s = [str(x) for x in df2]

        decoded_message = decoded_message + s

    new_word = ''.join(decoded_message)

    return new_word
  coded_message_str = str(coded_message)
  print('Your decoded message:', decode_message(coded_message_str))

