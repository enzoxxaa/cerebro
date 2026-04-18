---
tipo: deuda
acreedor: Mamá
monto: 50000
estado: auto-saldada
vencimiento: 2026-05-31
prioridad: baja
con-interes: false
tags:
  - finanzas
  - deuda
---

# Deuda Mamá

No requiere transferencia. Se salda automáticamente descontando **$25.000/mes durante 2 meses** de la mesada mensual de $50.000.

## Impacto en flujo de caja

- Mesada neta recibida durante los próximos 2 meses: **$25.000/mes** (en vez de $50.000).
- Esta deuda NO compite con los ingresos líquidos, por eso aparece con estado `auto-saldada`.

## Cronograma

- **abril:** primer descuento de $25.000 (mesada neta $25.000).
- **mayo:** segundo descuento de $25.000 (mesada neta $25.000).
- **junio:** mesada vuelve a $50.000 netos.
