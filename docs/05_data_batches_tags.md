
# **Estructura de organización de batches y sistema de etiquetado en Roboflow**

Este documento establece las directrices formales para la organización sistemática de los lotes (*batches*) y etiquetas (*tags*) dentro de los proyectos gestionados en la plataforma Roboflow. Esta estructura está diseñada para garantizar una trazabilidad precisa, facilitar el análisis comparativo entre versiones, y promover la escalabilidad del flujo de trabajo a medida que se incorporen nuevos conjuntos de datos, condiciones ambientales y tareas.

## **Organización de lotes (*batches*)**

Cada lote de imágenes representa una unidad de carga diferenciada, compuesta por una combinación específica de:

- Conjunto de datos de origen
- Fase experimental o iteración del proyecto
- Subtarea correspondiente (detección o segmentación)
- Condición o escenario representado
- División funcional del conjunto (entrenamiento, validación, prueba)

### **Convención de nomenclatura**

La denominación de los batches deberá seguir la siguiente estructura estándar:

```markdown
F[Num]_[Dataset]_[Escenario]_[Split]
```

Donde:

- `F[Num]` indica la fase o versión del experimento (por ejemplo, `F1`, `F2`, `F3`, etc.)
- `Dataset` corresponde al nombre del conjunto de datos empleado (`CARLA`, `BDD100K`, `ACDC`, `LISA`, `YOUTUBE`, etc.)
- `Condición o Escenario` hace referencia al contexto representado (por ejemplo, `fog`, `night`, `dirtroad`)
- `Split` representa la partición funcional (`train`, `val`, `test`, `unknown`)

### **Ejemplos de nomenclatura aplicada**

Cada lote debe corresponder a una unidad lógica coherente en términos de origen, naturaleza del escenario y propósito experimental.

- `F1_CARLA_train`
- `F2_ACDC_fog_val`
- `F3_YOUTUBE_dirtroad_night`
- `F4_LISA_night_full`
- `F2_BDD100K_subset`

## **Sistema de etiquetado (*tags*)**

Las etiquetas constituyen metadatos asociados a cada imagen del proyecto y permiten agrupar, filtrar, analizar y exportar subconjuntos de datos de forma estructurada, sin necesidad de duplicar proyectos o crear divisiones artificiales.

### **Categorías de etiquetas recomendadas**

| Categoría   | Ejemplos                                    | Descripción técnica                                                                 |
|-------------|---------------------------------------------|--------------------------------------------------------------------------------------|
| `source`    | `source:carla`, `source:acdc`, `source:youtube` | Identifica el conjunto de datos de procedencia.                                     |
| `scenario`  | `scenario:night`, `scenario:fog`, `scenario:rural`, `scenario:synthetic` | Describe la condición ambiental, lumínica o topográfica del entorno representado.  |
| `split`     | `split:train`, `split:val`, `split:test`, `split:unknown` | Indica la partición funcional a la que pertenece la imagen dentro del proyecto.    |
| `phase`     | `phase:1`, `phase:2`, `phase:3` | Representa la versión o etapa experimental del proceso de desarrollo.               |

### **Aplicación de etiquetas por lote**

Ejemplo aplicado a un lote específico del proyecto `hud-segmentation-v1`:

- **Nombre del batch:** `F2_ACDC_night_test`
- **Etiquetas asignadas:**
  - `source:acdc`
  - `scenario:night`
  - `split:test`
  - `phase:2`

Las etiquetas pueden asignarse durante la carga inicial del lote o bien posteriormente desde la interfaz de administración de datos del proyecto.

## **Propuesta de organización estructural**

La implementación de esta estructura permite reflejar de forma coherente la evolución del proyecto dentro de la plataforma Roboflow. A modo de ejemplo:

- **Proyecto:** `hud-detection-v1`
- **Versión:** `2` (correspondiente a la fase experimental F2)
- **Nombre del batch:** `F2_ACDC_fog_train`
- **Etiquetas aplicadas:**
  - `source:acdc`
  - `scenario:fog`
  - `split:train`
  - `phase:2`

Esta organización puede y debe repetirse de forma sistemática para cada lote nuevo, asegurando coherencia documental, trazabilidad de resultados y replicabilidad de experimentos.

## **Recomendaciones operativas**

- Respetar estrictamente las convenciones de nomenclatura definidas.
- Documentar en paralelo en hojas de control o repositorios internos las fases, lotes y etiquetas aplicadas.
- Utilizar los filtros por etiquetas en Roboflow para generar subconjuntos específicos destinados a entrenamiento, evaluación cruzada o exportación modular.
- Consolidar esta práctica como parte del protocolo estándar del ciclo de vida del proyecto.
