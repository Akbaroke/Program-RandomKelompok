import random

print('### Program Random Kelompok By Akbaroke >> https://github.com/Akbaroke/ ###\n')

O = 0
while O < 1:
    nama = open('Nama.txt', 'r')
    list_nama = []
    for i in nama:
        i = i.replace('\n', '')
        list_nama.append(i)

    random.shuffle(list_nama)

    fileA = []
    a = -1
    while a < 9:
        a += 1
        fileA.append(list_nama[a])

    fileB = []
    while a < 19:
        a += 1
        fileB.append(list_nama[a])

    fileC = []
    while a < 29:
        a += 1
        fileC.append(list_nama[a])

    fileD = []
    while a < 39:
        a += 1
        fileD.append(list_nama[a])

    fileE = []
    while a < 49:
        a += 1
        fileE.append(list_nama[a])

    fileF = []
    while a < 59:
        a += 1
        fileF.append(list_nama[a])


    # PEMBUATAN TABEL
    print('============================================================================================================================')
    print('|                                                 HASIL RANDOM NAMA KELOMPOK                                               |')
    print('============================================================================================================================')
    print('|              KELOMPOK A                |              KELOMPOK A                |              KELOMPOK A                |')
    for x in range(len(fileA)):
        isi = str(fileA[x])
        print('|   '+isi,end='')
        for y in range(40-3-len(isi)):
            print(' ',end='')
        isi1 = str(fileB[x])
        print('|   '+isi1,end='')
        for y in range(40-3-len(isi1)):
            print(' ',end='')
        isi2 = str(fileC[x])
        print('|   '+isi2,end='')
        for y in range(40-3-len(isi2)):
            print(' ',end='')
        print('|')
    print('============================================================================================================================')
    print('|              KELOMPOK D                |              KELOMPOK E                |              KELOMPOK F                |')
    for x in range(len(fileD)):
        isi = str(fileD[x])
        print('|   '+isi,end='')
        for y in range(40-3-len(isi)):
            print(' ',end='')
        isi1 = str(fileE[x])
        print('|   '+isi1,end='')
        for y in range(40-3-len(isi1)):
            print(' ',end='')
        isi2 = str(fileF[x])
        print('|   '+isi2,end='')
        for y in range(40-3-len(isi2)):
            print(' ',end='')
        print('|')
    print('============================================================================================================================')

    Q = input('RANDOM ULANG <y/n> ? ')
    if Q == 'y':
        O = 0
    else :
        O += 3

print('\n\tPROGRAM RANDOM SELESAI SILAHKAN CEK HASILNYA THANKYOU :)')