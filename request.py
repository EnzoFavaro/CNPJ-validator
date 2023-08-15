import requests
import re

#inserir o CNPJ
cnpj_bruto = "49.482.176/0001-16"
#tratamento de string
removed_chars = '.-/ '
CPNJ = '[%s]+' % re.escape(removed_chars)
final = re.sub(CPNJ, '', cnpj_bruto)

h = {
      'Authorization': '6857afe3-8873-47ed-a28d-0b462f4c6fd4-b35a481d-924a-4ea8-b63b-def48ff4c95f'
    }
payload = {
}
res_init = requests.get(f'https://api.cnpja.com/office/{final}', headers =h, params= payload)
resposta_init = res_init.json()
try:
    res = resposta_init['status']['id']
    if res == 2:
        print("CNPJ Ativo")
    else:
        print("CNPJ não ativo")
except:
    print("CNPJ não existe")