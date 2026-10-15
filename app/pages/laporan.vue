<script setup lang="ts">
useHead({
  title: 'Laporan Kinerja — PT Kabut Asap & Wisata Napas',
})

const columns = [
  { id: 'tahun', accessorKey: 'tahun', header: 'Tahun' },
  { id: 'pendapatan', accessorKey: 'pendapatan', header: 'Pendapatan (Rp)' },
  { id: 'laba', accessorKey: 'laba', header: 'Laba (Rp)' },
  { id: 'kabut', accessorKey: 'kabut', header: 'Hari Kabut' },
  { id: 'audit', accessorKey: 'audit', header: 'Audit Independen' },
]

const data = [
  { id: 'r2021', tahun: 2021, pendapatan: '4,2 M', laba: '2,1 M', kabut: 187, audit: 'Ditolak oleh auditor 1' },
  { id: 'r2022', tahun: 2022, pendapatan: '9,8 M', laba: '6,4 M', kabut: 214, audit: 'Ditolak oleh auditor 2' },
  { id: 'r2023', tahun: 2023, pendapatan: '15,1 M', laba: '11,3 M', kabut: 238, audit: 'Dalam proses' },
  { id: 'r2024', tahun: 2024, pendapatan: '22,7 M', laba: '18,9 M', kabut: 251, audit: 'Dijadwalkan ulang' },
  { id: 'r2025', tahun: 2025, pendapatan: '31,4 M', laba: '27,2 M', kabut: 276, audit: 'Belum diajukan' },
]

function auditColor(a: string) {
  if (a.includes('Ditolak')) return 'error'
  if (a.includes('proses')) return 'warning'
  return 'neutral'
}

const base = '/sarkas-bumk-kabut-asap'
</script>

<template>
  <UContainer class="py-14">
    <h1 class="text-3xl font-bold">Laporan Kinerja</h1>
    <p class="mt-3 text-(--ui-text-muted) max-w-2xl">
      Ringkasan lima tahun operasional. Angka bersifat klaim internal
      (self-reported) dan belum diverifikasi badan audit independen mana pun.
    </p>

    <UCard class="mt-8">
      <UTable :data="data" :columns="columns" class="w-full">
        <template #audit-cell="{ row }">
          <UBadge :color="auditColor(row.original.audit)" variant="subtle">
            {{ row.original.audit }}
          </UBadge>
        </template>
        <template #kabut-cell="{ row }">
          <span class="font-mono tabular-nums">{{ row.original.kabut }}</span>
        </template>
      </UTable>
    </UCard>

    <UAlert
      class="mt-6"
      color="warning"
      variant="subtle"
      icon="i-lucide-triangle-alert"
      title="Catatan metodologi"
      description="Pendapatan dihitung dari penjualan udara kaleng, paket wisata, dan sewa fasilitas rapat. Laba dihitung setelah dikurangi biaya operasional, biaya penerbangan pengurus, dan biaya penolakan audit."
    />

    <div class="grid sm:grid-cols-3 gap-4 mt-8">
      <UCard>
        <div class="text-3xl font-bold font-mono text-(--ui-primary)">276</div>
        <div class="text-sm text-(--ui-text-muted) mt-1">Hari kabut tercatat (2025)</div>
      </UCard>
      <UCard>
        <div class="text-3xl font-bold font-mono text-(--ui-primary)">86%</div>
        <div class="text-sm text-(--ui-text-muted) mt-1">Pertumbuhan laba tahunan</div>
      </UCard>
      <UCard>
        <div class="text-3xl font-bold font-mono text-(--ui-primary)">0</div>
        <div class="text-sm text-(--ui-text-muted) mt-1">Audit independen selesai</div>
      </UCard>
    </div>

    <!-- Grafik pertumbuhan -->
    <UCard class="mt-8">
      <h2 class="text-lg font-semibold mb-2">Tren Laba (Klaim Internal)</h2>
      <img
        :src="base + '/img/galeri-grafik-laba.svg'"
        alt="Grafik batang pertumbuhan laba PT KAW N tahun 2021 sampai 2025"
        width="1600"
        height="900"
        class="w-full rounded-lg ring-1 ring-(--ui-border)"
      />
      <p class="mt-2 text-xs text-(--ui-text-dimmed)">
        Grafik disusun dari catatan internal Bagian Keuangan. Tidak ada verifikasi
        pihak ketiga pada seluruh periode yang ditampilkan.
      </p>
    </UCard>

    <!-- Dokumen & audit -->
    <UCard class="mt-6">
      <div class="grid md:grid-cols-2 gap-6 items-center">
        <img
          :src="base + '/img/galeri-dokumen.svg'"
          alt="Tumpukan laporan tahunan dan berkas audit berstempel ditolak"
          width="1600"
          height="900"
          class="w-full rounded-lg ring-1 ring-(--ui-border)"
        />
        <div>
          <h3 class="font-semibold">Status Verifikasi</h3>
          <p class="mt-2 text-(--ui-text-muted)">
            Seluruh laporan tahunan tersedia dalam bentuk cetak di ruang keuangan.
            Permintaan audit independen yang masuk sejauh ini berakhir dengan
            stempel "DITOLAK" — dengan alasan data masih dalam proses digitalisasi.
          </p>
          <ul class="mt-3 space-y-2 text-sm">
            <li class="flex items-center gap-2">
              <UIcon name="i-lucide-x-circle" class="size-4 text-(--ui-error)" />
              Audit 2021 — ditolak (auditor belum terverifikasi)
            </li>
            <li class="flex items-center gap-2">
              <UIcon name="i-lucide-x-circle" class="size-4 text-(--ui-error)" />
              Audit 2022 — ditolak (data belum digital)
            </li>
            <li class="flex items-center gap-2">
              <UIcon name="i-lucide-clock" class="size-4 text-(--ui-warning)" />
              Audit 2023 — dalam proses penjadwalan ulang
            </li>
            <li class="flex items-center gap-2">
              <UIcon name="i-lucide-minus-circle" class="size-4 text-(--ui-text-dimmed)" />
              Audit 2025 — belum diajukan
            </li>
          </ul>
        </div>
      </div>
    </UCard>
  </UContainer>
</template>
