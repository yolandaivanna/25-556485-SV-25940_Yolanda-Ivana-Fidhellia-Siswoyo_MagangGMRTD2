Nama     : Yolanda Ivana Fidhellia Siswoyo
NIM      : 25/556485/SV/25940
Prodi    : Teknologi Rekayasa Internet

RINGKASAN DESKRIPSI TUGAS  :
- COMPUTER VISION
  1. Fitur
    Cuma fokus deteksi 3 objek: person, cell phone, dan cup.
    Tampilan kamera udah disesuaikan biar gak kebalik (anti-mirror).
    Menampilkan bounding box, nama objek, dan skor akurasi (confidence score).
    Pake model Nano (yolov8n.pt) jadi enteng dan kenceng.

  2. Library yang Dipakai
    Python 3
    ultralytics
    opencv-python
- PID
  Isi tugas ini ngebahas 3 percobaan tuning PID buat kontrol kecepatan motor robot pake optical encoder, target 150 RPM.
 
  Konfigurasi A (P doang) -> mentok di 138 RPM, nggak pernah nyampe target.
  Konfigurasi B (PI) -> overshoot sampe 195 RPM, osilasi, baru stabil di detik ke-4.
  Konfigurasi C (PID lengkap) -> naik mulus, overshoot dikit (154 RPM), stabil di bawah 1 detik.
   
  Ada juga bagian troubleshooting soal apa yang kejadian kalau roda ditahan halangan 5 detik terus dilepas mendadak 
  (integral windup -> lonjakan kecepatan berbahaya), sama solusinya pake anti-windup di software.
