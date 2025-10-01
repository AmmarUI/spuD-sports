Pertanyaan dan Jawaban Tugas 5

# 1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!

Prioritas selector CSS dilakukan dari skala specificity kecil ke besar. 
1. Inline style → paling kuat (misalnya <p style="color:red;">).
2. ID selector (#id-name {})
3. Class, pseudo-class, dan attribute selector (.class {}, :hover {}, [type=text] {}).
4. Element/tag selector (p {}, h1 {}, div {}).
5. Universal selector (* {}) → paling lemah.
6. Jika specificity sama, aturan yang ditulis paling terakhir di file CSS yang berlaku.

# 2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!

Responsive design adalah konsep untuk menyesuaikan tampilan website ke ukuran layar yang digunakan.
Hal ini penting karena:
- Sekarang website sudah tidak hanya digunakan pada desktop, namun banyak yang mengakses lewat mobile juga. Layar juga banyak yang berbeda ukuran atau aspect ratio.
- Tanpa responsive design, user experience buruk (teks kepotong, tombol kecil, layout berantakan).

Contoh aplikasi:
- Sudah responsive: Medium, platform blogging yang web-based, artikel ditampilkan dengan layout bersih, teks mudah dibaca, dan responsif di semua ukuran layar tanpa harus instal aplikasi.
- Belum responsive: Situs web lama (misalnya website sekolah atau pemerintahan yang masih fixed) di HP tampilannya harus discroll ke samping, teks terlalu kecil, dll.

# 3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!

- Margin: ruang di luar border elemen (jarak antar elemen)
- Border: garis yang mengelilingi elemen langsung
- Padding: jarak antara border dan elemen di dalemnya

# 4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!

Flexbox dan Grid Layout adalah dua modul CSS modern yang digunakan untuk membangun tata letak halaman. Flexbox digunakan untuk mengatur layout satu dimensi, baik itu baris maupun kolom. Flexbox mempermudah penempatan elemen dalam satu garis, misalnya untuk membuat navigasi horizontal, menata kartu produk dalam satu baris, atau meratakan konten secara vertikal di tengah. Grid Layout digunakan untuk mengatur layout dua dimensi, yaitu baris dan kolom sekaligus. Grid cocok digunakan untuk desain yang lebih kompleks seperti dashboard, galeri foto, atau tata letak majalah digital. Jadi, flexbox lebih unggul untuk penyusunan elemen dalam satu arah, sedangkan grid memberikan kendali penuh untuk tata letak dua arah.

# 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

Pertama, saya initialize css dengan memanggil cdn tailwind pada base.html. Saya juga menambahkan script dan reference untuk menggunakan font Lexend untuk heading dan font Inter untuk body. Lalu, saya membuat direktori static/css dan menambahkan file global.css yang isinya pengaturan font tersebut serta pengaturan style lainnya untuk setiap form. Setelah mengatur css untuk base keseluruhan, saya membuat navigation bar pada navbar.html dan mengincludenya pada main.html. Selanjutnya, saya mengatur styling css untuk setiap file html lainnya dan menambahkan item_card.html dan mengatur main.html agar penampilan setiap product pada web dapat menggunakan item_card.html tersebut. Lalu, saya menambahkan functionality edit dan delit item untuk user yang mengupload item tersebut.