# UX: de la tarea al comportamiento

Lee este documento al diseñar, implementar o auditar un flujo. Ajusta la profundidad a la tarea; un cambio de espaciado no requiere rediseñar la navegación.

## Tarea y jerarquía

Describe quién llega, qué necesita, qué información requiere antes de actuar y cómo reconoce el resultado. Elige una prioridad por pantalla o bloque de decisión. Las acciones de apoyo tienen menor peso visual, sin perder accesibilidad.

Organiza según frecuencia, secuencia y significado. Usa divulgación progresiva cuando la complejidad pueda esperar. Evita esconder información imprescindible detrás de interacción exploratoria. Conserva términos y patrones reconocibles en navegación, filtros, búsqueda y edición.

Prueba la lectura rápida sobre el render: qué estoy viendo, para qué sirve y qué puedo hacer. Si depende de explicar verbalmente la pantalla, revisa el contenido y la jerarquía.

## Estados que corresponden al producto

Para cada interacción afectada, considera únicamente los estados que existen:

| Estado | Criterio |
| --- | --- |
| Inicial | Ayuda a reconocer la tarea y comenzar. |
| Carga | Explica la espera real; reserva espacio y conserva contexto útil. |
| Vacío inicial | Indica qué falta y cómo empezar. |
| Sin resultados | Conserva filtros o consulta y permite corregirlos. |
| Error | Identifica el problema y ofrece una recuperación concreta. |
| Éxito | Confirma un resultado que ocurrió, en el lugar pertinente. |
| Deshabilitado | Explica el requisito cuando no resulta evidente. |
| Selección o edición | Hace reconocible qué se afecta y cómo terminar o deshacer. |

No introduzcas loaders en operaciones instantáneas ni demoras artificiales para mostrar animaciones. Un skeleton solo sirve si representa una estructura esperada; un indicador breve y accesible puede ser mejor para una espera indeterminada.

En prototipos, declara qué estados son simulados y qué acciones no están conectadas. Una respuesta visual no demuestra persistencia ni ejecución real.

## Formularios y recuperación

- Usa labels visibles y asociados; el placeholder no los sustituye.
- Agrupa campos relacionados, señala obligatoriedad y explica requisitos antes del error.
- Usa tipos de input, autocomplete e inputmode adecuados al dato.
- Valida en el momento útil, conserva valores y coloca el error junto al campo.
- Conecta mensajes y campos para tecnologías de asistencia; evita depender solo de color.
- Impide envíos duplicados durante una operación real y permite reintentar cuando falla.
- Mantén la persona en contexto al completar o corregir. Considera deshacer para acciones reversibles y protección proporcionada para acciones destructivas.

No añadas campos que el producto no necesita. En flujos por pasos, permite reconocer avance y volver sin perder datos cuando sea viable.

## Accesibilidad y previsibilidad

Usa HTML semántico antes de recrear controles. Revisa nombres accesibles, orden de tabulación, activación por teclado, foco visible y contraste de texto y controles. Comprueba el contraste con una herramienta o cálculo; mirar el color no lo verifica.

Las imágenes informativas necesitan texto alternativo basado en su contenido observado. Reserva `alt=""` para decoración real. Si todavía falta la imagen, registra esa integración como pendiente; no presentes un alt vacío de una fotografía protagonista como accesibilidad resuelta.

El orden de lectura y foco debe conservar sentido en todas las composiciones. No alteres solo el orden visual de forma que teclado y lector de pantalla recorran otra historia.

En diálogos, lleva el foco al contexto adecuado, mantenlo dentro de un modal real y restáuralo al cerrar. Proporciona salida por teclado y un control visible. Evita que banners, barras fijas o teclado oculten el elemento activo.

Los cambios de estado importantes deben percibirse sin exigir mirar un único punto o interpretar una animación. Usa anuncios accesibles proporcionados cuando el cambio no se comunica de otro modo.

## Contenido y complejidad

Usa verbos concretos para acciones y los mismos nombres para las mismas entidades. Los mensajes de error deben responder qué pasó y qué se puede hacer. Evita lenguaje espacial como «a la izquierda» si la composición cambia en mobile.

Prueba títulos y nombres largos, acentos, distintas cantidades, listas numerosas, listas vacías y contenido faltante. La traducción o el texto real no deberían desarmar una composición preparada solo para frases cortas.

No añadas búsqueda, tabs, filtros, notificaciones, dark mode o secciones por parecer propios de una aplicación. Cada elemento necesita una tarea o un requisito que lo justifique.

## Evidencia de cierre

Recorre la tarea principal y al menos su recuperación relevante. Informa qué estados se observaron, cuáles se simularon y qué no se pudo ejecutar. Una captura prueba apariencia; el recorrido aporta evidencia del comportamiento.
