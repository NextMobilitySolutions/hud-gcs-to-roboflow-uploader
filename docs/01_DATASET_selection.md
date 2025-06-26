# **Clasificación de datasets por tipo de anotación y uso**

Este proyecto emplea diferentes fuentes de datos visuales para entrenar modelos de visión artificial enfocados en dos tareas principales: **detección de objetos** y **segmentación semántica**. Cada dataset se ha clasificado cuidadosamente según su contenido, calidad de anotaciones y aplicabilidad al entorno vial.

## **Proyecto 1: Detección de objetos (Bounding Boxes)**

El objetivo de esta tarea es localizar instancias individuales de objetos relevantes para la conducción, como **peatones, vehículos, señales, semáforos o animales**, utilizando cajas delimitadoras (bounding boxes). Se han seleccionado los siguientes datasets para esta tarea:

| Dataset     | Incluido    | Justificación                                                                                                                                                               |
| ----------- | ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **BDD100K** | Sí        | Contiene objetos urbanos comunes (peatones, vehículos, señales, semáforos) con anotaciones bounding box en condiciones variadas. Las anotaciones al ser más senciallas se pueden hacer a través de IA.                                            |
| **LISA**    | Sí        | Especializado en detección de semáforos en horario diurno y nocturno. Muy útil para robustecer la clase `traffic_light`.                                                    |
| **YouTube** | Sí        | Se han extraído manualmente imágenes de rutas rurales, caminos sin demarcación y presencia de peatones u obstáculos inusuales. Las anotaciones se realizarán manualmente.   |
| **CULane**  | ⚠️ Opcional | Aunque está orientado a carriles, algunas secuencias pueden contener peatones o vehículos que pueden ser **anotados manualmente**. No incluye anotaciones nativas de detección. |
| **ACDC**    | Sí (Anotación Manual) | Dataset de condiciones adversas (noche, lluvia, niebla). Puede usarse para detectar objetos si se **anotan manualmente**. Útil en fases de validación extrema.                  |
| **CARLA**   | Sí | Dataset sintético. Puede utilizarse para exportar las anotaciones de bounding boxes desde el simulador para clases como `car`, `pedestrian`, `sign`.                       |

## **Proyecto 2: Segmentación semántica (Máscaras por píxel)**

La segmentación semántica permite etiquetar cada píxel de la imagen con una clase específica del entorno vial (ej. carril izquierdo, arcén, fondo, paso de cebra). Es fundamental para representar el entorno estructurado de forma densa. Se han seleccionado los siguientes datasets:

| Dataset     | Incluido | Justificación                                                                                                                                                                                                           |
| ----------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **BDD100K** | Sí     | Incluye anotaciones por píxel para elementos viales (carriles, señales horizontales, fondo). Ofrece gran diversidad de contextos urbanos.                                                                               |
| **CULane**  | Sí     | Dataset centrado en la segmentación de carriles. Presenta múltiples condiciones ambientales y complejidad visual.                                                                                                       |
| **ACDC**    | Sí     | Altamente recomendado por su cobertura de condiciones adversas (niebla, nieve, lluvia). Proporciona máscaras detalladas por píxel.                                                                                      |
| **YouTube** | Sí     | Aunque no incluye anotaciones de origen, se han extraído imágenes en condiciones rurales donde los carriles son poco visibles. Se realizarán anotaciones manuales para entrenar el modelo en entornos no estructurados. |
| **CARLA**   | Sí     | Dataset sintético con generación automática de máscaras perfectas por clase. Ideal para preentrenamiento y validación base.                                                                                             |

## **Datasets compartidos en ambos proyectos**

Algunos datasets, como `bdd100k`, `acdc`, `culane`, `carla` y `youtube`, se utilizarán en ambos proyectos debido a su riqueza visual y versatilidad. En estos casos, las imágenes se gestionarán de forma separada en cada proyecto Roboflow para evitar ambigüedades en el tipo de anotación (bounding box vs. máscara por píxel).

## **Consideraciones de uso**

* Las **anotaciones manuales** se realizarán mediante Roboflow, dividiendo por tipo de tarea.
* Se priorizará la calidad y diversidad de escenarios (día/noche, lluvia, curvas, sin líneas).
* En los datasets sin anotaciones nativas (ej. YouTube), se generarán etiquetas personalizadas.
* En los datasets sintéticos (CARLA), se mantendrá la correspondencia directa entre imagen y máscara.
* Se documentará cada subida y anotación en una hoja de control centralizada.
