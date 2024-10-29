import re
import glob, os
valid_ip = ''
unvalid_ip = ''
os.chdir(".")
ip = ""
valid_list = []
unvalid_list = []


valid_ip_check = r"\b(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b\.\b(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b\.\b(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b\.\b(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b"
for txt_list in glob.glob("*.txt"):
    with open(txt_list, 'r') as f:
        txt_text = f.read()
        search_ip = re.findall(r'\d+\.\d+\.\d+\.\d+/?[0-9]?[0-9]?', txt_text)

    for el in search_ip:
        ip += str(el)
        ip = ip.replace(',', '.')
        ip = ip.replace(' ', '')
        ip = ip.replace("\'", "")
        ip += '\n'
        result = re.match(valid_ip_check, el)
        if result:
            valid_ip += str(el)
            valid_ip += '\n'
            valid_list = valid_ip.split('\n')
            valid_list.sort()
        else:
            unvalid_ip += str(el)
            unvalid_ip += '\n'
            unvalid_list = unvalid_ip.split('\n')
            unvalid_list.sort()

valid_ip = str(valid_list).replace('\'', '').replace(',','').replace('[', '').replace(']','').replace(' ', '\n')
unvalid_ip = str(unvalid_list).replace('\'', '').replace(',','').replace('[', '').replace(']','').replace(' ', '\n')




with open('./IP/Корректные_IP.txt', 'w') as f:
    f.write(valid_ip)
with open('./IP/Корректные_IP.docx', 'w') as f:
    f.write(valid_ip)
with open('./IP/Корректные_IP.xlsx', 'w') as f:
    f.write(valid_ip)
with open('./IP/Не Корректные_IP.txt', 'w') as f:
    f.write(unvalid_ip)
with open('./IP/Не Корректные_IP.docx', 'w') as f:
    f.write(unvalid_ip)
with open('./IP/Не Корректные_IP.xlsx', 'w') as f:
    f.write(unvalid_ip)


























# with open("ip.docx", 'w') as f:
#     f.write(ip)











