import pycurl
from io import BytesIO
import certifi
import feedparser
import requests
import shutil
from .Haber import Haber

class Crawler:

    def __init__(self):
        pass

    def gez(self,url):
        self.b_obj = BytesIO()
        self.crl = pycurl.Curl()
        # Set URL value
        self.crl.setopt(self.crl.URL, url)
        self.crl.setopt(self.crl.CAINFO, certifi.where())
        # Write bytes that are utf-8 encoded
        self.crl.setopt(self.crl.WRITEDATA, self.b_obj)

        # Perform a file transfer
        self.crl.perform()

        # End curl session
        self.crl.close()

        # Get the content stored in the BytesIO object (in byte characters)
        self.get_body = self.b_obj.getvalue()
        self.get_body.decode('utf8')


    def parse(self,text=""):
        if text=="":text=self.get_body
        self.feed = feedparser.parse(text)
        return self.feed

    def indir(self):
        self.haberler=[]
        for item in self.feed.entries:
            haberbaglanti=item.img640x360.split("/")
            haberid=haberbaglanti[-2]
            resim=haberbaglanti[-1]
            haber=Haber(haberid,item.link,item.title,item.description,item.img640x360,"resimler/"+resim)
            self.haberler.append(haber)

            r = requests.get(item.img640x360, stream=True)
            with open("resimler/"+resim, 'wb') as f:
                shutil.copyfileobj(r.raw, f)