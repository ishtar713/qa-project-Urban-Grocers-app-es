# Proyecto Urban Grocers 

Este proyecto contiene pruebas automatizadas para la API de Urban Grocers, específicamente para la creación de kits de usuario.

# Descripción

El proyecto consiste en una serie de pruebas unitarias que verifican el funcionamiento correcto del endpoint de creación de kits de usuario en la API de Urban Grocers.

# Tecnologías utilizadas

- Python 3.13
- pytest: framework de pruebas unitarias
- requests: biblioteca para realizar peticiones HTTP

# Ejecución de las pruebas

Para ejecutar las pruebas, siga estos pasos:

1. Clone el repositorio
2. Instale las dependencias: `pip install -r requirements.txt`
3. Ejecute las pruebas: `pytest tests/create_kit_name_kit_test.py`
 
| № | Description | Error |
|---|-------------|-------|
| 1 | El número permitido de caracteres (1): kit_body = { "name": "a"} | Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud |
| 2 | El número permitido de caracteres (511): kit_body = { "name":"El valor de prueba para esta comprobación será inferior a"} | Código de respuesta: 201 El campo "name" en el cuerpo de la respuesta coincide con el campo "name" en el cuerpo de la solicitud |
| 3 | El número de caracteres es menor que la cantidad permitida (0): kit_body = { "name": "" } | Código de respuesta: 400 |
| 4 | El número de caracteres es mayor que la cantidad permitida (512): kit_body = { "name":"El valor de prueba para esta comprobación será inferior a" } | Código de respuesta: 400 |
| 5 | Se permiten caracteres especiales: kit_body = { "name": ""№%@"," } | Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud |
| 6 | Se permiten espacios: kit_body = { "name": " A Aaa " } | Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud |
| 7 | Se permiten números: kit_body = { "name": "123" } | Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud |
| 8 | El parámetro no se pasa en la solicitud: kit_body = { } | Código de respuesta: 400 |
| 9 | Se ha pasado un tipo de parámetro diferente (número): kit_body = { "name": 123 } | Código de respuesta: 400 |

# Estructura del proyecto

- `tests/`: Contiene los archivos de prueba
- `configuration.py`: Configuración de URLs y rutas
- `data.py`: Datos de prueba
- `sender_stand_request.py`: Funciones para enviar solicitudes a la API
- `README.md`: Este archivo
- `.gitignore`: Especifica archivos y directorios ignorados por git

# Convenciones de código

- Se utiliza snake_case para nombres de funciones y variables
- Los nombres de las variables son sustantivos descriptivos
- Los nombres de las funciones comienzan con un verbo y describen la acción que realizan
- Se evitan abreviaturas poco claras en los nombres