# **Subida de Imágenes desde Google Cloud Storage a Roboflow mediante URLs Firmadas**

Este repositorio proporciona una utilidad desarrollada en Python para automatizar la subida de imágenes almacenadas en un bucket de **Google Cloud Storage (GCS)** a un proyecto de **Roboflow**, utilizando URLs firmadas (Signed URLs). Esta aproximación permite una integración segura, eficiente y escalable, sin necesidad de descargar localmente los archivos o exponer rutas públicas.

El sistema ha sido diseñado para integrarse en flujos de trabajo avanzados de visión artificial, facilitando la preparación y alimentación de datasets desde infraestructura propia hacia herramientas externas como Roboflow.

## **Requisitos previos**

Antes de ejecutar esta herramienta, es necesario contar con los siguientes elementos:

- Un bucket de GCS con las imágenes organizadas en carpetas lógicas (por ejemplo: por escenario, split o dataset).
- Un proyecto creado en Roboflow con API Key válida.
- Una cuenta de servicio de Google Cloud con permisos mínimos de lectura sobre el bucket (`roles/storage.objectViewer`).
- El archivo de credenciales en formato `.json` correspondiente a dicha cuenta.
- Python 3.8 o superior instalado en el entorno de ejecución.

## **Estructura del repositorio**

```plaintext
hud-gcs-to-roboflow-uploader/
├── main.py                    # Script principal que automatiza la subida
├── config.py                  # Archivo de configuración del entorno y proyecto
├── requirements.txt           # Lista de dependencias necesarias
├── .gitignore                 # Exclusión de archivos sensibles (.json, temporales)
└── README.md                  # Documentación técnica del proyecto
```

El archivo de credenciales (`.json`) **no debe subirse al repositorio**, ya que contiene acceso autenticado a recursos de Google Cloud. Se recomienda incluirlo únicamente en el entorno local o de ejecución segura.

## **Instalación**

1. Clonar el repositorio:

    ```bash
    git clone https://github.com/NextMobilitySolutions/hud-gcs-to-roboflow-uploader
    cd hud-gcs-to-roboflow-uploader
    ```

2. Instalar las dependencias necesarias:

    ```bash
    pip install -r requirements.txt
    ```

3. Configurar el archivo `config.py` con las siguientes variables. Se proporciona además un ejemplo de cómo debe de ser este archivo en `config/config_example.py`:

    ```python
    GCS_BUCKET_NAME = "svr_object_storage"
    GCS_PREFIX = "silver/public/"  # Ruta dentro del bucket a procesar
    ROBOFLOW_API_KEY = "TU_API_KEY"
    ROBOFLOW_PROJECT_NAME = "nombre-del-proyecto-en-roboflow"
    DEFAULT_SPLIT = "train"
    GOOGLE_APPLICATION_CREDENTIALS = "roboflow-gcs-key.json"  # Ruta local al .json
    ```

## **Funcionamiento del script**

El script principal (`main.py`) realiza las siguientes operaciones:

1. Conecta con el bucket de GCS usando la cuenta de servicio proporcionada.
2. Recorre recursivamente los objetos almacenados bajo el prefijo especificado.
3. Genera una URL firmada (con expiración temporal) para cada imagen válida (`.jpg`, `.png`).
4. Realiza una llamada HTTP autenticada a la API de Roboflow para subir la imagen directamente desde GCS.
5. Asigna automáticamente el conjunto correspondiente (`train`, `test`, `val`) en base a la estructura del path o al valor por defecto configurado.

Este flujo evita descargar los archivos, reduciendo el consumo de red y mejorando el rendimiento para grandes volúmenes de datos.

## **Organización recomendada de carpetas**

Se recomienda que la estructura del bucket refleje claramente la lógica del dataset, incluyendo el split correspondiente. Por ejemplo:

```plaintext
silver/
└── public/
    └── acdc/
        └── fog/
            ├── train/
            ├── test/
            └── val/
```

El script detectará automáticamente el split (`train`, `test`, `val`) en el path. En caso de no encontrarlo, se aplicará el valor definido por defecto (`DEFAULT_SPLIT`).

## **Consideraciones de seguridad**

El archivo de credenciales (`.json`) debe mantenerse fuera del control de versiones y almacenarse únicamente en entornos seguros. Este archivo permite el acceso autenticado al bucket y no debe compartirse ni exponerse públicamente.

Se recomienda restringir el alcance de la cuenta de servicio al mínimo necesario, idealmente con permisos de solo lectura sobre el bucket específico utilizado para este flujo.

## **Licencia y uso**

Este proyecto se distribuye como una herramienta técnica de apoyo al proceso de integración de datos en Roboflow. Puede ser utilizado libremente en contextos académicos, experimentales o industriales, siempre y cuando se mantenga el uso responsable de credenciales y se respeten los términos de uso de Google Cloud y Roboflow.

Para entornos de producción o despliegue en servidores compartidos, se recomienda revisar y reforzar las medidas de seguridad y trazabilidad del acceso a los recursos implicados.
