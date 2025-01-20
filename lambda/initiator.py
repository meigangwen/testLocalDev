from bs4 import BeautifulSoup

def handle(event, context):
    soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
    print(soup.text)
    print("Hello world!")