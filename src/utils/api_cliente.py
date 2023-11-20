""" 
    Clase para el manejo del endpoint de clientes
    
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
from datetime import datetime
import os

from decouple import config


class Cliente():
    """ 
        Clase para el manejo del endpoint de clientes

        - El certificado de seguridad es auto firmado
        y no es valido para el dominio
        por lo que se debe deshabilitar la verificacion
        al realizar las peticiones a la api.
    """

    def __init__(self) -> None:
        """
        Constructor de la clase Cliente
        """

        logging.basicConfig(
            format='%(levelname)s:%(message)s',
            filename=f'{os.path.abspath("logs")}\{datetime.now().strftime("%Y-%m-%d")}.log',
            filemode='a',
            level=logging.INFO
        )
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        logging.info(
            f'[{date} (Api_Cliente)] - Creando instancia de la clase Cliente')

        self.url = config('APIURL')
        self.headers = {
            'Content-Type': 'application/json'
        }

        # Deshabilito los mensajes de advertencia de seguridad
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

    def get_all(self) -> json:
        """
        Obtiene todos los clientes y devuelve 
        la respuesta de la api en formato json.

        Returns:
            JSON: Respuesta de la api
        """

        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            self.response = requests.get(
                self.url, headers=self.headers, verify=False)
            self.json = self.response.json()
            self.status_code = self.response.status_code

            if self.status_code == 200:
                self.data = self.json['data']
            logging.info(
                f'''[{date} (Api_Cliente)] - GET /api/Clientes - {self.status_code}:
                {self.response}
                --------------------\n'''
            )
            return self.json

        except Exception as e:
            logging.error(f'[{date} (Api_Cliente)] - {e}')
            return None

    def get_by_id(self, id: int) -> int:
        """
        Obtiene un cliente por id y 
        lo asigna a los atributos de la clase Cliente
        Si el id no existe, los atributos de la clase Cliente
        quedan vacios.

        Args:
            id (int): id del cliente 

        Returns:
            int: status code de la respuesta
        """

        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
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

            logging.info(
                f'''[{date} (Api_Cliente)] - GET /api/Clientes/{id} - {self.status_code}:
                {self.response}
                --------------------\n'''
            )
            return self.status_code

        except Exception as e:
            logging.error(f'[{date} (Api_Cliente)] - {e}')
            return None

    def create(self, data: json) -> int:
        """
        Envia los datos de un cliente nuevo a la api
        y devuelve el status code de la respuesta.

        Args:
            data (JSON): Datos del cliente en formato json 

        Returns:
            int: Status code de la respuesta
        """

        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            self.response = requests.post(
                self.url, headers=self.headers, data=data, verify=False
            )
            self.json = self.response.json()
            self.id = self.json['id']
            self.status_code = self.response.status_code

            logging.info(
                f'''[{date} (Api_Cliente)] - POST /api/Clientes - {self.status_code}:
                {self.response}
                --------------------\n'''
            )
            return self.status_code

        except Exception as e:
            logging.error(f'[{date} (Api_Cliente)] - {e}')
            return None

    def update(self, id: int, data: json) -> int:
        """
        Actualiza los datos de un cliente existente
        y devuelve el status code de la respuesta.

        Args:
            id (int): id del cliente
            data (json): datos del cliente en formato json

        Returns:
            int: Status code de la respuesta
        """

        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            self.response = requests.put(
                f'{self.url}/{id}',
                headers=self.headers,
                data=data,
                verify=False
            )
            self.status_code = self.response.status_code

            logging.info(
                f'''[{date} (Api_Cliente)] - PUT /api/Clientes/{id} - {self.status_code}:
                {self.response}
                --------------------\n'''
            )
            return self.status_code

        except Exception as e:
            logging.error(f'[{date} (Api_Cliente)] - {e}')
            return None

    def delete(self, id: int) -> int:
        """
        Elimina un cliente por id y devuelve 
        el status code de la respuesta.

        Args:
            id (int): id del cliente

        Returns:
            int: Status code de la respuesta
        """

        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            self.response = requests.delete(
                f'{self.url}/{id}', headers=self.headers, verify=False
            )
            self.json = self.response.json()
            self.status_code = self.response.status_code
            logging.info(
                f'''[{date} (Api_Cliente)] - DELETE /api/Clientes/{id} - {self.status_code}:
                {self.response}
                --------------------\n'''
            )

            return self.status_code

        except Exception as e:
            logging.error(f'[{date} (Api_Cliente)] - {e}')
            return None
