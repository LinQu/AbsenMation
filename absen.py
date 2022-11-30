import datetime
from bs4 import BeautifulSoup
import base64
from PIL import Image
from colorama import Fore, Back, Style
import requests


tanggal = datetime.datetime.now().strftime("%d-%m-%Y")
# URL
login = 'https://satgas-covid19.polytechnic.astra.ac.id/mahasiswa/Page_Login.aspx'
default = 'https://satgas-covid19.polytechnic.astra.ac.id/mahasiswa/Default.aspx'
absen = 'https://satgas-covid19.polytechnic.astra.ac.id/mahasiswa/Page_Absen.aspx'

username = input('NIM: ')
password = input('Password: ')


# Login
cookies = {
    '_ga': 'GA1.3.1016601159.1664154820',
    '_gid': 'GA1.3.1235991604.1669596888',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    # Requests sorts cookies= alphabetically
    # 'Cookie': '_ga=GA1.3.1016601159.1664154820; _gid=GA1.3.1235991604.1669596888',
    'Origin': 'https://satgas-covid19.polytechnic.astra.ac.id',
    'Referer': login,
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

data = {
    '__EVENTTARGET': 'btnLogin',
    '__EVENTARGUMENT': '',
    '__VIEWSTATE': 'Qr74B2JiZiDd+w7/kNsN1ECEbAh9PePo0mzUKiT5aQDSvoggHQ1rEPvu4OHiW5L0cWOkXDoJ5JTVQL4TcSBKsWOcdwbPfWQhh/ZKt0HwUwo=',
    '__VIEWSTATEGENERATOR': '15F101B3',
    '__EVENTVALIDATION': 'ShokhxN/aYmPa4JYO0/NW2pgRGTQ+m0g3iGXFqyh0gJ53cM0ZQVaiY9EX+SafIUzK+JqKTPpEXvDT9vhY9ccJTVT0avOybTmmMVUFvgxUc6+joKMvPNnAq/d92tn6rky2PR875hBLr4vumzNWe72jDxRyujlypTPF9TiV6dv2Vc=',
    'txtUsername': username,
    'txtPassword': password,
}

response = requests.post(login, headers=headers, cookies=cookies, data=data)

# Get cookies
session = requests.Session()
session.get(login, headers=headers, cookies=cookies)
res = session.post(login, headers=headers, cookies=cookies, data=data)
res = session.get(default, headers=headers)
global polman
polman = res.request.headers['Cookie']
# replace cookie
polman = polman.replace('AbsensiPolmanAstra=', '')

try:
    if (response.status_code == 200):
        soup = BeautifulSoup(response.text, 'html.parser')
        print(Fore.GREEN)
        print("Login Succes\n"+Style.BRIGHT +
              "Login Sebagai : ", soup.findAll('b')[0].text)
        print(Style.RESET_ALL)
    else:
        print(Fore.RED+"Login Failed")
        print(Style.RESET_ALL)
except:
    print('Application Error')
    exit()

# absen


cookies = {
    '_ga': 'GA1.3.1016601159.1664154820',
    '_gid': 'GA1.3.1235991604.1669596888',
    'AbsensiPolmanAstra': polman,
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryU4HkzB1i5fBuUPzK',
    # Requests sorts cookies= alphabetically
    # 'Cookie': '_ga=GA1.3.1016601159.1664154820; _gid=GA1.3.1235991604.1669596888; AbsensiPolmanAstra=D9DBFE89FA326A6E21B417D6EAC3C604980562C910AFC0779B30D21506F553CD26D5BE481AAAA2A829D6B80CAAD4B9F4AD1ABE93F9F0F5164978DA04E5E5E4C86AEE90099B14A25469A19F7D695B285CF5D6598F6E21500DB29FA51BA4B12C424C48AA4C2F2896960D27036132B5326C39BFFDCFA3C8E5C3FD17E26FA8EA4F18D0E365B140FD00B2DB1FC40BA72C6CBC7CD122E5CB8CBF74BCA832F4A408866D60211D6798C308AA95496FD099ABB29B1928FC5F43258222C1AD54218703A32FAE8EC7F49E1A104AE78A954F26D2FF75; ASP.NET_SessionId=u3eaesxroatm4kzyjsypymex',
    'Origin': 'https://satgas-covid19.polytechnic.astra.ac.id',
    'Referer': 'https://satgas-covid19.polytechnic.astra.ac.id/mahasiswa/Page_Absensi.aspx',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

data = '------WebKitFormBoundaryU4HkzB1i5fBuUPzK\r\nContent-Disposition: form-data; name="__EVENTTARGET"\r\n\r\nctl00$MainContent$linkSubmitAdd\r\n------WebKitFormBoundaryU4HkzB1i5fBuUPzK\r\nContent-Disposition: form-data; name="__EVENTARGUMENT"\r\n\r\n\r\n------WebKitFormBoundaryU4HkzB1i5fBuUPzK\r\nContent-Disposition: form-data; name="__VIEWSTATE"\r\n\r\n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\r\n------WebKitFormBoundaryU4HkzB1i5fBuUPzK\r\nContent-Disposition: form-data; name="__VIEWSTATEGENERATOR"\r\n\r\nC53698AA\r\n------WebKitFormBoundaryU4HkzB1i5fBuUPzK\r\nContent-Disposition: form-data; name="__VIEWSTATEENCRYPTED"\r\n\r\n\r\n------WebKitFormBoundaryU4HkzB1i5fBuUPzK\r\nContent-Disposition: form-data; name="ctl00$MainContent$hidAlamat"\r\n\r\n\r\n------WebKitFormBoundaryU4HkzB1i5fBuUPzK\r\nContent-Disposition: form-data; name="ctl00$MainContent$hidPosisi"\r\n\r\n\r\n------WebKitFormBoundaryU4HkzB1i5fBuUPzK\r\nContent-Disposition: form-data; name="ctl00$MainContent$checkGejala$11"\r\n\r\n12\r\n------WebKitFormBoundaryU4HkzB1i5fBuUPzK\r\nContent-Disposition: form-data; name="ctl00$MainContent$ddlVaksin"\r\n\r\n3\r\n------WebKitFormBoundaryU4HkzB1i5fBuUPzK\r\nContent-Disposition: form-data; name="ctl00$MainContent$gridPertanyaan$ctl02$radioPertanyaan"\r\n\r\nradioPertanyaanTidak\r\n------WebKitFormBoundaryU4HkzB1i5fBuUPzK\r\nContent-Disposition: form-data; name="ctl00$MainContent$gridPertanyaan$ctl03$radioPertanyaan"\r\n\r\nradioPertanyaanTidak\r\n------WebKitFormBoundaryU4HkzB1i5fBuUPzK\r\nContent-Disposition: form-data; name="ctl00$MainContent$gridPertanyaan$ctl04$radioPertanyaan"\r\n\r\nradioPertanyaanTidak\r\n------WebKitFormBoundaryU4HkzB1i5fBuUPzK\r\nContent-Disposition: form-data; name="ctl00$MainContent$gridPertanyaan$ctl05$radioPertanyaan"\r\n\r\nradioPertanyaanTidak\r\n------WebKitFormBoundaryU4HkzB1i5fBuUPzK\r\nContent-Disposition: form-data; name="ctl00$MainContent$gridPertanyaan$ctl06$radioPertanyaan"\r\n\r\nradioPertanyaanTidak\r\n------WebKitFormBoundaryU4HkzB1i5fBuUPzK\r\nContent-Disposition: form-data; name="ctl00$MainContent$gridPertanyaan$ctl07$radioPertanyaan"\r\n\r\nradioPertanyaanTidak\r\n------WebKitFormBoundaryU4HkzB1i5fBuUPzK\r\nContent-Disposition: form-data; name="ctl00$MainContent$ddUrut"\r\n\r\nfma_tanggal desc\r\n------WebKitFormBoundaryU4HkzB1i5fBuUPzK\r\nContent-Disposition: form-data; name="ctl00$changeOldPassword"\r\n\r\n\r\n------WebKitFormBoundaryU4HkzB1i5fBuUPzK\r\nContent-Disposition: form-data; name="ctl00$changeNewPassword"\r\n\r\n\r\n------WebKitFormBoundaryU4HkzB1i5fBuUPzK\r\nContent-Disposition: form-data; name="ctl00$changeConfirmPassword"\r\n\r\n\r\n------WebKitFormBoundaryU4HkzB1i5fBuUPzK--\r\n'

response = requests.post('https://satgas-covid19.polytechnic.astra.ac.id/mahasiswa/Page_Absensi.aspx',
                         cookies=cookies, headers=headers, data=data)
print(response.text)
try:
    if (response.status_code == 200):
        soup = BeautifulSoup(response.text, 'html.parser')
        print(soup.findAll('img')[0].text)
        print(Fore.GREEN)
        qr = soup.findAll(id='imgBarcode')[0]['src']
        dec = base64.b64decode(qr.replace('data:image/png;base64,', ''))

        with open("qr.png", "wb") as fh:
            fh.write(dec)
            fh.close()

        print("Absen Berhasil pada tanggal: " + str(datetime.datetime.now()))

        img = Image.open('qr.png')
        img.show()
        print(Style.RESET_ALL)
    else:
        print(Fore.RED+"Absen Gagal")
        print(Style.RESET_ALL)
except Exception as e:
    print(Fore.BLACK+"Absen Erorr")
    print(e)
    print(Style.RESET_ALL)
