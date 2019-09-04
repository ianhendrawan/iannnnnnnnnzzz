#Yuk Main Game Buatan ku !
print("                                  \"Game Buatan Anak Bangsa\"")
print("                                       By Ian Hendrawan    ")
print("\nHalo, terimakasih karena sudah tertarik untuk bermain. Maka itu, langsung saja kita mulai yuk permainannya !")
nama_karakter = input ("Siapa nama anda : ")
umur_karakter = input ("Umur anda adalah : ")
rekening_karakter = input ("Nomor rekening anda adalah : ")
print("Terimakasih banyak sekali lagi untuk " + nama_karakter + ", karena sudah tertarik untuk mau bermain.")
print("Yuk, langsung jawab semua pertanyaan dibawah ini hingga habis !")
rumus = str("\"Jika terdapat sebuah perintah seperti NAKAMA = 'Girrafe Academy'\"")
soal_pertama = input ("1 + 1 = A) 2 B) 11 c) 3 : ")
if soal_pertama == "A":
    print("                             /|")
    print("                            / |")
    print("                           /  |")
    print("                          /   |")
    print("                         /    |")
    print("                        /     |")
    print("                       /      |")
    print("                      /       |")
    print("                     /        |")
    print("                    /_ _ _ _ _|")
    print("                              |")
    print("                  _ _ _ _ _ _ |_ _ _ _ _ _")
    print("                 /                       /")
    print("                /_ _ _ _ _ _ _ _ _ _ _ _/")
    soal_pertama_satu = input ("Bagus ! Anda sudah menjawab dengan benar ! Sekarang, menurut anda, gambar apakah yang ada di atas : A) Kapal B) Sesuatu Yang Abstrak : ")
    if soal_pertama_satu == "A":
        print("Anda sangat benar ! Tapi otak anda terlalu rasional. Jadi anda kalah. Coba lagi lain kali.")
    if soal_pertama_satu == "B":
        print("Anda benar !")
        dadu = input ("Sekarang silahkan ketikkan salah satu huruf dari 1, 2, 3, 4, 5 dan 6 : ")
        if dadu == "1":
              print("Angka 1 menunjukkan anda terlalu ambisius. Sehingga lebih baik anda dinyatakan kalah dan coba lagi lain kali.")
        if dadu == "2":
              print("Angka 2 menunjukkan anda ingin hidup normal dan tidak ingin menjadi yang pertama. Sehingga anda dinyatakan masih kalah dan coba lagi lain kali.")
        if dadu == "3":
              print("Angka 3 menunjukkan anda itu hidupnya pengennya yang biasa-biasa saja. Sehingga anda kalah.")
        if dadu == "4":
              print("Angka 4 tidak menunjukkan apa-apa. Anda kalah.")
        if dadu == "5":
              print("Angka 5 hampir benar ! Tapi anda maasih salah !")
        if dadu == "6":
              print("Anda kalah.")
if soal_pertama == "B":
    print(rumus + ", maka apakah rumus yang paling tepat untuk mengganti kata Girrafe ?")
    rumus_satu = input("1) print(nakama.replace(\"Girrafe\", \"Jerapah\") atau 2) Nakama = \"Jerapah Academy \" : ")
    if rumus_satu == "1":
        print("Anda benar ! Tapi masalah masih belum selesai sampai disini.")
        print("Soal berikut yang harus anda pecahkan adalah seperti ini...")
        print("\"Suatu ketika, ada seorang pemuda yang saudari perempuannya meninggal. Dan pada saat sedang berada di pemakaman, si pemuda ini melihat penampakan gadis cantik yang melambaikan tangannya dari arah kejauhan. Dan saat si pemuda ini berusaha untuk mendekati gadis tersebut, tiba-tiba gadis tersebut menghilang. Beberapa hari kemudian, di tempat yang sama, pemuda itu kembali di tempat pemakaman dan berhasil kembali melihat penampakan gadis tersebut.\"")
        kuburan = input ("Bagaimana caranya si pemuda itu bisa kembali melihat penampakan gadis tersebut ? -> 1) Dia membunuh anggota keluarganya atau 2) Dia bunuh diri : ")
        if kuburan == "1":
            print("Anda psikopat. Anda kalah. Coba lagi lain kali.")
        if kuburan == "2":
            print("Anda depresi ya ? Daripada ngejawab pertanyaan, mending ke psikolog gih buat konsultasi.")
    if rumus_satu == "2":
        print("Hmm jawaban anda tidak salah. Oleh karena itu, jawaban anda masih masuk akal.")
        print("Baiklah, mari kita langsung masuk ke soal berikutnya.")
        print("                                    --------------------------------------------")
        print("                                    | 1. Pajak Buruh      |  4 ( dalam persen) | ")
        print("                                    | 2. Pajak Pengusaha  |  8 ( dalam persen) | ")
        print("                                    | 3. Pajak Investor   |  0 (dalam persen)  | ")
        print("                                    | 4. Pajak Pemerintah |  1 (dalam persen)  | ")
        print("                                    |_ _ _ _ _ _ _ _ _ _ _|_ _ _ _ _ _ _ _ _ _ | ")
        jawab_soal = input ("Menurut mu, mengapa investor tidak perlu membayar pajak : ")
        print ("Wah " + nama_karakter + ",jawaban mu ngaco. Coba lagi dari awal ya sampai benar.")
if soal_pertama == "C":
    print("Dalam bisnis, 1+1 memang tidak selalu sama dengan dua. \nMaka itu memang sewarjarnya saja jika ada yang memilih jawaban ini.")
    print("Tapi, ayuk kita langsung masuk ke soal")
    bisnis = input("\nJika kamu memiliki sebuah bisnis, maka menurutmu apakah faktor paling penting yang harus dimiliki di masa-masa awal merintis ? -> A) Rekan yang bisa dipercaya. B) Profit yang banyak atau C) Produk yang berkualitas : ")
    if bisnis == "A":
        print("Selamat kamu benar ! Kamu telah berhasil menyelesaikan game ini dengan sempurna !")
        print("                                             \n~ Tamat.")
    if bisnis == "B":
        print("Ngaco. Jawab sampai benar !")
    if bisnis == "C":
        print("Ngaco. Jawab sampai benar !")



