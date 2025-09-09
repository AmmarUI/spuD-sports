1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

Dalam pengerjaan proyek ini, saya mulai dengan membuat repository git, lalu melakukan git clone. Setelah itu, saya menyalakan virtual environment agar mengisolasi dependensi proyek. Lalu, saya membuat file requirements.txt dan menginstall semua dependency yang dibutuhkan oleh proyek. Setelah semua berhasil terinstall, dilakukan konfigurasi settings.py, .env, serta .env.prod. Setelah itu, saya menyambungkan dan push proyek yang sudah dibuat ke Pacil Web Service (PWS).

Setelah konfigurasi awal sudah selesai, saya mulai membuat model, template, dan bentukan awal web. Pertama saya buat folder main, dan di dalamnya folder templates dan di dalamnya lagi membuat file main.html. Pada file main.html, didefinisikan metadata doctype, head yang berupa title web, dan heading dan paragraph. Selanjutnya, pada file models.py di folder main, didefinisikan class Shop menggunakan library models yang tersedia. Pada class tersebut didefinisikan:
• name: CharField, untuk menyimpan nama produk.
• price: IntegerField, untuk menyimpan harga produk.
• description: TextField, untuk deskripsi detail produk.
• thumbnail: URLField, untuk menyimpan tautan gambar produk.
• category: CharField, untuk mengkategorikan produk.
• is_featured: BooleanField, untuk menandai apakah produk tersebut unggulan atau tidak.

Selanjutnya, saya melakukan proses migrasi data dan routing. Akhirnya, saya melakukan push akhir ke git dan PWS.

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

Bagan tercantum pada link berikut: ristek.link/BaganRoutingDjango

Dalam Django, ketika pengguna mengakses sebuah URL, permintaan tersebut pertama kali diproses oleh urls.py, yang berfungsi untuk memetakan pola URL ke fungsi tertentu di views.py. View kemudian menangani permintaan tersebut dan, jika diperlukan, berinteraksi dengan models.py untuk mengambil atau menyimpan data ke dalam database. Setelah data yang dibutuhkan tersedia, view meneruskannya ke template seperti main.html, di mana data tersebut dirender menjadi HTML dan ditampilkan kepada pengguna.

3. Jelaskan peran settings.py dalam proyek Django!

Dalam proyek Django, settings.py berfungsi sebagai pengaturan dan pusat kendalinya proyek tersebut, semacam control panel. Hal ini termasuk juga konfigurasi fundamental yang dibutuhkan seperti aplikasi yang digunakan, template, database, dll.. 

4. Bagaimana cara kerja migrasi database di Django?

Migrasi di Django digunakan untuk "synchronize" perubahan yang dilakukan ke model kepada database. Simpelnya, proses ini dilakukan dalam dua tahap, yaitu pertama dengan command makemigrations lalu dengan command migrate. Command makemigrations akan ngescan model dan membandingkannya dengan versi yang sekarang ada. Lalu, akan mempersiapkan hal baru yang ingin dimigrate. Lalu, command migrate akan "push" migration yang sudah disiapkan oleh makemigrations ke database. Ini bisa diperkirakan seperti version control untuk database proyek.

5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

Menurut saya, Django dijadikan framework untuk permulaan pembelajaran pengembangan perangkat lunak karena beberapa hal yang membuatnya beginner-friendly. Pertama, Django berbasis python yang merupakan high level language yang mudah dipahami. Django memiliki documentation yang sangat luas dan bisa diexplore, dengan memiliki banyak modules dan libraries yang sudah tersedia. Django juga menyediakan banyak hal yang untuk pemula sangat bingung untuk diimplementasikan, seperti ORM, admin interface, sistem autentikasi, dan bahkan fitur keamanan.

6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?

Tidak ada kak, sudah sangat bagus dan saya sangat mengapresiasi penjelasan yang diberi untuk setiap kodenya sehingga bisa memahami kodenya dan tidak hanya copy-paste saja.