#Poke-ncrypt!

import csv

print('Welcome to Poke-ncrypt!')


#Step 1: Prompt for Pokemon Team
dex = open('Pokedex Entries Formatted.csv', mode='r')
csv_reader = csv.reader(dex)
rows = list(csv_reader)


print('Choose your Pokemon: You can select by name or Pokedex number (original 151 only)')


team = []
print(len(team))
while len(team) < 6:
    pkmn = input("Enter Pokmeon name or number, or type 'done': ")
    append_Success = False

    if pkmn.lower() == 'done':
        break
    
    try:
        pkmn_num = int(pkmn)
        if pkmn_num > 151:
            print ("Invalid Input: We don't recognize those new-fangled Pokemon. There are only 151!")
            continue
        else:
            team.append(rows[pkmn_num][1])
            append_Success = True
    except ValueError:
        pkmn = pkmn.capitalize()
        for row in rows:
            if row[1] == pkmn:
                team.append (pkmn)
                append_Success = True
                continue
    if not append_Success:
            print('Invalid Input: Please type the name of a Pokmeon')

#print(team)

            

        
        
""" for pkmn in team:
    file.seek(0)
    for row in csv_reader:
        # Access specific cells using index
        if row[1] == pkmn:
            entriesArray.append ((row[2]))  # Adjust the indices as per your
            break """


#Teams for testing.
#team = ['Charizard', 'Pikachu', 'Bellsprout', 'Mew', 'Porygon', 'Zapdos'] #Main Testing variable
#team = ['Weedle'] # Test with one pokemon


#Step 2: Select encrypt or decrypt

## action = 'encrypt'
## action = 'decrypt'

def choose_Decrypt_Encrypt():
    while True:
        choice = input("encrypt or decrypt: ").lower()
        if choice in ["encrypt", "decrypt"]:
            return choice
        else:
            print("Invalid choice. type 'encrypt' or 'decrypt'")

action = choose_Decrypt_Encrypt()
print (action)

#Step 3: Prompt for Text
plainText=''
cipherText=''
if action == 'encrypt':
    plainText = input("Please input the plain text message you wish to encrypt: ")

else:
     cipherText = input("Please input the cipher text to be decrypted")


#decrypt_test_prompt = "A etfsi fx tam cskc pyya Fuop oc zqi wzrf jtg Zi gfhtl mmmd am ul vrtt gede Pv gjedr tssr pw qh geaal O dmce xzrzpp ttzqal vvy obhl Benuehcfk ngy nvq obrv Cueh Iwfsdch cw ytllkzttgu Oze sswxj nnsv'm mfabvv  (Asoxfcf, qiige fewov 'xg exz) Fxl yhc ifv up G sqhk mt'a me ecetvlc (Zfdwuby) Zl, ccj'vl hc fifb bfzpqz Rr j asxtk de oifl vxxiaw (Zzisrde, xoffi ichfl 'tm lpz) U prgwk wz bewc Ylj cqyllkk jllc qcco cw zpyhbga Wgu wxocw qe fer Q'zf lahks bfi Kwxkqbb Ycnll ihmpp 'fa tdx Uhlyi gtaca 'la eyz Kltv!"
#text_entry = "I wanna be the very best Like no one ever was To catch them is my real test To train them is my cause I will travel across the land Searching far and wide Each Pokemon to understand The power that's inside  (Pokemon, gotta catch 'em all) Its you and me I know it's my destiny (Pokemon) Oh, you're my best friend In a world we must defend (Pokemon, gotta catch 'em all) A heart so true Our courage will pull us through You teach me and I'll teach you Pokemon Gotta catch 'em all Gotta catch 'em all Yeah!"



#Step 4: Assemble Pokedex entries

entriesArray = []

for pkmn in team:
    dex.seek(0)
    for row in rows:
        # Access specific cells using index
        if row[1] == pkmn:
            entriesArray.append ((row[2]))  # Adjust the indices as per your
            break

# dex.close #closes the pokedex file.

print (entriesArray) #for testing

#Step 5: Modify with level modifiers

#This will funcitonality will be added later

#Step 6: Combine Pokedex entries to create key

key = ''
for entry in entriesArray:
    key += entry

print (key)  ## This is for testing

## IF ENCRYPT  ##

#Step 7: Use Key to encrypt PT message

#from copilot
def vigenere_cipher(plain_text, key):
    result = []
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    plain_text_int = [ord(i) for i in plain_text]
    
    for i in range(len(plain_text_int)):
        if plain_text[i].isalpha():  # Ensuring only alphabetic characters are processed
            shift = key_as_int[i % key_length] - 65 if plain_text[i].isupper() else key_as_int[i % key_length] - 97
            value = (plain_text_int[i] + shift - 65) % 26 + 65 if plain_text[i].isupper() else (plain_text_int[i] + shift - 97) % 26 + 97
            result.append(chr(value))
        else:
            result.append(plain_text[i])  # Non-alphabetic characters are added as is

    return ''.join(result)


if action == "encrypt":
    ct = vigenere_cipher(plainText, key)
    print (ct)

 ## IF DECRYPT ##

#Step 7: Use Key to decrypt CT message 
def vigenere_decrypt(cipher_text, key):
    result = []
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    cipher_text_int = [ord(i) for i in cipher_text]
    
    for i in range(len(cipher_text_int)):
        if cipher_text[i].isalpha():  # Ensuring only alphabetic characters are processed
            shift = key_as_int[i % key_length] - 65 if cipher_text[i].isupper() else key_as_int[i % key_length] - 97
            value = (cipher_text_int[i] - shift - 65) % 26 + 65 if cipher_text[i].isupper() else (cipher_text_int[i] - shift - 97) % 26 + 97
            result.append(chr(value))
        else:
            result.append(cipher_text[i])  # Non-alphabetic characters are added as is

    return ''.join(result)

if action == 'decrypt':
    pt = vigenere_decrypt(cipherText, key)
    print (pt)