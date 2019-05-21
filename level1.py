

def decrypt_message(message):
    decrypted_message = ""
    for c in message:
        decrypted_message += chr(ord(c)+2)
    return decrypted_message


encrypted_message = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq " \
                    "glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu " \
                    "ynnjw ml rfc spj."
url = "map"

print(decrypt_message(encrypted_message))
print("http://www.pythonchallenge.com/pc/def/"+decrypt_message(url)+".html")
