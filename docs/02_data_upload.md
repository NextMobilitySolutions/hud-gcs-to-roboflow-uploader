# **Plan Estratégico de Dataset para HUD – Detección y Segmentación**

Este documento presenta el **plan estratégico de organización y subida de datasets a Roboflow**, estructurado en torno a dos proyectos clave:

* `HUD Detection`: Enfocado en la **detección de elementos relevantes** en entornos urbanos y rurales, incluyendo obstáculos, peatones y semáforos.
* `HUD Segmentation`: Dedicado a la **segmentación semántica por píxeles**, con especial atención a condiciones adversas, caminos irregulares y zonas sin señalización.

Ambos proyectos están divididos en **fases temáticas**, que agrupan datasets según su naturaleza y contexto visual. Esta estructuración permite una planificación clara, facilita el entrenamiento iterativo de modelos, y asegura una cobertura robusta en distintos escenarios del mundo real y sintético.

Cada fase incluye:

* El nombre temático para facilitar su comunicación.
* Los datasets utilizados.
* El número de imágenes a subir.
* Comentarios clave sobre el tipo de anotación o las condiciones visuales.

En conjunto, el plan contempla la preparación de **\~60.000 imágenes** entre tareas de detección y segmentación, apoyando el desarrollo de modelos base como **YOLOv8**, **YOLO-NAS**, **DeepLabV3+** y **U-Net**.

## **Plan de subida a Roboflow: HUD Detection**

| Fase | Nombre de Fase                     | Dataset                           | Imágenes a subir | Comentarios                                                |
| ---- | ---------------------------------- | --------------------------------- | ---------------- | ---------------------------------------------------------- |
| F1   | **Baseline Urbano Sintético**      | **CARLA**                         | 1.864            | Anotación automática (`train`, `val`)                      |
|      |                                    | **BDD100K (subset)**              | 3.000            | Solo detección. Balanceado de `train`, `val`, `test`       |
| F2   | **Visión Nocturna Extrema**        | **ACDC (fog, night, snow, rain) (subset)** | 6.000            | Detección manual de obstáculos en condiciones difíciles    |
|      |                                    | **YouTube (night/forest)**        | 3.686            | Detección manual. Etiquetar peatones, animales, obstáculos |
| F3   | **Carreteras Rurales Irregulares** | **YouTube (bumpy, villages)**     | 6.164            | Subida completa de `dirtroad_*`, `villages`                |
|      |                                    | **LISA (night)**                  | 6.000            | Detección de semáforos nocturnos                           |
| F4   | **Cobertura Completa Urbana**      | **LISA (restante)**               | 5.389            | Día y noche. Semáforos y contexto vial                     |
|      |                                    | **BDD100K (resto)**               | 4.000            | Segunda parte del dataset                                  |

> **Total estimado detección:** **40.000 imágenes**

## **Plan de subida a Roboflow: HUD Segmentation**

| Fase | Nombre de Fase                     | Dataset                       | Imágenes a subir | Comentarios                                                            |
| ---- | ---------------------------------- | ----------------------------- | ---------------- | ---------------------------------------------------------------------- |
| F1   | **Segmentación Sintética Inicial** | **CARLA**                     | 1.864            | Máscaras del simulador                                                 |
|      |                                    | **CULane**                    | 2.049            | Segmentación nativa de carriles                                        |
| F2   | **Adversidad en Píxeles**          | **ACDC (completo)**           | 8.012            | Niebla, nieve, lluvia, noche. Subida total. Con `train`, `val`, `test` |
|      |                                    | **YouTube (night/forest)**    | 3.686            | Segmentación manual por píxel. Entornos oscuros/no estructurados       |
| F3   | **Paisaje Rural Denso**            | **YouTube (bumpy, villages)** | 6.714            | Entornos sin marcas, con vegetación, curvas. Etiquetado completo       |
| F4   | **Consolidación y Revisión**       | **BDD100K (segmentación)**    | 3.000            | Subset balanceado para segmentar (`road`, `lane`, etc.)                |
|      |                                    | **ACDC (revisión)**           | 1.000            | Casos conflictivos o mal anotados                                      |

> **Total estimado segmentación:** **26.000 imágenes**

## **Resumen final**

| Proyecto              | Total estimado imágenes | Nº de fases | Nombre del modelo base |
| --------------------- | ----------------------- | ----------- | ---------------------- |
| `hud-detection-v1`    | **40.000**              | 4           | YOLOv8 / YOLO-NAS      |
| `hud-segmentation-v1` | **26.000**              | 4           | DeepLabV3+ / U-Net     |
| **Total general**     | **\~66.000**            | 8           | —                      |
