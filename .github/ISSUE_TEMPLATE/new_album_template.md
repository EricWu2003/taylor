---
name: New Album Alert
about: Submit a PR that includes a new Taylor Swift album
title: NEW ALBUM ALERT: ...
labels: ''
---

Checklist of things that should be updated when adding a new album:

- [ ] Add lyrics to `data-raw/lyrics`
- [ ] Add singles and release dates to `data-raw/releases.xlsx`
- [ ] Add metacritic score to bottom of `data-raw/taylor-lyrics.R`
- [ ] Run `data-raw/taylor-lyrics.R`
- [ ] Add album cover to `inst/album-covers` using `data-raw/album-covers.R`
- [ ] Add color palette to `R/taylor-album-palettes.R`
- [ ] Add color to existing `album_compare` palette in `R/taylor-album-palettes.R`
- [ ] Add new album to factor levels in `R/taylor-album-palettes.R`
- [ ] Update CSS for pkgdown theme
- [ ] Create new hex logo, update favicons
- [ ] Add tests for new palettes to `tests/testthat/test-ggplot2-color-scales.R`
