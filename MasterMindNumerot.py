import random

def main():
    print("Tervetuloa pelaamaan Master mindin numeroversiota!")
    print("Arvausmahdollisuuksia on 10. Tulos arvauksesta ilmoitetaan")
    print("muodossa oikeat numerot oikeilla paikoilla/väärillä paikoilla.")
    print("Rivissä on neljä numeroa. Käytä numeroita 1-6.")
    rivi = satunnaisrivi()
    #print("Ohjelma arpoi rivin", rivi)
    arvaus = 1
    oikein = False

    while arvaus < 11 and oikein == False: #korkeintaan 10 arvauskertaa
        arvausrivi = kysy_arvaus(arvaus)
        if arvausrivi == rivi: #kokonaan oikein
            oikein = True
        else: #oikeat värit oikeilla ja väärillä paikoilla
            oikea_paikka, vaara_paikka = tarkasta_numerot(rivi,arvausrivi)
            print(oikea_paikka,"/",vaara_paikka)
        arvaus += 1
    if oikein == True:
        print("Onnittelut! Arvasit rivin.")
    else:
        print("Oikea rivi on",rivi)

def satunnaisrivi():
    r = ""
    for x in range(1,5):
        luku = random.randrange(1,6)
        r += str(luku)
    return r

def kysy_arvaus(a):
    oikea = False
    while oikea==False: #kunnes saadaan neljän merkin rivi, arvot 1-6
        kysymys = "Arvaus numero "+str(a)+": "
        ar = input(kysymys)
        if len(ar)!=4:
            print("Syötä neljä merkkiä")
        elif oikeat_merkit(ar) == False:
            print("Merkkien pitää olla välillä 1-6")
        else:
            oikea = True
    return ar

def oikeat_merkit(syote):
    om = True
    for x in range(0,4):
        if (syote[x])not in ['1','2','3','4','5','6']:
            om = False
    return om
                
def tarkasta_numerot(r,ar):
    r = list(r)
    ar = list(ar)
    op = 0
    vp = 0
    for x in range(0,4): #oikea numero oikealla paikalla
        if ar[x]==r[x]:
            op += 1
            ar[x]=str(7) #sijainnista vertaaminen ei enää onnistu
            r[x]=str(0) #tästä ei voi enää löytää samalla numerolla
    if op < 3: #jos oikeilla paikoilla 3, neljännen täytyy olla väärä kirjain
        for x in range(0,4): #oikea numero väärälla paikalla
            for y in range(0,4):
                if ar[x]==r[y] and x!=y:
                    vp += 1
                    ar[x]=str(7) #sijainnista vertaaminen ei enää onnistu
                    r[y]=str(0) #tästä ei voi enää löytää samalla numerolla
    return op,vp

main()
