# Dirección visual y referencias

Lee este documento para definir una dirección, producir referencias o evaluar si una propuesta tiene identidad. Los bloqueos y sus excepciones viven únicamente en la sección 2 de `SKILL.md` y siguen vigentes en toda exploración.

## Ficha de dirección

Devuelve una ficha que permita tomar decisiones durante el trabajo. Adapta su longitud al proyecto:

| Campo | Debe resolver |
| --- | --- |
| Producto, audiencia y tarea | Qué usa la persona, para qué y en qué contexto. |
| Acción y jerarquía | Qué se reconoce primero, qué necesita entender y qué hace después. |
| Contenido | Qué existe realmente, qué falta y qué simulaciones se acordaron. |
| Idea visual | Una frase concreta que describa la relación entre contenido y composición. |
| Sistema | Familias tipográficas disponibles, escala, paleta plana, espaciado, superficies e imágenes. |
| Comportamiento | Qué explica el movimiento y dónde permanece quieta la interfaz. |
| Mobile | Prioridad de lectura, navegación y acción en pantalla pequeña. |
| Controles | Valores efectivos de `DESIGN_VARIANCE`, `MOTION_INTENSITY` y `VISUAL_DENSITY`, con su efecto visible. |
| Procedencia | Decisiones del usuario, recomendaciones, suposiciones, origen de los valores y excepciones expresas. |

Una idea como «archivo de piezas con índice lateral y fotografía protagonista» orienta decisiones. Adjetivos como «premium, moderno y limpio» necesitan concretarse antes de guiar una implementación.

La ficha puede vivir en la conversación. Guárdala en el proyecto si es parte de lo pedido o el trabajo necesita un documento persistente; no crees documentación auxiliar para cada ajuste.

## Controles de Taste y sus niveles

Los valores iniciales están definidos en `SKILL.md`; ese es el único lugar donde se configura el punto de partida. Conserva los tres controles explícitos en la ficha, aunque el usuario responda en lenguaje natural. Ajusta los valores efectivos al producto y registra si provienen del brief, una referencia, una elección del usuario o el perfil inicial.

| Control | 1–3 | 4–7 | 8–10 |
| --- | --- | --- | --- |
| `DESIGN_VARIANCE` | Retícula estable, alineaciones consistentes y proporciones repetidas. | Desplazamientos controlados, cambios de proporción, ritmo entre texto e imágenes. | Composición expresiva: masas de distinto tamaño, asimetría marcada y secuencia visual propia. |
| `MOTION_INTENSITY` | Feedback inmediato y transiciones discretas, normalmente sin entradas automáticas. | Continuidad espacial, cambios de estado perceptibles y un gesto expresivo acotado. | Coreografía protagonista, transiciones espaciales o secuencias ligadas al contenido y justificadas por el producto. |
| `VISUAL_DENSITY` | Pocas unidades, ancho de lectura controlado y separación generosa. | Lectura cotidiana equilibrada y agrupación por tarea. | Información frecuente y compacta, filas o columnas precisas y controles que conservan legibilidad. |

La alta variación no obliga a usar masonry, superposiciones ni espacios vacíos gigantes. La alta intensidad no habilita adornos bloqueados ni bucles. La alta densidad no justifica controles diminutos. Registra la razón de cada elección, no una precisión numérica ficticia.

En el tablero A–H, cada dirección puede explorar un perfil distinto; anota sus diferencias cuando ayuden a elegir. En la dirección seleccionada, conserva un perfil único y adapta su expresión a cada dispositivo: mobile no hereda superposiciones que impidan operar.

## Escala tipográfica y pesos

Define una escala y papeles concretos en lugar de depender de «tipografía premium». Como referencias iniciales ajustables: cuerpo de 16 px relativos al tamaño raíz; texto largo de unas 45–65 letras por línea; títulos de 32–40 px en mobile y 48–64 px en desktop cuando el contenido lo admita. Son referencias de composición, no tamaños obligatorios para todos los productos.

| Papel | Referencia de peso | Criterio |
| --- | --- | --- |
| Texto de lectura | 400 | Mantener lectura cómoda y contraste suficiente. |
| Labels y acciones | 500–600 | Diferenciar función sin convertir cada control en protagonista. |
| Encabezados | 500–700 | Construir jerarquía junto con tamaño, espacio y proporción. |
| Datos | Peso consistente y cifras tabulares cuando convenga | Facilitar comparación; monospace solo si sirve a la dirección. |

Comprueba qué pesos y caracteres ofrece la familia real. Una familia editorial puede resolver jerarquía con otros pesos; no fuerces negrita sintética ni uses una mezcla ornamental de estilos dentro de una palabra. Mantén los bloqueos de tipografía del núcleo.

## Tablero de ocho direcciones

Úsalo cuando se pidan referencias o una exploración de ocho estilos. Conserva producto, audiencia, contenido y acción principal para que la comparación tenga sentido.

Una biblioteca inicial posible:

| Dirección | Decisión a explorar |
| --- | --- |
| Editorial tipográfica | Ritmo de lectura y tipografía como estructura. |
| Utilitaria técnica | Densidad, precisión y operación repetida. |
| Modernista cálida | Proporción, espacio y cercanía. |
| Industrial | Estructura, señalización, contraste y materiales. |
| Brutalismo sobrio | Jerarquía directa y composición deliberadamente cruda. |
| Archivo cultural | Clasificación, índices y relaciones entre piezas. |
| Fotográfica | Encuadre, secuencia de imágenes y diálogo con el texto. |
| Lúdica geométrica | Forma, color plano y comportamiento expresivo. |

Adapta o reemplaza estas familias según el producto; no es una lista obligatoria para cada tablero. Las diferencias deben exceder paleta y fuente. Cada propuesta debe cambiar al menos una decisión estructural relevante: jerarquía, composición, uso de imágenes o forma de explorar el contenido.

Para una imagen 4 × 2, reserva una celda coherente por dirección y acompaña el resultado con una leyenda A–H. Comprueba el tablero generado: ocho celdas distintas, correspondencia clara con la leyenda y cumplimiento de los bloqueos. Si una celda viola el brief, corrígela antes de ofrecerla como opción. La generación de imágenes puede producir texto imperfecto; no lo presentes como copy aprobado.

Para referencias reales, inspecciona las pantallas antes de citarlas y enlaza su fuente. Explica qué se toma y qué se descarta. No atribuyas una propuesta generada a un producto real.

## Prompt de generación adaptable

Adjunta las imágenes reales que tengas disponibles; no afirmes haberlas adjuntado cuando solo se proporcionó una descripción. Construye el prompt con:

1. Producto, audiencia, tarea y contenido acordados.
2. Tipo de resultado: tablero A–H o pantalla detallada de una dirección elegida.
3. Dimensiones y relación de aspecto. Para pantalla detallada, define desktop y mobile por separado o en dos marcos claramente separados.
4. Composición, tipografía, color, imágenes y densidad acordados.
5. Todos los bloqueos aplicables de la sección 2 de `SKILL.md` y las excepciones expresas.
6. Requisito de contenido legible, jerarquía clara y una acción principal; sin inventario de funcionalidades para llenar espacio.

Pide contenido de interfaz sin marco de dispositivo o chrome de navegador, salvo solicitud expresa. No estires una composición desktop para rellenar un marco mobile. Recompón según sus prioridades.

Si faltan imágenes del producto, pregunta por su uso cuando sea decisivo o propone una dirección que pueda sostenerse con el material real. No sustituyas automáticamente imágenes pertinentes por fotos aleatorias o ilustraciones decorativas.

## Evaluación visual y feedback

Compara la referencia elegida con el render, no con una descripción de cómo debería verse. Revisa las relaciones entre elementos y el encuadre completo, además de los detalles aislados.

Usa estos criterios de aceptación:

- La pantalla comunica producto, tarea y siguiente paso sin una explicación externa.
- La idea visual se reconoce en decisiones conectadas de tipografía, composición, imágenes y comportamiento.
- La pieza se sostiene con su contenido específico; no depende de métricas o decoración de relleno.
- La jerarquía sigue funcionando con texto real y al pasar a mobile.
- Los espacios, alineaciones, saltos, recortes y estados muestran intención y coherencia.
- El resultado respeta la referencia y las correcciones ya acordadas.

Si alguien dice «no me convence», localiza la dimensión afectada antes de regenerar todo. En una mezcla de referencias, elige una dirección dominante y explica cómo se integrará el gesto secundario.
