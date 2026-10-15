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
  </UContainer>
</template>
