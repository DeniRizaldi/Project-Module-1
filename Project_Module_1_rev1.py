# Bismillah
# Gudang - Data Stock

####### Stock Initialization

Menu = ['1. Report Data Stok Spare Part',
        '2. Menambahkan Data Stok Spare Part',
        '3. Mengubah Data Stok Spare Part',
        '4. Menghapus Data Stok Spare Part',
        '5. Keluar']

stok = [{'Kode' : 'ORP12', 'Nama' : 'O-Ring', 'Spesifikasi' : '12 mm', 
             'Quantity' : 3, 'Lokasi' : 'R02'},
        {'Kode' : 'NWP21', 'Nama' : 'Clamp', 'Spesifikasi' : '21 Pa', 
             'Quantity' : 2, 'Lokasi' : 'L04'},
        {'Kode' : 'WL430', 'Nama' : 'Spring', 'Spesifikasi' : '1 N', 
             'Quantity' : 5, 'Lokasi' : 'R03'}]

    
def Main_Menu () :
    MainMenu = True
    while MainMenu != '5' :
        print ('\n======= Data Record Stok Spare Part =======\n')
        for i in Menu :
            print (i)
        MainMenu = input('Silakan pilih Main_Menu [1-5] : ')
        if MainMenu == '1' :
            Report_Menu()
        elif MainMenu == '2' :
            Create_Menu()
        elif MainMenu == '3' :
            Update_Menu()
        elif MainMenu == '4' :
            Delete_Menu()    
        elif MainMenu == '5':
            print ('\nTerima kasih dan sampai jumpa!!!')
            break #untuk menghentikan pengkondisian
        #else :
        #    print ("\n======= Pilihan yang anda masukkan salah =======\n")
            
              
def Report_Menu () :
    ReportMenu = True
    while ReportMenu != '3' :   
        print ('\n+++++++ Report Data Stok Spare Part +++++++')
        print ('1. Report seluruh Stok Spare Part')
        print ('2. Report Stok Spare Part tertentu')
        print ('3. Kembali ke Menu Utama') 
        ReportMenu = input('Silakan pilih Sub Menu Report Data [1-3] : ')
    
        if ReportMenu == '1':
            if len(stok) !=0 :
                print ('\nDaftar Stok Spare Part :')
                for j, i in enumerate (stok):
                    print (f"{j+1}. Kode : {i['Kode']}, Nama : {i['Nama']}, Spesifikasi : {i['Spesifikasi']}, Quantity : {i['Quantity']}, Lokasi : {i['Lokasi']} ")
        
            else :
                print ('\n******* Stok Spare Part tidak ada *******')
            
            continue

        elif ReportMenu == '2' :
            if len(stok) !=0 :
                std = input('Masukkan Kode Spare Part : ').upper()
                print (f"Data Spare Part dengan Kode : {std}")
                for j, i in enumerate(stok):
                    if i ['Kode'] == std :
                        print (f"{j+1}. Kode : {i['Kode']}, Nama : {i['Nama']}, Spesifikasi : {i['Spesifikasi']}, Quantity : {i['Quantity']}, Lokasi : {i['Lokasi']} ") 
                        break
                else :
                    print ('\n******* Spare Part tidak Terdaftar *******')
            else :
                print ('\n******* Tidak ada Spare Part *******')
        elif ReportMenu == '3':
            break
        else :
            print ('\n******* Pilihan Menu tidak ada *******')


def Create_Menu () :
    while True :
        print ('\n+++++++ Menambah Data Stok Spare Part +++++++')
        print ('1. Tambah Data Stok Spare Part')
        print ('2. Kembali ke Menu Utama') 
        CreateMenu = input('Silakan pilih Sub Menu Create Data [1-2] : ')     

        if CreateMenu == '1':
            if len(stok) !=0 :
                addKode = input('Masukkan Kode Spare Part : ').upper()
                for j, i in enumerate (stok):
                    if addKode == i['Kode'] :
                        print ('Spare Part sudah ada')
                        break

                else : 
                    addNama = input('Masukkan Nama Spare Part : ').upper()
                    addSpek = input('Masukkan Spesifikasi Spare Part : ').upper()
                    addQty = input('Masukkan Quantity Spare Part : ').upper()
                    addLoc = input('Masukkan Lokasi Spare Part : ').upper()
                    
                    tambahan = {
                        'Kode' : '{}'.format(addKode),
                        'Nama' : '{}'.format(addNama),
                        'Spesifikasi' : '{}'.format(addSpek),
                        'Quantity' : '{}'.format(addQty),
                        'Lokasi' : '{}'.format(addLoc),
                    }
                    print('\nSpare Part yang ditambahkan adalah : ',tambahan)
                    checkerCreate = input('\nApakah sudah benar? (Y/N) : ').upper()
                    if checkerCreate == 'Y':
                        stok.append(tambahan)
                        print('\n--- Spare Part berhasil ditambahkan ---')
                    elif checkerCreate == 'N':
                        print('\n--- Spare Part tidak ditambahkan ---')
                    else:
                        break                
                    

        elif CreateMenu == '2':
            break        
        
        else :
            print ('\n******* Pilihan Menu tidak ada *******')

def Update_Menu () :
    UpdateMenu = True
    while UpdateMenu != '2' :   
        print ('\n+++++++ Mengubah Data Stok Spare Part +++++++')
        print ('1. Ubah Data Stok Spare Part')
        print ('2. Kembali ke Menu Utama') 
        UpdateMenu = input('Silakan pilih Sub Menu Update Data [1-2] : ')     
        
        if UpdateMenu == '1':
           if len(stok) !=0 :
                updtKode = input('Masukkan Kode Spare Part : ').upper()

                for i in range(len(stok)):
                    if updtKode == stok[i]['Kode'] :
                        print ('Spare Part yang ingin diubah adalah : ', stok[i])
                        nameupdt = input('\nMasukkan kolom yang ingin diubah  : ').lower()

                        if nameupdt == 'kode' :
                            ubahKode = input('\nUpdate Kode : ').upper()
                            confKode = input('\nApakah Data akan diubah? [Y/N] : ').lower()
                            if confKode == 'y' :
                                stok[i]['Kode'] = ubahKode
                                print('\nData berhasil diubah')
                                break
                            elif confKode == 'n' :
                                print('\nData tidak diubah')    

                        if nameupdt == 'nama' :
                            ubahNama = input('\nUpdate Nama : ').upper()
                            confNama = input('\nApakah Data akan diubah? [Y/N] : ').lower()
                            if confNama == 'y' :
                                stok[i]['Nama'] = ubahNama
                                print('\nData berhasil diubah')
                                break
                            elif confNama == 'n' :
                                print('\nData tidak diubah')

                        if nameupdt == 'spesifikasi' :
                            ubahSpek = input('\nUpdate Spesifikasi : ').upper()
                            confSpek = input('\nApakah Data akan diubah? [Y/N] : ').lower()
                            if confSpek == 'y' :
                                stok[i]['Spesifikasi'] = ubahSpek
                                print('\nData berhasil diubah')
                                break
                            elif confSpek == 'n' :
                                print('\nData tidak diubah')  

                        if nameupdt == 'quantity' :
                            ubahQty = input('\nUpdate Quantity : ').upper()
                            confQty = input('\nApakah Data akan diubah? [Y/N] : ').lower()
                            if confQty == 'y' :
                                stok[i]['Quantity'] = ubahQty
                                print('\nData berhasil diubah')
                                break
                            elif confQty == 'n' :
                                print('\nData tidak diubah') 

                        if nameupdt == 'lokasi' :
                            ubahLoc = input('\nUpdate Lokasi : ').upper()
                            confLoc = input('\nApakah Data akan diubah? [Y/N] : ').lower()
                            if confLoc == 'y' :
                                stok[i]['Lokasi'] = ubahLoc
                                print('\nData berhasil diubah')
                                break
                            elif confLoc == 'n' :
                                print('\nData tidak diubah')

                    else :
                        print ('Data tidak ada!!!')   
                        break      
                else :
                    print ('\n******* Pilihan Menu tidak ada *******')             
                        

def Delete_Menu () :
    DeleteMenu = True
    while DeleteMenu != '2' :   
        print ('\n+++++++ Delete Data Stok Spare Part +++++++')
        print ('1. Hapus Stok Spare Part')
        print ('2. Kembali ke Menu Utama') 
        DeleteMenu = input('Silakan pilih Sub Menu Report Data [1-3] : ')
        
        if DeleteMenu == '1':
            if len(stok) !=0 :
                delCode = input('\nMasukkan Kode Spare Part yang ingin dihapus : ').upper()
                for i in range (len(stok)):
                    if delCode == stok[i]['Kode']:
                        print('\nSpare Part yang ingin dihapus adalah : ', stok[i])
                        confDel = input('\nApakah yakin ingin menghapus data ini? (Y/N) : ').lower()
                        if confDel == 'y' :
                            del stok[i]
                            print('\nSpare Part berhasil dihapus')
                            break
                        elif confDel == 'n':
                            print('\nSpare Part tidak terhapus')
                            break
                        else :
                            print('\nMenu yang anda masukkan salah')
                            break
                else :
                    print ('\nSpare Part tidak ditemukan')
                    break
            else :
                print ('\nSpare Part sudah tidak ada stok')
        elif DeleteMenu == '2':
            break        
        else :
            print ('\n******* Pilihan Menu tidak ada *******')

Main_Menu()
