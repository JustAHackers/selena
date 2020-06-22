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
    open("sele.py","w").write(decrypt("85e44c1e4cb324eff5ed7dabf3b1151391f1cb56eb10c007025e0d0619171f2b80fb20f65434153d6f9ffaead1393540b93fa985b91155a2fb297e6d0bb1bbcebc8685b35f59403ca557bd476e697e0d99a81ecc8fae9c1b3fe87fe6aa45d3b4f6129efce4f21dcef1cf8bce4cf196b31b7aed3d243f02f564120d0bf29892622d9a98812618941ab4063acae7186c4eaa28267a466d572a862ff0d2a150eb36513d5383e4f21dcef1cf8bce4cf196b31b7aed3d243f02f564120d0bf29892622d9a98812d8c1eb3b284c434a6c618548e3a18e03aaae775e39e02f8d55675cffe09b86bfecdc4eae23472fea9723777d3f35b5c87de3728fc7816cf64f16b23b4063acae7186c4e4c5a55fac95d4dcdfd874e46af97ecf8e45737db750f833b31e2c6a8081916129d88ef78764d7609111457d481136abe41e61f5ae2dfe58b36f6369f57f676e7d3fb0decf42c31a5f13e1727c2004e15b025d3c0294a4802a21c21b327fdda7f9d0cfe9b2778ea3a15318a2337196d1de818cf9cbc3785a1e7c105f1cbe2d0225799c81be010370f8bc0f3729e84a4d211ad52d23673c395d4f1edfff6c62328e4f21dce5a33f7235cbfbe2ceac974c0e68834390208465205c07515f100104fabac71861513988e9bff5ead1af0a51111a6caf39bb6411fbf4aa26575fb34324dc59022e69568c66d0e34ef7756e5e463b4d72a52cb183457340c68f094e5c80e170543ec504198915383c3969066aeac2d261f21bcf2e863b4d72a71257c70cf75fe1f5b86e3009339febc8ceddf8452cb18341f4550c5d8073c1e4da0c30c9abfac27929b1d47d313c522dcde782a7fb55cdc63f9b54059badedea037921c982dc1bdc6ef2f9a4f3a81e5848ba0f05b949b80653f3d1f3dc00c0a3246f2ac8ac251ef988b71774947cddd5986f36753a6f8c8b98fb6a5544a9412d9627b4f70cf0df5b577c9569cf22f6574f0cc691e88f3739e9b41380c98643e8a61e470700b21145267b8f0ec4f487379fbee29ea23bf0c1bf0c4db2d6c3b014102e916ea40524179642bf5bf4809534947cddd5986f36753a6f8c8b98fb6a5544a9412d9627b4f70cf0df5b577c9569cf22f6574f0cc69380a98064445ccc59292a9f2653f3d1f283218adc42c773a43406e4474872c3254aa87471d1bd8c476fa152c774333b1f10ea0178298ce2d98c8b5c0af185a2a5c5ab5c54a1bfa77087cf02592c48e0857427eb80e577621b24df90eb0507aaeb8f574d630c66b66774b2418a52e9ce0b98fb6a583be0867d56d0270e643a2ebca0b7ea758db207dce7610eae5c9a3cef105dd6757427eb8893fcce4f1cf8bceca5b26c71d47476dd68337728391ac281a4e3138b98fb6a55bfe743d460d44fe2885a9c9a21c21b32f2b9bd6fd6c953bb7beb1e40693ee67555fa975e56925e5730e244b4937fa3ad11f873d90bb19fe90a55cab690d8202228e695dabb61790bcbb0fbe0e7fda7dbd6a13257eee8fb8ddcbbfc3e2a91344b705341ce908bf6d4f0da2e30d0cb34e80737cb60344dc1aad42c79a7521a6def6430f18b5a41ca82e58e4c0bca128fab27491236489681b48c5dc10b9b40d8344aa600d56a73529887bb1656a025b8af51729289fa28cb02b196adc5986f3674ab14db17ce653bedefa2901ca0e502809d52f9a9f0090ac|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|8|16",key))

if "__main__" == __name__:
   unlock(getpass.getpass("Key : "))
