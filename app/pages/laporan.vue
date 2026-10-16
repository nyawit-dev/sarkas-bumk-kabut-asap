<script setup lang="ts">
useHead({ title: "Laporan Kinerja — PT Kabut Asap & Wisata Napas" })

const columns = [
  { id: "tahun", accessorKey: "tahun", header: "Tahun" },
  { id: "pendapatan", accessorKey: "pendapatan", header: "Pendapatan (Rp)" },
  { id: "laba", accessorKey: "laba", header: "Laba (Rp)" },
  { id: "kabut", accessorKey: "kabut", header: "Hari Kabut" },
  { id: "audit", accessorKey: "audit", header: "Audit Independen" },
]

const data = [
  { id: "r2021", tahun: 2021, pendapatan: "4,2 M", laba: "2,1 M", kabut: 187, audit: "Ditolak oleh auditor 1" },
  { id: "r2022", tahun: 2022, pendapatan: "9,8 M", laba: "6,4 M", kabut: 214, audit: "Ditolak oleh auditor 2" },
  { id: "r2023", tahun: 2023, pendapatan: "15,1 M", laba: "11,3 M", kabut: 238, audit: "Dalam proses" },
  { id: "r2024", tahun: 2024, pendapatan: "22,7 M", laba: "18,9 M", kabut: 251, audit: "Dijadwalkan ulang" },
  { id: "r2025", tahun: 2025, pendapatan: "31,4 M", laba: "27,2 M", kabut: 276, audit: "Belum diajukan" },
]

function auditColor(a: string) {
  if (a.includes("Ditolak")) return "error"
  if (a.includes("proses")) return "warning"
  return "neutral"
}

const chartPoints = [
  { tahun: 2021, laba: 2.1, day: 187 },
  { tahun: 2022, laba: 6.4, day: 214 },
  { tahun: 2023, laba: 11.3, day: 238 },
  { tahun: 2024, laba: 18.9, day: 251 },
  { tahun: 2025, laba: 27.2, day: 276 },
]

const chartWidth = 400
const chartHeight = 120
const maxLaba = 27.2
const maxDay = 276
</script>

<template>
  <UContainer class="py-14">
    <h1 class="text-3xl font-bold">Laporan Kinerja</h1>
    <p class="mt-3 text-(--ui-text-muted) max-w-2xl">
      Ringkasan lima tahun operasional. Angka bersifat klaim internal
      (self-reported) dan belum diverifikasi badan audit independen mana pun.
    </p>

    <!-- Tabel ───────────────────────────────────────────────────────── -->
    <UCard class="mt-8">
      <UTable :data="data" :columns="columns" class="w-full">
        <template #audit-cell="{ row }">
          <UBadge :color="auditColor(row.original.audit)" variant="subtle">
            {{ row.original.audit }}
          </UBadge>
        </template>
        <template #kabut-cell="{ row }">
          <span class="mono font-mono tabular-nums">{{ row.original.kabut }}</span>
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

    <!-- Statistik ───────────────────────────────────────────────────── -->
    <div class="grid sm:grid-cols-3 gap-4 mt-8">
      <div class="rounded-xl border border-(--ui-border) p-4">
        <div class="mono font-mono text-2xl font-bold">276</div>
        <div class="text-sm text-(--ui-text-muted) mt-1">Hari kabut tercatat (2025)</div>
      </div>
      <div class="rounded-xl border border-(--ui-border) p-4">
        <div class="mono font-mono text-2xl font-bold">86%</div>
        <div class="text-sm text-(--ui-text-muted) mt-1">Pertumbuhan laba tahunan</div>
      </div>
      <div class="rounded-xl border border-(--ui-border) p-4">
        <div class="mono font-mono text-2xl font-bold">0</div>
        <div class="text-sm text-(--ui-text-muted) mt-1">Audit independen selesai</div>
      </div>
    </div>

    <!-- Grafik tanpa SVG ─────────────────────────────────────────────── -->
    <UCard class="mt-8">
      <h2 class="text-lg font-semibold mb-4">Tren Laba (Klaim Internal)</h2>
      <div class="w-full overflow-hidden" style="max-height:280px">
        <div class="flex items-end gap-4 h-full">
          <template v-for="(p, i) in chartPoints" :key="p.tahun">
            <div
              class="flex-1 flex flex-col items-center gap-2"
              style="max-width:80px"
            >
              <span
                class="w-full rounded-t-sm"
                :style="{
                  height: `${(p.laba / maxLaba) * 100}%`,
                  background: i === 4 ? 'var(--ui-primary)' : 'color-mix(in oklab, var(--ui-primary) 60%, transparent)',
                  minHeight: i === 4 ? '120px' : '40px',
                }"
              />
              <span class="text-[10px] text-(--ui-text-muted) mono font-mono">{{ p.tahun }}</span>
            </div>
          </template>
        </div>
      </div>
      <p class="mt-2 text-xs text-(--ui-text-dimmed)">
        Grafik disusun dari catatan internal Bagian Keuangan. Tidak ada verifikasi
        pihak ketiga pada seluruh periode yang ditampilkan.
      </p>
    </UCard>

    <!-- Status Verifikasi ─────────────────────────────────────────────── -->
    <UCard class="mt-6">
      <div class="grid md:grid-cols-2 gap-6 items-center">
        <!-- Status audit as text -->
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
