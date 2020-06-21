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
    open("sele.py","w").write(decrypt("17e9cde1146b16493eef62f3b9496612cd76081a89784ebd7780b34a42bb154922a35311e8d61707e2ceba1d1105b6e660048d2d79d0775f3a3921b2d688907612e40c026ffe0e17e4e16ba10c013198ee2bcb2914b1eff478ebccc04f5616e7c6f43152997dc03d02434e2aa35d3675199e18536019eb2017e7462e75878de3f984c30081b19811095febbdd63304dfe39704b4ccf1d6ef156e80043f7ebba14faf7ac61abe93591f47f353ac9558b2f31495e9688ea0bf2d2026fc0ca926b3db04020a0c882dd49ee5e91568bd193d3f37ab7637273e1c43aa4f76c5cdc957d6cdd340f7fa81074659efac1335adb6d00dda72edca01c3f42eb06648201cd7ce4294ea122fe4fc1403bd1bcc84b0da62a85ea0a7a5ddbd94540b2b8fb8b5faa86054b0beb4de369d4255ca58c5e5fa9b6035710415b0ac08ea1ee584e642a491fdc4bcec093548e0030ea20bfc6d05ef89c8ed51e1994af3d61167665012667840e5b682dd9689fc7d875ae3d88bad68b9d3350e6ea012fe9e6d5235bacb0d994439583003753aab34a13285249736af8b05ef40d0d9e4d5d7cf7055cfd5199b87a24a05834cb3ac170ca69582b7ef8ad12b826ddec013a34f1ec67a181e6bab62a47254f9c1674404dd4a75260db2037af37969e014f1da9197d69d1faa7d3e5d81731cd2de4651dabd41765e00dd75fb4044985a7d8bc09736d9aaef67586821484c20163f0cef67ec064ddb5a81bae40205cd738cfda8c0302c3f7ebba1cf92057bd9f023e1beeb3e3e7f6b6b1251501a59989195550adf2e8b8a6b68a0c5ce1c7b046fe5f8baf34f1908a865aa6d0202d035239026c8daf07df4bc6e5b892c562d91229be9f2447e92ff0f9cd0c1dbf011559a4b529e0a6fd54f2f147f97aa3f6541c476aa6e5def9d4651e6d4b7f53b99a25b3b1b6258c03c48a6488778c2e27188a4c44ec5495d86dffc6cb6d3064b3e82b0c86b467fdb9a2174581a57125dda1db2a291264288ca85f84ea33d5abc9b86d304637cdd7aa5f22d348f0881356abc0b1386616ee50d3b33053bf73db0ac3fd0478095387f049c204f23d12aff1e33b868ebc40d7d86df092593fb7d569d6799aee85158c00fa0d5bc8e155926af3d2db969c081d7b3b9aa3d50e6f23c784dfcc610bfec6d1668f683fb1d47d884de5b600f89f305e4f498bc092ddf8fe48e0da63e98fc642ba809dd751dc573fba7c1b992c6268ef2bbf68c005364066aeb55cb6baa05b394ca18a2d05b262aaa9fccd3546d7c0f98ad5e2fd407dd91ebaaa1e155ce2035f5ee43f1ff3ff06f43aae486c603c4fc43eb70bc05577a77eb6606b74b647861a69d4c41f60d1c6e7b8f57f50f55e0100d5d20c573922e5fe7bc044847e523b24c2ee3b6d43050a9e85aa45fddd7e4d09916c2bb09edcc2db3eafeaa79e20dbe400ad0b2988725138fdfc8c677ba1dd1760f21739fac38032dcc583f90486f91941041b181443b3dd6d9258597be915a23f90e313962234bc8c6a366dc6a5cc51a876cf6642a3b4b24867f9fd47bc6b28433f598418164225135640f3b2de1190588c6477fae8be0599cd8ff19b177410a78d6b6caea81fbcedb98d7d8a931057243c3e9ae34d7beb03e81525f7c098efac6726efe91c7cc1790503f8f4e6d10b9e26727ce31e057a6453d44e06f52ad12940ac90d3ddba3f37d9cb390e6d73714a7bdc7e26ea84928ae6dd3c3fc5c021e38b12002001432edccc70db11dbb08a5f29a85261dc573fb58df7458b365e3765a9c55606f1f90b17f3f2aa5a62d9ef01707e801a54b53a456b25304dc9c7ddf7d0623150ed52903858936abe866140d9c11cdd98e126dc858df7458ec01d242192d28f4a5f491770a815f9d5cabe48dd8ecf574a15fda5e6a991e0d2a9218229d6ca5d62466db694cd1f8df4142feaef99d625bff565450a199e651a13f97af5b8f9d137175fff651c8eefccc9ce85ff0de6d163f207cbcc68919ec717cb3445d20c573cb2695013fb8e598c6b43bdd977c26b38553d8883229852d854d54db1c4e0e05b3690fbd68697723e46d84c30c08ab5a53f908da432e599b814d5ac0bee6a6662627ede09324b13cf172ee598f7b5436027cb104125752da79f1d2c82007c4445376f34f57d52858417c99066624ce1e2ee3fd5f97981a7455094897df42d4cd29fadcc04a4809ceb54dc26ef663a3881406608be7336505f46dd3bca7aec804d845e067b95a153427fd7bcf0212b0537e1f376c0205f2f61938f4579485a6fac53ab5e9790b2e6a824268dd14e79778f42e10c657a97b80426c9c4c8fc598d11180f199113e754d522eaaa9ea0e3161a3cff60c9dca41e021abae223978fe832e863098ce9359bcd35d3cfe63786b6513e6ba5a25f159048f4cced618baae2ddc2747e16a2f809b62b3d58779dcbfcf|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|8|11",key))

if "__main__" == __name__:
   unlock(getpass.getpass("Key : "))
