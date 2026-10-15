<script setup lang="ts">
useHead({
  title: 'Legal & Disclaimer — PT Kabut Asap & Wisata Napas',
})
</script>

<template>
  <UContainer class="py-14 max-w-3xl">
    <h1 class="text-3xl font-bold">Legal &amp; Disclaimer</h1>

    <UAlert
      class="mt-6"
      color="error"
      variant="subtle"
      icon="i-lucide-alert-octagon"
      title="Karya Satire — Semua Isinya Rekaan"
      description="PT Kabut Asap & Wisata Napas (PT KAW N) TIDAK ADA. Desa Konoha dalam konteks ini adalah latar fiksi. Tidak ada perusahaan, desa, badan usaha, atau individu nyata yang digambarkan di situs ini."
    />

    <div class="prose prose-sm dark:prose-invert mt-8 space-y-6">
      <section>
        <h2 class="text-lg font-semibold">Sifat Konten</h2>
        <p class="mt-2 text-(--ui-text-muted)">
          Seluruh nama, angka, kutipan, tabel kinerja, dan pernyataan di situs ini
          adalah fiksi yang dibuat untuk tujuan hiburan dan kritik sosial berbentuk
          parodi. Angka kinerja, sertifikat, dan kutipan pengurus bersifat
          <strong>self-reported</strong> dalam konteks rekaan dan tidak boleh
          dikutip sebagai fakta.
        </p>
      </section>

      <section>
        <h2 class="text-lg font-semibold">Tidak Ada Afiliasi</h2>
        <p class="mt-2 text-(--ui-text-muted)">
          Situs ini tidak berafiliasi, disponsori, atau didukung oleh perusahaan
          milik negara, badan usaha milik desa, lembaga pemerintah, atau entitas
          komersial mana pun. Kemiripan nama dengan entitas nyata adalah kebetulan
          yang disengaja sebagai bagian dari teknik satir.
        </p>
      </section>

      <section>
        <h2 class="text-lg font-semibold">Kontak</h2>
        <p class="mt-2 text-(--ui-text-muted)">
          Situs ini tidak menyediakan layanan nyata dan tidak menerima pembayaran.
          Formulir kontak bersifat ilustratif. Untuk pertanyaan serius mengenai
          konten, hubungi pembuat situs melalui repositori GitHub proyek ini.
        </p>
      </section>
    </div>

    <USeparator class="my-8" />
    <p class="text-xs text-(--ui-text-muted)">
      Dibuat dengan Nuxt 4 + Nuxt UI. Situs ini bersifat parodi dan dilindungi
      sebagai karya ekspresi.
    </p>
  </UContainer>
</template>
