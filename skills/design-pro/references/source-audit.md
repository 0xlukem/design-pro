# Auditoría estática de patrones

El script `scripts/audit_ui.py` usa solo Python 3 y la biblioteca estándar. Lee el código y devuelve JSON por stdout; no modifica el proyecto, instala dependencias ni accede a la red.

## Ejecutar

Resuelve `SKILL_DIR` como la carpeta desde la que leíste esta skill. No presupongas una ruta personal ni un directorio exclusivo de un asistente.

```sh
python3 "$SKILL_DIR/scripts/audit_ui.py" "/ruta/al/proyecto" --file src/hero.tsx --file src/styles.css
```

Usa `--file` repetido para limitar la revisión al código afectado. Sin ese argumento recorre archivos de interfaz del proyecto y excluye dependencias y salidas de build habituales; podría informar problemas preexistentes fuera del cambio. No amplíes el alcance del trabajo para eliminarlos automáticamente.

## Reglas y resultados

| Regla | Detecta | Tratamiento |
| --- | --- | --- |
| DP001 | Funciones CSS de gradiente, gradientes SVG y utilidades comunes de Tailwind | Revisar el bloqueo y cualquier excepción explícita. |
| DP002 | Declaraciones e imports comunes de Inter, fuentes web y utilidades habituales | Revisar el bloqueo y cualquier excepción explícita. |
| DP003 | Sintaxis común de repetición infinita y utilidades de pulso, rebote o giro | Revisión contextual: puede ser actividad decorativa o un indicador funcional. |

El script conserva números de línea y omite comentarios de sintaxis común. No es un parser completo: nombres calculados, CSS escapado, variables, recursos raster y otras construcciones pueden quedar fuera. Strings de ejemplos o contenido pueden producir falsos positivos. Inspecciona cada hallazgo en su contexto.

- Salida **0**: sin patrones pendientes dentro del alcance; **no** significa «diseño aprobado».
- Salida **1**: hay bloqueos o revisiones contextuales pendientes.
- Salida **2**: error de entrada, lectura o configuración; no se completó la auditoría.

El JSON declara siempre `scope: "static_source_patterns_only"` y `creative_verdict: "not_assessed"`. Llegar de muchos hallazgos a cero solo cierra esa revisión de patrones. No habilita a declarar que el brief, la identidad o la animación quedaron logrados.

No detecta semánticamente eyebrows, copy genérico, cards de relleno, CTAs competidores, jerarquía, contraste, recortes, comportamiento ni calidad del movimiento. Eso requiere revisar el render y recorrer la experiencia.

Conserva sus resultados como higiene de fuente y usa las revisiones separadas de [aceptación](acceptance.md) para el cierre del trabajo. No promedies el recuento del auditor con una valoración visual o temporal ni elimines un efecto expresamente pedido solo para reducir DP003: revisa y registra el alcance de la petición.

## Excepciones acotadas

Cuando corresponda, pasa `--exceptions /ruta/excepciones.json`. Cada entrada debe nombrar regla, archivo relativo y rango de líneas. Esta lista registra decisiones, no concede permisos ni demuestra que una solicitud sea auténtica. Vincúlala al pedido real en la conversación; no inventes una excepción para conseguir salida 0.

Ejemplo de formato para un gradiente pedido expresamente en una región concreta:

```json
[
  {
    "rule": "DP001",
    "path": "src/hero.css",
    "start_line": 12,
    "end_line": 12,
    "basis": "user-request",
    "reason": "El usuario habilitó el gradiente solo en este fondo.",
    "user_request": "Quiero un gradiente en el fondo del hero."
  }
]
```

Para DP003, `basis: "functional"` permite registrar un indicador de procesamiento real con `reason` que explique qué representa, cuándo termina y cómo se adapta a movimiento reducido. No habilita gradientes ni Inter.

Para un falso positivo real en una cadena de ejemplo u otra sintaxis fuera de uso visual, explica el hallazgo en la entrega. Mantén la salida pendiente si el script no puede expresarlo; no inventes una petición humana ni un propósito funcional.

Vuelve a revisar los rangos después de editar: las líneas pueden cambiar. El informe incluye excepciones no utilizadas para detectar configuraciones desalineadas. Conserva la evidencia proporcional en el trabajo temporal o en el sistema de revisión existente.
