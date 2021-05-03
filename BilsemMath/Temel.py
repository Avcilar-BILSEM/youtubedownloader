import random

class Temel:

    def __init__(self):
        print("Temel Sınıfı Yüklendi")

    def __del__(self):
        print("Beni yıktın!")

    def topla(self,*args):
        if isinstance(args[0],list):
            return sum(args[0])
        elif isinstance(args[0],(int,float)):
            return sum(args)

    def rasgeleListe(self,elemansayisi,basla=0,bit=100):
        liste=[]
        for i in range(0,elemansayisi):
            liste.append(random.randrange(basla,bit))
        return liste