# Design Pro

Skill para diseñar, construir y revisar interfaces web con identidad, UX clara y mobile comprobado. Incluye una entrevista creativa, controles de dirección y bloqueos explícitos contra los clichés habituales de las interfaces generadas por IA.

La versión 1.2 añade un contrato positivo del brief y revisiones independientes de funcionamiento, fidelidad visual e impacto temporal. Conservar una paleta no resuelve la dirección de arte; un auditor sin hallazgos tampoco aprueba el resultado creativo.

Conserva los tres controles y el catálogo creativo de [Taste Skill](https://github.com/Leonxlnx/taste-skill), y los integra en un flujo propio. Una técnica del catálogo puede ser una referencia sin estar habilitada por defecto.

Las instrucciones están en español. El agente responde en el idioma de la persona que la usa. El paquete comparte el mismo núcleo para Claude Code y Codex y no depende de otra skill, un plugin determinado ni un framework específico.

## Instalación

Con Node.js y npm disponibles, ejecutá desde el proyecto donde quieras usarla:

```sh
npx skills add 0xlukem/design-pro --skill design-pro -a claude-code -a codex
```

Para instalarla a nivel de usuario en ambos agentes, agregá `-g`:

```sh
npx skills add 0xlukem/design-pro --skill design-pro -a claude-code -a codex -g
```

El comando usa el [CLI de Agent Skills](https://github.com/vercel-labs/skills). También podés copiar la carpeta completa [`skills/design-pro`](skills/design-pro) dentro de `.claude/skills/` para Claude Code o `.agents/skills/` para Codex. Conservá sus referencias, script y licencia junto al `SKILL.md`.

## Uso

En Claude Code, invocá `/design-pro`. En Codex, mencioná `$design-pro`.

Ejemplos de pedidos:

```text
Usá design-pro para crear una app personal de lecturas.
Todavía no tengo dirección visual: empezá con la entrevista.
```

```text
Usá design-pro. Quiero explorar ocho estilos para un archivo fotográfico.
Primero mostrame una imagen dividida en ocho referencias A–H.
```

```text
Usá design-pro para auditar esta pantalla, read only.
Revisá jerarquía, estados, teclado y los breakpoints reales.
```

```text
Usá design-pro para ajustar solo el título mobile.
Conservá la composición y el espaciado ya elegidos.
```

## Cómo trabaja

1. **Reconoce el alcance.** Separa creación, rediseño abierto, dirección elegida, ajuste puntual y auditoría.
2. **Entrevista integrada.** Para proyectos nuevos o rediseños abiertos, hace al menos 15 preguntas sustantivas en rondas de 3 a 5. Las repreguntas dependen de las respuestas. Un ajuste puntual no reinicia la entrevista.
3. **Dirección visual.** Distingue marca conservada de dirección resuelta y traduce cada requisito a un resultado observable de composición, tipografía, material, motion y encuadre. Landing y editor pueden necesitar perfiles distintos.
4. **Referencias opcionales.** Si se piden al comienzo, prepara temprano un tablero de ocho direcciones con el mismo brief. Al cerrar la dirección puede generar una referencia detallada de desktop y mobile.
5. **Implementación contextual.** Reutiliza el stack, los componentes y los tokens existentes. Si una escena animada define el pedido, construye y observa primero esa pieza antes de extender su dirección. Conserva los estados y la recuperación que el producto necesita.
6. **Verificación independiente.** Revisa funcionamiento, fidelidad al brief e impacto temporal por separado. No compensa una dirección equivocada con usabilidad, compilación o ausencia de overflow. Declara fallos y pendientes con evidencia.

El usuario puede pedir explícitamente saltar la entrevista o delegar las decisiones. La generación de imágenes requiere una herramienta disponible: la skill no incluye un servicio de imágenes ni una API key.

## Controles de dirección

| Control | Valor inicial | Qué cambia |
| --- | --- | --- |
| `DESIGN_VARIANCE` | **8** | Variación de composición, proporciones y asimetría. |
| `MOTION_INTENSITY` | **6** | Presencia del movimiento y continuidad de los cambios. |
| `VISUAL_DENSITY` | **4** | Información que comparte el espacio y ritmo de lectura. |

La entrevista y las referencias ajustan estos valores. Son controles de diseño, no pesos internos del modelo. Los bloqueos visuales prevalecen sobre cualquier nivel de intensidad.

La [guía de dirección](skills/design-pro/references/visual-direction.md) desarrolla los niveles, la escala tipográfica y los pesos. La [guía de motion](skills/design-pro/references/motion.md) incluye referencias ajustables de timing y física.

## Bloqueos por defecto

- Gradientes decorativos, mesh, glows y halos.
- Eyebrows y badges decorativos sobre títulos.
- Inter y la sustitución automática por una misma fuente en todos los proyectos.
- Una palabra del título resaltada con subrayado dibujado, color, cursiva o mezcla ornamental de familias.
- CTAs promocionales paralelos con igual peso.
- Bento de relleno, filas genéricas de tres cards y cajas innecesarias.
- Copy intercambiable y prueba social inventada.
- Fade-up repetido, typewriter ornamental, cards flotantes, botones magnéticos, scroll secuestrado y bucles decorativos.

Una petición explícita habilita un recurso solo en el alcance nombrado. «Premium», «moderno» o una referencia que contiene ese efecto no habilitan excepciones silenciosas. Labels, foco de teclado, enlaces reconocibles y controles funcionales siguen cumpliendo su función.

La tabla completa y sus excepciones están en [`SKILL.md`](skills/design-pro/SKILL.md).

## Repertorio visual y mobile

El [catálogo creativo](skills/design-pro/references/creative-library.md) conserva **45 recursos y cinco arquetipos de Taste**, clasificados como elegibles, condicionales o disponibles solo por pedido explícito. Incluye composición, navegación, retículas, galerías, contenedores, scroll, tipografía y microinteracciones.

La [guía de UX](skills/design-pro/references/ux.md) cubre tarea, navegación, formularios, estados, accesibilidad y recuperación. La [guía mobile](skills/design-pro/references/mobile-qa.md) exige una composición propia, pruebas de contenido e interacción, anchos representativos, límites B−1/B/B+1 y revisión de rangos intermedios.

Una captura estrecha no demuestra una prueba en un dispositivo real. La entrega debe distinguir el render observado, la emulación y el uso real.

## Auditor estático

El script usa Python 3 y la biblioteca estándar. Lee código, devuelve JSON y no modifica el proyecto:

```sh
python3 skills/design-pro/scripts/audit_ui.py /ruta/al/proyecto --file src/hero.tsx --file src/styles.css
```

Detecta sintaxis habitual de gradientes (`DP001`), uso de Inter (`DP002`) y bucles que necesitan revisión contextual (`DP003`). Permite registrar excepciones justificadas por archivo y líneas. No puede evaluar por sí solo composición, clichés semánticos, UX, contraste ni accesibilidad.

Consultá [alcance, códigos de salida y excepciones](skills/design-pro/references/source-audit.md).

## Aceptación del brief

La [guía de aceptación](skills/design-pro/references/acceptance.md) exige un resultado por cada requisito explícito. Para movimiento protagonista requiere observar la secuencia completa: transformación, ritmo, amplitud y resolución. Píxeles distintos o un control Pause no demuestran por sí solos ese impacto.

Para una revisión amplia, un informe JSON puede comprobarse con:

```sh
python3 skills/design-pro/scripts/check_acceptance.py /ruta/review.json --root /ruta/al/proyecto
```

Este script solo comprueba coherencia del registro y tipos de evidencia. Mantiene abiertas las revisiones fallidas, ausentes o sin evidencia adecuada; el resultado del auditor estático es informativo y no puede compensarlas. No observa videos ni certifica calidad estética. Un informe con todas sus declaraciones y referencias coherentes queda `ready_for_review`, no aprobado automáticamente.

## Desarrollo y comprobaciones

Las pruebas no necesitan instalar dependencias:

```sh
python3 -m unittest discover -s tests -v
```

La suite cubre el auditor y la coherencia de aceptación, incluida la regresión de una interfaz que pasa controles técnicos pero falla el brief expresivo. Las comprobaciones de formato, enlaces, integridad y respuestas de ensayo complementan esa suite. No equivalen a probar un flujo completo con imágenes y navegador dentro de ambos asistentes ni a certificar calidad creativa.

```text
design-pro/
├── README.md
├── LICENSE
├── .gitignore
├── skills/
│   └── design-pro/
│       ├── SKILL.md
│       ├── LICENSE
│       ├── agents/openai.yaml
│       ├── references/
│       │   ├── visual-direction.md
│       │   ├── creative-library.md
│       │   ├── ux.md
│       │   ├── motion.md
│       │   ├── acceptance.md
│       │   ├── mobile-qa.md
│       │   └── source-audit.md
│       └── scripts/
│           ├── audit_ui.py
│           └── check_acceptance.py
└── tests/
    ├── fixtures/expressive_brief_regression.json
    ├── test_audit_ui.py
    └── test_acceptance.py
```

## Origen y licencia

Design Pro está basada en la skill `design-taste-frontend` de **[Taste Skill, por Leonxlnx](https://github.com/Leonxlnx/taste-skill)**. Conserva sus tres controles y el repertorio creativo, con instrucciones adaptadas y un flujo propio de entrevista, UX y verificación.

Distribuida bajo [MIT](LICENSE). Se conservan el aviso de copyright y la licencia de Taste, y se añade el crédito de las modificaciones de Lucas Malizia. La carpeta instalable incluye su propia copia de la licencia para conservar la atribución al distribuirla por separado.
