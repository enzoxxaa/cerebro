---
tipo: nota-tecnica
proyecto: seminario
fecha: 2026-08-26
tags:
  - infra
  - pi
---

# Setup de `learn/` — subagentes y log

Registro de qué estaba roto y cómo quedó arreglado, para no re-descubrirlo.

## Cómo arrancar la sesión

```bash
tmux new -A -s pi 'pi -c'      # -c continúa la última sesión; tmux es OBLIGATORIO para subagentes
```

Y dentro de pi, una vez:

```
/md-log Presentación seminario.md
```

Eso vincula el log y **rellena hacia atrás** toda la sesión. Se desvincula con `/md-unlog`.

> [!warning] Dos requisitos no obvios
> - **tmux**: `pi-interactive-subagents` lanza cada subagente en un panel tmux. Fuera de tmux no hay subagentes.
> - **Sesión persistente**: con `--no-session` los subagentes fallan con `Error: no session file`.

## Qué estaba roto (4 fallas)

| # | Falla | Causa raíz | Arreglo |
|---|---|---|---|
| 1 | No existía la tool `subagent` | Ninguna implementación de subagentes instalada | `pi install git:github.com/amosblomqvist/pi-interactive-subagents` |
| 2 | `researcher` sin herramientas | Declaraba `web_search`/`web_fetch`, que **no existen** en pi y **tampoco los trae** ese repo (los espera en `~/.pi/agent/extensions/`, son privados del autor) | Escritas desde cero |
| 3 | `researcher`, `scout`, `worker` sin modelo válido | Pedían `openrouter/z-ai/glm-5.3`; solo hay auth de Anthropic | Cambiados a `anthropic/claude-sonnet-5` |
| 4 | `visual-tools` no renderizaba | Hardcodeado a macOS: rutas `.app` de Chrome, MacPorts/Homebrew en PATH, y una devDependency apuntando a `file:/Users/amos/...` que rompía `npm install` | Añadidas rutas Linux; devDependency eliminada; `npm install` corrido |

## Extensiones escritas

Ambas viven donde `pi-interactive-subagents` las busca, así que sirven **tanto** a los subagentes **como** a la sesión principal.

### `~/.pi/agent/extensions/web-search/index.ts` → tool `web_search`

Tres backends, todos sin API key:

| `source` | Backend | Devuelve |
|---|---|---|
| `web` (default) | DuckDuckGo Lite | título, URL, snippet |
| `papers` | OpenAlex (fallback Crossref) | venue, año, **nº de citas**, DOI, abstract reconstruido del `abstract_inverted_index` |
| `pubmed` | Europe PMC | abstract completo, PMID/PMCID, flag open-access |

### `~/.pi/agent/extensions/web-fetch/index.ts` → tool `web_fetch`

`r.jina.ai` (URL → Markdown limpio, aguanta páginas con JS) y si falla, fetch directo + reducción HTML→texto local. **No parsea PDFs** → usar la landing page del DOI o el HTML de PMC.

Cero dependencias npm en ambas (usan `fetch` global de Node).

## Agentes disponibles

| Agente | Origen | Modelo |
|---|---|---|
| `researcher` | `.pi/agents/` (proyecto) | `claude-sonnet-5` |
| `mermaid-maker` | `.pi/agents/` (proyecto) | `claude-sonnet-5` |
| `svg-maker` | `.pi/agents/` (proyecto) | `claude-sonnet-5` |
| `scout` | `~/.pi/agent/agents/` (global) | `claude-sonnet-5` |
| `worker` | `~/.pi/agent/agents/` (global) | `claude-sonnet-5` |

Precedencia de directorios: `package → global (~/.pi/agent/agents) → project (.pi/agents)`, gana el último. Por eso `scout`/`worker` se sobrescribieron en **global** en vez de editar el clon instalado: `pi update` pisaría los cambios en el clon.

## `pi-claude-auth` y los subagentes — no hay conflicto

Duda razonable: `pi-interactive-subagents` lanza al hijo con `--no-extensions` + `--tools <lista>` + un `-e` por cada extensión que respalde una tool declarada (ver `applySandboxToParts`). O sea que **`pi-claude-auth` NO se carga en el hijo**.

No importa, y esta es la razón:

1. `pi-claude-auth` lee `~/.claude/.credentials.json` y **siembra** `~/.pi/agent/auth.json`.
2. Esa entrada quedó como `anthropic → {type: "oauth", access, refresh, expires}`.
3. **pi soporta OAuth de Anthropic de forma nativa**: `auth.json` es la prioridad #2 en su orden de resolución de auth, y refresca los tokens solo.

Conclusión: `pi-claude-auth` es solo el *puente inicial*. Una vez sembrado `auth.json`, el core de pi se encarga — y el hijo hereda la suscripción igual.

Evidencia de que el hijo sí autenticó por suscripción: el error fue
`400 "You're out of extra usage. Add more at claude.ai/settings/usage"`.
Ese mensaje es de la ruta OAuth/suscripción. Con una API key agotada el error
sería `"credit balance is too low"`. Cuota real, no configuración.

## Estado de la verificación

- `web_search` con `source=papers`, `web` y `pubmed` — **probado, devuelve resultados reales**
- `web_fetch` sobre la doc de PLUMED — **probado**
- Render Mermaid con `/usr/bin/chromium` — **probado, PNG 236×382 generado**
- Carga de extensiones en pi — **probado**: `subagents, ask-user-question, md-log, quiz, visual-tools, web-fetch, web-search`
- `subagents_list` descubre los 5 agentes — **probado**
- Spawn real del `researcher` en panel tmux — **llegó a la API**, y ahí murió con
  `400 invalid_request_error: You're out of extra usage`. Es cuota de la cuenta, no configuración.
  Si reaparece: esperar la recarga de cuota.
