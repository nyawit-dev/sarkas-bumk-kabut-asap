<script setup lang="ts">
useHead({
  title: 'Layanan — PT Kabut Asap & Wisata Napas',
})

const services = [
  {
    icon: 'i-lucide-wind',
    title: 'Pengemasan Udara',
    desc: 'Udara desa dikemas ke dalam kaleng 400ml dengan label premium. Stok terbatas mengikuti jadwal kabut.',
    price: 'Mulai Rp 12.500',
    features: ['Kaleng aluminium daur ulang*', 'Sertifikat keaslian desa', 'Tanpa pengawet'],
  },
  {
    icon: 'i-lucide-mountain-snow',
    title: 'Tur Kabut & Matahari',
    desc: 'Paket wisata melihat matahari terbit dari titik tertinggi desa. Termasuk transportasi, pemandu, dan selimut.',
    price: 'Mulai Rp 890.000',
    features: ['Jadwal subuh', 'Pemandu bersertifikat', 'Opsi camping'],
  },
  {
    icon: 'i-lucide-plane',
    title: 'Rapat Koordinasi Luar Negeri',
    desc: 'Fasilitas rapat darurat di luar negeri untuk pengurus. Termasuk akomodasi bintang lima dan penerbangan langsung.',
    price: 'Rp 43.000.000/malam',
    features: ['Akses lounge bandara', 'Penerbangan pagi hari', 'Bebas jadwal kabut'],
  },
  {
    icon: 'i-lucide-sprout',
    title: 'Rehabilitasi Napas',
    desc: 'Program penggantian napas untuk warga terdampak. Tahap perencanaan; pelaksanaan menunggu anggaran berikutnya.',
    price: 'Rp 0 (rencana)',
    features: ['Kuesioner kesehatan', 'Rujukan rumah sakit', 'Estimasi pelaksanaan: 2031'],
  },
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
          <UIcon :name="service.icon" class="size-10 text-(--ui-primary) shrink-0" />
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
      </UCard>
    </div>

    <p class="mt-8 text-xs text-(--ui-text-muted)">
      *Kaleng daur ulang dari kaleng udara yang sudah habis. Daur ulang dilakukan
      oleh pihak ketiga; jaminan mutul belum tersedia.
    </p>
  </UContainer>
</template>
