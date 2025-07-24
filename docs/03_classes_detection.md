# D**efinición de clases para detección de objetos en HUD vehicular**

Este documento recoge la descripción formal de las clases utilizadas en el modelo de detección de objetos mediante *bounding boxes* en el sistema HUD (Head-Up Display) vehicular. Estas clases están orientadas a identificar, localizar y clasificar elementos móviles o normativos del entorno urbano y carretero, con el fin de proporcionar información contextual relevante en tiempo real.

Este modelo es complementario al de segmentación semántica, y se focaliza en aquellos objetos cuya posición, tipo o existencia varían dinámicamente y, por tanto, requieren seguimiento o reconocimiento puntual.

## **Tabla de clases y descripciones**

| Clase                | Descripción técnica                                                                 |
|----------------------|--------------------------------------------------------------------------------------|
| `animal`             | Ser vivo no humano que puede irrumpir en la vía, como perros, gatos o fauna silvestre. Su detección es crucial para prevenir accidentes. |
| `bicycle`            | Vehículo de tracción humana de dos ruedas. Incluye bicicletas tradicionales y eléctricas. |
| `bus`                | Vehículo de gran tamaño destinado al transporte colectivo de pasajeros. |
| `car`                | Vehículo motorizado de uso personal, de tamaño medio. Incluye coches urbanos y sedanes. |
| `direction_sign`     | Señalización vertical que indica direcciones o rutas, como flechas o paneles informativos. |
| `mandatory_sign`     | Señales que imponen una obligación específica (ej. “gire a la derecha”, “circulación obligatoria”). |
| `motorcycle`         | Vehículo motorizado de dos o tres ruedas, diseñado para uso individual o en pareja. |
| `obstacle`           | Elemento físico inesperado o fijo que representa un riesgo para la circulación. Puede incluir escombros, objetos caídos o mobiliario urbano. |
| `parking_sign`       | Señales que indican zonas permitidas o restringidas para el estacionamiento. |
| `pedestrian`         | Persona transitando a pie en las proximidades de la vía. |
| `prohibition_sign`   | Señales que expresan restricciones (ej. “prohibido girar”, “prohibido adelantar”). |
| `speed_limit_sign`   | Señales que establecen la velocidad máxima permitida en un tramo determinado. |
| `stop_sign`          | Señal octogonal que ordena detener completamente el vehículo antes de reanudar la marcha. |
| `tractor`            | Vehículo agrícola o de carga pesada, generalmente usado fuera del entorno urbano. |
| `traffic_cone`       | Elemento de señalización temporal que delimita zonas de obras, desvíos o accidentes. |
| `traffic_light`      | Dispositivo electrónico que regula la prioridad de paso mediante señales luminosas. |
| `train`              | Composición ferroviaria en movimiento o en cruce de intersecciones viarias. |
| `truck`              | Vehículo de transporte pesado, de gran tamaño y múltiples ejes. |
| `unknown_sign`       | Señales poco frecuentes o no reconocibles, pero cuya existencia debe registrarse para análisis posteriores. |
| `warning_sign`       | Señales que alertan de un peligro próximo (curvas, cruce de animales, obras, etc.). |
| `yield_sign`         | Señal de “ceda el paso”, generalmente triangular e invertida, que exige dar prioridad a otros vehículos. |

---

## Consideraciones

- Todas las clases descritas deben ser etiquetadas utilizando coordenadas rectangulares (*bounding boxes*), indicando su posición y extensión sobre la imagen.
- En caso de ambigüedad visual, puede utilizarse la clase `unknown_sign` para registrar elementos inciertos que requieran validación manual o entrenamiento posterior.
- El modelo está optimizado para operar conjuntamente con el sistema de segmentación semántica, al que complementa identificando elementos dinámicos o puntuales que no se modelan por regiones continuas.
