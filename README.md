Pertanyaan dan Jawaban Tugas 3

1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Data delivery menjadi semacam "backbone" dari pengembangan sebuah platform. Data delivery dapat menentukan kecepatan, keamanan, dan seberapa akurat informasi ditukar antara server dan database ke pengguna.

2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

Dari yang saya ketahui, perbedaan dari XML dan JSON yang terutama terlihat adalah bahwa JSON lebih mudah dilihat dan dicerna informasinya karena penampilan yang lebih "clean". Namun, XML bisa lebih cocok untuk dokumen dan project yang menggunakan data structure lebih complex karena dapat diextend dengan custom data types. Tapi, untuk mayoritas orang, JSON lebih mudah digunakan karena sifatnya yang lebih simpel.

3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?

Dalam Django, method is_valid() digunakan untuk memeriksa apakah data yang dimasukkan ke dalam form sudah sesuai dengan aturan validasi. Jika valid, Django akan menyediakan data yang sudah dibersihkan melalui cleaned_data sehingga aman untuk digunakan atau disimpan ke database. Jika tidak valid, method ini akan menyimpan pesan kesalahan di form.errors agar bisa ditampilkan ke pengguna. Dengan demikian, is_valid() penting untuk menjaga keamanan, konsistensi data, dan memberikan feedback yang jelas kepada pengguna.

4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

csrf_token digunakan sebagai lapisan keamanan untuk mencegah serangan Cross-Site Request Forgery (CSRF). Token ini adalah kode unik yang dikirim bersama form dan diverifikasi oleh server ketika form dikirim kembali. Jika csrf_token tidak ditambahkan, maka form menjadi rentan terhadap serangan tersebut. Artinya, penyerang bisa membuat sebuah halaman berbahaya yang diam-diam mengirim permintaan ke server Django dengan memanfaatkan sesi pengguna yang sedang login. Misalnya, tanpa disadari pengguna bisa dipaksa melakukan aksi penting seperti mengubah password, melakukan transaksi, atau menghapus data, hanya karena ia membuka situs berbahaya saat masih login di aplikasi. Dengan kata lain, tanpa csrf_token, penyerang dapat menyamar sebagai pengguna sah dan memanfaatkan sesi autentikasi korban untuk menjalankan aksi berbahaya.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

Pertama, saya mengubah model Shop yang saya buat pada tugas sebelumnya menjadi model Item karena menurut saya lebih cocok untuk kedepannya. Lalu, saya tambahkan fungsi-fungsi untuk XML dan JSON, lalu push ke github sebagai langkah awal. Setelah itu, saya menambahkan base.html di direktori baru pada main dan mengisinya dengan metadata yang diperlukan untuk project ini. Lalu, saya sesuaikan main.html dan mulai menambahkan fungsi create_item dan show_item pada views.py. Kemudian, saya menyesuaikan urlpattern pada urls.py dan membuat tampilan untuk keduanya dengan membuat create_item.html dan juga show_item.html. Setelah itu, saya lakukan migrasi dan melakukan testing functionality yang baru dibuat. Terakhir, saya push ke github dan pws.

6. Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?

Tidak ada kak, menurut saya sudah cukup jelas dan sangat membantu memahami kode yang ditulis.

7. Screenshot Postman : ristek.link/ScreenshotPostmanTugas3PBP