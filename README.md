# Sarkas BUMK — Kabut Asap

**PT Kabut Asap & Wisata Napas (PT KAW N)** — situs satire profil Badan Usaha Milik Desa (BUMK) fiksi di "Desa Konoha".

> ⚠️ **Seluruh isi situs adalah rekaan untuk karya satire.** PT KAW N tidak ada, Desa Konoha adalah latar fiksi, dan tidak ada afiliasi dengan perusahaan, desa, atau badan nyata mana pun. Angka kinerja bersifat klaim internal dalam konteks rekaan. Situs bersifat `noindex, nofollow`.

## Tentang

Situs ini memparodikan konvensi situs profil BUMN/BUMD: hero korporat, pita statistik, tabel kinerja, dan lini produk — dengan konten yang absurd. Tema diambil dari berita viral Indonesia: kabut asap vs pejabat ke luar negeri, udara kemasan, rapat di luar negeri.

## Fitur

- **Beranda** — hero, statistik self-reported, 4 produk, kutipan pengurus
- **Layanan** — 4 lini usaha lengkap dengan harga
- **Laporan Kinerja** — tabel 5 tahun (TanStack Table via `UTable`)
- **Generator BUMK** — generator interaktif nama + sertifikat + statistik acak
- **Legal** — disclaimer satire penuh

## Teknologi

- **Nuxt 4** + file-based routing (`pages/`)
- **Nuxt UI v4** (`@nuxt/ui`) — semua komponen UI: `UApp`, `UHeader`, `UFooter`, `UNavigationMenu`, `UCard`, `UTable`, `UButton`, `UInput`, `UBadge`, `UAlert`, dll.
- Tailwind CSS v4 (bawaan modul Nuxt UI)
- Static site generation → GitHub Pages

## Development

```bash
bun install
bun run dev          # dev server
bun run generate     # build static ke .output/public
```

Verifikasi lokal (server dengan baseURL-rewrite, lihat `scripts/serve-static.py`):

```bash
python3 scripts/serve-static.py .output/public /sarkas-bumk-kabut-asap 4199
```

## Deploy

Push ke `main` → GitHub Actions (`bun install` + `bun run generate` + upload Pages artifact) → deploy ke `nyawit-dev.github.io/sarkas-bumk-kabut-asap/`.

## Lisensi

MIT — karya fiksi/satire, bebas digunakan ulang dengan tetap mencantumkan sifat satire-nya.
