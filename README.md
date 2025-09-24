Pertanyaan dan Jawaban Tugas 4

# 1. Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.

AuthenticationForm adalah form yang sudah tersedia dari Django yang berfungsi untuk implementasi proses autentikasi pengguna seperti login, logout, dan registrasi. 
Kelebihan:
- Built-in dari Django, gaperlu implementasi form sendiri dan gaperlu mengembangkan dari nol lagi
- Error handling yang jelas
- Sudah terintegrasi dengan keseluruhan framework Django
Kekurangan:
- Terbatas pada username dan password, tidak bisa menggunakan email, OTP, atau apapun lainnya
- Very barebones, sehingga untuk mengubah penampilannya ataupun jika ingin menambah fitur keamanan lainnya seperti 2FA perlu mengembangkannya sendiri

# 2.  Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?

Secara garis besar autentikasi adalah memverifikasi user, sedangkan otorisasi adalah mengatur user tersebut memiliki akses ke apa saja. Django mengimplentasi hal ini dengan modul/library default yang sudah dimiliki, yaitu django.contrib.auth dan lainnya untuk authorization. Untuk otorisasi, contohnya adalah dengan penggunaan decorator @login_required untuk fungsi-fungsi tertentu pada views.py.

# 3. Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?

Session adalah state holder yang disimpan secara server-side, sedangkan cookies dapat disimpan secara client-side. Kelebihan utama dari session dibanding cookie adalah dalam keamanan data dan juga size penyimpanan. Sedangkan, kelebihan utama dari cookies adalah keringanannya dan bahwa dia persistent di client side, sehingga jika server restart akan tetap tersimpan. Kekurangan dari session adalah bahwa dia hanya bertahan selama satu sesi, biasanya langsung hilang setelah user logout atau session expired. Selain itu, session tetap membutuhkan cookie untuk menyimpan session ID, sehingga masih melibatkan cookies. Kekurangan dari cookie adalah dalam sisi keamanan, dengan isinya bisa dilihat dan dimodifikasi di sisi client. Selain itu, user juga dapat dengan mudah menghapus cookies, sehingga menyebabkan state hilang.

# 4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?

Seperti yang dibahas pada nomor sebelumnya, salah satu kekurangan terbesar cookie adalah dalam keamanan data, sehingga ia tidak aman secara default. Cookie rentan terhadap session hijacking, cross-site scripting, CSRF, dll.. Untuk menangani hal ini, Django memiliki berbagai cara, terutama adalah dengan hanya menyimpan session ID pada cookies, dengan data dari session tersebut disimpan pada server. Sehingga, meskipun mungkin cookie sendiri rentan, setidaknya data yang sensitif aman. Selain itu, Django memiliki berbagai cara untuk menangani CSRF protection, seperti yang diimplementasi dengan CSRF Token pada tugas sebelumnya.

# 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

Pertama, saya mengimplementasi fungsi login terlebih dahulu, dan membuat tampilan awal dari website menjadi laman login, dan menambahkan decorator @login_required pada fungsi view show_main dan create_item. Setelah itu, saya membuat file login.html untuk tampilan web login, dengan menggunakan AuthenticationForm dan juga messages sehingga dapat membuat entry user dan interaksi dengan user secara mudah. Lalu, saya mengimplementasi fungsi registrasi dengan menggunakan UserCreationForm yang sudah disediakan oleh Django, dan menambahkan register.html untuk tampilan halaman registrasi. Akhirnya, saya menambahkan fitur logout untuk melengkapi user authentication process.

Setelah melakukan testing fitur user authentication, saya menghubungkan model Item dengan User dengan menggunakan django.contrib.auth.models untuk import User dan menambahkan datafield user pada model Item. Lalu, saya mengedit fungsi create_item untuk save user saat create item dengan request.user. Setelah melakukan itu, saya membuat dua akun dan tiga produk di masing2 akun lalu test fungsi filter.

Setelah melakukan checklist yang lain, baru saya mulai mengimplementasi cookies. Pada fungsi login, ditambahkan metode set_cookie sebelum user diredirect ke halaman main, dengan isi cookie tersebut merupakan timestamp login. Lalu, di fungsi logout ditambahkan metode untuk delete cookie tersebut sebelum user dikembalikan ke halaman login. Terakhir, saya mengubah main.html untuk menampilkan data login terakhir dan menyesuaikan context pada fungsi show_main dengan menggunakan request.COOKIES.get, dengan default value 'Never'.