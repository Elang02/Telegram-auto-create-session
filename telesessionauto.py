import requests,time,os,string,random
from bs4 import BeautifulSoup
from telethon.sync import TelegramClient 
from telethon.errors.rpcerrorlist import SessionPasswordNeededError

character = string.ascii_letters
while True:
    proxies = {
        'https': f'your_proxy_here',
        'http': f'your_proxy_here',
    }
    number = input('Number : ')
    path = f'session/{number}.session'
    if os.path.exists(path):
        print(f"File sesi sudah ada '{path}'.")
        continue
    s = requests.Session()

    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'en-US,en;q=0.9,ru;q=0.8,id;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://my.telegram.org',
        'priority': 'u=1, i',
        'referer': 'https://my.telegram.org/auth',
        'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
        # 'cookie': 'stel_acid=FXnTRCIKUKCdedjhsoAkl6Pohtkby9TlJUGLiOnBAkbnVmV-gQaejsS9UYHsLRwT',
    }

    data = {
        'phone': number,
    }

    response = s.post('https://my.telegram.org/auth/send_password',  headers=headers, data=data, proxies=proxies)
    print(response.text)
    random_hash = response.json()['random_hash']

    otp = input('OTP : ')
    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'en-US,en;q=0.9,ru;q=0.8,id;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://my.telegram.org',
        'priority': 'u=1, i',
        'referer': 'https://my.telegram.org/auth',
        'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
        # 'cookie': 'stel_acid=FXnTRCIKUKCdedjhsoAkl6Pohtkby9TlJUGLiOnBAkbnVmV-gQaejsS9UYHsLRwT',
    }

    data = {
        'phone': number,
        'random_hash': random_hash,
        'password': otp,
    }

    response = s.post('https://my.telegram.org/auth/login', headers=headers, data=data, proxies=proxies)
    print(s.cookies.get_dict())
    time.sleep(5)
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9,ru;q=0.8,id;q=0.7',
        'priority': 'u=0, i',
        'referer': 'https://my.telegram.org/',
        'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
        # 'cookie': 'stel_acid=FXnTRCIKUKCdedjhsoAkl6Pohtkby9TlJUGLiOnBAkbnVmV-gQaejsS9UYHsLRwT; stel_token=8346f75ecd6ce0e5ebc5a06f37b8b3ba8346f7528346bfe982dd7e6ea6d4cc31ae8d5',
    }

    response = s.get('https://my.telegram.org/apps', headers=headers, proxies=proxies)
    soup = BeautifulSoup(response.text,'html.parser')
    hash = soup.find('input', attrs={'name': 'hash'})['value']
    print(hash)
    time.sleep(3)
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,ru;q=0.8,id;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://my.telegram.org',
        'priority': 'u=1, i',
        'referer': 'https://my.telegram.org/apps',
        'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
        # 'cookie': 'stel_acid=FXnTRCIKUKCdedjhsoAkl6Pohtkby9TlJUGLiOnBAkbnVmV-gQaejsS9UYHsLRwT; stel_token=9a36d9086830862bf2b58be82ec89dec9a36d9049a369e7e8038147a54e597a007b97',
    }
    web = ''.join(random.choice(string.ascii_lowercase) for i in range(5))
    title = ''.join(random.choice(character) for i in range(8))
    short_name = ''.join(random.choice(character) for i in range(6))
    print(web)
    data = {
        'hash': hash,
        'app_title': title,
        'app_shortname': short_name,
        'app_url': f'{web}.com',
        'app_platform': 'android',
        'app_desc': '',
    }

    response = s.post('https://my.telegram.org/apps/create', headers=headers, data=data, proxies=proxies)
    print(response.text)
    time.sleep(5)
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9,ru;q=0.8,id;q=0.7',
        'priority': 'u=0, i',
        'referer': 'https://my.telegram.org/',
        'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
        # 'cookie': 'stel_acid=FXnTRCIKUKCdedjhsoAkl6Pohtkby9TlJUGLiOnBAkbnVmV-gQaejsS9UYHsLRwT; stel_token=2197a6c628f537554914faea9569e2222197a6ca2197e5c497c4f62dacebb66acf107',
    }

    response = s.get('https://my.telegram.org/apps', headers=headers, proxies=proxies)
    soup = BeautifulSoup(response.text, 'html.parser')
    all_span = soup.find_all('span', {'class': 'form-control input-xlarge uneditable-input'})
    api_id = all_span[0].text
    api_hash = all_span[1].text
    print(api_id)
    print(api_hash)

    # --- Konfigurasi ---
    # Ganti dengan kredensial Anda dari my.telegram.org

    # Nama file sesi untuk menyimpan login Anda

    # Username bot yang memiliki Web App
    path = os.path.join('session',number)
    client = TelegramClient(path, api_id=api_id, api_hash=api_hash)
    client.connect()
    print("Client Telethon started...")
    if not client.is_user_authorized():
        # Jika belum, mulai proses login dengan nomor telepon dari variabel
        client.send_code_request(number)
        try:
            client.sign_in(number, input('Masukkan kode OTP: '))
        except SessionPasswordNeededError:
            password = input('Two-step verification enabled. Please enter your password: ')
            client.sign_in(password=password)
    with open('telesession.txt','a')as f:
        f.write(f'{number}|{api_hash}|{api_id}\n')

    client.disconnect()
