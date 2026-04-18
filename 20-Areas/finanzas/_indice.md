---
tipo: indice-area
area: finanzas
tags:
  - finanzas
  - indice
---

# 💰 Finanzas — Dashboard

> Dashboard vivo de deudas, ingresos y plan de pago. Actualizado: **2026-04-17**.

## Deudas pendientes

![[deudas.base#pendientes]]

## Ingresos próximos

![[ingresos.base#pendientes]]

## Plan de pago vigente

### Fin de abril (~30-abr) — entran $255.000

| Destino | Monto | Nota |
|---|---|---|
| Gastos fijos abril | $75.000 | Colchón para no quedar ilíquido |
| [[deuda-java-urgente\|Java urgente]] | $24.000 | Saldar |
| [[deuda-daniel\|Daniel]] | $5.000 | Saldar (micro-deuda) |
| [[deuda-cmr\|CMR abono]] | $151.000 | Deja saldo de $69.000 |
| **Total** | **$255.000** | |

### Mayo — entran ~$309.000

| Destino | Monto | Nota |
|---|---|---|
| Gastos fijos mayo | $75.000 | |
| [[deuda-cmr\|CMR liquidar]] | $69.000 | Cierra CMR |
| [[deuda-java-resto\|Java resto]] | $140.000 | Cierra Java |
| Colchón | $25.000 | Semilla de fondo de emergencia |

**Estado al 1-jun:** cero deudas. Capacidad de ahorro desde junio ~$259.000/mes.

## Reglas operativas

Cada vez que entra plata, el orden de pago es:

1. Gastos fijos del mes.
2. Deuda con interés ([[deuda-cmr|CMR]]).
3. Deuda exigida con fecha (Java urgente).
4. Micro-deudas (Daniel).
5. Deuda sin interés y con holgura (Java resto).
6. Colchón/ahorro.

## Alertas activas

- ⚠️ **Verificar fecha real de CMR** en app. Declarado "5-abr" pero hoy es 17-abr → puede estar en mora con interés acumulándose.
- ⚠️ **Confirmar con Java** si los $24.000 urgentes pueden esperar a 30-abr o requieren adelanto desde el retiro Racional.

## Supuestos que, si fallan, rompen el plan

1. CMR no está en mora avanzada.
2. Clases particulares de abril se cobran antes del 30-abr.
3. Gastos fijos mensuales no superan $100.000.
4. No aparecen deudas ni gastos nuevos imprevistos.

## Cómo mantener este dashboard

1. Cuando se paga una deuda parcialmente: editar el `monto` de la nota para que refleje el saldo restante.
2. Cuando se salda una deuda: cambiar `estado` de `pendiente` a `saldada`.
3. Cuando se recibe un ingreso: cambiar `estado` de `pendiente` a `recibido`.
4. Al comenzar un mes nuevo: duplicar las notas de ingresos con el mes actualizado (p. ej. `ingreso-clases-mayo.md`).
5. Las Bases refrescan la vista automáticamente.
