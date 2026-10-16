<script setup lang="ts">
useHead({ title: "Galeri — PT Kabut Asap & Wisata Napas" })

const photos: Photo[] = [
  { title: "Pagi Hari di Zona Operasional", caption: "Desa Konoha dan hamparan sawah diterpa kabut pagi. Titik ini menjadi sumber utama pengemasan udara premium kami — udara diambil langsung sebelum kabut turun menutupi titik pengemasan.", meta: "Zona Utama · 06.12 WIB" },
  { title: "Wisatawan Menanti Matahari", caption: "Kelompok peserta tur matahari berkumpul di puncak bukit pukul 03.00. Pengalaman berkabut bintang lima tetap diberikan meski matahari tidak terbit.", meta: "Puncak Wisata · 03.14 WIB" },
  { title: "Ruang Rapat Koordinasi", caption: "Kantor koordinasi luar negeri PT KAW N. Ruangan ini digunakan untuk rapat darurat penanganan kabut, dengan jarak pandang yang mendukung produktivitas pengurus.", meta: "Kantor Cabang · 2023" },
  { title: "Distribusi Udara Kaleng", caption: "Armada truk PT KAW N mengangkut kaleng udara premium ke titik penjualan mitra. Jadwal distribusi menyesuaikan kondisi kabut harian.", meta: "Rute Desa · Senin & Kamis" },
  { title: "Gudang Penyimpanan", caption: "Kaleng udara premium tertata rapi di gudang desa. Kapasitas penyimpanan saat ini 50.000 kaleng — cukup untuk dua musim kabut sedang.", meta: "Gudang Desa · Kapasitas 50.000" },
  { title: "Petani di Tengah Kabut", caption: "Warga tetap bekerja di sawah menggunakan masker. PT KAW N mengapresiasi ketangguhan petani Konoha sebagai mitra udara terbaik kami.", meta: "Blok Sawah Timur · 07.40 WIB" },
  { title: "Konferensi Pers Tahunan", caption: "Konferensi pers tahunan PT KAW N di hadapan wartawan. Agenda utama: peluncuran laporan kinerja dan pengumuman rencana Program Napas Bersama.", meta: "Balai Desa · Desember 2025" },
  { title: "Arsip Laporan & Audit", caption: "Tumpukan laporan tahunan dan berkas permintaan audit independen. Semua permintaan audit ditolak dengan alasan data masih dalam proses digitalisasi.", meta: "Ruang Keuangan" },
  { title: "Kantor Pusat PT KAW N", caption: "Gedung kantor utama di pinggir desa, berdiri sejak 2019. Bagian bawah gedung sering tertutup kabut — kondisi yang kami anggap sebagai pemandahan alami.", meta: "Kantor Pusat · Est. 2019" },
  { title: "Stasiun Pemantau Udara", caption: "Alat pemantau kualitas udara milik perusahaan. Pembacaan terakhir: indeks 1.240 — status \"berbahaya\", yang secara komersial berarti \"permintaan tinggi\".", meta: "Stasiun #1 · Realtime" },
  { title: "Kegiatan Bersama Warga", caption: "Acara gotong royong bersih udara yang dihadiri dua panitia dan delapan kursi kosong. Kehadiran warga bersifat sukarela dan sangat dihargai.", meta: "Halaman Kantor" },
  { title: "Kaleng di Warung Desa", caption: "Kaleng udara premium ditata di warung desa. Papan harga menyatakan penyesuaian tarif mengikuti tingkat kabut — transparansi penuh*.", meta: "Warung Bu Desa" },
  { title: "Ruang Produksi Pengemasan", caption: "Jalur produksi pengemasan udara dengan kapasitas 400ml per siklus. Status produksi: aktif, selama pasokan udara mentah dari puncak memadai.", meta: "Unit Produksi" },
  { title: "Matahari Terbit Tersamar", caption: "Matahari terbit di ufuk timur, samar di balik lapisan kabut. Visual ini digunakan dalam materi promosi Paket Wisata Matahari.", meta: "Bukit Timur · 05.48 WIB" },
  { title: "Lalu Lintas Sore Hari", caption: "Kemacetan panjang di jalan desa akibat jarak pandang terbatas. PT KAW N mengimbau warga berangkat lebih awal — atau berjalan kaki*.", meta: "Jalan Raya Desa" },
  { title: "SD Konoha 1", caption: "Siswa SD Konoha 1 berbaris dengan masker menuju kelas. Kegiatan belajar tetap berjalan normal selama kabut di bawah ambang batas.", meta: "SD Konoha 1" },
  { title: "Jalur Pendakian Puncak", caption: "Jalur pendakian menuju Puncak Wisata dengan papan petunjuk khas. Panjang rute ±2 km, dapat ditempuh dalam 90 menit jika kabut tidak terlalu pekat.", meta: "Rute Pendakian · 2 km" },
  { title: "Papan Pengumuman Desa", caption: "Empat pengumuman resmi PT KAW N di papan desa: jadwal tur, kenaikan harga udara, rencana Program Napas Bersama, dan penjadwalan ulang rapat warga.", meta: "Papan Desa" },
  { title: "Balai Desa Konoha", caption: "Balai desa tempat rapat warga diadankan — atau seharusnya diadakan. Rapat terakhir dijadwalkan ulang karena pengurus menghadiri rapat koordinasi di luar negeri.", meta: "Balai Desa" },
  { title: "Toko Kelontong Mitra", caption: "Etalase kaleng udara di toko kelontong mitra. Harga Rp 12.500 per kaleng, disesuaikan dengan tingkat kabut harian untuk keberlanjutan usaha.", meta: "Toko Mitra #4" },
  { title: "Pemantauan Udara dengan Drone", caption: "Drone perusahaan memantau sebaran kabut dari ketinggian. Data pemantauan digunakan untuk menentukan titik pengambilan udara terbaik setiap pagi.", meta: "Pemantauan Harian" },
  { title: "Lambang di Dinding Kantor", caption: "Lambang resmi PT KAW N: matahari yang tetap bersinar di balik kabut — filosofi \"terang di tengah ketidakpastian\" yang terpatri di dinding kantor pusat.", meta: "Lobi Kantor" },
  { title: "Grafik Pertumbuhan Laba", caption: "Grafik klaim pertumbuhan laba 2021–2025. Tiga permintaan audit independen ditolak sepanjang periode, sehingga angka bersifat self-reported sepenuhnya.", meta: "Laporan Tahunan 2025" },
  { title: "Lingkungan Operasional", caption: "Cerobong industri di belakang permukiman warga. Sumber kabut utama desa — yang sekaligus bahan baku utama produk kami. Siklus yang saling menguntungkan.", meta: "Zona Industri" },
  { title: "Tim Kecil Kami", caption: "Dua karyawan tetap bekerja di kantor pusat. Jam kerja 08.00–14.00 WIB, atau lebih awal jika kabut terlalu tebal untuk pulang dengan aman.", meta: "Kantor Pusat" },
  { title: "Produk Andalan", caption: "Udara Kaleng Premium 400ml dengan label bergaransi Desa Konoha. Dikemas langsung di sumber, stok terbatas mengikuti jadwal kabut.", meta: "SKU: KALENG-400" },
]

const base = "/sarkas-bumk-kabut-asap"
</script>

<template>
  <UContainer class="py-14">
    <h1 class="text-3xl font-bold">Galeri</h1>
    <p class="mt-3 text-(--ui-text-muted) max-w-2xl">
      {{ photos.length }} dokumentasi visual kegiatan, produk, dan pemandangan khas operasional
      PT KAW N. Klik salah satu kartu untuk melihat lebih besar, lalu gunakan tombol
      panah atau keyboard (← →) untuk berpindah.
    </p>

    <!-- Grid kartu tanpa gambar ────────────────────────────────────── -->
    <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-5 mt-10">
      <UCard
        v-for="(photo, i) in photos"
        :key="photo.title"
        class="h-full cursor-pointer transition hover:border-(--ui-primary)/40 hover:shadow-lg"
        role="button"
        tabindex="0"
        @click="activeIndex = i"
        @keydown.enter="activeIndex = i"
        @keydown.space.prevent="activeIndex = i"
      >
        <!-- Blockkode visual monospace ──────────────────────────────── -->
        <div class="w-full aspect-[4/3] rounded-xl bg-(--ui-bg-elevated) flex items-center justify-center p-4">
          <div class="w-full h-full rounded bg-white/70 p-3 text-xs font-mono leading-relaxed">
            <code class="text-(--ui-primary)">
              ┌─ <span class="text-xs text-(--ui-text-muted)">{{ String(i+1).padStart(2,'0') }}</span> ───────────────┐<br/>
              <span class="text-xs">│</span> <span class="text-xs text-(--ui-text)">{{ photo.title }}</span><br/>
              <span class="text-xs">│</span> <span class="text-xs text-(--ui-text-muted)">{{ photo.caption }}</span><br/>
              <span class="text-xs">│</span> <span class="text-xs text-(--ui-text-dimmed)">{{ photo.meta }}</span><br/>
              <span class="text-xs">└───────────────────────────────────────────────┘</span><br/>
            </code>
          </div>
        </div>

        <div class="mt-3">
          <div class="flex items-baseline justify-between gap-2">
            <div class="font-semibold">{{ photo.title }}</div>
            <div class="font-mono text-xs text-(--ui-text-dimmed) shrink-0">{{ String(i+1).padStart(2,'0') }}</div>
          </div>
          <div class="text-xs text-(--ui-primary) font-mono mt-0.5">{{ photo.meta }}</div>
          <p class="text-xs text-(--ui-text-muted) mt-1">{{ photo.caption }}</p>
        </div>
      </UCard>
    </div>

    <!-- Kredit (antislop: tanpa foto, catatan situs) ─────────────────── -->
    <USeparator class="my-8" />
    <section class="text-xs text-(--ui-text-muted) space-y-1">
      <p class="font-semibold text-(--ui-text)">Catatan Desain</p>
      <p>
        Situs ini disusun tanpa penggunaan fotografi atau ilustrasi. Setiap kartu
        menggunakan blok teks monospace sebagai representasi visual korporat. Semua
        narasi dan angka adalah rekaan untuk karya satire.
      </p>
      <p class="mt-2">
        *Klaim internal perusahaan (self-reported). Tidak ada verifikasi pihak ketiga.
      </p>
    </section>
  </UContainer>
</template>
