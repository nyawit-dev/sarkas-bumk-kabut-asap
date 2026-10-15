<script setup lang="ts">
useHead({
  title: 'Tentang Kami — PT Kabut Asap & Wisata Napas',
})

const base = '/sarkas-bumk-kabut-asap'

const visi = 'Menjadikan kabut sebagai sumber daya strategis Desa Konoha yang berkelanjutan, transparan*, dan menguntungkan.'

const misi = [
  'Mengemas setiap butir udara dengan standar premium desa.',
  'Mengembangkan wisata matahari sebagai komoditas eksklusif musiman.',
  'Menyediakan fasilitas rapat luar negeri bagi pengurus yang membutuhkan jarak pandang jelas.',
  'Merencanakan Program Napas Bersama untuk seluruh warga pada 2031.',
]

const timeline = [
  {
    year: '2019',
    title: 'Pendirian',
    desc: 'PT KAW N didirikan oleh kepala desa bersama tiga pengurus dengan modal awal Rp 50 juta dari kas desa. Fokus awal: mengelola titik pemandangan puncak.',
  },
  {
    year: '2020',
    title: 'Musim Kabut Pertama',
    desc: 'Kabut terparah sejak dekade lalu justru membuka peluang: udara desa mulai diminati sebagai komoditas kemasan.',
  },
  {
    year: '2021',
    title: 'Produk Pertama',
    desc: 'Udara Kaleng Premium diluncurkan dengan harga Rp 12.500. 40.000 kaleng terjual dalam tiga bulan — rekor penjualan kemasan udara di wilayah kami*.',
  },
  {
    year: '2022',
    title: 'Ekspansi Wisata',
    desc: 'Paket Wisata Matahari dibuka. Kuota 40 orang/hari habis dalam 48 jam setiap kali dibuka, mendorong pengembangan titik pandang kedua.',
  },
  {
    year: '2023',
    title: 'Kantor Cabang Luar Negeri',
    desc: 'Kantor koordinasi di luar negeri diresmikan "untuk memantau praktik terbaik pengelolaan kabut". Biaya operasional tercatat sebagai investasi strategis.',
  },
  {
    year: '2024',
    title: 'Penolakan Audit',
    desc: 'Permintaan audit independen kedua ditolak oleh pengurus dengan alasan "data masih dalam proses digitalisasi".',
  },
  {
    year: '2025',
    title: 'Ekosistem Napas',
    desc: 'Program Napas Bersama diumumkan dalam rapat tahunan. Pelaksanaan ditargetkan 2031 setelah prioritas pembangunan lini usaha lain selesai.',
  },
]

const org = [
  { name: 'Direktur Utama', desc: 'Memimpin arah strategis perusahaan dan mewakili PT KAW N dalam setiap rapat, di mana pun lokasinya.', icon: 'i-lucide-user-round' },
  { name: 'Kepala Divisi Udara', desc: 'Bertanggung jawab atas pengemasan, kualitas, dan distribusi udara kaleng.', icon: 'i-lucide-wind' },
  { name: 'Manajer Pemasaran', desc: 'Mengelola citra merek, kampanye "udara segar untuk semua*", dan kuota penjualan harian.', icon: 'i-lucide-megaphone' },
  { name: 'Kepala Keuangan', desc: 'Mengelola arus kas, anggaran rapat, dan penolakan permintaan audit independen.', icon: 'i-lucide-calculator' },
  { name: 'Koordinator Wisata', desc: 'Menjadwalkan tur matahari dan memastikan setiap peserta mendapat pengalaman berkabut bintang lima.', icon: 'i-lucide-mountain' },
  { name: 'Staf Administrasi', desc: 'Mengelola kuesioner kesehatan, arsip digitalisasi data, dan surat-menyurat desa.', icon: 'i-lucide-clipboard-list' },
]
</script>

<template>
  <UContainer class="py-14">
    <div class="grid lg:grid-cols-[1fr_320px] gap-10">
      <div>
        <h1 class="text-3xl font-bold">Tentang Kami</h1>
        <p class="mt-3 text-(--ui-text-muted) max-w-2xl">
          PT Kabut Asap &amp; Wisata Napas (PT KAW N) adalah Badan Usaha Milik Desa
          yang beroperasi sejak 2019 di Desa Konoha. Kami mengelola komoditas
          kabut, udara, dan matahari sebagai sumber daya ekonomi desa.
        </p>

        <!-- Visi Misi -->
        <section class="mt-10">
          <h2 class="text-2xl font-bold mb-4">Visi &amp; Misi</h2>
          <UCard>
            <h3 class="font-semibold">Visi</h3>
            <p class="mt-1 text-(--ui-text-muted)">{{ visi }}</p>
            <USeparator class="my-4" />
            <h3 class="font-semibold">Misi</h3>
            <ul class="mt-2 space-y-2">
              <li v-for="m in misi" :key="m" class="flex items-start gap-2 text-sm text-(--ui-text-muted)">
                <UIcon name="i-lucide-check" class="size-4 text-(--ui-success) mt-0.5 shrink-0" />
                {{ m }}
              </li>
            </ul>
          </UCard>
        </section>

        <!-- Sejarah -->
        <section class="mt-12">
          <h2 class="text-2xl font-bold mb-6">Sejarah Singkat</h2>
          <ol class="relative border-l-2 border-(--ui-primary)/40 ml-4 space-y-8">
            <li v-for="item in timeline" :key="item.year" class="pl-6 relative">
              <span class="absolute -left-[9px] top-1 size-4 rounded-full bg-(--ui-primary) ring-4 ring-(--ui-bg)" />
              <div class="font-mono font-bold text-(--ui-primary)">{{ item.year }}</div>
              <div class="font-semibold mt-1">{{ item.title }}</div>
              <p class="text-sm text-(--ui-text-muted) mt-1">{{ item.desc }}</p>
            </li>
          </ol>
        </section>
      </div>

      <!-- Sidebar gambar -->
      <aside class="space-y-4">
        <UCard>
          <img
            :src="base + '/img/lambang.svg'"
            alt="Lambang resmi PT KAW N"
            width="400"
            height="400"
            class="w-full rounded-lg"
          />
          <div class="mt-2 text-center text-sm font-semibold">Lambang Resmi</div>
          <p class="text-xs text-(--ui-text-muted) text-center mt-1">Matahari bersinar di balik kabut.</p>
        </UCard>
        <UCard>
          <img
            :src="base + '/img/hero-haze.svg'"
            alt="Pemandangan Desa Konoha diterja kabut"
            width="1600"
            height="900"
            class="w-full rounded-lg"
          />
          <div class="mt-2 text-sm font-semibold">Zona Operasional</div>
          <p class="text-xs text-(--ui-text-muted) mt-1">Hamparan sawah dan pemukiman di bawah kabut pagi.</p>
        </UCard>
        <UCard>
          <img
            :src="base + '/img/galeri-kantor.svg'"
            alt="Kantor pusat PT KAW N"
            width="1600"
            height="900"
            class="w-full rounded-lg"
          />
          <div class="mt-2 text-sm font-semibold">Kantor Pusat</div>
          <p class="text-xs text-(--ui-text-muted) mt-1">Gedung utama operasional sejak 2019.</p>
        </UCard>
        <UCard>
          <img
            :src="base + '/img/galeri-karyawan.svg'"
            alt="Karyawan PT KAW N di kantor"
            width="1600"
            height="900"
            class="w-full rounded-lg"
          />
          <div class="mt-2 text-sm font-semibold">Tim Kami</div>
          <p class="text-xs text-(--ui-text-muted) mt-1">Dua karyawan tetap di kantor pusat.</p>
        </UCard>
        <UCard>
          <img
            :src="base + '/img/galeri-stasiun-udara.svg'"
            alt="Stasiun pemantau kualitas udara"
            width="1600"
            height="900"
            class="w-full rounded-lg"
          />
          <div class="mt-2 text-sm font-semibold">Stasiun Pemantau</div>
          <p class="text-xs text-(--ui-text-muted) mt-1">Indeks udara terkini: 1.240 (berbahaya).</p>
        </UCard>
        <UButton label="Lihat semua 26 gambar di Galeri" to="/galeri" variant="outline" block />
      </aside>
    </div>

    <!-- Struktur Organisasi -->
    <section class="mt-16">
      <h2 class="text-2xl font-bold mb-6">Struktur Pengurus</h2>
      <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-4">
        <UCard v-for="o in org" :key="o.name">
          <div class="flex items-center gap-3">
            <div class="size-10 rounded-full bg-(--ui-primary)/10 flex items-center justify-center shrink-0">
              <UIcon :name="o.icon" class="size-5 text-(--ui-primary)" />
            </div>
            <div class="font-semibold">{{ o.name }}</div>
          </div>
          <p class="mt-2 text-sm text-(--ui-text-muted)">{{ o.desc }}</p>
        </UCard>
      </div>
      <p class="mt-4 text-xs text-(--ui-text-dimmed)">
        *Nama dan jababan pengurus bersifat rekaan. Tidak ada individu nyata yang digambarkan.
      </p>
    </section>

    <p class="mt-10 text-xs text-(--ui-text-muted)">
      *Transparansi dan "udara segar untuk semua" adalah klaim internal perusahaan.
      Seluruh isi halaman ini adalah rekaan untuk karya satire.
    </p>
  </UContainer>
</template>
