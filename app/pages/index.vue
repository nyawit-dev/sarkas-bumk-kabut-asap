<script setup lang="ts">
useHead({ title: "PT Kabut Asap & Wisata Napas — BUMK Desa Konoha" })

const stats = [
  { label: "Kaleng Udara Terjual", value: "1.240.000", suffix: " kaleng", note: "internal" },
  { label: "Tingkat Kejernihan Desa", value: "94", suffix: " %*", note: ""},
  { label: "Kantor Cabang", value: "1", suffix: " di luar negeri", note: ""},
  { label: "Audit Independen", value: "3", suffix: " kali ditolak", note: ""},
]

const timeline = [
  { year: "2019", title: "Pendirian", desc: "Berdiri dengan modal awal Rp 50 juta dari kas desa, dikelola langsung oleh tiga pengurus." },
  { year: "2021", title: "Produk Pertama", desc: "Meluncurkan Udara Kaleng Premium. 40.000 kaleng terjual dalam tiga bulan pertama." },
  { year: "2022", title: "Ekspansi Wisata", desc: "Paket Wisata Matahari diluncurkan. Kuota habis dalam 48 jam setiap kali dibuka." },
  { year: "2023", title: "Kantor Cabang", desc: "Membuka kantor koordinasi di luar negeri untuk \"memantau praktik terbaik pengelolaan kabut\"." },
  { year: "2025", title: "Ekosistem Napas", desc: "Merencanakan Program Napas Bersama. Pelaksanaan ditargetkan 2031." },
]

const products = [
  { icon: "i-lucide-wind", title: "Udara Kaleng Premium", price: "Rp 12.500", unit: "/ kaleng 400ml", desc: "Dikemas langsung di sumber, tepat sebelum sumbernya ditutup kabut. Segar, asli, terbatas." },
  { icon: "i-lucide-sunrise", title: "Paket Wisata Matahari", price: "Rp 890.000", unit: "/ orang", desc: "Saksikan matahari tanpa filter kabut. Pendakian dimulai pukul 03.00, matahari dijamin terbit*." },
  { icon: "i-lucide-building-2", title: "Kamar Rapat di Luar Negeri", price: "Rp 43.000.000", unit: "/ malam", desc: "Rapat koordinasi darurat penanganan kabut. Akses cepat ke bandara, bebas antre, bebas kabut." },
  { icon: "i-lucide-heart-handshake", title: "Program Napas Bersama", price: "Rp 0", unit: "/ pernapas", desc: "Setiap warga berhak bernapas. Kuota harian terbatas; sistem antrean digital sedang dikembangkan." },
]

const quotes = [
  { text: "Kabut bukan masalah, kabut adalah cakrawala baru kami.", role: "Direktur Utama, pidato tahunan" },
  { text: "Kami tidak menutup akses udara, kami mengoptimalkan pengalaman bernapas.", role: "Kepala Divisi Udara" },
  { text: "Warga tidak rugi — mereka justru mendapat udara segar dalam kemasan.", role: "Manajer Pemasaran" },
]

// ── Antislop: header corporate, no images ────────────────────────────
</script>

<template>
  <div class="deck">
    <!-- Hero full-bleed ────────────────────────────────────────────── -->
    <section class="hero-clean">
      <UContainer class="py-16 sm:py-22">
        <div class="grid lg:grid-cols-2 gap-10 items-center">
          <div>
            <div class="topline">
              <span class="kicker">PT KAW N — Desa Konoha, Kaltim</span>
              <span class="header-clock">Siang · 06.12 WIB · Kabut ketebalan 12 m</span>
            </div>
            <h1 class="mt-6">
              Kabut bukan masalah.
              <span class="text-(--ui-primary)">Kabut adalah produk.</span>
            </h1>
            <p class="mt-6 text-base text-(--ui-text-muted)">
              PT Kabut Asap &amp; Wisata Napas (PT KAW N) adalah Badan Usaha Milik Desa (BUMK)
              yang mengelola komoditas paling melimpah di Konoha: udara berwarna,
              jarak pandang rendah, dan kesempatan bisnis di tengahnya.
            </p>
            <div class="mt-8 flex flex-wrap gap-3">
              <UButton label="Lihat Layanan" to="/layanan" size="lg" />
              <UButton label="Baca Laporan Kinerja" to="/laporan" size="lg" variant="outline" />
            </div>
          </div>
        </div>
      </UContainer>
    </section>

    <!-- Stat strip ─────────────────────────────────────────────────── -->
    <UContainer class="py-10">
      <UCard>
        <div class="stats-grid">
          <div v-for="stat in stats" :key="stat.label">
            <dt>{{ stat.label }}</dt>
            <dd class="mono font-mono tabular-nums">
              {{ stat.value }}<span class="text-base font-normal text-(--ui-text-muted)">{{ stat.suffix }}</span>
            </dd>
          </div>
        </div>
        <p class="mt-6 text-xs text-(--ui-text-muted)">
          *Angka di atas adalah klaim internal perusahaan, belum diaudit badan independen mana pun.
        </p>
      </UCard>
    </UContainer>

    <!-- Produk & Layanan Unggulan ───────────────────────────────────── -->
    <UContainer class="py-10">
      <h2 class="text-2xl font-bold mb-6">Produk &amp; Layanan Unggulan</h2>
      <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-4">
        <UCard v-for="product in products" :key="product.title" class="flex flex-col">
          <div class="flex items-center gap-3 mb-3">
            <UIcon :name="product.icon" class="size-6 text-(--ui-primary)" />
            <span class="text-xs uppercase tracking-widest text-(--ui-text-muted)">{{ product.title }}</span>
          </div>
          <p class="text-sm text-(--ui-text-muted) flex-1">{{ product.desc }}</p>
          <div class="mt-4 pt-3 border-t border-(--ui-border) flex justify-between items-center">
            <span class="font-mono font-bold">{{ product.price }}</span>
            <span class="text-xs text-(--ui-text-muted)">{{ product.unit }}</span>
          </div>
        </UCard>
      </div>

      <!-- Produk andalan ────────────────────────────────────────────── -->
      <UCard class="mt-6">
        <div class="grid md:grid-cols-[220px_1fr] gap-6 items-center">
          <!-- Logo mark, text-based seal ─────────────────────────────── -->
          <div class="flex items-center justify-center py-8">
            <div class="w-24 h-24 rounded-full border-2 border-(--ui-primary) flex items-center justify-center text-[clamp(1.4rem,4vw,2.4rem)] font-bold font-mono text-(--ui-primary) shadow-lg">
              PT KAW N
            </div>
          </div>
          <div>
            <h3 class="text-xl font-bold">Produk Andalan: Udara Kaleng Premium</h3>
            <p class="mt-2 text-(--ui-text-muted)">
              Dikemas langsung di titik pemandangan terbaik desa, sebelum kabut turun.
              Tersedia dalam kemasan 400ml dengan label bergaransi Desa Konoha.
              Stok mengikuti jadwal kabut — tidak ada jaminan ketersediaan besok.
            </p>
            <dl class="mt-4 grid grid-cols-2 gap-2 text-sm">
              <div><dt class="text-(--ui-text-muted)">Volume</dt><dd class="mono font-mono font-semibold">400 ml</dd></div>
              <div><dt class="text-(--ui-text-muted)">Sumber</dt><dd class="mono font-mono font-semibold">Puncak Wisata</dd></div>
              <div><dt class="text-(--ui-text-muted)">Harga</dt><dd class="mono font-mono font-semibold">Rp 12.500</dd></div>
              <div><dt class="text-(--ui-text-muted)">Garansi</dt><dd class="mono font-mono font-semibold">Segar sampai rumah*</dd></div>
            </dl>
            <p class="mt-3 text-xs text-(--ui-text-dimmed)">
              *Garansi berlaku selama kaleng belum dibuka dan kabut belum menguap.
            </p>
          </div>
        </div>
      </UCard>
    </UContainer>

    <!-- Timeline singkat ────────────────────────────────────────────── -->
    <section class="bg-(--ui-bg-elevated)/50">
      <UContainer class="py-14">
        <h2 class="text-2xl font-bold mb-8">Perjalanan Kami</h2>
        <div class="max-w-2xl">
          <ol class="relative border-l-2 border-(--ui-primary)/40 ml-4 space-y-8">
            <li v-for="item in timeline" :key="item.year" class="pl-6 relative">
              <span class="absolute -left-[10px] top-1 size-4 rounded-full bg-(--ui-primary) ring-4 ring-(--ui-bg)" />
              <div class="mono font-mono font-bold">{{ item.year }}</div>
              <div class="font-bold">{{ item.title }}</div>
              <p class="text-sm text-(--ui-text-muted) mt-1">{{ item.desc }}</p>
            </li>
          </ol>
          <UButton label="Selengkapnya: Tentang Kami" to="/tentang" variant="link" class="mt-6" />
        </div>
      </UContainer>
    </section>

    <!-- Kutipan ─────────────────────────────────────────────────────── -->
    <UContainer class="py-14">
      <h2 class="text-2xl font-bold mb-8">Kata Pengurus</h2>
      <div class="grid md:grid-cols-3 gap-6">
        <blockquote v-for="quote in quotes" :key="quote.text" class="border-l-4 border-(--ui-primary) pl-4">
          <p class="italic">"{{ quote.text }}"</p>
          <footer class="mt-2 text-sm text-(--ui-text-muted)">— {{ quote.role }}</footer>
        </blockquote>
      </div>
    </UContainer>

    <!-- Sertifikasi ─────────────────────────────────────────────────── -->
    <UContainer class="pb-14">
      <div class="cert-row">
        <span class="cert-badge">
          <svg viewBox="0 0 24 24"><path d="M12 2L15.09 8.26L22 9.27L17 14.14L18.18 21.02L12 17.77L5.82 21.02L7 14.14L2 9.27L8.91 8.26L12 2Z"/></svg>
          Lisensi 04-2024
        </span>
        <span class="cert-badge">
          <svg viewBox="0 0 24 24"><path d="M12 2L15.09 8.26L22 9.27L17 14.14L18.18 21.02L12 17.77L5.82 21.02L7 14.14L2 9.27L8.91 8.26L12 2Z"/></svg>
          ISO 9001:2023
        </span>
        <span class="cert-badge">
          <svg viewBox="0 0 24 24"><path d="M12 2L15.09 8.26L22 9.27L17 14.14L18.18 21.02L12 17.77L5.82 21.02L7 14.14L2 9.27L8.91 8.26L12 2Z"/></svg>
          Skualifikasi Desa
        </span>
        <span class="cert-badge">
          <svg viewBox="0 0 24 24"><path d="M12 2L15.09 8.26L22 9.27L17 14.14L18.18 21.02L12 17.77L5.82 21.02L7 14.14L2 9.27L8.91 8.26L12 2Z"/></svg>
          Aman &amp; Sehat
        </span>
      </div>
    </UContainer>

    <!-- CTA Generator ───────────────────────────────────────────────── -->
    <UContainer class="pb-14">
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
