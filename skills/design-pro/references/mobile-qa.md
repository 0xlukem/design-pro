# Responsive y mobile con evidencia

Lee este documento antes de entregar una implementación o auditoría visual. Aplica el recorrido a las pantallas y comportamientos afectados; amplía cuando el cambio alcance un componente compartido.

## Composición mobile

Decide prioridades de lectura, acción, navegación, recortes, densidad y elementos fijos. La pantalla pequeña necesita su propia composición coherente con la dirección elegida. Evita resolverla únicamente reduciendo la fuente o apilando todo sin jerarquía.

Conserva la tarea y la información esencial. Si una tabla requiere dos dimensiones, puede usar un contenedor de scroll reconocible; eso no justifica overflow horizontal de toda la página. Comprueba que los controles no queden fuera de alcance.

Si se produce una referencia visual, muestra desktop y mobile de la misma dirección. El tablero de estilos no sustituye esta decisión.

## Elegir anchos y breakpoints

Inspecciona los breakpoints reales de los componentes afectados. Ajusta la composición donde el contenido deja de funcionar, sin asumir que las clases estándar cubren todos los rangos.

| Grupo | Puntos de prueba de partida |
| --- | --- |
| Mobile | 320, 360, 390 y 430 CSS px. |
| Tablet | 768 o 820, y 1024 si cambia estructura u orientación. |
| Desktop | 1280 o 1440; 1920 o mayor cuando la superficie lo requiere. |
| Límites | Para cada breakpoint relevante B, comprobar B−1, B y B+1. |
| Rangos | Redimensionar entre puntos para encontrar anchos intermedios rotos. |

Estos anchos son puntos de verificación, no una exigencia de crear media queries para cada uno. En un ajuste acotado, realiza la comprobación profunda donde cambia el comportamiento y una regresión proporcionada en los otros rangos.

Ejemplo: si el menú cambia a 768 px, revisar 767, 768 y 769. Si el texto falla a 910, corregir ese rango aunque no sea una medida de dispositivo habitual.

## Revisar contenido y espacio

- Desbordamiento horizontal de página y de componentes; no ocultarlo globalmente para hacer pasar la prueba.
- Saltos de títulos, ancho de lectura, tamaños legibles y espaciado entre secciones.
- Encuadre completo: cuánto contenido, imagen y siguiente acción se ve en la altura disponible.
- Protagonismo prometido: comprobar que el medio o la demostración pedidos dominen donde corresponde y no queden desplazados debajo del primer encuadre por el texto o los controles.
- Imágenes con dimensiones reservadas, recorte pertinente y resolución adecuada.
- Nombres y títulos largos, acentos, cantidades grandes, vacíos, listas extensas y datos faltantes.
- Cambios de fuente o carga de medios que alteran la composición.

## Revisar operación

Recorre las acciones principales por touch emulado o real y por teclado. Comprueba menú, búsqueda, filtros, formularios, diálogos y recuperación de errores según el producto.

Usa 44 × 44 CSS px como objetivo práctico de área táctil, con separación suficiente. Es una decisión de calidad de esta skill, no una afirmación de que todo criterio AA exige 44 px. Los iconos pueden ser pequeños dentro de un área interactiva adecuada.

Revisa orden de foco, control enfocado visible, zoom y movimiento reducido. Comprueba que un sticky o una barra flotante no tape texto, resultados ni acciones.

Comprueba alturas bajas y orientación horizontal donde afecten la operación. En formularios, considera teclado virtual, scroll al campo activo y controles de envío. Si el entorno permite observar un dispositivo real, verifica también barras del navegador y áreas seguras.

No elijas `100dvh` universalmente: usa altura por contenido, `svh` estable o `dvh` adaptable según el comportamiento esperado. El teclado virtual y las barras del navegador requieren observación específica; una captura desktop estrecha no demuestra su funcionamiento.

## Capturas y recorrido

Usa el mismo viewport, scroll y estado al comparar referencia, antes y después. Recorre la página con scroll real antes de capturar secciones cuya aparición depende del scroll. Espera la carga y el tamaño final de los medios.

Incluye el viewport real del panel o ventana donde se evalúa el trabajo si se conoce; no compruebes solo presets amplios. Registra ancho, alto y posición del medio protagonista. Un hero correcto a 1440 px puede relegar su demostración en una ventana más estrecha aunque no haya overflow.

Si se solicitó una escena animada, observa el mismo ciclo en el encuadre mobile y en el principal. Adaptar el coste o la disposición no debe convertirla silenciosamente en la imagen fija que el brief descartó. La alternativa accesible con movimiento reducido conserva el significado y se evalúa por separado.

Las capturas prueban composición. Ejecutar acciones prueba comportamiento. Combina ambos cuando el pedido incluya interacción.

La fidelidad al brief y el impacto temporal se registran además de los resultados responsive en [aceptación](acceptance.md). El resultado sin overflow no compensa un medio protagonista invisible o un lenguaje visual distinto del pedido.

Para trabajo amplio, conserva un registro de evidencia proporcional:

| Pantalla o flujo | Viewport y estado | Composición | Operación | Evidencia o pendiente |
| --- | --- | --- | --- | --- |
| Elemento revisado | Ancho × alto, orientación, estado | Resultado observado | Acción y resultado | Captura, traza o limitación concreta |

No rellenes esta tabla con aprobaciones supuestas. Registra solo lo ejecutado. Los screenshots y logs pueden permanecer como material temporal de trabajo; no deben convertirse automáticamente en entregables del producto.

## Qué significa verificado

- «Responsive revisado» requiere render observado en los rangos afectados y recorrido de los estados relevantes.
- «Mobile emulado» identifica una prueba con viewport, touch o perfil emulado.
- «Dispositivo real» solo describe una prueba efectuada en ese dispositivo.
- «Accesibilidad revisada» enumera qué se comprobó; no implica una certificación completa.
- Si el navegador o una superficie no están disponibles, declara la limitación y las revisiones efectivamente realizadas. No sustituyas evidencia por una promesa.

## Referencias técnicas

- [web.dev: breakpoints según contenido](https://web.dev/learn/design/media-queries)
- [web.dev: diseño responsive accesible](https://web.dev/articles/accessible-responsive-design)
- [web.dev: viewport pequeño, grande y dinámico](https://web.dev/blog/viewport-units)
- [W3C: Reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html)
- [W3C: Target Size (Enhanced)](https://www.w3.org/WAI/WCAG22/Understanding/target-size-enhanced.html)
