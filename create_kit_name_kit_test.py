import sender_stand_request
import data

# Función auxiliar para crear una copia del kit_body con un nombre específico

def get_kit_body(kit_name):
    current_kit_body = data.kit_body.copy()
    current_kit_body['name'] = kit_name
    return current_kit_body

# Función para realizar aserciones en pruebas positivas: Preparación
def positive_assert(kit_name):
    kit_body = get_kit_body(kit_name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body)

    assert kit_response.status_code == 201
    assert kit_response.json()['name'] == kit_name

# Función para realizar aserciones en pruebas negativas: Preparación
def negative_assert(kit_name):
    kit_body = get_kit_body(kit_name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body)

    assert kit_response.status_code == 400

# Función específica para la prueba 8 (sin el parámetro 'name') :
def negative_assert_no_name(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body)

    assert response.status_code == 400

#Prueba 1 - El número permitido de caracteres  "a" (1):
def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert(data.kit_body_name_t1)

#Prueba 2 - El número permitido de caracteres (511):
def test_create_kit_511_letter_in_name_get_success_response():
    positive_assert(data.kit_body_name_t2)

#Prueba 3 - El número de caracteres es menor que la cantidad permitida (0):
def test_create_kit_empty_name_get_error_response():
    negative_assert(data.kit_body_name_t3)

#Prueba 4 - El número de caracteres es mayor que la cantidad permitida (512):
def test_create_kit_512_letter_in_name_get_error_response():
    negative_assert(data.kit_body_name_t4)

#Prueba 5 - Se permiten caracteres especiales ""№%@",":
def test_create_kit_has_special_symbol_in_name_get_success_response():
    positive_assert(data.kit_body_name_t5)

#Prueba 6 - Se permiten espacios " A Aaa ":
def test_create_kit_has_space_in_name_get_success_response():
    positive_assert(data.kit_body_name_t6)

#Prueba 7 - Se permiten números "123" :
def test_create_kit_has_number_in_name_get_success_response():
    positive_assert(data.kit_body_name_t7)

# Prueba 8: Solicitud sin el parámetro 'name' { }:
def test_create_kit_no_name_get_error_response():
    kit_body = data.kit_body.copy()
    kit_body.pop('name')
    negative_assert_no_name(kit_body)

#Prueba 9 - Se ha pasado un tipo de parámetro diferente (número):
def test_create_kit_number_type_name_get_error_response():
    kit_body = get_kit_body(data.kit_body_name_t9)
    response = sender_stand_request.post_new_client_kit(kit_body)

    assert response.status_code == 400