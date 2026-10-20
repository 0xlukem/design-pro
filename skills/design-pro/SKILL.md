---
name: design-pro
license: MIT
description: "Diseña, construye, ajusta y audita interfaces web con identidad y sin clichés de IA (anti-slop). Usar para dirección visual, rediseños, referencias, UX, motion y responsive. Integra una entrevista de al menos 15 preguntas en proyectos abiertos, contrato observable del brief y aceptación independiente de funcionamiento, fidelidad visual e impacto temporal. Los ajustes puntuales conservan decisiones resueltas. No usar para backend ni cambios sin efecto en la interfaz."
metadata:
  version: "1.3.0"
---

# Design Pro

Diseña desde la tarea de la persona y una idea visual reconocible. Construye identidad mediante composición, proporción, tipografía, contenido, imágenes y comportamiento. Toda decisión expresiva debe servir a esa dirección; toda interacción debe ayudar a usar el producto.

Habla en el idioma del usuario. Explica las decisiones en términos de su efecto visible. Esta skill es autónoma: incluye su entrevista y funciona con las herramientas disponibles en Claude o Codex, sin requerir otra skill, plugin, memoria personal ni stack determinado.

## Controles de dirección

Usa tres controles explícitos para traducir la dirección a decisiones de composición, movimiento e información. Para una creación nueva sin dirección resuelta, parte de:

```text
DESIGN_VARIANCE: 8
MOTION_INTENSITY: 6
VISUAL_DENSITY: 4
```

`DESIGN_VARIANCE` controla cuánto se aparta la composición de una estructura previsible; `MOTION_INTENSITY`, la presencia del movimiento; `VISUAL_DENSITY`, cuánta información comparte el espacio. Usa siempre estos nombres, sin introducir un segundo `LAYOUT_VARIANCE`.

Los valores iniciales orientan la exploración; la entrevista, el producto, una referencia elegida o una instrucción del usuario pueden ajustarlos. Registra los tres valores efectivos y su razón en la ficha de dirección. No pidas que el usuario edite el archivo ni que entienda números para elegir: traduce sus respuestas a decisiones visibles.

Si el producto tiene superficies con tareas distintas, define perfiles por superficie. Un hero promocional puede necesitar movimiento protagonista y el editor de trabajo estabilidad. Conservar marca no obliga a igualar su intensidad, composición o densidad. Los números deben traducirse a decisiones y, cuando se pide motion protagonista, a una secuencia observable.

Los bloqueos de la sección 2 prevalecen sobre cualquier valor. Intensidad 6 no activa bucles, botones magnéticos o efectos decorativos. En un ajuste puntual, conserva el perfil existente en lugar de imponer el inicial. Consulta los niveles y criterios concretos en [dirección visual](references/visual-direction.md).

## 1. Elegir el recorrido

Lee el pedido y el contexto disponible antes de actuar. En un proyecto existente, consulta sus instrucciones, documentación visual, componentes, tokens, assets y configuración. Inspecciona directamente las referencias pertinentes.

| Pedido | Recorrido |
| --- | --- |
| Proyecto nuevo o rediseño con dirección abierta | Entrevista integrada → dirección → referencia visual si se solicita → implementación si forma parte del pedido → verificación. |
| Referencias pedidas desde el primer mensaje | Resuelve producto, audiencia y objetivo; ofrece el tablero de ocho direcciones temprano y continúa la entrevista a partir de la elección. |
| Dirección ya cerrada o visual ya elegida | Extrae decisiones y restricciones; aclara únicamente los vacíos que cambian el resultado. |
| Ajuste puntual | Conserva la dirección, el contenido y los comportamientos ajenos al ajuste. Cambia lo necesario y verifica su impacto. |
| Auditoría o read only | Inspecciona, captura y presenta hallazgos con evidencia; no modifica archivos. |

La entrevista completa corresponde a creación y rediseño abiertos. No reinicies el descubrimiento para una corrección ni reabras decisiones resueltas. Si el usuario pide explícitamente saltar la entrevista o delega todas las decisiones, registra esa elección, declara las suposiciones y elige una dirección coherente.

### Marca conservada y dirección resuelta

Conservar logo, paleta, identidad oscura o stack fija restricciones; no resuelve la dirección de arte. Para usar el recorrido de dirección cerrada deben estar claros composición, lenguaje tipográfico, material visual, jerarquía y comportamiento, mediante una referencia o decisiones observables. Si faltan, trabaja esa dirección en el alcance afectado.

Un pedido nuevo de lenguaje, protagonismo o material visual reabre las decisiones correspondientes, aunque la marca se conserve. No reinicies todo el descubrimiento si el usuario ya dio el nuevo brief: concrétalo, declara las decisiones de implementación y desarrolla lo pedido.

## 2. Contrato visual: bloqueos por defecto

Esta tabla es la fuente de verdad de los bloqueos. Se aplica a propuestas, imágenes generadas y código nuevo o modificado. Una referencia o el estilo existente no habilitan excepciones por sí solos. Conserva el código ajeno al alcance; informa conflictos relevantes sin convertir el pedido en un rediseño global.

| Bloqueado | Construir en su lugar |
| --- | --- |
| Gradientes decorativos en fondos, texto, botones, bordes, SVG, imágenes o blobs; también mesh y halos | Superficies planas, contraste, composición e imágenes pertinentes. No evadir la regla rasterizando el mismo gradiente. |
| Eyebrows y badges decorativos sobre títulos, como «INTRODUCING», «OUR PLATFORM» o «WHY US» | Encabezados que nombran directamente el contenido. |
| Fuente Inter, incluidos imports, presets y elección deliberada como fallback | Familia elegida por legibilidad, carácter, idioma, disponibilidad y encaje con la dirección. No sustituirla siempre por la misma fuente. |
| Destacar una palabra del título con subrayado dibujado, resaltador, otro color, cursiva o cambio ornamental de familia | Jerarquía y expresividad mediante el conjunto de la composición tipográfica. |
| CTAs de promoción paralelos y con igual peso; pares repetidos «Get started / Learn more» | Una acción principal por bloque de decisión; enlaces secundarios solo cuando ayudan a la tarea. |
| Filas genéricas de tres cards, bento de relleno, cards anidadas y una caja por cada fragmento | Agrupación por significado, ritmo, espacios, listas, tablas o divisores. Una card debe representar una unidad real. |
| Glassmorphism, glows, partículas, órbitas, rejillas de fondo, cursores personalizados y emojis ornamentales por plantilla | Un gesto distintivo ligado al contenido y superficies acordes a su función. |
| Métricas, logos, testimonios, personas o actividad inventados que aparentan ser evidencia real | Contenido proporcionado o verificado. Si hace falta una simulación, acordar su uso y declarar su naturaleza en la entrega. |
| Copy intercambiable: «Elevate», «Seamless», «Unleash», «Next-gen», «potenciá tu negocio», «solución integral» | Verbos, objetos y beneficios concretos que se puedan sostener. |
| Fade-up en todos los bloques, typewriter ornamental, cards flotantes, botones magnéticos, scroll secuestrado y bucles decorativos | Movimiento causal y acotado, con inicio, cambio y resolución. |

### Excepciones y función

- Una petición explícita puede habilitar un recurso, con alcance concreto. Registra recurso, ubicación y pedido que lo habilita. «Premium», «moderno», «editorial» o «como esta referencia» no anulan la tabla.
- Un pedido explícito de hero animado, video con glitch o pieza audiovisual exige construir esa expresión en el alcance nombrado. Las transformaciones y transiciones necesarias de esa pieza no requieren una nueva consulta por cada efecto. Conserva los bloqueos independientes: el género cyberpunk por sí solo no habilita gradientes, Inter o varios CTAs.
- Si una referencia elegida contiene un recurso bloqueado, explica cómo conservar su intención con otro tratamiento. Pregunta por una excepción solo si el conflicto impide cumplir una instrucción concreta.
- Los labels de formularios, breadcrumbs, foco visible, subrayado convencional de enlaces y categorías funcionales son semántica, no eyebrows o énfasis ornamental.
- Guardar, cancelar, editar o paginar son controles funcionales. La regla de un CTA no limita artificialmente las acciones necesarias de una aplicación.
- Una escala de color necesaria para interpretar un dato debe ser semántica y explicable; no sirve de excusa para introducir fondos decorativos.
- Un indicador de procesamiento real puede necesitar un bucle. Debe tener propósito verificable, alternativa accesible y finalizar con el estado correspondiente.
- Las simulaciones no habilitan avisos de «demo», «prueba» o «vista previa» en el producto por defecto. Declara sus límites en la conversación; añade etiquetas al producto solo cuando el usuario las pide o se acuerdan expresamente.

## 3. Entrevista integrada

Para creación o rediseño abiertos, realiza al menos **15 preguntas sustantivas** en rondas de **3 a 5**. Espera las respuestas de una ronda antes de preguntar por decisiones que dependan de ellas. Cada pregunta puede ofrecer 2–3 opciones explicadas y una recomendación contextual, sin preseleccionar silenciosamente la respuesta.

Inspecciona por tu cuenta lo que el proyecto puede responder. No preguntes qué librerías o archivos existen. Si el prompt ya resuelve una pregunta, conserva la respuesta y usa ese espacio para profundizar otra decisión: no repitas preguntas ni rellenes la cuota con preferencias irrelevantes.

Estas quince preguntas son la base adaptable de la entrevista:

1. ¿Qué tiene que conseguir la persona al usar esto? Define un resultado concreto.
2. ¿Para quién lo diseñamos y qué conocimientos o dificultades trae?
3. ¿Cuál es la acción principal que queremos facilitar?
4. ¿En qué contexto y dispositivos lo usará: primera visita, uso frecuente, poco tiempo o sesiones largas?
5. ¿Qué contenido es indispensable y qué debe quedar afuera?
6. ¿Qué necesita entender o confiar antes de actuar?
7. ¿Qué tres cualidades debería transmitir? Explica opciones como preciso, cálido, técnico, editorial, sobrio o lúdico.
8. ¿Qué te gusta exactamente de las referencias elegidas: estructura, ritmo, tipografía, imágenes o comportamiento?
9. ¿Qué querés evitar además de los bloqueos predeterminados?
10. ¿Qué papel debería tener la tipografía: funcional, protagonista, compacta o editorial?
11. ¿Qué carácter debería tener el color y qué restricciones reales existen?
12. ¿Qué llevará el peso visual: producto real, fotografía, ilustración, datos o composición tipográfica?
13. ¿Qué debe explicar o expresar el movimiento, y qué momentos necesitan tranquilidad?
14. ¿Qué tarea debe poder completarse en mobile con la misma claridad que en desktop?
15. ¿Qué situaciones frustrarían más a la persona y cómo debería recuperarse de ellas?

Las repreguntas deben resolver ambigüedades. Ante «minimalista», distingue cantidad de información, decoración y espacio. Ante «dinámico», distingue feedback, narrativa y actividad ambiental. No pidas que el usuario domine vocabulario de diseño.

La entrevista termina cuando se han trabajado las quince preguntas y están claras tarea, jerarquía, dirección y restricciones. Si quedan decisiones que afectan esas bases, profundiza antes de generar o construir. No presentes las quince preguntas juntas como un formulario rígido.

## 4. Dirección y referencia visual

Tras la entrevista o ante una dirección ya definida, lee [dirección visual](references/visual-direction.md). Produce una ficha breve con objetivo, audiencia, acción principal, contenido, idea visual dominante, tipografía, color, imágenes, motion, prioridad mobile y excepciones explícitas. Separa decisiones del usuario de recomendaciones y suposiciones.

Cuando se pidan estilos o alternativas, consulta la [biblioteca de estilos y lenguajes visuales](references/style-library.md). Conserva el repertorio de referencias y elige familias por el brief; un estilo no impone un efecto, un componente ni una excepción a los bloqueos.

Traduce los requisitos explícitos a un contrato positivo: pedido → resultado observable → evidencia que lo validará. Incluye el carácter visual y el protagonismo del material, además de las funciones. Un claim, una familia tipográfica o un color aislados no demuestran una dirección. Si el pedido exige una escena animada protagonista, un retrato fijo con variaciones mínimas no satisface ese contrato.

Define `DESIGN_VARIANCE`, `MOTION_INTENSITY` y `VISUAL_DENSITY` según el caso y explica su efecto visible. Son controles de diseño, no pesos internos del modelo ni parámetros exactos de render. Una referencia elegida determina la composición por encima de esos controles.

Cuando necesites resolver cómo presentar, ordenar, comparar, explorar, operar o narrar contenido, consulta el [catálogo de decisiones visuales](references/creative-library.md). Elige por el problema del brief y comprueba su criterio mobile; evita acumular patrones por variedad. El tablero de ocho estilos explora direcciones; el catálogo ayuda a convertir la dirección elegida en una interfaz concreta.

### Si pide referencias desde el primer prompt

Con producto, audiencia y objetivo claros, crea temprano **un tablero de ocho direcciones A–H**, normalmente en una imagen 4 × 2. No esperes a terminar toda la entrevista para ayudar a elegir un lenguaje visual. Si falta ese contexto mínimo, pregunta solo lo necesario primero.

Mantén el mismo brief y contenido en las ocho celdas. Varía composición, jerarquía y lenguaje visual de forma sustancial. Todas respetan los bloqueos. Usa una herramienta de generación de imágenes disponible cuando se soliciten propuestas generadas; identifica las referencias reales y sus fuentes. No presentes una imagen sintética como un sitio real.

El tablero sirve para comparar dirección, no para aprobar legibilidad en miniatura. Acompáñalo con una leyenda A–H y amplía la opción elegida. Si se combinan opciones, define una dirección dominante y una síntesis coherente.

### Imagen del resultado elegido

Al cerrar el brief, ofrece una sola vez: «La dirección elegida es [resumen]. ¿Querés que genere una referencia visual de cómo quedaría, incluyendo desktop y mobile?».

- Si ya pidió esa imagen, genérala cuando el brief esté listo sin volver a preguntarlo.
- Si acepta la imagen, muéstrala y espera su elección o correcciones antes de implementar desde ella. Una imagen genérica no sustituye la composición mobile.
- Si declina y la implementación está pedida, continúa con la dirección acordada; las imágenes no son una puerta obligatoria.
- Si aporta una referencia suficiente, analízala y úsala; no generes alternativas adicionales sin motivo.
- Si la generación no está disponible, explica el límite. Ofrece un wireframe o especificación como alternativa y deja que el usuario elija; nunca afirmes que generaste una imagen.

## 5. UX e implementación

Antes de construir o revisar un flujo, lee [UX](references/ux.md). Resuelve tarea, jerarquía, navegación, estados relevantes, errores, recuperación y accesibilidad. Usa contenido real o simulaciones acordadas. No inventes funcionalidades para llenar espacio.

En código existente, conserva su stack, tokens y componentes. Comprueba dependencias y versiones antes de importar. En proyectos nuevos, elige la solución más simple que cumpla el producto; no impongas React, Tailwind, un paquete de iconos o un motor de animación.

Separa comportamiento donde mejore la claridad. Prefiere estado cercano a su uso y reutiliza patrones del proyecto. Los límites servidor/cliente solo se aplican si el framework los soporta; los componentes servidor pueden cargar datos. No reduzcas un sistema entero a componentes estáticos para cumplir una receta.

Crea jerarquía con espaciado, agrupación y tipografía antes de añadir superficies. Elige Grid o Flex según la relación del contenido. Reserva dimensiones de imágenes y medios para mantener estable el layout. Usa las capacidades reales de cada biblioteca y comprueba su API.

Cuando se añada o cambie movimiento, lee [motion](references/motion.md). Selecciona el motor existente o la herramienta mínima necesaria y conserva el comportamiento funcional sin animación.

Cuando el hero o una demostración animada definan el pedido, construye y revisa primero esa pieza con sus medios reales, tipografía, CTA y encuadre. Observa la secuencia completa a velocidad normal en el viewport objetivo antes de extender esa dirección al resto de la superficie. No requiere una aprobación humana adicional si el usuario ya delegó la implementación; requiere una evaluación honesta contra el brief. Corrige los desvíos materiales antes de multiplicarlos en otras secciones.

Respeta el material visual rechazado: si se descarta una imagen base, revisa también sus derivados y reutilizaciones en cards u otras piezas del alcance. Elige muestras variadas por lo que deben demostrar, sin repetir un asset por comodidad ni inventar resultados que el producto no produce.

## 6. Verificar y entregar

Toda implementación visual requiere [verificación responsive y mobile](references/mobile-qa.md). Inspecciona el render en un navegador disponible y recorre el flujo afectado. Mantén la superficie de navegador que el usuario haya pedido. Si faltan herramientas, entrega el trabajo posible y declara con precisión qué no se pudo verificar.

Aplica la [aceptación del brief](references/acceptance.md) en tres revisiones independientes: **funcionamiento**, **fidelidad al brief** e **impacto temporal** cuando se solicita movimiento. Cada requisito explícito necesita su propio resultado. No promedies las revisiones ni compenses un fallo expresivo con orden, usabilidad o compilación. Una revisión pendiente permanece pendiente.

Compara contra la referencia usando el mismo viewport, posición de scroll y estado. Revisa proporciones, saltos de línea, encuadre, distancias, imágenes, acciones y lectura mobile. El ancho total sin overflow no demuestra por sí solo buena UX mobile.

Para revisar código nuevo o modificado, usa el [auditor estático](references/source-audit.md) cuando haya Python 3 disponible. Detecta patrones de gradientes, Inter y bucles que necesitan contexto; no evalúa gusto, UX ni accesibilidad. Revisa sus hallazgos y realiza siempre la inspección visual.

El resultado `0` del auditor, ausencia de overflow, un build correcto o fotogramas con píxeles distintos son evidencia técnica acotada. Ninguno aprueba por sí solo la identidad visual, el protagonismo, el ritmo o la transformación solicitados. Para motion protagonista debes observar reproducción real; una captura o un contador de frames no sustituyen esa evaluación.

Antes de entregar, comprueba:

- Los bloqueos se cumplen o tienen una excepción explícita y acotada.
- Se reconoce la tarea principal y el contenido tiene una jerarquía deliberada.
- Los rasgos visuales, el material protagonista y cada requisito explícito del brief están visibles en el resultado y tienen evidencia pertinente.
- Los controles y estados afectados funcionan; no se presenta una animación como prueba de éxito real.
- Si se pidió una demostración animada, la secuencia tiene transformación perceptible, ritmo y resolución; se observó completa en su encuadre real.
- La composición y operación mobile se comprobaron en anchos representativos, límites de breakpoints y rangos intermedios.
- Teclado, foco, contraste y movimiento reducido se revisaron donde corresponde.
- El resultado conserva la dirección acordada y las decisiones aprobadas fuera del cambio.

Entrega qué cambió, por qué, qué se verificó y qué límites quedan. Distingue generación de imagen, código escrito, render observado y uso real. No prometas una evaluación estética infalible ni pruebas en dispositivos o asistentes donde no se ejecutó el flujo.

Ante «no me convence», identifica si falla composición, tipografía, densidad, color, imágenes, UX o movimiento; pregunta lo mínimo para resolverlo y modifica esa dimensión conservando el resto.
