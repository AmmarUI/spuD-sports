# spuD Sports ⚽
Nama : Abdurrahman Ammar Abqary
NPM : 2406495994
Kelas : PBP D

History README Tugas:
[Tugas 2](https://github.com/AmmarUI/spuD-sports/wiki/README-Tugas-2)
[Tugas 3](https://github.com/AmmarUI/spuD-sports/wiki/README-Tugas-3)
[Tugas 4](https://github.com/AmmarUI/spuD-sports/wiki/README-Tugas-4)
[Tugas 5](https://github.com/AmmarUI/spuD-sports/wiki/README-Tugas-5)

---

## 1. Perbedaan antara synchronous request dan asynchronous request

Synchronous request:
- Saat client (browser) mengirim request ke server, browser menunggu respon sampai selesai.
- Selama menunggu, pengguna tidak bisa berinteraksi dengan bagian lain dari halaman (stuck / reload penuh).
- Contoh: form submit biasa → halaman reload penuh dengan data baru.

Asynchronous request:
- Browser mengirim request ke server tanpa menghentikan interaksi user.
- Respon diterima di background, lalu DOM diperbarui sebagian tanpa reload halaman.
- Contoh: AJAX (fetch, XMLHttpRequest) → data ditampilkan langsung.

## 2. Bagaimana AJAX bekerja di Django (alur request–response)

1. User action: misalnya klik tombol "Add Product".
2. JavaScript AJAX call: JS (fetch/XHR) kirim request ke endpoint Django (/create-item-ajax) dengan data.
3. Django view: menerima request, memproses (validasi, simpan ke database), lalu balas dengan JsonResponse atau HttpResponse.
4. Browser callback: JavaScript menerima respon → update tampilan DOM (misalnya menambahkan card baru ke daftar produk).
5. Halaman tidak reload penuh, hanya bagian tertentu yang berubah.

## 3. Keuntungan menggunakan AJAX dibandingkan render biasa di Django

- Lebih cepat → hanya data yang dikirim/diterima, bukan seluruh halaman.
- Hemat bandwidth → tidak perlu kirim ulang CSS, JS, layout.
- UX lebih baik → interaksi terasa mulus tanpa reload.
- Dynamic UI → data bisa dimuat/diubah secara real-time.
- Bisa buat single-page-like apps walau pakai Django tradisional.

## 4. Bagaimana cara memastikan keamanan saat menggunakan AJAX untuk Login dan Register di Django

- Gunakan CSRF token: pastikan AJAX request menyertakan token CSRF untuk POST request.
- Validasi input di server: jangan hanya di client, tapi juga gunakan form Django (UserCreationForm, AuthenticationForm).
- Gunakan HTTPS: agar username & password tidak bocor di jaringan.
- Session management: gunakan login(request, user) dan logout(request) bawaan Django, jangan bikin sendiri.

## 5. Bagaimana AJAX mempengaruhi pengalaman pengguna (User Experience) pada website

- Responsif: User tidak terganggu reload halaman → lebih mulus.
- Real-time feel: data bisa diperbarui langsung (misalnya cart update, notifikasi).
- Lebih interaktif: modal, toast, refresh list tanpa reload.
- Kurangi frustasi user: misalnya gagal login → langsung muncul error di layar tanpa reload.
- Kekurangan: jika implementasi salah, user bisa bingung karena URL tidak berubah / tidak bisa di-refresh untuk lihat state yang sama.