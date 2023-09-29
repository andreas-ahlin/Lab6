
import timeit


class Song:

    def __init__(self, data):
        self.trackId = data[0]
        self.låtId = data[1]
        self.artist = data[2]
        self.låtNamn = data[3]


def readfile(filename):
    songlist = []
    with open(filename, 'r', encoding='utf-8') as songfile:
        for line in songfile:
            data = line.split('<SEP>')
            song = Song(data)
            songlist.append(song)
    songlist = songlist[0:1000]
    return songlist


# def quicksort(lista):  #ChatGPT
#     if len(lista) <= 1:
#         return lista

#     pivot = lista[len(lista) // 2].låtNamn
#     mindre = [x for x in lista if x.låtNamn < pivot]
#     lika = [x for x in lista if x.låtNamn == pivot]
#     större = [x for x in lista if x.låtNamn > pivot]

#     return quicksort(mindre) + lika + quicksort(större)

def quicksort(data):  # Tagit från föreläsning 8
    sista = len(data) - 1
    qsort(data, 0, sista)


def qsort(data, low, high):  # Tagit från föreläsning 8
    pivotindex = (low+high)//2
    # flytta pivot till kanten
    data[pivotindex], data[high] = data[high], data[pivotindex]

    # damerna först med avseende på pivotdata
    pivotmid = partitionera(data, low-1, high, data[high].låtNamn)

    # flytta tillbaka pivot
    data[pivotmid], data[high] = data[high], data[pivotmid]

    if pivotmid-low > 1:
        qsort(data, low, pivotmid-1)
    if high-pivotmid > 1:
        qsort(data, pivotmid+1, high)


def partitionera(data, v, h, pivot):  # Tagit från föreläsning 8
    while True:
        v = v + 1
        while data[v].låtNamn < pivot:
            v = v + 1
        h = h - 1
        while h != 0 and data[h].låtNamn > pivot:
            h = h - 1
        data[v], data[h] = data[h], data[v]
        if v >= h:
            break
    data[v], data[h] = data[h], data[v]
    return v


def bubbelsortera(data):
    n = len(data)
    bytt = True
    while bytt:
        bytt = False
        for i in range(n-1):
            if data[i].låtNamn > data[i+1].låtNamn:
                data[i], data[i+1] = data[i+1], data[i]
                bytt = True


def main():

    filename = "unique_tracks.txt"

    lista = readfile(filename)

    bubbleSortTime = timeit.timeit(
        stmt=lambda: bubbelsortera(lista), number=1)
    print("BubbleSort tog", round(bubbleSortTime, 4), "sekunder")

    filename = "unique_tracks.txt"

    lista = readfile(filename)
    quickSortTime = timeit.timeit(stmt=lambda: quicksort(lista), number=1)
    print("Quicksort tog", round(quickSortTime, 4), "sekunder")


main()


# ______ quicksort O(n*log(n))     Bubble O(n^2)
# n=1000  0.002 sek                 0.1669 sek
# n=10000 0.026 sek                 17.6556
# n=100000 0.3769 sek
# n=100000 5.4792 sek


# Resultaten blev inte som förväntade och beror förmodligen på hur listan är sorterad
#  från början. Hur implementationen ser ut för quicksort då detta är en mer komplex sortering.
