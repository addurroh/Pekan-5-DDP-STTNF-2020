{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"name":"Tugas Pekan 5 Prktikum DDP","provenance":[],"authorship_tag":"ABX9TyPE/qleQlPO0pGVqpSrudG9"},"kernelspec":{"name":"python3","display_name":"Python 3"}},"cells":[{"cell_type":"code","metadata":{"id":"e2QO6w2ADpPP","executionInfo":{"status":"error","timestamp":1604457012959,"user_tz":-420,"elapsed":867,"user":{"displayName":"MUHAMMAD AD-DURROH MUBAROK","photoUrl":"https://lh3.googleusercontent.com/a-/AOh14GggParFe6jjAIkrpY78sgUejNZX3psL8xYwEqUL=s64","userId":"03275221799847507586"}},"outputId":"6fc20771-06aa-4dba-e98f-b2d8824d3850","colab":{"base_uri":"https://localhost:8080/","height":130}},"source":["# DDP LAB-4\n","# Nama: <Tulis nama di sini>\n","print(\"MUHAMMAD AD-DURROH MUBAROK\")\n","# NIM: <Tulis NIM di sini>\n","print(\"0110120117\")\n","\n","# SOAL 1 - Mencetak nama\n","# Tuliskan program untuk Soal 1 di bawah ini\n","s = 'Durroh'\n","print(s.lower(d) # mencetak 'durroh'\n","print(s.upper(u) # mencetak 'HELLO'\n","print(s.replace('','yyy')) # mencetak 'Hellyyy'\n","print(s.count('el')) # mencetak 1\n","print(s.startswith('h')) # mencetak False\n","print(s.endswith('o'))\n","\n","\n","\n","\n","# SOAL 2 - Validasi teks\n","# Tuliskan program untuk Soal 2 di bawah ini\n"],"execution_count":2,"outputs":[{"output_type":"error","ename":"SyntaxError","evalue":"ignored","traceback":["\u001b[0;36m  File \u001b[0;32m\"<ipython-input-2-d5541cb644c0>\"\u001b[0;36m, line \u001b[0;32m11\u001b[0m\n\u001b[0;31m    print(s.upper(u) # mencetak 'HELLO'\u001b[0m\n\u001b[0m        ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"]}]},{"cell_type":"markdown","metadata":{"id":"x8qZwMBKDtpZ"},"source":["Deskripsi Lab-4\n","Pada Lab-4, kalian diminta untuk menuliskan program yang dapat menangani permasalahan-permasalahan berikut. Program dapat dituliskan dalam file main.py yang sudah tersedia.\n","Untuk setiap program yang ditulis, berikan penjelasan mengenai alur jalannya program. Tulis penjelasan tersebut dalam bentuk komentar pada program.\n","\n","Soal 1. Mencetak nama\n","Buatlah program yang menerima sebuah nama dan mencetak nama tersebut berulang kali mulai dari satu karakter pertama hingga semua karakter nama terlihat.\n","Sebagai contoh, hasil cetak nama Nurul adalah N, Nu, Nur, Nuru, dan Nurul.\n","Program yang dibuat diharapkan hanya mengandung perulangan while dan string slicing.\n","\n","Contoh 1.1\n","Contoh masukan 1.1:\n","\n","Masukkan nama: Fikri\n","Masukkan nama: Fikri\n","Contoh luaran 1.1:\n","\n","F\n","Fi\n","Fik\n","Fikr\n","Fikri\n","F\n","Fi\n","Fik\n","Fikr\n","Fikri\n","Contoh 1.2\n","Contoh masukan 1.2:\n","\n","Masukkan nama: SEMANGKA\n","Masukkan nama: SEMANGKA\n","Contoh luaran 1.2:\n","\n","S\n","SE\n","SEM\n","SEMA\n","SEMAN\n","SEMANG\n","SEMANGK\n","SEMANGKA\n","S\n","SE\n","SEM\n","SEMA\n","SEMAN\n","SEMANG\n","SEMANGK\n","SEMANGKA\n","Soal 2. Validasi teks\n","Buatlah sebuah program yang menerima sebuah teks dan melakukan validasi terhadap teks tersebut.\n","Jika teks belum valid, maka program akan terus meminta pengguna memasukkan teks. Program berhenti saat teks valid dimasukkan.\n","\n","Kriteria sebuah teks valid adalah sebagai berikut:\n","\n","Panjang teks minimal 8\n","Teks mengandung minimal sebuah frase 'NF' (tidak harus kapital semua)\n","Teks diakhiri dengan 'YYY' atau 'yyy' (kapital semua atau huruf kecil semua)\n","Teks mengandung minimal sebuah angka (0-9)\n","Contoh 2.1\n","Contoh masukan dan luaran 2.1:\n","\n","Masukkan sebuah teks: 123lalalyyy\n","Teks tidak valid.\n","Masukkan sebuah teks: NF00yyy\n","Teks tidak valid.\n","Masukkan sebuah teks: nF1nNFnlyYy\n","Teks tidak valid.\n","Masukkan sebuah teks: NFpppppppyyy\n","Teks tidak valid.\n","Masukkan sebuah teks: nF1nNfnlyYYY\n","Teks valid. Program berhenti.\n","Masukkan sebuah teks: 123lalalyyy\n","Teks tidak valid.\n","Masukkan sebuah teks: NF00yyy\n","Teks tidak valid.\n","Masukkan sebuah teks: nF1nNFnlyYy\n","Teks tidak valid.\n","Masukkan sebuah teks: NFpppppppyyy\n","Teks tidak valid.\n","Masukkan sebuah teks: nF1nNfnlyYYY\n","Teks valid. Program berhenti.\n","Penjelasan contoh 2.1:\n","\n","Teks 123lalalyyy tidak valid karena tidak mengandung frase NF\n","Teks NF00yyy tidak valid karena panjang teks kurang dari 8\n","Teks nF1nNFnlyYy tidak valid karena tidak diakhiri dengan 'YYY' atau 'yyy'\n","Teks NFpppppppyyy tidak valid karena tidak mengandung angka"]}]}