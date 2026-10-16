<script setup lang="ts">
useHead({ title: "Layanan — PT Kabut Asap & Wisata Napas" })

const services = [
  {
    title: "Pengemasan Udara",
    desc: "Udara desa dikemas ke dalam kaleng 400ml dengan label premium. Stok terbatas mengikuti jadwal kabut.",
    price: "Mulai Rp 12.500",
    features: ["Kaleng aluminium daur ulang*", "Sertifikat keaslian desa", "Tanpa pengawet"],
    specs: [
      { k: "Volume", v: "400 ml" },
      { k: "Kandungan", v: "Udara desa 99,9%*" },
      { k: "Umur simpan", v: "Sampai kabut turun lagi" },
      { k: "Sertifikasi", v: "Label bergaransi desa" },
    ],
  },
  {
    title: "Tur Kabut & Matahari",
    desc: "Paket wisata melihat matahari terbit dari titik tertinggi desa. Termasuk transportasi, pemandu, dan selimut.",
    price: "Mulai Rp 890.000",
    features: ["Jadwal subuh", "Pemandu bersertifikat", "Opsi camping"],
    specs: [
      { k: "Titik kumpul", v: "Pukul 03.00 WIB" },
      { k: "Durasi", v: "4–6 jam (tergantung jarak pandang)" },
      { k: "Kuota", v: "40 orang/hari" },
      { k: "Jaminan", v: "Matahari terbit atau uang kembali*" },
    ],
  },
  {
    title: "Rapat Koordinasi Luar Negeri",
    desc: "Fasilitas rapat darurat di luar negeri untuk pengurus. Termasuk akomodasi bintang lima dan penerbangan langsung.",
    price: "Rp 43.000.000/malam",
    features: ["Akses lounge bandara", "Penerbangan pagi hari", "Bebas jadwal kabut"],
    specs: [
      { k: "Peserta", v: "Maks. 8 pengurus" },
      { k: "Agenda", v: "Evaluasi kabut + kerja sama" },
      { k: "Termasuk", v: "Kamar, sarapan, penerbangan" },
      { k: "Frekuensi", v: "Sesuai kebutuhan kabut" },
    ],
  },
  {
    title: "Rehabilitasi Napas",
    desc: "Program penggantian napas untuk warga terdampak. Tahap perencanaan; pelaksanaan menunggu anggaran berikutnya.",
    price: "Rp 0 (rencana)",
    features: ["Kuesioner kesehatan", "Rujukan rumah sakit", "Estimasi pelaksanaan: 2031"],
    specs: [
      { k: "Sasaran", v: "Seluruh warga terdampak" },
      { k: "Status", v: "Perencanaan" },
      { k: "Anggaran", v: "Menunggu prioritas" },
      { k: "Target", v: "2031" },
    ],
  },
]

const faqs = [
  { q: "Apakah udara kaleng benar-benar dari Desa Konoha?", a: "Ya — dikemas di Puncak Wisata, tepat sebelum kabut turun menutupi titik pengemasan. Setiap kaleng membawa label bergaransi desa." },
  { q: "Bagaimana jika matahari tidak terbit saat tur?", a: "Peserta tetap menerima pengalaman berkabut bintang lima* dan voucher ulang tahun. Pengembalian dana tidak berlaku untuk cuaca." },
  { q: "Kenapa rapat koordinasi harus di luar negeri?", a: "Karena di dalam negeri kabut sering menghalangi visibilitas rapat. Di luar negeri, jarak pandang mendukung produktivitas pengurus." },
  { q: "Kapan Program Napas Bersama dimulai?", a: "Saat ini dalam tahap perencanaan. Estimasi pelaksanaan 2031, bergantung pada ketersediaan anggaran setelah pengembangan lini usaha lain." },
]
</script>

<template>
  <UContainer class="py-14">
    <h1 class="text-3xl font-bold">Layanan Kami</h1>
    <p class="mt-3 text-(--ui-text-muted) max-w-2xl">
      Empat lini usaha utama PT KAW N, dirancang untuk memaksimalkan nilai
      setiap butir udara dan setiap momen kabut.
    </p>

    <div class="grid md:grid-cols-2 gap-6 mt-10">
      <UCard v-for="service in services" :key="service.title">
        <div class="flex items-start gap-4">
          <div class="size-12 rounded-full bg-(--ui-primary)/10 flex items-center justify-center shrink-0">
            <UIcon :name="service.title === 'Pengemasan Udara' ? 'i-lucide-wind' : service.title === 'Tur Kabut & Matahari' ? 'i-lucide-mountain-snow' : service.title === 'Rapat Koordinasi Luar Negeri' ? 'i-lucide-plane' : 'i-lucide-sprout'" class="size-6 text-(--ui-primary)" />
          </div>
          <div class="flex-1">
            <h2 class="text-lg font-semibold">{{ service.title }}</h2>
            <p class="mt-1 text-sm text-(--ui-text-muted)">{{ service.desc }}</p>
            <ul class="mt-3 space-y-1">
              <li v-for="f in service.features" :key="f" class="flex items-center gap-2 text-sm">
                <UIcon name="i-lucide-check" class="size-4 text-(--ui-success)" />
                {{ f }}
              </li>
            </ul>
            <div class="mt-4 font-mono font-bold text-(--ui-primary)">{{ service.price }}</div>
          </div>
        </div>

        <dl class="mt-4 grid grid-cols-2 gap-x-4 gap-y-2 text-sm">
          <template v-for="spec in service.specs" :key="spec.k">
            <dt class="text-(--ui-text-muted)">{{ spec.k }}</dt>
            <dd class="mono font-mono text-right">{{ spec.v }}</dd>
          </template>
        </dl>
      </UCard>
    </div>

    <p class="mt-8 text-xs text-(--ui-text-muted)">
      *Kaleng daur ulang dari kaleng udara yang sudah habis. Daur ulang dilakukan
      oleh pihak ketiga; jaminan mutul belum tersedia. Kandungan udara sesuai
      pengukuran internal kami.
    </p>

    <!-- FAQ -->
    <section class="mt-16">
      <h2 class="text-2xl font-bold mb-6">Pertanyaan yang Sering Diajukan</h2>
      <UAccordion :items="faqs" class="max-w-3xl">
        <template #body="{ item }">
          <p class="text-(--ui-text-muted) px-1 pb-2">{{ item.a }}</p>
        </template>
      </UAccordion>
    </section>
  </UContainer>
</template>
