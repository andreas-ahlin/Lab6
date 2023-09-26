def binary_search(data, key):
    low = 0
    high = len(data)-1

    while low <= high:
        middle = (low + high)//2
        if data[middle] == key:
            return data[middle]
        else:
            if key < data[middle]:
                high = middle - 1
            else:
                low = middle + 1
    return None


def main():
    # Läs in listan
    indata = input().strip()
    the_list = indata.split()
    # Läs in nycklar att söka efter
    key = input().strip()
    while key != "#":
        print(binary_search(the_list, key))
        key = input().strip()


main()
