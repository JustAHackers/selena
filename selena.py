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
    open ("sele.py","w").write(decrypt("f68c1ab09e2c71dfb117e3386d9d93438b7763c51898ef659b95c4af705069990bbd90e48eb2faa27e23b76403aec4ba4d4a49122f2a57a8ca1013b3dffdf4bc293535e1237a9e65564529c266feab7c4dd61d9904700338ba0b53665dda3953914bc477777a1b5b8c1131dabee44f17688ff2241da854dbf63c68eb4ffcf0b4e2fff1e1c63a6bec1b0e912ef6be3ecf92e213d295ed60f2183b7f7ea11993ab5e1a2e48dabcd9394d688ccb0a3f134ed3119d0c7a5224288f801b8400cadc62d9c021b616210d62709907b39a3657e93089b9c4eebecdb05a69e65d69787d382e7f66bd36302ca218de0f03bf9a3d476c36c470b5ac9e8c34ebe6cec75be6b42e7f66bd423e626b7d041ec0fe273871c055c7e38738dde9e2966ee82b72d76cc23a55f64fc77af56a9a57b758f2f268256fb09cf411aba46a3b1a55f9227eb9697ad528dc730281709907b39a3657e93089b9c4eebecdb05a69e65d69787d382e7f66bd36302ca218de0f03bf9a3d476c36c470b5ac9e8c34ebe6cec75be6b42e7f66bd423e626babab5f6b066d5792b32aaac55667255641521d7049f5f08f8f3cb31694dd5acbef0833889aea58b79a7d8588da423b366c36c470b1e326e61bb01fc78f45946acb06c845b54309f800dca24317f5e9aee9ff28dbc1454dd719e3de7f0a3f134e403ba504ae6595896207c1cad68786abf64962b6fe273871c055c7e38738dde9e2966ee82b72d76cfbbed82725edad0088d5fee1bb25226a03b607f54124f41e0ed54f9db4f3eb0f5c1bff513a7c238038b9ba8eea4b186a072d1d7152dac64d02a780f3b982a961d746148f4bc159a5b0bf1917cb69604688c6685e8b5f651e1e4acdcc3c4c56031c70cf147393c18ec835bd0e94381255194fa4a951fca086dcf4ccc798a41898b4f2af9eeb7871c37a9ff2c481c3372d091f9017b183887cd57b395b25f8869e8c3b712ac6ecfac003abc15758f563612d21560f737fa77c437e711d37bd09f1fa9bc315b54e7720ddabcdfe3e10e4b6bdfa96d4eebecdb05a69e65d7d5dd628451acd3910828334c7def67aefb758a297dd7ec0b8e452f8aa4eafcff4b89ae028c3842aa4a7448bedae60268316bb3d7e9e6747734b2f49bf009a147fa1619f1741c894d9a00b204d688ccb774d132268438b9c0a757b435637948202ca766a709907b39a3657e938b209403e10e4b631dbf689144d5eba94dff6dd83d2f4500bba1cd51d4fd035106729c1fb1b868c79fc9765bd631c903e802a9a88cd246c8639b928443e24871af088da2c4bfe0b072d1d717afff20a04852752e226a287f1ba39a0438be58d950a6e5b9eb9281909e8ffc4b857ac9c04852752889d02622f2d47e348596f73f1ba39a0104b9b7986ff0f9e236e7daf08a5849b33766960e881644237bd09f1cd0df37834a5f666903cc080337f8a184f087b704743457620e3d49222e4b179e6ae70a3ba25df199e3c35fcdb19f512832bad23f051c191242d9d39e2b6e989e0b75225221593e41103e558c71124df5002b31cba25df1909e8ffc437bd09f1f95efb743df52d78293535e1335cf00eb80532a7381c4301f1ba39a037bd09f14f0232508fbb9171efccd8162ce169463eacedaaefd8a541816e4b3b9987b37a6d78f2fc00de463ee5645c736b84a0a7a88bb4a637bd09f109e8ffc40a9532c663d2e164741a28c8c90e13199d8d4302aea716537eb5ccafd535350c2f2a57a8578b2a73d34daf564dd937c3ab1998824ecc0a7a3275253687d33c11ac1aeb9ff1ba39a037bd09f19cf46712009726cbe019b690b8d6bfc409165c8d68c74a8095291f8b7d10ebcef5a1d5ba2de1c3747ef09b2c234608c2c9aa755637bd09f109e8ffc40a9532c6d6e285b1d0512c40dfbc6bf9de123be509e8ffc437bd09f12e323ebdb982a961f4b2028f6a6c8d54d2fd45b52197692138428cd6737fa77cce7bc2f6179dad72b06204eaba0071e2a6fdd426147c03265cb1d56cd0a9cea6af832b06767862c9ec1436e0861da04de2fff1e16d8e7616f3028ca1de123be53487de447886b42b1b1d7bfa06e552d3a041291abae4099a024f89d1dc6592d8d83de49b058ec83dad3f6c164ca9411e41769108176e874caac7c8212aa294b60ba2d646b0b9a53c537394bb145cd41d4061014d32aaa09090232c3a0314dd655e2062f674152b748c90647de9c048231202757eff0ff64870a4f56838a559fd86dc2f5a659244cacce88854041d579234dce29f3821cab29abef2638b998076cf531adf1e12159659a0cccd0c1cf1c581f22f526856ef89fbd763533751f686e88164423157addf951bbc3e5b4c30d061ce6385a5730eb52fce3d95fbd7e1d2a836ba402ab6c399e8816442fe6be242705927c3134cfa6c8ea87734d71e34c7951bbc3e7992386471e060dd604f1c6f83dc51e058ecdaf22f8b6d274d391e5860180c89520b7ae9|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|8|8",key))

if "__main__" == __name__:
   unlock("")
