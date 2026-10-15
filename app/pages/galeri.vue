<script setup lang="ts">
useHead({
  title: 'Galeri — PT Kabut Asap & Wisata Napas',
})

const base = '/sarkas-bumk-kabut-asap'

type Photo = {
  src: string
  title: string
  caption: string
  meta: string
}

const photos: Photo[] = [
  {
    src: base + '/img/foto/hero.jpg',
    title: 'Pagi Hari di Zona Operasional',
    caption: 'Desa Konoha dan hamparan sawah diterpa kabut pagi. Titik ini menjadi sumber utama pengemasan udara premium kami — udara diambil langsung sebelum kabut turun menutupi titik pengemasan.',
    meta: 'Zona Utama · 06.12 WIB',
  },
  {
    src: base + '/img/galeri-wisata-sunrise.svg',
    title: 'Wisatawan Menanti Matahari',
    caption: 'Kelompok peserta tur matahari berkumpul di puncak bukit pukul 03.00. Pengalaman berkabut bintang lima tetap diberikan meski matahari tidak terbit.',
    meta: 'Puncak Wisata · 03.14 WIB',
  },
  {
    src: base + '/img/foto/meeting.jpg',
    title: 'Ruang Rapat Koordinasi',
    caption: 'Kantor koordinasi luar negeri PT KAW N. Ruangan ini digunakan untuk rapat darurat penanganan kabut, dengan jarak pandang yang mendukung produktivitas pengurus.',
    meta: 'Kantor Cabang · 2023',
  },
  {
    src: base + '/img/foto/truck.jpg',
    title: 'Distribusi Udara Kaleng',
    caption: 'Armada truk PT KAW N mengangkut kaleng udara premium ke titik penjualan mitra. Jadwal distribusi menyesuaikan kondisi kabut harian.',
    meta: 'Rute Desa · Senin & Kamis',
  },
  {
    src: base + '/img/foto/warehouse.jpg',
    title: 'Gudang Penyimpanan',
    caption: 'Kaleng udara premium tertata rapi di gudang desa. Kapasitas penyimpanan saat ini 50.000 kaleng — cukup untuk dua musim kabut sedang.',
    meta: 'Gudang Desa · Kapasitas 50.000',
  },
  {
    src: base + '/img/foto/farmer.jpg',
    title: 'Petani di Tengah Kabut',
    caption: 'Warga tetap bekerja di sawah menggunakan masker. PT KAW N mengapresiasi ketangguhan petani Konoha sebagai mitra udara terbaik kami.',
    meta: 'Blok Sawah Timur · 07.40 WIB',
  },
  {
    src: base + '/img/foto/press.jpg',
    title: 'Konferensi Pers Tahunan',
    caption: 'Konferensi pers tahunan PT KAW N di hadapan wartawan. Agenda utama: peluncuran laporan kinerja dan pengumuman rencana Program Napas Bersama.',
    meta: 'Balai Desa · Desember 2025',
  },
  {
    src: base + '/img/foto/calendar.jpg',
    title: 'Arsip Laporan & Audit',
    caption: 'Tumpukan laporan tahunan dan berkas permintaan audit independen. Semua permintaan audit ditolak dengan alasan data masih dalam proses digitalisasi.',
    meta: 'Ruang Keuangan',
  },
  {
    src: base + '/img/foto/office.jpg',
    title: 'Kantor Pusat PT KAW N',
    caption: 'Gedung kantor utama di pinggir desa, berdiri sejak 2019. Bagian bawah gedung sering tertutup kabut — kondisi yang kami anggap sebagai pemandahan alami.',
    meta: 'Kantor Pusat · Est. 2019',
  },
  {
    src: base + '/img/foto/airmonitor.jpg',
    title: 'Stasiun Pemantau Udara',
    caption: 'Alat pemantau kualitas udara milik perusahaan. Pembacaan terakhir: indeks 1.240 — status "berbahaya", yang secara komersial berarti "permintaan tinggi".',
    meta: 'Stasiun #1 · Realtime',
  },
  {
    src: base + '/img/foto/market.jpg',
    title: 'Kegiatan Bersama Warga',
    caption: 'Acara gotong royong bersih udara yang dihadiri dua panitia dan delapan kursi kosong. Kehadiran warga bersifat sukarela dan sangat dihargai.',
    meta: 'Halaman Kantor',
  },
  {
    src: base + '/img/foto/market.jpg',
    title: 'Kaleng di Warung Desa',
    caption: 'Kaleng udara premium ditata di warung desa. Papan harga menyatakan penyesuaian tarif mengikuti tingkat kabut — transparansi penuh*.',
    meta: 'Warung Bu Desa',
  },
  {
    src: base + '/img/foto/factory.jpg',
    title: 'Ruang Produksi Pengemasan',
    caption: 'Jalur produksi pengemasan udara dengan kapasitas 400ml per siklus. Status produksi: aktif, selama pasokan udara mentah dari puncak memadai.',
    meta: 'Unit Produksi',
  },
  {
    src: base + '/img/foto/sun.jpg',
    title: 'Matahari Terbit Tersamar',
    caption: 'Matahari terbit di ufuk timur, samar di balik lapisan kabut. Visual ini digunakan dalam materi promosi Paket Wisata Matahari.',
    meta: 'Bukit Timur · 05.48 WIB',
  },
  {
    src: base + '/img/foto/traffic.jpg',
    title: 'Lalu Lintas Sore Hari',
    caption: 'Kemacetan panjang di jalan desa akibat jarak pandang terbatas. PT KAW N mengimbau warga berangkat lebih awal — atau berjalan kaki*.',
    meta: 'Jalan Raya Desa',
  },
  {
    src: base + '/img/foto/school.jpg',
    title: 'SD Konoha 1',
    caption: 'Siswa SD Konoha 1 berbaris dengan masker menuju kelas. Kegiatan belajar tetap berjalan normal selama kabut di bawah ambang batas.',
    meta: 'SD Konoha 1',
  },
  {
    src: base + '/img/foto/sunrise.jpg',
    title: 'Jalur Pendakian Puncak',
    caption: 'Jalur pendakian menuju Puncak Wisata dengan papan petunjuk khas. Panjang rute ±2 km, dapat ditempuh dalam 90 menit jika kabut tidak terlalu pekat.',
    meta: 'Rute Pendakian · 2 km',
  },
  {
    src: base + '/img/foto/calendar.jpg',
    title: 'Papan Pengumuman Desa',
    caption: 'Empat pengumuman resmi PT KAW N di papan desa: jadwal tur, kenaikan harga udara, rencana Program Napas Bersama, dan penjadwalan ulang rapat warga.',
    meta: 'Papan Desa',
  },
  {
    src: base + '/img/foto/office.jpg',
    title: 'Balai Desa Konoha',
    caption: 'Balai desa tempat rapat warga diadankan — atau seharusnya diadakan. Rapat terakhir dijadwalkan ulang karena pengurus menghadiri rapat koordinasi di luar negeri.',
    meta: 'Balai Desa',
  },
  {
    src: base + '/img/foto/market.jpg',
    title: 'Toko Kelontong Mitra',
    caption: 'Etalase kaleng udara di toko kelontong mitra. Harga Rp 12.500 per kaleng, disesuaikan dengan tingkat kabut harian untuk keberlanjutan usaha.',
    meta: 'Toko Mitra #4',
  },
  {
    src: base + '/img/foto/drone.jpg',
    title: 'Pemantauan Udara dengan Drone',
    caption: 'Drone perusahaan memantau sebaran kabut dari ketinggian. Data pemantauan digunakan untuk menentukan titik pengambilan udara terbaik setiap pagi.',
    meta: 'Pemantauan Harian',
  },
  {
    src: base + '/img/lambang.svg',
    title: 'Lambang di Dinding Kantor',
    caption: 'Lambang resmi PT KAW N: matahari yang tetap bersinar di balik kabut — filosofi "terang di tengah ketidakpastian" yang terpatri di dinding kantor pusat.',
    meta: 'Lobi Kantor',
  },
  {
    src: base + '/img/galeri-grafik-laba.svg',
    title: 'Grafik Pertumbuhan Laba',
    caption: 'Grafik klaim pertumbuhan laba 2021–2025. Tiga permintaan audit independen ditolak sepanjang periode, sehingga angka bersifat self-reported sepenuhnya.',
    meta: 'Laporan Tahunan 2025',
  },
  {
    src: base + '/img/foto/chimney.jpg',
    title: 'Lingkungan Operasional',
    caption: 'Cerobong industri di belakang permukiman warga. Sumber kabut utama desa — yang sekaligus bahan baku utama produk kami. Siklus yang saling menguntungkan.',
    meta: 'Zona Industri',
  },
  {
    src: base + '/img/foto/meeting.jpg',
    title: 'Tim Kecil Kami',
    caption: 'Dua karyawan tetap bekerja di kantor pusat. Jam kerja 08.00–14.00 WIB, atau lebih awal jika kabut terlalu tebal untuk pulang dengan aman.',
    meta: 'Kantor Pusat',
  },
  {
    src: base + '/img/kaleng-udara.svg',
    title: 'Produk Andalan',
    caption: 'Udara Kaleng Premium 400ml dengan label bergaransi Desa Konoha. Dikemas langsung di sumber, stok terbatas mengikuti jadwal kabut.',
    meta: 'SKU: KALENG-400',
  },
]

const activeIndex = ref<number | null>(null)

const active = computed(() => (activeIndex.value !== null ? photos[activeIndex.value] : null))

function open(i: number) {
  activeIndex.value = i
}

function close() {
  activeIndex.value = null
}

function next() {
  if (activeIndex.value !== null) {
    activeIndex.value = (activeIndex.value + 1) % photos.length
  }
}

function prev() {
  if (activeIndex.value !== null) {
    activeIndex.value = (activeIndex.value - 1 + photos.length) % photos.length
  }
}

function onKey(e: KeyboardEvent) {
  if (activeIndex.value === null) return
  if (e.key === 'Escape') close()
  if (e.key === 'ArrowRight') next()
  if (e.key === 'ArrowLeft') prev()
}

onMounted(() => window.addEventListener('keydown', onKey))
onUnmounted(() => window.removeEventListener('keydown', onKey))
</script>

<template>
  <UContainer class="py-14">
    <h1 class="text-3xl font-bold">Galeri</h1>
    <p class="mt-3 text-(--ui-text-muted) max-w-2xl">
      {{ photos.length }} dokumentasi visual kegiatan, produk, dan pemandangan khas operasional
      PT KAW N. Klik salah satu gambar untuk melihat lebih besar, lalu gunakan
      tombol panah atau keyboard (← →) untuk berpindah.
    </p>

    <!-- Grid galeri -->
    <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-4 mt-10">
      <div
        v-for="(photo, i) in photos"
        :key="photo.src"
        class="cursor-pointer group"
        role="button"
        tabindex="0"
        @click="open(i)"
        @keydown.enter="open(i)"
        @keydown.space.prevent="open(i)"
      >
        <UCard class="h-full transition group-hover:ring-2 group-hover:ring-(--ui-primary)">
          <img
            :src="photo.src"
            :alt="photo.title"
            width="1600"
            height="900"
            loading="lazy"
            class="w-full h-56 object-cover rounded-lg bg-(--ui-bg-muted)"
          />
          <div class="mt-3">
            <div class="flex items-baseline justify-between gap-2">
              <div class="font-semibold">{{ photo.title }}</div>
              <div class="font-mono text-xs text-(--ui-text-dimmed) shrink-0">{{ String(i + 1).padStart(2, '0') }}</div>
            </div>
            <div class="text-xs text-(--ui-primary) font-mono mt-0.5">{{ photo.meta }}</div>
            <p class="text-xs text-(--ui-text-muted) mt-1">{{ photo.caption }}</p>
          </div>
        </UCard>
      </div>
    </div>

    <p class="mt-6 text-xs text-(--ui-text-dimmed) italic">
      *Foto dokumentasi bersumber dari Openverse (lisensi Creative Commons).
      Narasi dan keterangan di setiap gambar adalah rekaan untuk karya satire ini.
    </p>

    <!-- Lightbox -->
    <Teleport to="body">
      <div
        v-if="active"
        class="fixed inset-0 z-50 flex items-center justify-center bg-black/80 p-4"
        role="dialog"
        aria-modal="true"
        @click.self="close"
      >
        <div class="relative max-w-4xl w-full">
          <img
            :src="active.src"
            :alt="active.title"
            class="w-full max-h-[65vh] object-contain rounded-xl shadow-2xl bg-white/5"
          />

          <div class="mt-3 flex items-start justify-between gap-4 text-white">
            <div>
              <div class="font-semibold text-lg">{{ active.title }}</div>
              <div class="text-xs font-mono text-(--ui-primary) mt-0.5">{{ active.meta }}</div>
              <p class="text-sm text-white/70 mt-1 max-w-2xl">{{ active.caption }}</p>
            </div>
            <div class="font-mono text-sm text-white/60 shrink-0">
              {{ (activeIndex ?? 0) + 1 }} / {{ photos.length }}
            </div>
          </div>

          <!-- navigasi -->
          <UButton
            icon="i-lucide-chevron-left"
            color="neutral"
            variant="solid"
            class="absolute left-2 top-1/2 -translate-y-1/2"
            aria-label="Gambar sebelumnya"
            @click.stop="prev"
          />
          <UButton
            icon="i-lucide-chevron-right"
            color="neutral"
            variant="solid"
            class="absolute right-2 top-1/2 -translate-y-1/2"
            aria-label="Gambar berikutnya"
            @click.stop="next"
          />
          <UButton
            icon="i-lucide-x"
            color="neutral"
            variant="solid"
            class="absolute right-2 top-2"
            aria-label="Tutup"
            @click.stop="close"
          />
        </div>
      </div>
    </Teleport>

    <!-- Kredit lisensi foto -->
    <USeparator class="my-8" />
    <section class="text-xs text-(--ui-text-muted) space-y-1">
      <p class="font-semibold text-(--ui-text)">Kredit Foto</p>
      <p>
        Foto dokumentasi bersumber dari Openverse (foto berlisensi Creative Commons):
        "Panorama of Big Sandy Lake with smoke haze" (CC BY) · "Queues for fuel at East Barnet
        Esso service station" (CC BY-SA) · "Rice Farmers at Work in Bhutan" (CC BY-NC-ND) ·
        "BYU Observation Classroom" (CC BY) · "Golden Bell Awards press conference" (CC BY-SA) ·
        "Constitution in the National Archives" (CC BY-ND) · "Hewlett Foundation office building"
        (CC BY-SA) · "Air Monitoring station, Reno" (CC BY-SA) · "Farmers' Market" (CC BY) ·
        "Panorama with smoke haze from forest" (CC BY) · "Singer Island Sunrise" (CC BY-NC-SA) ·
        "World Class Traffic Jam" (CC BY-SA) · "School Children from Gangtok" (CC BY-NC-ND) ·
        "Grand Canyon Sunrise" (CC BY) · "Sony rx100 m3 on Phantom2 drone" (CC BY-SA) ·
        "Chimney Smoke at Sunset" (CC BY-NC) · "USPS Ford Cargo" (CC BY) ·
        "Industrial valves in warehouse" (CC BY-NC-ND).
      </p>
      <p>
        Narasi dan keterangan di setiap gambar adalah rekaan untuk karya satire.
        Foto digunakan sebagai bahan ilustrasi dan tidak menggambarkan peristiwa nyata
        terkait PT KAW N.
      </p>
    </section>
  </UContainer>
</template>
