from bs4 import BeautifulSoup
import base64
from PIL import Image
from colorama import Fore, Back, Style
import requests

# variabel cookies


def login(username, password):
    url = 'https://satgas-covid19.polytechnic.astra.ac.id/mahasiswa/Page_Login.aspx'
    default = 'https://satgas-covid19.polytechnic.astra.ac.id/mahasiswa/Default.aspx'
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
        'Referer': url,
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

    try:
        session = requests.Session()
        session.get(url, headers=headers, cookies=cookies)
        r = session.post(url, headers=headers, cookies=cookies, data=data)
        r = session.get(default, headers=headers)
        global polman
        polman = r.request.headers['Cookie']
        # replace cookie
        polman = polman.replace('AbsensiPolmanAstra=', '')

        response = requests.post(url, cookies=cookies,
                                 headers=headers, data=data)

        if (response.status_code == 200):
            soup = BeautifulSoup(response.text, 'html.parser')
            print(Fore.GREEN)
            print("Login Succes\n"+Style.BRIGHT +
                  "Login Sebagai : ", soup.findAll('b')[0].text)
            print(Style.RESET_ALL)
            # absen()
        else:
            print(Fore.RED+"Login Failed")
            print(Style.RESET_ALL)
    except:
        print(Fore.BLACK+"Login Failed")
        print(Style.RESET_ALL)


def absen():
    cookies = {
        '_ga': 'GA1.3.1016601159.1664154820',
        '_gid': 'GA1.3.1235991604.1669596888',
        'AbsensiPolmanAstra': 'D9DBFE89FA326A6E21B417D6EAC3C604980562C910AFC0779B30D21506F553CD26D5BE481AAAA2A829D6B80CAAD4B9F4AD1ABE93F9F0F5164978DA04E5E5E4C86AEE90099B14A25469A19F7D695B285CF5D6598F6E21500DB29FA51BA4B12C424C48AA4C2F2896960D27036132B5326C39BFFDCFA3C8E5C3FD17E26FA8EA4F18D0E365B140FD00B2DB1FC40BA72C6CBC7CD122E5CB8CBF74BCA832F4A408866D60211D6798C308AA95496FD099ABB29B1928FC5F43258222C1AD54218703A32FAE8EC7F49E1A104AE78A954F26D2FF75',
        'ASP.NET_SessionId': 'u3eaesxroatm4kzyjsypymex',
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

    try:
        if (response.status_code == 200):
            soup = BeautifulSoup(response.text, 'html.parser')
            print(soup.findAll('img')[0].text)
            print(Fore.GREEN)
            print("Absen Berhasil")
            qr = soup.findAll(id='imgBarcode')[0]['src']
            dec = base64.b64decode(qr.replace('data:image/png;base64,', ''))

            with open("qr.png", "wb") as fh:
                fh.write(dec)
                fh.close()
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


def download():
    cookies = {
        '_ga': 'GA1.3.1016601159.1664154820',
        '_gid': 'GA1.3.1235991604.1669596888',
        'ASP.NET_SessionId': 'u3eaesxroatm4kzyjsypymex',
        'AbsensiPolmanAstra': polman,
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryZ8LzWb0A7I3wOA70',
        # Requests sorts cookies= alphabetically
        # 'Cookie': '_ga=GA1.3.1016601159.1664154820; _gid=GA1.3.1235991604.1669596888; ASP.NET_SessionId=u3eaesxroatm4kzyjsypymex; AbsensiPolmanAstra=21FE505761F8464EAD2C58AC6F74CD799020693BCEE658DD90C0DA2FB9C92728EAB4E407CB8E3F7A86171E496B981227D6818C6621E86E138D42D5E50624A544FCDB9B8C6BE744C254BECBDC8A47E9446C97FBAD005E5EF5C1B63AFD8647A57D90DFB2D1A42C213A0B12E8F15787F1ED5CA1EBFF2536FB318FF159004B4E8F8DE666D02D0524019BA20874B4CCE8611E05277F34A0B30B65F6AF28367665ED81ADF3E1ACD8B0AD089800299123834B5B0BCC27DAB4E44DCB48BAF6F09B0C057EA1E4ADA6CA4F4EDAC934597CF3E349A2',
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

    data = '------WebKitFormBoundaryZ8LzWb0A7I3wOA70\r\nContent-Disposition: form-data; name="__EVENTTARGET"\r\n\r\nctl00$MainContent$gridData$ctl02$linkDetail\r\n------WebKitFormBoundaryZ8LzWb0A7I3wOA70\r\nContent-Disposition: form-data; name="__EVENTARGUMENT"\r\n\r\n\r\n------WebKitFormBoundaryZ8LzWb0A7I3wOA70\r\nContent-Disposition: form-data; name="__VIEWSTATE"\r\n\r\neHnMYLxJgZQLn9lNsJEK6vBcmpwRw5/TLRMq5dCaVIpdcJLSUv6+Lu+PWVCBc5gJWsW+hKJUiegXAqsSiwQ2ojaHZpBnDXSaErxPyI5PB8FH+rXTMmRyFhUl9pbWUAb5HuqLB65ixVjQeR3fU9C3xSGAyBVEIVaXK789eM1GMFbcPUmoSUGcbAkpQ85Vi/VYX4bDluiACk9UcpEKOwWMGtZ/SLNucHaaIjBITWHE5+RSlyscXJhY04VUVS+BoSB51+mkVSiQ3kMke35DznlPh9WDIji29yNIX+mL6ZYfr5cA/Hhjo5PdL4wR5Hp/ggT3Ei+yWu4PhKHB9P53XS6MSbu5+rb9+tY8tlnIXH0ZgXAGHHDCuYaVJW6bs/Oo3WQGahaIBSP4zhg9caD4eruZbDW0rk79lJ/+aismur5qxRBV+2lwaiWYfQ1KNhDk3L99Dq5KMmv0vui2j7quuBgM//dyJieMH3/yk05y/aDf1ep95A0TESNnR2LdopLfHgSNl7pgZ5R/e8++9ppLH6+NKsQyk0ruWaE1XxVbx6FyzjremCk1WuZOO+G/EtGtPYxmpElp6LQ47q/GFo4spVg2F3h7ZLIFf4m2QCeebRHNKORZs0+nUkNrDu6sh31wm2k/Hn/IbadmF9aiuMu9YuKsknd+dXjECr7qwmIZGbxNlBRz5n9lsTwPILfdiu57lzYrD4m9jtnh8rHEr6IQpVki6vVZ62rax4/9QxMVbX88yUUGggMInGdGeOyOF5dmFTrVidn2BKssu9fFuFmC4XIM2zE3UGa5R6FjHP/48BbOxIWPBvNcOEZzbBtywvbUkR+oJ9M27xaUk1AabPpJyDlnl0HNGaTadZMx4GOH1Kfef/WIfE9VRUZHM09uoq+wlBQPreAcTDeGCswpfynaXbPL4rFQyVpl2Bc2PCjg2oC4dX2i3sboOTAJjZkFA7AU9F9tj7vtBJSrMXio4BO22xWgAszCvd3rK9beHOXO8HAV5RM4eeitVNFTS5Po5pP0iFpNMiTm6UmP2fljiVsYFi3WnhpC4CAMgbgWcq+cRlY9lerxF8pgxUx2lwiIRFC8ouizjFfztf1SOhQZTLFFCEgHY+094HkmQei6/Rc0AXola0QoU8jzmizVP8hYylenRI79GRveCJo7yaZ+03zpvWTgcVI4JW7z8jdNwSJbeI0/KVZt6uQKAEUlKfO10CzHOvMNboeyS3lgJM/lB07I1c3G+VXCm/1x5+p+FKKqWdzueftTltYr5RIDdQ3CdioTJLMd1FdLMkq2ICQaPab6yPn/E6m448uvy/6tY/KgOgFq+Uq8bnt/jZK9fJSsW58LuFQy5+Qo3mG/hJGpI8RElB3XbWdORCBJuV5tBo5e8hEKCL0xXRsGiEGsU3wOqpBra5tg4Wq12/la7HaxdGQ6uDvlkSlEENZf+LvGvxogcs1h2NiQn+4J0ZV8M3aUUYqF1y3UqQDImG0NntFPYxdfJQswM4TI15d52Vn+xmGokQioyBmMBgBwGE/X8vFvZBqXj8mRV1WF+guYvEqTt8C5W4Vct1pVBAj5ecK6c8qtW8zPlIrkWnkn5mOZ1XO3RjwFZmjp+1azMhM914O7eo+GRX+ZwFeDQ7KmrGkMSMce8AitgUPP0Vg+ULhMfagczNQ7+hPQ7GbcwteQ0VSktAtcxwWwKA7M3hafcuGLDIZ8T417lh7vMyG+h8GGbRMGpR1QM0+4xQGQqT+/B0oVt8BiwgdqsF3RxmnnRpIjqO2pKfMr5ZSf/pDGMvt19pUGDB6+jLlFByH1CGOSi0aAXZWFYi+/b1ETDRmk4fEd1LayI8D6ex/vvzIgjiP+qv68AsMT7FF8YJK//P4wH6PsCl5E1gt5DMZ2pf/7LXQLSceWgklAtH3o/8wlzly2mT1w+hWXD4kKi91wgF3gmv4lnS0llgWq9ivddC2NO7moBinFJHSg4GTe1HLH6f0hS7lAHKNKN4pKVQPulVmXPL9/WnnbGcKCNVk495dsgN+6T1x1Fe32/KV9NP8gfqfqCnjC2RqvGYeL9G3x4/S5ykqVS29E7glHrNsyRbQrUjJ4DR9lkiZ7zlLQDoHURGn53MyMVZrmtgVwjdobPJC5dJBY9fJvr2WouqsoRh5WdVf7YlH0j5CLpUti5ym6nN/+9kFygwr199NBIDv9tNICW4HlGpRDmHgfD18Aj1oZCdtjpN9Ikl3NQ5QRMopcun8jwXNxgfmBIhjrxJlWcVJcIonojqsg/TX4e80WN+GTG9joZsDXfr+uA84fiJJXT1+xgiAFUCi9o3QYBrMPCOvhg2RWchq4lzP2F0pNJVr1vjP824fJORBtWd6bq0TF0Cr2uqXHJQIBX4VD2b9l0rXfIhXMt7zrMpAUazGXhbbWubNPVWzQdAb3AKX4McINPmBFnyVYr4JVWLuTOy5fhNcv2TW/LLC+eOoh9YaWcGrqvVxxZRTwx3FSjeUn5peEWtLtK6zmpWMl8P1RHGG2uziqw1+/FlbNHRQ171GKTsQXgnJVT9AQibD3iedkdhaoACvBerfP4Zp3BLU6rPS+PmTve/JlqvOIAxWrxCtwmWYRZlCSLYNLwXhRP8DUrQ4aK1pnTaP4PWxf4WODKZe7TjPxR61rDQ1ePP0vRR+utZDXdG8G/ieflkdA2B+nCfVAB8vlZn5CxOBIutt9F8v5AFFclXmVGOQioqUOiRfRequY/WkX2quQ1V/n5jgn2Xxyj1eP721yfuha0kqrk6NOIEGP6ZEvz6wKI47QtOaBwf0OMhlXwtL5USQEkr0Nc17uzuKhzbgKChezPIYFcK64iCm4nVOVf5BzT3OZU++wYmM4LLe7o+Ra/B5mhwSR3TrISIJBNZ5VGB9EFpiLVTrmoGXSGlsS85VeKqtI/tOaaNOZhYfmwfv5vCfc26/RxShmYwIleAD8e/4wUpPa+ORVmdAdLGp4uw7qMLgvU7AxldkOZDBKwet+hz3XvJRIrlNYHdIKakTHz5VpLvB+onXucMkjdIXOy7wBOqVK3WV2aOjG6bbFf/0UVAB/3mQlmPGlFrtAKTXUej7PCBnUTk+y89F0LyZfK452saXYmfkeBu8Rh1IZ61Oy4BnF7+oGXgemJ+Zz7njScg/2qX4eJCxzyyuKZhnR1z3O9nPaRNNYAxhAIp9d4lJes12woc/iPzd4hyEczXFdQyTf9XDYCRcElXb6IdE/955U3XjhQyMuKvBwXcSuQPEvEJdniEIPYDDDiYdHZYtDpyTvUh4Tn+Q9aMVrIP91g2iOt21JF53M9dCyhmRWxfMl7KPo2MXpYANa/8Ja4cvFBqADsscD/WvgCHeMcdeFGI7g5QzRH8hzh3XiRr0jIxg9IL5M+886fk2BhXPFYyZihXivkSIoG72YjNH9qb4e+pG5U7v1wXTkKZtq3W6SoCJwA3i6Vnoc75CHKdbeFqYCwD8uGw7CkMwmyGv9/Fc+FJITbAuRgeIcaESWLuFiRg9YsXfuwiMbQ/+AsEN53hnMXyg6Xb41HWWoz5DpGnpbgoEFWY5WIOz8B3km27swa2IXYTxb/iNAihlZYYgX0N2zKnCm7dCLguo6FjxsVnS7a00PtKso0tSxbmUWdr7pqkkrBxkK6cpkOV9+Z19875Fc48Wx23z2RNY7x5qJv+0FJsfXazyWNl+5OtedlR9Z2cQc9U+B+H9ffKoaN0OEar5S9jYh+3wLmhYi7kqvb1lSfF5ExzMGxXXV5alAm+elKjOq4G4245aged4V/sRQZjs1Pev85yldgm9/seOw6KSr/q4sYDxT0AmyxrK47856lXMYDkrPq1KgxO0mEia8RMjnOaWu5YH5e72uxfCWOPWWDhGCMDosDkKuiLTYW8LAW+4l6Zy49MGk1h1dedrcqVjMzrcYpj2x+2LGydfY8wUYY2g4OQo+WBs8RlDM9RXdViY9uGaf30q/4VBFRdzRaEGOdfZlt0lcS/777lE2EOh8Cg1hScWpJ8FeGBmkbx8xgzh4zc4DI0ihyWGp0J8mrmDlrWaDMiZyDXd9JL5yuNVCYHr1GQA1rcu/kbZNwZpgCbHcNSKY+Gsk2HCkysZs/Lrbr5uCmJb3yszGm2DDAxNxqMCjAJfiqwuyUTlv1dotxqDudwe4zVvR6ht1dffz8AXUKmPFxuxCpQYuNA/ytHr9GDFaqLniYIdFnxFl4Q6E20u1CPFIjWWdGwhy0fOArpJuT9P+MQq1W4LL2Ui95JvwfmQRaugEitSSIaPWf7oIu/T5MrzyF26BWeMnziSs+4sLVlQYxGV94hsimMaxpuDlJnBXYRCt7CgX2Qs+ta5CAKTf1kMqfubeFJ6j/FoKqpViMyJQm34fMLVXCQ3HYU0fQw6Zkz9vC8bpH/I/pJbW405fezRAi/UxGx0gznJ5wYQXyEp5EjsEZjuOJnR5qZJB5ulwzC8gknWmlu2+2ilIsytGB20Dqw88rxA13v+BsvMrtBymvjCfhJpOFjkNJhCPbuJdoTI1nvYThIRrRjKFHQ2dYYwvPAYkVQ0mV2Flw3tYTUR1f9TW6ruL+5BF25rxL3IfOL5nE8/1NXz/cw8bIKl4ZDof+t6GpBA+5DBiPJ1Rv1Yv2wQ6dP/dEriDiNlCiSjcH3qxQxxvl/muymhhK112mN7huJ8vQvxWcWMdh2/w2pF9zJEbl7JAyhURmI3jVfwYZccppnerbr9vBFu/r8ApWUIZcw+Mcy0jNJSNhRyAYYEX0BFU5RVSpaiV17OO7TuoQRtD5R6o+pKZDX9nosf/w4mUOPgDFHFst2Bq+FA2kNCIHrsi+L23v2fEKnWgJT71cjhlj6hbYtbnbfeF2fwgUpmTljfl1qSAPDOiSvl88pIsWeT7PrBkf1jLvAPjgPFPl5AKMPr6/LiI8YLGei86LTrAQjBYthnGolI8groYgv5ZnBHNEHCOmbTW7CgL83bsLIwQlEUHmq+SSWO9Lh9bhjiD9Ueynyezi9B6BIeeke8aK1XjdncrtDxHn/v0LH7xq9DaiCRgiA2Ybu64N4AFqImo4S1zAn1ZGzc67JSIUm79UrTTHQrfNVOU93WgEazCdqk8Dvd7jebK7qvzWqNPh8c4sCNIreEy8na+hLI/q4jmD7NN+4HLDgz8ImcvL1OEbQvybzm/ISf/B+CDWgiWmfFhzY5i/UUHrsmiI2Y5hB9WWpPORGTfQE7i/YfW9g7GDRYTUojZfoBv1gSrTXfZewDZKEC1juxWRFLnWIapl5y4EL2bYB1tGcGkbEcHqsgtY1PZY6RTf1ZzEaQYvrkkLCslpVbMBNis18dT0iVIpGNE7NN+R7j9W9jEsClAzHbp1xnV4hFiL3IMAYFfRAlXbDGRVlES/psj5cB5HhWJbg6abb/wHzmb3FwWgl5qXklPk2K1DoqnjG81cbUug0kUV6znPDIuQjBkEBIHATbuxE4FUplfpO/jUAFAT7eD+QR4D4osX6iPI5F6O0639mCSlmJAP8gWZ44qhvJm7UYWO5l8lpf7nGlsqLQd79/7jaRaXdHQ97gtrTmpL70DwnDpYO5BpZAe+61w/d9cHX9vzMhoZw+PwxriUKp5TlV3nNkNcVb7Plg9gSw2E34Z1+rbhAzytTa4C1WSWVBvSaiFW7QTUCf8Vp9LR1rWuFacBYKcDkE+yoG5AsMLNx5tgsgYcMgiRJLsEywfcbOVptubQ707uRn940XZEex46ioi9NCTv+2au+4NyVBTiYjOLu1UR1DWFrwhwrZhQ52ZvYzgEHInVJYI2lS0cjqUg8gYh2joR4u/H8g8VXGArCdBdrH+u/WHydk8AcxS1Sid9x2NHdsrP3j3m4o2Nfs4Fy0IbLxK0+swkHyD20LdYuqMs/ZnTvCIfmDPU74NXGZ8tLcBoQuAX76pOx4E/mXH146vOUGL6PDbIid4BtDs+HQByw2R/oAw7a82HKt559ALoJOVDqulI4PCj6eDMO9xABKx2V0+W2GJeqHUMd4T8JcCxZBUN9qkm8mn6oJcJIL7vQ95I3IXmtEZfY5LLzuVyuKf7ZFVvWpsN//fzgHSGsGT2Bo60foMBAohHwAolXXvRiXcKm3Gab0OjaPvmNMZdVD/w+60E4ehlX5KjvQEjcVhOduidxWk3X/Q/U1jix4cS/DYHZZk04ZAvZRHynxAzd5GKGk77ho8jkuUsmcLeYhoesE4TawP2PIcoNlFRpKRICvwIhBjpLsizxPrU9OftlISUoahMyT7vWd9NkiorgBSN1bJOu1nDCo=\r\n------WebKitFormBoundaryZ8LzWb0A7I3wOA70\r\nContent-Disposition: form-data; name="__VIEWSTATEGENERATOR"\r\n\r\nC53698AA\r\n------WebKitFormBoundaryZ8LzWb0A7I3wOA70\r\nContent-Disposition: form-data; name="__VIEWSTATEENCRYPTED"\r\n\r\n\r\n------WebKitFormBoundaryZ8LzWb0A7I3wOA70\r\nContent-Disposition: form-data; name="ctl00$MainContent$txtCari"\r\n\r\n\r\n------WebKitFormBoundaryZ8LzWb0A7I3wOA70\r\nContent-Disposition: form-data; name="ctl00$MainContent$ddUrut"\r\n\r\nfma_tanggal desc\r\n------WebKitFormBoundaryZ8LzWb0A7I3wOA70\r\nContent-Disposition: form-data; name="ctl00$changeOldPassword"\r\n\r\n\r\n------WebKitFormBoundaryZ8LzWb0A7I3wOA70\r\nContent-Disposition: form-data; name="ctl00$changeNewPassword"\r\n\r\n\r\n------WebKitFormBoundaryZ8LzWb0A7I3wOA70\r\nContent-Disposition: form-data; name="ctl00$changeConfirmPassword"\r\n\r\n\r\n------WebKitFormBoundaryZ8LzWb0A7I3wOA70--\r\n'

    response = requests.post('https://satgas-covid19.polytechnic.astra.ac.id/mahasiswa/Page_Absensi.aspx',
                             cookies=cookies, headers=headers, data=data)

    try:
        if (response.status_code == 200):
            soup = BeautifulSoup(response.text, 'html.parser')
            print(soup.findAll('img')[0].text)
            print(Fore.GREEN)
            print("Absen Berhasil")
            qr = soup.findAll(id='imgBarcode')[0]['src']
            print(Style.BRIGHT+"Scan QR Code ini untuk absen")
            dec = base64.b64decode(qr.replace('data:image/png;base64,', ''))

            with open("qr.png", "wb") as fh:
                fh.write(dec)
                fh.close()
            img = Image.open('qr.png')
            img.show()

            print(Style.RESET_ALL)
        else:
            print(Fore.RED+"Absen Gagal")
            print(Style.RESET_ALL)
    except Exception as e:
        print(Fore.BLACK+"Absen Gagal/Erorr")
        print(e)
        print(Style.RESET_ALL)


def logout():
    url = 'https://satgas-covid19.polytechnic.astra.ac.id/mahasiswa/Page_Logout.aspx'
    cookies = {
        '_ga': 'GA1.3.1016601159.1664154820',
        '_gid': 'GA1.3.1235991604.1669596888',
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        # Requests sorts cookies= alphabetically
        # 'Cookie': '_ga=GA1.3.1016601159.1664154820; _gid=GA1.3.1235991604.1669596888; AbsensiPolmanAstra=1B2D5FC43133603966A6B50E9D742A839537713B5077AD3FC30E354514AC5BE1458FCD1DAB963B546C98711B8E7502660893824FFF45C49B68E16EECCB6F3F0B5491A78A649894C29A9336D8D8975694236520F110D2722D08D91E79CF046701C6C60AFB8A23B6F8D4D438285971CFF19A0C0851B2998F0EADA2AC60F3295ABBB818F9C250E7DF66CCC515488622FC1F920866F4CB41753BDC1537BABA31F5687714B8060C37634F36A41D7ACB20BB9FFFAE86235EC730C7618BF425B388381BEAA42521323D478AC0D0FA00C17CBC3B',
        'Referer': 'https://satgas-covid19.polytechnic.astra.ac.id/mahasiswa/',
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

    response = requests.get(url, cookies=cookies, headers=headers)


print(Style.RESET_ALL)
# username = input("NIM      : ")
# password = input("Password : ")
# session = login(username, password)
#session = absen()
download()
