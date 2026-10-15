<script setup lang="ts">
useHead({
  title: 'Generator BUMK — PT Kabut Asap & Wisata Napas',
})

const prefixes = ['Kabut', 'Asap', 'Udara', 'Napas', 'Kabut Asap', 'Sebar', 'Jarak Pandang', 'Langit']
const cores = ['Emas', 'Sejuk', 'Tinggi', 'Jernih', 'Bersih', 'Terbatas', 'Premium', 'Aspal']
const sectors = ['Wisata', 'Pengemasan', 'Katering', 'Transportasi', 'Real Estet', 'Energi', 'Kesehatan Napas']
const taglines = [
  'Bersama menapaki hari yang tak terlihat.',
  'Dari desa, untuk udara yang lebih baik.',
  'Melayani dengan napas penuh.',
  'Terang di tengah ketidakpastian.',
  'Mitra napas keluarga Indonesia.',
  'Melangkah bersama menuju cakrawala baru.',
]

const state = reactive({
  prefix: '',
  core: '',
  sector: '',
  tagline: '',
})

const fullName = computed(() => {
  const p = state.prefix || pick(prefixes)
  const c = state.core || pick(cores)
  const s = state.sector || pick(sectors)
  return `BUMK ${p} ${c} — Badan Usaha Milik Desa (${s})`
})

const fullTagline = computed(() => state.tagline || pick(taglines))

function pick<T>(arr: T[]): T {
  return arr[Math.floor(Math.random() * arr.length)]
}

function randomize() {
  state.prefix = pick(prefixes)
  state.core = pick(cores)
  state.sector = pick(sectors)
  state.tagline = pick(taglines)
}

function reset() {
  state.prefix = ''
  state.core = ''
  state.sector = ''
  state.tagline = ''
}

// Sertifikat & laporan palsu untuk hasil generator
const certificateNo = computed(() => `SK/${Math.floor(1000 + Math.random() * 9000)}/BUMK/${new Date().getFullYear()}`)
const fakeStats = computed(() => ({
  revenue: `${(Math.random() * 30 + 5).toFixed(1)} M`,
  hazeDays: Math.floor(Math.random() * 100 + 200),
  audits: Math.floor(Math.random() * 4),
}))
</script>

<template>
  <UContainer class="py-14">
    <h1 class="text-3xl font-bold">Generator BUMK</h1>
    <p class="mt-3 text-(--ui-text-muted) max-w-2xl">
      Susun nama, sektor, dan slogan usaha milik desamu. Hasilnya bisa langsung
      dicetak sebagai contoh parodi.
    </p>

    <div class="grid lg:grid-cols-2 gap-8 mt-10">
      <!-- Form -->
      <UCard>
        <h2 class="font-semibold mb-4">Isi Detail</h2>
        <div class="space-y-4">
          <UFormField label="Kata Depan" hint="Misal: Kabut, Udara, Napas">
            <UInput v-model="state.prefix" placeholder="(acak bila kosong)" />
          </UFormField>
          <UFormField label="Kata Inti" hint="Misal: Emas, Jernih, Sejuk">
            <UInput v-model="state.core" placeholder="(acak bila kosong)" />
          </UFormField>
          <UFormField label="Sektor Usaha">
            <UInput v-model="state.sector" placeholder="(acak bila kosong)" />
          </UFormField>
          <UFormField label="Slogan">
            <UInput v-model="state.tagline" placeholder="(acak bila kosong)" />
          </UFormField>
        </div>
        <div class="flex gap-3 mt-6">
          <UButton label="Acak Semua" icon="i-lucide-shuffle" @click="randomize" />
          <UButton label="Reset" variant="outline" color="neutral" @click="reset" />
        </div>
      </UCard>

      <!-- Preview -->
      <UCard>
        <h2 class="font-semibold mb-4">Pratinjau</h2>
        <div class="rounded-lg bg-(--ui-bg-elevated) p-6 text-center space-y-3">
          <UIcon name="i-lucide-building" class="size-12 text-(--ui-primary) mx-auto" />
          <div class="text-xl font-bold">{{ fullName }}</div>
          <div class="text-sm italic text-(--ui-text-muted)">"{{ fullTagline }}"</div>
          <UBadge color="primary" variant="subtle">No. Sertifikat: {{ certificateNo }}</UBadge>
        </div>

        <div class="grid grid-cols-3 gap-3 mt-4 text-center">
          <div class="rounded-lg border border-(--ui-border) p-3">
            <div class="text-lg font-bold font-mono">{{ fakeStats.revenue }}</div>
            <div class="text-xs text-(--ui-text-muted)">Pendapatan (Rp)</div>
          </div>
          <div class="rounded-lg border border-(--ui-border) p-3">
            <div class="text-lg font-bold font-mono">{{ fakeStats.hazeDays }}</div>
            <div class="text-xs text-(--ui-text-muted)">Hari Kabut</div>
          </div>
          <div class="rounded-lg border border-(--ui-border) p-3">
            <div class="text-lg font-bold font-mono">{{ fakeStats.audits }}</div>
            <div class="text-xs text-(--ui-text-muted)">Audit Selesai</div>
          </div>
        </div>

        <UAlert
          class="mt-4"
          color="neutral"
          variant="subtle"
          icon="i-lucide-info"
          title="Ini semua rekaan"
          description="Angka di atas dihasilkan secara acak di browsermu. Tidak ada lembaga nyata yang terlibat."
        />
      </UCard>
    </div>
  </UContainer>
</template>
