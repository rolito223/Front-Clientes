import json
from utils.api_cliente import Cliente

if __name__ == '__main__':
    print('Iniciando testeo de la clase Cliente')
    cliente = Cliente()

    data = json.dumps({
        "id": 5,
        "name": "Roberto2",
        "lastName": "Corintios3",
        "address": "Manuel 123",
        "city": "Pensylvania",
        "zipCode": "1234",
        "dni": 12345678,
        "phone": "12345678",
        "email": "roberto.corintios@pensylvania.com"
    })
    print(cliente.create(data))
    print(cliente.update("5", data))
    print(cliente.get_by_id(5))
    print(cliente.delete(5))
    print(cliente.get_by_id(7))
    print(cliente.name)

    print('Finalizando testeo de la clase Cliente')
