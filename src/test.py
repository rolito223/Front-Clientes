import json
from utils.api_cliente import Cliente

if __name__ == '__main__':
    print('Iniciando testeo de la clase Cliente')
    cliente = Cliente()

    # data = json.dumps({
    #     "id": 5,
    #     "name": "Roberto2",
    #     "lastName": "Corintios3",
    #     "address": "Manuel 123",
    #     "city": "Pensylvania",
    #     "zipCode": "1234",
    #     "dni": 12345678,
    #     "phone": "12345678",
    #     "email": "roberto.corintios@pensylvania.com"
    # })
    # print(cliente.create(data))
    # print(cliente.update("5", data))
    # print(cliente.get_by_id(5))
    # print(cliente.delete(5))
    # print(cliente.get_by_id(7))
    # print(cliente.name)
    if cliente.get_all() == 200:
        for d in cliente.data:
            print(f'{d["id"]} - {d["name"]} - {d["lastName"]} - {d["address"]} - {d["city"]} - {d["zipCode"]} - {d["dni"]} - {d["phone"]} - {d["email"]}')
    print('Finalizando testeo de la clase Cliente')
