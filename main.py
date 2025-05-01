from bs4 import BeautifulSoup
import requests
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

url="https://appbrewery.github.io/instant_pot/"
live_url="https://www.amazon.in/Noise-Advanced-Bluetooth-Brightness-Smartwatch/dp/B0B6BPTFT5/ref=sr_1_5?crid=R86GT915GW0B&dib=eyJ2IjoiMSJ9.KmUauYdmypFShxRqnjAbeVtlAYPXddaykIz3OWBWOIBoLgw5UMy7J3tSHqA8xOXflbQB1laDPcnw0qm5siO83-OdV_He3C39B0DC7uRYKC6XnUBcFTCh9zaVpz3LZUFVENWaRy17dYT2XScKZ9jqAZMoHvWCF2kCS65pKwum7ff6W_7vmUrx7DAFFHRmQzynONO36e98uoX0XnF8g5eGa4Vufj5IvyFaKP4JwQ5XGf0.dc0wRI1Vkj2uapXhvwvv_CsIqrbfkilV7IhJqBoGS_8&dib_tag=se&keywords=digital%2Bwatch%2Bfemale&qid=1746068117&sprefix=digital%2Bwatch%2Bfemale%2Caps%2C235&sr=8-5&th=1"


headers={
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
        "Priority": "u=0, i",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
}

response=requests.get(url=live_url,headers=headers)

soup=BeautifulSoup(response.content,"html.parser")
price=soup.find(class_="a-price-whole").get_text()

final_price=int(price.split(".")[0])



title=soup.find(id="productTitle").get_text().strip()

BUY_PRICE=850

if final_price<BUY_PRICE:
    message=f"{title} is on sale for {price}!"

    MY_EMAIL=os.getenv("my_email")
    PASSWORD=os.getenv("password")


    with smtplib.SMTP("smtp.gmail.com",587) as connection:
            connection.starttls()
            result=connection.login(user=MY_EMAIL,password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,to_addrs=MY_EMAIL, msg=f"Subject:Amazon Price Alert!\n\n {message}\n{url}".encode("utf-8"))

else:
    print("No price drop yet!")