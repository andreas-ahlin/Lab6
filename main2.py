
import timeit


class Song:

    def __init__(self, data):
        self.trackId = data[0]
        self.låtId = data[1]
        self.artist = data[2]
        self.låtNamn = data[3]

    def __lt__(self, other):
        self.artistNamn < self.other


def readfile(filename):
    songlist = []
    with open(filename, 'r', encoding='utf-8') as songfile:
        for line in songfile:
            data = line.split('<SEP>')
            song = Song(data)
            songlist.append(song)
    songlist = songlist[0:1000000]
    return songlist


def binary_search(data, key):  # Taget från föreläsning 3 O(log(n))
    low = 0
    high = len(data)-1

    while low <= high:
        middle = (low + high)//2
        if data[middle].låtNamn == key:
            return True
        else:
            if key < data[middle].låtNamn:
                high = middle - 1
            else:
                low = middle + 1
    return False


def linsok(songList, key):  # Taget från föreläsning 3 O(n)
    for song in songList:
        if song.låtNamn == key:
            return True
    return False


def createDict(lista):
    hashtabell = dict()
    for song in lista:
        hashtabell[song.låtNamn] = None
        # Sökning i hashtabellen
    return hashtabell


def main():

    filename = "unique_tracks.txt"

    lista = readfile(filename)

    n = len(lista)
    print("Antal element =", n)
    lista = sorted(lista, key=lambda x: x.låtNamn)

    sista = lista[n//64]
    testnamn = sista.låtNamn
    print(testnamn)
    linjtid = timeit.timeit(stmt=lambda: linsok(
        lista, testnamn), number=1000)
    print("Linjärsökningen tog", round(linjtid, 4), "sekunder")

    bintid = timeit.timeit(stmt=lambda: binary_search(
        lista, testnamn), number=1000)
    print("Binärsökningen tog", round(bintid, 4), "sekunder")

    songDict = createDict(lista)
    dicttid = timeit.timeit(
        stmt=lambda: songDict.get(testnamn, None), number=1000)
    print("Hashtabellsökning tog ", round(dicttid, 4), "sekunder")


main()

# ___________Linjsok     #Binsok     #hashtabell
# n=250000  0.2824 sek   0.0042 sek  0.0001 sek
# n=500000  0.5583 sek   0.0041 sek  0.0001 sek
# n=1000000 1.9664 sek   0.0045 sek  0.0001 sek
