import requests
from bs4 import BeautifulSoup as bs
import urllib.request

def about():
    print("""

    Welcome to CSEKod
    In this blog I am posting tutorials and articles about latest Technical Skills collected from various social networks and blogs

    visit www.csekod.tech for more.


    In this app you can download any video from instragram by entering sharable link
    """)

def download():
    r2=input("Enter the link : ") #"https://www.instagram.com/p/CGc1qc3sCaE/?igshid=yrtf29h7a1fu"
    print("Start Downloading ...")
    r=requests.get(r2)
    soup=bs(r.content,"html.parser")

    url = soup.find("meta",  property="og:video:secure_url")

    v = input("Enter Video Name : ")+".mp4"

    urllib.request.urlretrieve(url["content"], v) 

n=int(input( """
1. Download
2. About 
Enter Your Choise : """))
if (n==1):
    download()
    print("Video Downloaded")
elif (n==2):
    about()
