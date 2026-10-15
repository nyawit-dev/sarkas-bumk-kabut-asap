<script setup lang="ts">
useHead({
  title: 'PT Kabut Asap & Wisata Napas — BUMK Desa Konoha',
})

const stats = [
  { label: 'Kaleng Udara Terjual', value: '1.240.000', suffix: 'kaleng' },
  { label: 'Tingkat Kejernihan Desa', value: '94', suffix: ' %*' },
  { label: 'Kantor Cabang', value: '1', suffix: ' di luar negeri' },
  { label: 'Audit Independen', value: '3', suffix: ' kali ditolak' },
]

const products = [
  {
    icon: 'i-lucide-wind',
    title: 'Udara Kaleng Premium',
    price: 'Rp 12.500',
    unit: '/ kaleng 400ml',
    desc: 'Dikemas langsung di sumber, tepat sebelum sumbernya ditutup kabut. Segar, asli, terbatas.',
  },
  {
    icon: 'i-lucide-sunrise',
    title: 'Paket Wisata Matahari',
    price: 'Rp 890.000',
    unit: '/ orang',
    desc: 'Saksikan matahari tanpa filter kabut. Pendakian dimulai pukul 03.00, matahari dijamin terbit*.',
  },
  {
    icon: 'i-lucide-building-2',
    title: 'Kamar Rapat di Luar Negeri',
    price: 'Rp 43.000.000',
    unit: '/ malam',
    desc: 'Rapat koordinasi darurat penanganan kabut. Akses cepat ke bandara, bebas antre, bebas kabut.',
  },
  {
    icon: 'i-lucide-heart-handshake',
    title: 'Program Napas Bersama',
    price: 'Rp 0',
    unit: '/ pernapas',
    desc: 'Setiap warga berhak bernapas. Kuota harian terbatas; sistem antrean digital sedang dikembangkan.',
  },
]

const quotes = [
  {
    text: 'Kabut bukan masalah, kabut adalah cakrawala baru kami.',
    role: 'Direktur Utama, pidato tahunan',
  },
  {
    text: 'Kami tidak menutup akses udara, kami mengoptimalkan pengalaman bernapas.',
    role: 'Kepala Divisi Udara',
  },
  {
    text: 'Warga tidak rugi — mereka justru mendapat udara segar dalam kemasan.',
    role: 'Manajer Pemasaran',
  },
]
</script>

<template>
  <div>
    <!-- Hero -->
    <section class="sarkas-hero">
      <UContainer class="py-16 sm:py-24">
        <div class="max-w-2xl">
          <UBadge color="warning" variant="subtle" size="lg" class="mb-4">
            BUMK • Didirikan 2019
          </UBadge>
          <h1 class="text-4xl sm:text-5xl font-bold leading-tight">
            Kabut bukan masalah.
            <span class="text-(--ui-primary)">Kabut adalah produk.</span>
          </h1>
          <p class="mt-6 text-lg text-(--ui-text-muted)">
            PT Kabut Asap &amp; Wisata Napas (PT KAW N) adalah Badan Usaha Milik Desa (BUMK)
            yang mengelola komoditas paling melimpah di Konoha: udara berwarna,
            jarak pandang rendah, dan kesempatan bisnis di tengahnya.
          </p>
          <div class="mt-8 flex flex-wrap gap-3">
            <UButton label="Lihat Layanan" to="/layanan" size="lg" />
            <UButton label="Baca Laporan Kinerja" to="/laporan" size="lg" variant="outline" />
          </div>
        </div>
      </UContainer>
    </section>

    <!-- Statistik self-reported -->
    <UContainer class="py-10">
      <UCard>
        <div class="grid grid-cols-2 lg:grid-cols-4 gap-6 text-center">
          <div v-for="stat in stats" :key="stat.label">
            <div class="text-3xl sm:text-4xl font-bold font-mono tabular-nums text-(--ui-primary)">
              {{ stat.value }}<span class="text-base font-normal text-(--ui-text-muted)">{{ stat.suffix }}</span>
            </div>
            <div class="mt-1 text-sm text-(--ui-text-muted) sarkas-claim inline-block pb-1">
              {{ stat.label }}
            </div>
          </div>
        </div>
        <p class="mt-6 text-xs text-(--ui-text-muted)">
          *Angka di atas adalah klaim internal perusahaan, belum diaudit badan independen mana pun.
        </p>
      </UCard>
    </UContainer>

    <!-- Produk -->
    <UContainer class="py-10">
      <h2 class="text-2xl font-bold mb-6">Produk &amp; Layanan Unggulan</h2>
      <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-4">
        <UCard v-for="product in products" :key="product.title" class="flex flex-col">
          <UIcon :name="product.icon" class="size-8 text-(--ui-primary) mb-3" />
          <h3 class="font-semibold">{{ product.title }}</h3>
          <p class="mt-2 text-sm text-(--ui-text-muted) flex-1">{{ product.desc }}</p>
          <div class="mt-4 pt-3 border-t border-(--ui-border)">
            <span class="font-mono font-bold">{{ product.price }}</span>
            <span class="text-xs text-(--ui-text-muted) ml-1">{{ product.unit }}</span>
          </div>
        </UCard>
      </div>
    </UContainer>

    <!-- Kutipan -->
    <section class="bg-(--ui-bg-elevated)/50">
      <UContainer class="py-14">
        <h2 class="text-2xl font-bold mb-8">Kata Pengurus</h2>
        <div class="grid md:grid-cols-3 gap-6">
          <blockquote v-for="quote in quotes" :key="quote.text" class="border-l-4 border-(--ui-primary) pl-4">
            <p class="italic">"{{ quote.text }}"</p>
            <footer class="mt-2 text-sm text-(--ui-text-muted)">— {{ quote.role }}</footer>
          </blockquote>
        </div>
      </UContainer>
    </section>

    <!-- CTA Generator -->
    <UContainer class="py-14">
      <UCard class="text-center">
        <h2 class="text-2xl font-bold">Ingin mendirikan BUMK sendiri?</h2>
        <p class="mt-2 text-(--ui-text-muted)">
          Gunakan Generator BUMK untuk menyusun nama, produk, dan laporan kinerja usaha milik desamu.
        </p>
        <UButton label="Buka Generator" to="/generator" size="lg" class="mt-6" />
      </UCard>
    </UContainer>
  </div>
</template>
