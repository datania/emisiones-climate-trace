# Emisiones Climate TRACE 🌍

Repositorio para descargar y organizar los datasets públicos de emisiones de Climate TRACE para España. Climate TRACE es una coalición independiente que combina observaciones satelitales, sensores remotos e IA para estimar emisiones de gases de efecto invernadero y compartirlas con el público casi en tiempo real.

El portal [Climate TRACE Data](https://climatetrace.org/data) ofrece descargas gratuitas por país, sector, tipo de gas y activo industrial, con series anuales disponibles desde 2015, métricas de calidad y documentación metodológica para cada conjunto.

Este repositorio sincroniza los paquetes `country_packages` para el código ISO `ESP`, manteniendo copias reproducibles de los archivos CSV y notas descriptivas publicadas en [climatetrace.org](https://climatetrace.org).

## 🚀 Descarga

```bash
make data
```

## 📂 Estructura de datos

```
data/
└── raw/
    ├── co2/
    │   ├── ABOUT_THE_DATA/        # Metodología y diccionario de campos
    │   └── DATA/
    │       ├── power/             # Sectores y subsectores con series anuales (2015 en adelante)
    │       ├── industry/
    │       └── forestry_and_land_use/
    ├── co2e_100yr/
    ├── ch4/
    └── ...                        # n2o, pm2_5, vocs, bc, etc.
```

Los archivos CSV comparten columnas clave como `iso3_country`, `sector`, `subsector`, `start_time`, `end_time`, `gas` y `emissions_quantity`, lo que permite combinar emisiones por actividad, año y gas. Cada carpeta `ABOUT_THE_DATA` incluye resúmenes de metodología, cobertura geográfica y explicaciones sobre las métricas de confianza publicadas por Climate TRACE.

## 📄 Licencia

MIT.
