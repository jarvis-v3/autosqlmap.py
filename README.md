# autosqlmap

# Penggunaan Script

Script ini digunakan untuk melakukan pengujian keamanan pada sebuah website. Ia mencakup tahapan seperti menginstal alat yang diperlukan, mengambil URL target, membuat daftar kata sandi, dan menjalankan alat pengujian seperti SQLMap dan Hydra.

## Prasyarat
- Python 3.x
- Akses root atau hak akses yang diperlukan untuk menginstal alat melalui `sudo apt install`

## Instalasi
1. Pastikan Python 3.x telah terinstal pada sistem Anda.
2. Pastikan Anda memiliki akses root atau hak akses yang diperlukan untuk menginstal alat melalui `sudo apt install`.
3. Salin kode script ke sebuah file dengan nama `hackwebsite.py`.

## Penggunaan
1. Buka terminal atau command prompt.
2. Navigasikan ke direktori tempat Anda menyimpan file script.
3. Jalankan perintah `python website_security_tester.py`.
4. Masukkan URL target website yang ingin Anda uji.
5. Periksa apakah alat yang diperlukan telah terinstal. Jika belum, script akan mencoba menginstalnya.
6. Script akan membuat daftar kata sandi menggunakan Crunch dengan nama `password_list.txt`.
7. Script akan menjalankan SQLMap untuk mencari celah keamanan pada database.
8. Script akan menjalankan Hydra untuk menguji kredensial dengan menggunakan daftar kata sandi yang telah dibuat.

## Catatan
- Script ini mengasumsikan bahwa Anda memiliki akses root atau hak akses yang diperlukan untuk menginstal alat melalui `sudo apt install`.
- Script menggunakan Crunch untuk membuat daftar kata sandi dengan format `@@@username@@@`.
- Script menggunakan SQLMap dengan tingkat keamanan tinggi (`--level=5`) dan risiko tinggi (`--risk=3`).
- Script menggunakan Hydra dengan HTTP Post form untuk menguji kredensial.
- Script akan meminta URL target dan mengasumsikan bahwa nama pengguna yang digunakan adalah "admin".

Script tersebut akan meminta URL target dan mengasumsikan bahwa nama pengguna yang digunakan adalah "admin". Jika Anda ingin mengubah nama pengguna, Anda dapat mengganti nilai username pada variabel username.

Jika Anda ingin menjalankan script ini secara langsung, Anda perlu memastikan bahwa Python 3.x telah terinstal pada sistem Anda dan memiliki akses root atau hak akses yang diperlukan untuk menginstal alat melalui sudo apt install. Pastikan juga bahwa alat yang diperlukan seperti SQLMap, Hydra, dan Crunch telah terinstal pada sistem Anda. Jika tidak, script akan mencoba menginstalnya secara otomatis.

Jika Anda menjalankan script ini secara langsung dan memiliki kesulitan atau pertanyaan, silakan tanyakan!
