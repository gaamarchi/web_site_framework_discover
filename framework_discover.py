import hashlib
import argparse
parser = argparse.ArgumentParser(description='port Scan')
parser.add_argument('path', help='path for icon')
args = parser.parse_args()
path_arg = args.path

#abrindo o arquivo e gerando o dicionario
with open("frameworkRaw.txt","r") as arquivo:
    framework = arquivo.read()

framework_dict = {}


temp = framework.split('\n')
for i in temp:
    item = i.split(":")
    if item != [""]:
        framework_dict[item[0]]=item[1]


def md5sum(path_img):
    with open(path_img, 'rb') as f:
        md5hash = hashlib.md5()
        for chunk in iter(lambda: f.read(8192), b''):
            md5hash.update(chunk)
        return md5hash.hexdigest()
        
md5hash = md5sum(path_arg)
if framework_dict[md5hash]:
    print(f"o site usa o framework:{framework_dict[md5hash]}")
else:
    print("framework não encontrado")