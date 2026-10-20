# Aceptación del brief y evidencia

Lee este documento al revisar o cerrar una implementación visual. Conserva la profundidad proporcional al alcance: un ajuste pequeño puede informar resultados en pocas líneas; un rediseño o hero expresivo necesita requisitos y evidencia trazables.

## Tres revisiones independientes

| Revisión | Qué debe cumplirse | Evidencia pertinente |
| --- | --- | --- |
| Funcionamiento | La tarea principal, estados, recuperación, accesibilidad y adaptación afectadas funcionan. | Recorrido de interacción, resultados de pruebas y mediciones pertinentes. |
| Fidelidad al brief | Composición, lenguaje visual, tipografía, material, protagonismo y pedidos concretos aparecen en el resultado. | Render observado en el encuadre objetivo; comparación con las decisiones o referencias acordadas. |
| Impacto temporal | Cuando se pide movimiento, su transformación, amplitud, secuencia, ritmo y resolución cumplen el papel pedido. | Reproducción completa observada a velocidad normal, grabación o referencia de reproducción; fotogramas clave como apoyo. |

Una revisión aprobada no compensa otra fallida. No uses un promedio ni un único «score de calidad». Si falta evidencia necesaria, el resultado es pendiente. La revisión temporal puede no aplicar a un pedido estático; no puede marcarse no aplicable cuando el brief pide animación.

El auditor de patrones es higiene de fuente. Un build, ausencia de overflow, un contador de frames, el botón Pause o imágenes con píxeles distintos aportan información limitada. No responden si la pieza tiene el lenguaje o impacto que se pidió.

## Convertir el brief en criterios

Antes de implementar, registra cada requisito decisivo como **pedido → resultado esperado observable → forma de comprobarlo**. Al revisar, añade lo observado y el estado: cumple, falla o pendiente.

Incluye los requisitos expresivos, no solo los botones y funciones. Distingue conservar marca de resolver dirección. Cuando una misma marca incluye landing y editor, revisa cada superficie por su función; una UI de trabajo estable no obliga a hacer estático el hero promocional.

Para un hero protagonista, comprueba primero:

1. Que el material elegido corresponde al brief y a las correcciones; un asset rechazado no reaparece en sus derivados.
2. Que el medio tiene el peso prometido dentro del encuadre real, también en una ventana estrecha.
3. Que el lenguaje surge de composición, tipografía, material y comportamiento combinados, además de la paleta o el claim.
4. Que hay una transformación y una secuencia reconocibles, con ritmo y resolución adecuados.
5. Que la acción principal y la lectura siguen siendo usables durante la pieza.

Si falla una de estas bases, revisa esa pieza antes de propagar su tratamiento al resto de la superficie. Esto es evaluación del trabajo, no una aprobación humana adicional obligatoria.

## Caso de regresión

Una landing de una herramienta visual pide hero potente con carácter hacker, ejemplo animado protagonista, acceso al editor y cards con muestras. El resultado tiene navegación correcta, fondo oscuro, texto alusivo y un retrato fijo con interferencia mínima. Las cards repiten el retrato y el auditor llega a cero hallazgos.

El funcionamiento puede haber mejorado y la higiene puede estar resuelta, mientras fidelidad e impacto temporal fallan. Cambiar algunos frames no transforma ese resultado en la escena pedida. La corrección necesita volver al material, la dirección y la secuencia; quitar más patrones no responde por sí solo al problema.

Esta regresión evalúa el procedimiento, no obliga a usar estética hacker ni una animación particular en otros proyectos.

## Informe opcional en JSON

Para cambios amplios o una validación repetible, puedes registrar la revisión y ejecutar:

```sh
python3 "$SKILL_DIR/scripts/check_acceptance.py" /ruta/review.json --root /ruta/al/proyecto
```

El script usa Python 3 estándar, lee el informe y comprueba coherencia y referencias de evidencia locales. No observa un video, mide gusto ni convierte declaraciones en una aprobación creativa. Solo puede validar el registro de una revisión que realmente hiciste.

Formato mínimo:

```json
{
  "schema_version": 1,
  "scope": "Hero y acceso al editor",
  "motion_required": true,
  "hygiene": {"source_audit_unresolved": 0, "build": "pass"},
  "checks": [
    {
      "id": "B1",
      "gate": "brief",
      "request": "Una demostración animada protagonista",
      "expected": "La escena ocupa el foco del hero en el primer encuadre",
      "observed": "La revisión del render todavía está pendiente",
      "status": "pending",
      "evidence": []
    }
  ]
}
```

Añade los checks de funcionamiento y de motion que el alcance requiere. Los valores de `gate` son `functional`, `brief` y `motion`; los de `status`, `pass`, `fail`, `pending` y `not_applicable`. Este último solo es válido para motion cuando no se pidió movimiento, con motivo en `observed`.

Cada evidencia tiene `kind`, `ref` y `note`. Los tipos son `interaction`, `test_run`, `measurement`, `source`, `screenshot`, `contact_sheet`, `video` y `playback`. `ref` puede ser una ruta relativa a `--root` o una URL HTTP(S); las rutas locales deben existir. Las URLs no se descargan ni verifican automáticamente. `note` explica qué se observó o qué demuestra el archivo.

Un check de funcionamiento declarado aprobado necesita evidencia de interacción, prueba, medición o reproducción. Uno visual necesita render: screenshot, video o reproducción. Uno temporal necesita `video` o `playback`; una medición de píxeles o contact sheet por sí sola deja la revisión pendiente. La existencia de archivos o URLs no demuestra que su contenido sea correcto ni que se hayan revisado.

- **0 / `ready_for_review`:** el registro declara todos los requisitos aplicables cumplidos con tipos de evidencia pertinentes. El juicio visual sigue siendo responsabilidad de la revisión real.
- **1 / `needs_revision`:** hay una revisión fallida, pendiente, ausente o sin evidencia adecuada. La higiene técnica no cambia este resultado.
- **2 / `error`:** el informe o sus rutas son inválidos; no se pudo completar la comprobación.

No cambies estados, inventes reproducciones ni marques motion como opcional para obtener salida 0. La entrega debe conservar fallos y pendientes con su evidencia y explicar qué falta resolver.
