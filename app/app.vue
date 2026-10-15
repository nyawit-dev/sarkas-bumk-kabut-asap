<script setup lang="ts">
const navItems = [
  { label: 'Beranda', to: '/', exact: true },
  { label: 'Layanan', to: '/layanan' },
  { label: 'Laporan Kinerja', to: '/laporan' },
  { label: 'Generator', to: '/generator' },
  { label: 'Legal', to: '/legal' },
]
</script>

<template>
  <UApp>
    <UHeader>
      <template #left>
        <ULink to="/" :aria-current="undefined" class="flex items-center gap-2">
          <span class="font-bold text-lg">PT KAW<span class="text-(--ui-primary)">N</span></span>
          <span class="hidden sm:inline text-xs text-(--ui-text-muted)">BUMK Desa Konoha</span>
        </ULink>
      </template>

      <UNavigationMenu :items="navItems" class="hidden lg:flex" />

      <template #right>
        <UButton
          label="Hubungi Kami"
          to="/legal"
          variant="subtle"
          size="sm"
        />
      </template>

      <template #body>
        <UNavigationMenu :items="navItems" orientation="vertical" class="-mx-2.5" />
      </template>
    </UHeader>

    <UMain>
      <NuxtPage />
    </UMain>

    <UFooter>
      <template #left>
        <p class="text-xs text-(--ui-text-muted)">
          PT Kabut Asap &amp; Wisata Napas — Badan Usaha Milik Desa (BUMK) Konoha.
          <strong class="text-(--ui-text)">Seluruh isi situs ini adalah rekaan untuk karya satire.</strong>
          Bukan lembaga nyata; tidak ada afiliasi dengan perusahaan, desa, atau badan apa pun.
        </p>
      </template>
    </UFooter>
  </UApp>
</template>
