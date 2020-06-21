####    How To Open This Script?    ####
###     Use unlock Function         ####
import getpass,hashlib,base64
def hasher(text,length,key):
    if length > 64:
       raise ValueError("hash length should be lower than 64")
    result = hashlib.sha256(text+key+text).hexdigest()[:length][::-1]
    return result #return final result


def separator(text,length):
    return [text[i:i+length] for i in range(0,len(text),int(length))]

def decrypt(text,key):
    textsplit = text.split("!-!")
    encrypted,shuffled,hash_length,separate_length = textsplit[0].split("|")
    encrypted = separator(encrypted,int(hash_length))
    encrypted2 = separator("".join(encrypted),int(hash_length))
    shuffled = separator(shuffled,int(separate_length))
    primary_key_is_true = True
    for i in shuffled:
        hashed = hasher(i,int(hash_length),key)
        if hashed in encrypted:
           encrypted[encrypted.index(hashed)] = i

    for i in encrypted:
        if i in encrypted2 and len(textsplit) == 1:
           raise KeyError("Wrong Key")
        elif i in encrypted2:
           primary_key_is_true = False
           break

    if primary_key_is_true:
       result = base64.b64decode("".join(encrypted)[::-1])

    if len(textsplit) >= 2 and primary_key_is_true == False:
       master_key = separator(textsplit[1],int(hash_length))
       master_key2 = separator("".join(master_key),int(hash_length))
       for i in shuffled:
           hashed = hasher(i,int(hash_length),key)
           if hashed in master_key:
              master_key[master_key.index(hashed)] = i

       for i in master_key:
           if i in master_key2:
              raise KeyError("Wrong Key")
       result = base64.b64decode("".join(master_key)[::-1])
    return result

def unlock(key):
    open("sele.py","w").write(decrypt("946a8e5aa28b6ae9b56c20b4e60e16c971787f521a41a28c890e1319934c83ca4403615c6d787ec7bbc10506999c2f2a30fbb9171847562bf89bfbc63c68eb789dc7793535e1c0b922364529c2820381701373cb422d509fe860f2ab4d91a984beb9c58dfa85fa503047003388bb81375368d195fbd53e470033818a5def16cb3ee3f0d7f4218523e766235f53ecfaa330ce9a4fc3de5a3f23a57a99a838f0d5644cfab9ea39c7edb74bacd10755ff2aaa090b1aa8e286de7f2b38ab06cf99d6e8281f36feec2ba2141753ab1bd36ddcc210701022871c6dc24df6c9786638db11d6bccb4c37637cc859da527c609c2792dadf321f94fc6b335d6c1b4b1bdaf3f3f8c70ccd106e320f466fe692cce687e728fd0c9cd27bb41c3372db996f8f2aaa090b1aa8e286de7f2b38ab06cf99d6e8281f36feec2ba2141753ab1bd36ddcc210701022871c6dc24df6c9786638db11d6bcce9e1a56ae30dfebdb12f2df00df949bc1e6f721c2eec411d701da63487123fd2b6fb199c021b6c45af338ab83bedda3953da5bfe78d6bfc49165c8d43b97fb63fa36b3b1268e3dabd735b7e6df049b3a15da7b59a3f23a5055144363fa36ba5ec8cad3343db62a0ea1a527c609c2792dadf321f94fc6b335d6c1b2a15745c7fe6e5bc159a50bf1917b6960468c6685e3aa1ed42f6e90ff5fc6ef27d4fe82ca766a597e083edcc02d91a66d7ef39a09ce27e7e5d21bd746c6c14f3f2474f18e3d3dc80da4623440603d7cf06fe94a8d8de68fa38cd1d61f2ab4bd92a3c11ac759b9f939f37669603979ba5b7f0e59edcc57b67e5dc144ee105ae6e3158a614a08498f0d2fd45b54d25b784d2743e2a6666c92716f9ea0da8a142a8bde123be59e8ffc49713ecc4dfd92976094aefbc6bf9c414ffab38ab06748997656dc6492a0f4086bc8b668a92c83c78987327856d01e45b662427c3db7961242698a11783f86068efb0028a76895342e68184032b65c18b029715f31363b36966b3da71124df58ba95ea25df1927bfd6b6a2e941262817b2aaa090b1aa8e20512c40fbc6bf9ea58bc6dd4a91d5439a0148f8213ebecdb05f66b1f5d4816d89d1c83eaf6eb0edaa50cd43ab20331590fa18658b99d1e6b9fc86c5597e083edcc02dc338759c6592d86b2da097bd09f1990f0d25e83f1988164427bd09f1c338759c6592d8fd4285937fa77c37e711d7bd09f13dd6c2cf070ca7bd76353b50a6d60a3b3b36a2e941f023250fbb9171fccd816f89bfbcccd6a9000805460abbb6e7bd09f1ec20f6c458494e80532a7310a52b332dc6c8dbe5c1d3dae314f70e35f66fddbb0cc4cf377c36a6a2e941cf4671209726cb1f8f7a898c1f027660a4561dcf225af003ffbb91718cd6d49e1db3b77ff0cd7fbb9171fccd816bc01987bac4618df52d7893535e177c21b09e8ffc4a9532c66e285b186de7f2b38ab067489976c7efbd1a37a95c0fcb36a9ed4c061b8901fe123be548ad4c7a80fd698b48dc645fd5bc4716a0469966c890e131962c98133ca3e110c1c9da128fa451faaf58720e111d99ff7277b41234370c56be840676a75a8b90b00024370c56130b576a91dc31a8062ea90ad99e0abbb6e7bd09f118a5deff0342dfd931934a8d7e879e8ffc4a9532c6ab9554f362200bbf790e61502e5c6413cdbd65569cdfa4e4ebf68b265ddd10a3cd6c5e65a2ab2969c5c8637b4b5f0de80527ccd48c1a89f650f51977bd09f1e404867e288287589257de123be548ad4c7d7b94653a4d20619b5096c6f4e30ce529d59ed11c06bf4604ed261c5a15e579d8e1a46e91756387051c8ec92187d8e1a46fff0ea3c892b4fdb0decc4716a0469966c890e1319379c5b3f6c4432cabcd311ba39a0e8ead92b9f939f39bc41e90e13191e0cb9d9e8ffc419769218428cd637fa77ce7bc2f6f5afd4ed7d0cb4d00cb46faf7c92f4c9d3101477aad5b6fc511aab461ce950a9e8ffc4711e0f1f455591dfe209a9e8ffc4abd727609df739e66c0e08b70ed699fe3524aca95dba58f5de17e4067bd09f19e8ffc4c9c54d14d1548b5bbd20b4fd5e46d78febd53260aedfa16859e8ffc47bd09f1ec20f6c458494e80532a7310a52b332dc6c8dbe5c1d3dae314f70e35f66fddbb0cc4cf377c36ae3cd42a1ba39a07bd09f1cf4671209726cb1f8f7a898c1f027660a4561dcf225af003ffbb91718cd6d49e1db3b77ff0cd7fbb9171fccd816bc01987bac4618df52d7893535e177c21b09e8ffc47bd09f1e7fd42038ff6170f7bfc4f6cb83b89cd1fde673a9a86b4fb820eb567c822e67869a7eb9ac8576ca9044d1ba39a07bd09f1cf4671209726cb019b690486923f029e4307bd09f19e8ffc4e8ead92b9f939f39bc41e90e1319474bc57eedf5fc20e8e48964e969a3454c9a578e0b87332bb14c1b380310ed7f54a80341a28c1d062c2f0a92294f6b8aecf181071788777c8b8353a51854c2d23b7e5493adb604b9b796ff0f9e36e7daf46704cef181071487de44886b42bb1d7bfa6e552d3041291aaa294b6ff740208d555f40d710daf356fb0c3457f381490bd68a464c563787fc181a1b2f14d06a0b5366dda3953b05fa22ff8542769eeccf84081f65a3709978a9dc2c5cfb1905a64ac6f10c5b5883ce8fac9aa9ccdd804322dcf5d0723e2b9aca02e810fe33492b339b636308a3ae84762c37773304f7eb6b2fe282eaeb764749a2bd0772cb4b3ef92e516f8d3fa0a5e1f3f608bfeedc9c46ccda627d80de3be692fd0679655473120b2eb613c4d6e121596c2616796ec96503fdbd1b71e34c751bbc3e99238641e060ddc2f901b3dc51e08ecdaf2f8b6d27d391e580180c8920b7ae9|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|7|8",key))

if "__main__" == __name__:
   unlock(getpass.getpass("Key : "))
