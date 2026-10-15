// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2025-07-15',
  devtools: { enabled: true },

  // Semua komponen UI dari Nuxt UI (@nuxt/ui), tema Tailwind v4 bawaan modul.
  modules: ['@nuxt/ui'],

  css: ['~/assets/css/main.css'],

  nitro: {
    preset: 'github-pages',
  },

  app: {
    baseURL: '/sarkas-bumk-kabut-asap/',
    head: {
      htmlAttrs: { lang: 'id' },
      title: 'PT Kabut Asap & Wisata Napas — BUMK Desa Konoha',
      meta: [
        { charset: 'utf-8' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
        {
          name: 'description',
          content:
            'Profil resmi PT Kabut Asap & Wisata Napas, BUMK Desa Konoha. Seluruh isi adalah rekaan untuk karya satire.',
        },
        { name: 'robots', content: 'noindex, nofollow' },
      ],
    },
  },

  ui: {
    colorMode: false,
  },
})
