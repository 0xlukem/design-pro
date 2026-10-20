# Motion con propósito

Lee este documento cuando el pedido incluya movimiento o se modifiquen animaciones. Los bloqueos y excepciones están en `SKILL.md`; un nivel alto de intensidad no los desactiva.

## Diseñar el cambio

Describe cada animación importante con este contrato:

| Campo | Pregunta |
| --- | --- |
| Disparador | ¿Qué acción o cambio real la inicia? |
| Propósito | ¿Explica relación, estado, foco o identidad? |
| Transformación | ¿Qué cambia y qué permanece como ancla? |
| Resolución | ¿En qué estado usable termina y cuándo? |
| Alternativas | ¿Cómo funciona con touch, teclado y movimiento reducido? |

Si no puedes describir el propósito, conserva la interfaz quieta. El movimiento debe terminar donde deja a la persona lista para continuar.

El protagonismo expresivo es un propósito válido cuando forma parte del brief. No reduzcas ese pedido a un hover o a feedback de controles por considerar que toda animación debe ser utilitaria. Distingue una demostración conceptual de una salida real del producto y no atribuyas al producto transformaciones que no soporta.

## Pieza protagonista y secuencia

Cuando se pide un hero audiovisual, una escena totalmente animada o una demostración potente, define antes de extender el diseño:

- **Material:** qué existe en la escena y qué assets se aceptaron o rechazaron.
- **Transformación:** cambio de estructura, materia, forma o relación que la persona debe percibir.
- **Secuencia:** estado inicial → desarrollo → cambio principal → resolución; el retorno también se diseña si la pieza se repite.
- **Encuadre y lectura:** cuánto ocupa la pieza, qué se ve al entrar y cómo convive con el CTA y el título en cada superficie.
- **Ritmo y amplitud:** tiempos de acción y lectura, variación suficiente para cumplir el brief y estabilidad donde se necesita actuar.

Como ejemplo de estructura, una señal puede aparecer, reconstruirse, interrumpirse y resolver en una composición distinta. Elige las fases y su duración según el contenido; no impongas esta secuencia a todas las piezas.

Implementa y observa primero el ciclo completo con el medio real. Si el brief exige transformación protagonista, variar ruido o tracking sobre la misma imagen no basta por el simple hecho de producir frames distintos. Lo mismo ocurre con un crossfade genérico entre estados cuando se pidió una transformación específica.

Un loop expresamente solicitado puede tener narrativa y propósito. Registra su alcance y haz legible su progresión; conserva pausa, accesibilidad y adaptación al dispositivo. La regla contra bucles ornamentales no debe neutralizar una pieza audiovisual pedida explícitamente.

Las cards o muestras deben demostrar lo que anuncian. Si prometen un comportamiento animado, una captura a un tiempo fijo no lo demuestra. Si la tarea solo requiere comparar apariencia estática, una muestra fija puede ser correcta: registra la diferencia sin convertir todas las cards en animaciones por obligación.

## Personalidad coherente

Elige cualidades concretas según el producto: preciso, mecánico, pesado, elástico, delicado o enérgico. Define una familia breve de duraciones, recorridos y curvas. La masa percibida y la distancia informan el timing; ninguna curva de resorte es universalmente «premium».

Usa un gesto distintivo dominante por flujo o sección protagonista, acompañado de transiciones discretas. La expresividad puede ser intensa donde ayude a la narrativa; el contenido de trabajo frecuente necesita estabilidad y respuesta inmediata.

Como punto de partida ajustable, el feedback directo suele requerir decenas de milisegundos y las transiciones locales unos pocos cientos. Observa el resultado: la duración no debe retrasar la tarea ni impedir leer. No añadas esperas artificiales para completar una coreografía.

### Referencias numéricas de timing y física

Conserva parámetros concretos como puntos de partida revisables, nunca como garantía estética o de rendimiento:

| Situación | Referencia inicial | Ajuste |
| --- | --- | --- |
| Respuesta a presión o hover | 80–150 ms | La acción se reconoce inmediatamente y sigue accesible sin hover. |
| Cambio local o salida breve | 150–250 ms | Mantener continuidad sin demorar la siguiente acción. |
| Expansión, detalle o cambio de contexto | 250–400 ms | Relacionar origen y destino con una resolución legible. |
| Cascada justificada | Separación de 30–70 ms, presupuesto total breve | Evitar que el último elemento útil espere para poder usarse. |
| Resolución precisa | Asentamiento sin rebote perceptible | Adecuada cuando la posición final importa para leer, comparar o accionar. Ajustar la curva a la distancia. |
| Resolución elástica | Un sobrepaso breve como máximo, si la dirección lo justifica | Ajustar masa y amortiguación en la API instalada hasta lograr ese comportamiento; comprobar interrupción y repetición. |

Registra los valores elegidos para el gesto dominante y sus variantes cuando la dirección dependa del movimiento. Si el motor no usa esos parámetros físicos, conserva el carácter observable mediante sus controles propios. La tabla es una referencia de diseño; verifica la implementación en el render.

## Ejemplos causales

| Situación | Relación a preservar |
| --- | --- |
| Reordenar | La pieza conserva continuidad, hace visible origen y destino y se asienta donde queda. |
| Filtrar | El conjunto permite entender qué permanece, qué sale y qué aparece. |
| Abrir detalle | El elemento elegido conecta con el contexto ampliado y permite volver a su origen. |
| Cambiar vista | La persona mantiene una referencia de posición o selección. |
| Confirmar una acción | La respuesta acompaña el resultado real en el lugar pertinente. |
| Revelar una secuencia editorial | El cambio ayuda a leer una relación o historia propia del contenido. |

Estos ejemplos explican decisiones; no son recetas para añadirlas a todos los productos. Evita simular datos que se reordenan o actividad que no sucede.

## Implementación y coste

Reutiliza el motor instalado y comprueba su versión y API. CSS puede bastar para transiciones pequeñas; un motor adicional necesita una necesidad concreta. Motores distintos pueden coexistir en partes independientes, pero no deben competir por la misma propiedad del mismo elemento.

Para cambios continuos, evita actualizaciones de estado que rerendericen el árbol cada frame. Usa mecanismos adecuados del motor, valores mutables o una animación nativa. Prioriza transform y opacity cuando cumplan el efecto; no prometas aceleración GPU o fluidez sin observar su coste.

Las transiciones de geometría necesitan una estrategia consciente de layout, transformaciones o API nativa; medir y escribir layout repetidamente puede ser costoso. No uses `transition: all`: declara las propiedades necesarias.

Limpia listeners, observers, timelines y timers al salir. Pausa trabajo continuo cuando no se ve o la pestaña queda inactiva. Usa `will-change` solo cuando sea útil y retíralo cuando corresponda.

`memo` no es una garantía de rendimiento. Aísla el trabajo por responsabilidad y mide el problema real antes de añadir optimizaciones. Mantén una versión usable si el script tarda, falla o no llega a ejecutar la entrada.

## Touch y accesibilidad

El efecto hover es un enriquecimiento para punteros capaces. Toda acción y dato esencial deben estar disponibles por touch y teclado. Un elemento que se mueve persiguiendo el cursor no puede dificultar acertar el control.

Con `prefers-reduced-motion`, simplifica o elimina movimiento no esencial conservando resultado, foco y feedback. Mantén el contenido visible; un elemento con opacity 0 a la espera de una animación desactivada es un fallo.

Si existe movimiento automático funcional, ofrece control cuando corresponda y evita interferir con la lectura. Un indicador de procesamiento debe terminar al resolver la operación; la app no puede aparentar actividad perpetua.

## Verificar ritmo y comportamiento

Observa la secuencia completa: entrada, interrupción, repetición, salida y retorno. Prueba acción rápida, cambio de estado antes de que termine y preferencia de movimiento reducido.

Una imagen no valida ritmo. Cuando el movimiento define la propuesta, ofrece una prueba interactiva corta con pausa y repetición; agrega scrub o velocidad reducida si ayudan a revisar. No generes un video o estudio costoso por defecto para un hover sencillo.

Informa qué se observó y bajo qué condiciones. Si afirmas un objetivo de frames por segundo, acompáñalo con una medición del recorrido y dispositivo o entorno usado.

### Impacto temporal independiente

Evalúa a velocidad normal la lectura del cambio principal, amplitud, progresión, pausas y resolución. Revisa también primer encuadre, final, retorno y cambio de ejemplo. Un control Pause funcional verifica reproducción; no demuestra calidad de coreografía.

Conserva una grabación o una referencia de reproducción observada, más fotogramas de las fases relevantes si ayudan a comparar. Una contact sheet comunica estructura, pero no sustituye mirar la secuencia en tiempo real. Si no puedes observar reproducción, el impacto queda pendiente; no lo apruebes a partir del código.

Un límite programado de actualizaciones es una decisión, no una medición de FPS. Si el presupuesto de rendimiento obliga a cambiar el lenguaje o la fluidez, explica y resuelve ese conflicto; no reduzcas silenciosamente la expresión que define el pedido. Un tratamiento deliberado de pocos fotogramas puede ser válido si es la dirección elegida, no una excusa automática.

Registra el resultado en la revisión temporal de [aceptación](acceptance.md). La diferencia de píxeles entre dos imágenes solo prueba cambio; debe acompañarse de la evaluación del brief y del ciclo completo.

## Referencias técnicas

Verifica la API de la biblioteca instalada con su documentación oficial cuando haga falta. Para accesibilidad y límites de memoización:

- [W3C: Animation from Interactions](https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html)
- [W3C: Pause, Stop, Hide](https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide.html)
- [React: memo](https://react.dev/reference/react/memo)
