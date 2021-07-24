#! /usr/bin/python3
# -*- coding:utf-8 -*-


import os
import json
import hashlib

from dialog_info import dialog_info



print('\033[93m' + '['+"Loja Horizon OS"+'] ' + 'Lendo hash de dados...', '\033[0m')

def load_json(root_folder):
    try:    
        json_path = os.path.abspath(os.path.join(root_folder+'/Dados/Loja.json'))
        with open(json_path, "rb") as json_file:
            json_hash = hashlib.md5()
            while chunk := json_file.read(8192):
                json_hash.update(chunk)
        expected_hash = "377caa7edf3cb23ce1ecc6ead2f6d25f"
        

        if json_hash.hexdigest() == expected_hash:
            
            return json.load(open(json_path))
            

        else:
            dialog_info("Loja Horizon OS", "Foi detectado uma alteração de 'hash' no Arquivo:\
                \n\n"+json_path+"\
                \n\n Hash esperado: "+expected_hash+" \n\n Hash obtido: "+json_hash.hexdigest()+"", "Ok")
            exit()
    except Exception as e:
        
        dialog_info("Loja Horizon OS", "Ocorreu um erro ao ler o arquivo:\
            \n\n"+json_path+"\n\n Certifique-se de que o arquivo existe.\
            \n\n\ "+str(e), "Ok")
        exit()