---
license: mit
pretty_name: Climate TRACE Spain Emissions
tags:
  - climate
  - greenhouse-gases
  - spain
---

# Climate TRACE Spain Emissions

This dataset mirrors the Climate TRACE country packages for Spain (ISO alpha-3 `ESP`). It contains Parquet (zstd) extracts converted from the CSVs published by [Climate TRACE](https://climatetrace.org/data). All columns are stored as text to avoid type inference failures. Cast as needed.

## Contents

- `raw/<gas>/ABOUT_THE_DATA/`: original documentation supplied by Climate TRACE (PDF methodology summary and CSV data dictionary).
- `raw/<gas>/DATA/`: annual emission series (2015 onward) partitioned by sector and subsector. All Parquet files share the core columns `iso3_country`, `sector`, `subsector`, `start_time`, `end_time`, `gas`, `emissions_quantity`, `emissions_unit`, and confidence metrics.
- Gases currently mirrored: carbon dioxide (`co2`), methane (`ch4`), nitrous oxide (`n2o`), ammonia (`nh3`), nitrogen oxides (`nox`), sulfur dioxide (`so2`), particulate matter (`pm2_5`), volatile organic compounds (`vocs`), carbon monoxide (`co`), black carbon (`bc`), organic carbon (`oc`), and carbon dioxide equivalents (`co2e_20yr`, `co2e_100yr`).
