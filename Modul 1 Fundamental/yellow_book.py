
kontak=[
    {'nama':'Polisi','nomor':'110','kota':'Indonesia'},
    {'nama':'Ambulans','nomor':'118','kota':'Indonesia'}
]


def tampilan ():
    global kontak
    if len(kontak)==0:
        print('\n\tTIDAK ADA DATA')
    elif len(kontak)>0:
        print('\nindex\t|Nama\t|Nomor Kontak\t|Kota\t|'.expandtabs(16))
        for i in range(len(kontak)):
            print (f'{i}\t|{kontak[i]["nama"]}\t|{kontak[i]["nomor"]}\t|{kontak[i]["kota"]}\t|'.expandtabs(16))
            

def read_data():
    global kontak
    while True:
        print('\n1. Tampilkan daftar kontak\n2. Cari kontak\n3. Kembali ke menu')
        arah_read=int(input('Anda ingin menampilkan: '))
        if arah_read==1:
            tampilan()
        elif arah_read==2:
            global kontak
            count=0
            identify=(input('Masukkan nama atau nomor telepon yang ingin ditampilkan: ').capitalize())
            for i in range(len(kontak)):
                if identify in kontak[i]['nama'] or identify in kontak[i]['nomor']:
                    print(f'\nIndex\t|Nama\t|Nomor telepon\t|Kota\t|\n{i}\t|{kontak[i]["nama"]}\t|{kontak[i]["nomor"]}\t|{kontak[i]["kota"]}\t|'.expandtabs(15))
                elif identify not in kontak[i]['nama']or identify not in kontak[i]['nomor']:
                    count+=1
                    if count==len(kontak):
                        print('\nNomor belum tersimpan')             
        elif arah_read==3:
            break
        elif arah_read>3:
            print('Pilihan yang Anda masukkan salah')
            
def tambah_kontak ():
    global kontak
    while True:
        print('\n\t+--- MENU ---+\n1. Tambah Kontak\n2. Kembali ke menu utama'.expandtabs(4))
       
        arah_tambah= int(input('Anda ingin menampilkan: '))
        if arah_tambah==1:
            while True:
                no=(input('\nMasukkan nomor kontak: '))
                count=0
                for i in range(len(kontak)):
                    if str(no) in str(kontak[i]['nomor']):
                        print('xxxxxx NOMOR SUDAH ADA xxxxxx')
                        break
                    elif str(no) not in str(kontak[i]['nomor']):
                        count+=1
                        if count==len(kontak):
                            nama=input('Masukkan nama kontak: ').capitalize()
                            kota=input('Masukkan kota domisili kontak: ')
                            simpan=input('Apakah anda ingin menyimpan nomor ini?\n(Y/N)').upper()
                            if simpan=='Y':
                                kontak.append({'nama':nama,'nomor':no,'kota':kota})
                                print('Nomor tersimpan')
                                tampilan()
                                break
                            elif simpan=='N':
                                break
                break
        elif arah_tambah==2:
            hold=(input('Anda ingin kembali ke menu utama? \n(Y/N) ').upper())
            if hold=='Y':
                break
            elif hold=='N':
                continue
        elif arah_tambah>2:
            print('Pilihan yang Anda masukkan salah')

def update_kontak():
    global kontak
    while True:
        count=0
        print('\t+-- MENU --+\n1. Edit Data\n2. Kembali ke menu utama ')
        arah_update=int(input('Anda ingin menampilkan: '))
        if arah_update== 1:
            tampilan()
            data_ubah=(input('Masukkan nama atau nomor kontak yang ingin diubah: ').capitalize())
            for i in range(len(kontak)):
                if data_ubah in str(kontak[i]['nama'])or data_ubah in str(kontak[i]['nomor']):
                    print(f'\nNama\t|Nomor\t|Kota\t|\n{kontak[i]["nama"]}\t|{kontak[i]["nomor"]}\t|{kontak[i]["kota"]}')
                    hold=input('Apakah anda ingin mengubah data nomor ini? \n (Y/N) ').upper()
                    if hold == 'Y':
                        input_kolom=input('Masukkan kolom yang ingin diubah: ').lower()
                        if input_kolom == 'nama':
                            ubah_nama=input('Masukkan data yang baru: ')
                            kontak[i]['nama']=ubah_nama
                            print('\nDATA SUDAH TERUPDATE')
                        elif input_kolom=='nomor':
                            ubah_nomor=input('Masukkan data yang baru: ')
                            kontak[i]['nomor']=ubah_nomor
                            print('\nDATA SUDAH TERUPDATE')
                        elif input_kolom=='kota':
                            ubah_kota=input('Masukkan data yang baru: ')
                            kontak[i]['kota']=ubah_kota
                            print('\nDATA SUDAH TERUPDATE')
                    elif hold == 'N':
                        break
                    
                elif data_ubah not in str(kontak[i]['nama'] or data_ubah in str(kontak[i]['nomor'])):
                    count+=1
                    if count==len(kontak):
                        print('\nDATA YANG ANDA CARI TIDAK ADA')
                       
           
        elif arah_update==2:
            hold=(input('Anda ingin kembali ke menu utama? \n(Y/N) ').upper())
            if hold=='Y':
                break
            elif hold=='N':
                continue
        elif arah_update>2:
            print('Pilihan yang Anda masukkan salah')
    
def hapus_data():
    global kontak
    count=0
    while True:
        print('\t+-- MENU --+\n1. Hapus data\n2. Kembali ke menu utama')
        arah_hapus=int(input('Anda ingin: '))
        if arah_hapus==1:
            tampilan()
            nomor_hapus=input('Masukkan nomor yang ingin dihapus: ')
            for i in range(len(kontak)):
                if nomor_hapus in str(kontak[i]['nomor']):
                    konfirmasi=input('Anda ingin menghapus data nomor ini?\n(Y/N): ').upper()
                    if konfirmasi=='Y':
                        del kontak[i]
                        print('Data sudah terhapus')
                        break
                    elif konfirmasi=='N':
                        break
                elif str(nomor_hapus) not in str(kontak[i]['nomor']):
                    count+=1
                    if count==len(kontak):
                        print('Data yang anda cari tidak ada')
        elif arah_hapus==2:
            hold=(input('Anda ingin kembali ke menu utama? \n(Y/N) ').upper())
            if hold=='Y':
                break
            elif hold=='N':
                continue
        elif arah_hapus>2:
            print('Pilihan yang Anda masukkan salah')
        
    

    
        
    


while True:
    print('\n\t+---MENU UTAMA---+\n1. Tampilkan daftar kontak\n2. Tambahkan kontak baru\n3. Ubah data kontak\n4. Hapus kontak\n5. Keluar'.expandtabs(3))
    direction=int(input('Anda ingin menuju ke: '))
    if direction == 1:
        read_data()
    elif direction ==2:
        tambah_kontak()
    elif direction==3:
        update_kontak()
    elif direction==4:
        hapus_data()
    elif direction==5:
        hold=(input('Anda ingin keluar dari program? \n(Y/N) ').upper())
        if hold=='Y':
            break
        elif hold=='N':
            continue
    elif direction>5:
        print('\n-- PILIHAN YANG ANDA MASUKKAN SALAH! --')
