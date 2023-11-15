""" Clase para el manejo del endpoint de clientes
    
    - Los endpoints son: 
        [GET]/api/Clientes Obtiene todos los clientes
        [GET]/api/Clientes/{id} Obtiene un cliente por id
        [POST]/api/Clientes Crea un nuevo cliente
        [PUT]/api/Clientes/{id} Actualiza un cliente
        [DELETE]/api/Clientes/{id} Elimina un cliente
    
    - Los campos que manejan los endpoints son:
        {
            'id': 0,
            'name': 'string',
            'lastName': 'string',
            'address': 'string',
            'city': 'string',
            'zipCode': 'string',
            'dni': 0,
            'phone': 'string',
            'email': 'string'
        }
    
"""
import requests
import urllib3
import json
import logging


class Cliente():
    def __init__(self) -> None:
        # El certificado de seguridad es auto firmado
        # y no es valido para el dominio
        # por lo que se debe deshabilitar la verificacion

        self.url = 'https://localhost:44356/api/Clientes'
        self.headers = {
            'Content-Type': 'application/json'
        }

        # Deshabilita los mensajes de advertencia
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

        self.data = {}
        self.response = None
        self.json = None
        self.status_code = None
        self.message = None
        self.id = None
        self.name = None
        self.lastName = None
        self.address = None
        self.city = None
        self.zipCode = None
        self.dni = None
        self.phone = None
        self.email = None

    def get_all(self):
        self.response = requests.get(
            self.url, headers=self.headers, verify=False)
        self.json = self.response.json()
        self.status_code = self.response.status_code

        if self.status_code == 200:
            self.data = self.json['data']

        return self.json

    def get_by_id(self, id):
        self.response = requests.get(
            f'{self.url}/{id}', headers=self.headers, verify=False
        )
        self.json = self.response.json()
        self.status_code = self.response.status_code
        if self.status_code == 200:
            self.name = self.json['name']
            self.lastName = self.json['lastName']
            self.address = self.json['address']
            self.city = self.json['city']
            self.zipCode = self.json['zipCode']
            self.dni = self.json['dni']
            self.phone = self.json['phone']
            self.email = self.json['email']

        return self.status_code

    def create(self, data):
        self.response = requests.post(
            self.url,
            headers=self.headers,
            data=data,
            verify=False
        )

        self.json = self.response.json()
        self.id = self.json['id']
        self.status_code = self.response.status_code
        return self.status_code

    def update(self, id, data):
        self.response = requests.put(
            f'{self.url}/{id}',
            headers=self.headers,
            data=data,
            verify=False
        )
        # self.json = self.response.json()
        self.status_code = self.response.status_code
        return self.response.status_code

    def delete(self, id):
        self.response = requests.delete(
            f'{self.url}/{id}', headers=self.headers, verify=False
        )
        self.json = self.response.json()
        self.status_code = self.response.status_code
        return self.status_code


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
    # UPDATE DEVUELVE 400 BAD REQUEST PROBABLEMENTE
    # SEA EL FORMATO DEL ENDOPOINT

    # print(cliente.create(data))
    # print(cliente.update("5", data))
    # print(cliente.get_by_id(5))
    # print(cliente.delete(5))
    print(cliente.get_by_id(7))
    print(cliente.name)
