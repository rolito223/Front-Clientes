from flet import *
import flet as ft
import json
import logging
from datetime import datetime
import os
from threading import Thread
from time import sleep

from utils.api_cliente import Cliente


class TabContentSearch(ft.UserControl):
    """
        Clase que contiene el contenido de la pestaña de busqueda
    Args:
        ft (_type_): _description_
    """

    def __init__(self):
        """
            Constructor de la clase TabContentSearch
        """
        super().__init__()
        self.title = "Crear Clientes"
        self.description = "CRUD de clientes"
        self.language = "es"
        self.author = "Raul Andres Orlando"
        self.keywords = "CRUD, clientes, api"

        self.vertical_alignment = ft.MainAxisAlignment.CENTER

        self.textbox_row = ft.Text()

        self.tb_id = ft.TextField(
            label="ID",
            bgcolor='#1a1c1e',
            read_only=False
        )

        self.tb_name = ft.TextField(
            label="Nombre",
            value="",
            capitalization=ft.TextCapitalization.WORDS,
            keyboard_type=ft.KeyboardType.NAME,
            bgcolor='#1a1c1e',
            read_only=True
        )

        self.tb_lastName = ft.TextField(
            label="Apellido",
            value="",
            capitalization=ft.TextCapitalization.WORDS,
            keyboard_type=ft.KeyboardType.NAME,
            bgcolor='#1a1c1e',
            read_only=True
        )

        self.tb_address = ft.TextField(
            label="Domicilio",
            value="",
            capitalization=ft.TextCapitalization.WORDS,
            keyboard_type=ft.KeyboardType.STREET_ADDRESS,
            bgcolor='#1a1c1e',
            read_only=True
        )

        self.tb_city = ft.TextField(
            label="Ciudad",
            value="",
            capitalization=ft.TextCapitalization.WORDS,
            keyboard_type=ft.KeyboardType.NAME,
            bgcolor='#1a1c1e',
            read_only=True
        )

        self.tb_zipcode = ft.TextField(
            label="Codigo Postal",
            value="",
            capitalization=ft.TextCapitalization.CHARACTERS,
            keyboard_type=ft.KeyboardType.TEXT,
            bgcolor='#1a1c1e',
            read_only=True
        )

        self.tb_dni = ft.TextField(
            label="DNI",
            value="",
            capitalization=ft.TextCapitalization.NONE,
            keyboard_type=ft.KeyboardType.NUMBER,
            bgcolor='#1a1c1e',
            read_only=True,
            on_change=self.blank_error
        )

        self.tb_phone = ft.TextField(
            label="Telefono",
            capitalization=ft.TextCapitalization.NONE,
            keyboard_type=ft.KeyboardType.PHONE,
            bgcolor='#1a1c1e',
            read_only=True,
            on_change=self.blank_error
        )

        self.tb_email = ft.TextField(
            label="E-Mail",
            value="",
            keyboard_type=ft.KeyboardType.EMAIL,
            bgcolor='#1a1c1e',
            read_only=True,
            on_change=self.blank_error
        )

        self.button_search = ft.FloatingActionButton(
            icon=ft.icons.SEARCH_OUTLINED,
            bgcolor=ft.colors.BLUE_500,
            on_click=self.button_clicked
        )

        self.button_update = ft.FloatingActionButton(
            icon=ft.icons.UPDATE_OUTLINED,
            disabled=True,
            bgcolor=ft.colors.BLUE_500,
            on_click=self.button_clicked
        )

        self.button_delete = ft.FloatingActionButton(
            icon=ft.icons.DELETE_OUTLINE,
            disabled=True,
            bgcolor=ft.colors.RED_500,
            on_click=self.button_clicked
        )

        self.button_restart_fields = ft.FloatingActionButton(
            icon=ft.icons.RESET_TV_OUTLINED,
            on_click=self.action_button_restart_fields,
            bgcolor=ft.colors.YELLOW_400,
            disabled=True
        )

    def build(self) -> ft.Control:
        """
            Construye el contenido de la pestaña de busqueda
        Returns:
            ft.Control: Contenido de la pestaña de busqueda
        """
        fields = ft.Column(
            controls=[
                ft.Divider(height=10, color='#212121'),
                ft.Row(
                    controls=[
                        self.textbox_row,
                        self.tb_id,
                        self.tb_name,
                        self.tb_lastName,
                        self.tb_address,
                        self.tb_city,
                        self.tb_zipcode,
                        self.tb_dni,
                        self.tb_phone,
                        self.tb_email,

                    ],
                    wrap=True,
                    alignment=ft.MainAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER
                ),
                ft.Divider(height=20, color='#212121'),
                ft.Row(
                    controls=[
                        self.button_search,
                        self.button_update,
                        self.button_delete,
                        self.button_restart_fields
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER
                ),
                ft.Divider(height=20, color='#212121')
            ],
            spacing=20,
            scroll=ft.ScrollMode.AUTO
        )
        self.contenedor = ft.Container(
            col={"sm": 12, "md": 10, "lg": 4, "xl": 5},
            content=fields,
            padding=20,
            margin=ft.margin.only(top=20),
            border_radius=15,
            border=ft.border.all(2, ft.colors.BLACK),
            bgcolor=ft.colors.GREY_900
        )
        return (
            ft.ResponsiveRow(
                [self.contenedor],
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER
            )
        )

    def blank_error(self, e: ft.ControlEvent) -> None:
        """
            Reseteal la propiedad counter_text y counter_style
        de los campos de texto
        Args:
            e (ft.ControlEvent): Evento change de los campos de texto
        """
        e.control.counter_text = ""
        e.control.counter_style = None
        e.control.update()

    def is_blank(self) -> bool:
        """
            Chequea si algun campo de texto esta vacio

        Returns:
            bool: True si hay campos vacios, False caso contrario
        """
        if self.tb_address.value == "" or self.tb_city.value == "" or self.tb_dni.value == "" or self.tb_email.value == "" or self.tb_lastName.value == "" or self.tb_name.value == "" or self.tb_phone.value == "" or self.tb_zipcode.value == "":
            return True

    def check_email(self, email: str) -> bool:
        """
            Valida el formato correcto de un email
        Args:
            email (str): Cadena de texto a validar

        Returns:
            bool: True si el email no es valido, False caso contrario
        """
        if len(email) < 8 or email.find("@") == -1 or email.find(".") == -1:
            return True

        mail = email.split('@')
        if len(mail) != 2:
            return True

        if len(mail[0]) < 1 or len(mail[1]) < 4:
            return True

        if mail[1].find('.') == -1:
            return True

        doms = mail[1].split('.')
        if len(doms) < 2:
            return True

        return False

    def validate_phone(self, phone: str) -> bool:
        """
            Valida el formato correcto de un numero de telefono
        Maximo 12 digitos - Minimo 10 digitos
        Debe contener solo numeros
        Args:
            phone (str): Cadena de texto a validar
        Returns:
            bool: True si el numero de telefono no es valido, False caso contrario
        """

        if (len(phone) >= 10) and (len(phone) <= 13) and (phone.isnumeric()):
            return False
        else:
            return True

    def action_button_restart_fields(self, e: ft.ControlEvent = None) -> None:
        """
            Resetea los campos de texto
        Args:
            e (ft.ControlEvent, optional): Evento click del boton. Defaults to None.
        """
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        logging.info(f'[{date} (Search)] - Boton presionado: Reiniciar campos')
        self.restart_fields()
        self.update()

    def restart_fields(self) -> None:
        """
            Resetea los campos de texto
        """
        self.tb_id.value = ""
        self.tb_name.value = ""
        self.tb_lastName.value = ""
        self.tb_address.value = ""
        self.tb_city.value = ""
        self.tb_zipcode.value = ""
        self.tb_dni.value = ""
        self.tb_phone.value = ""
        self.tb_email.value = ""

        self.tb_id.read_only = False
        self.tb_name.read_only = True
        self.tb_lastName.read_only = True
        self.tb_address.read_only = True
        self.tb_city.read_only = True
        self.tb_zipcode.read_only = True
        self.tb_dni.read_only = True
        self.tb_phone.read_only = True
        self.tb_email.read_only = True

    def clear_textbox(self) -> None:
        """
            Limpia el contenido del textbox_row
        """
        sleep(7)
        self.textbox_row.value = ""
        self.textbox_row.color = ft.colors.WHITE
        self.update()

    def button_clicked(self, e: ft.ControlEvent) -> None:
        """
            Maneja los eventos click de los botones:

        button_search:
                Busca un cliente por id y completa los campos de texto
                del formulario con los datos del cliente encontrado.
                Luego habilita los campos de texto para poder actualizar.
                Habilita los botones de actualizar, eliminar y reiniciar campos.
                Si el cliente no existe, muestra un mensaje en el campo de texto.

        button_delete:
                Elimina un cliente por id.
                Si el cliente se elimina correctamente, muestra un mensaje en el 
                campo de texto textbox_row, reinicia los campos de texto y el estado
                de los botones.
                Si el cliente no se elimina correctamente, muestra un mensaje en el
                campo de texto textbox_row.

        button_update: 
                Valida que todos los valores de los campos de texto sean correctos.
                Luego envia los datos al endpoint de la api para actualizar el cliente.
                Si el cliente se actualiza correctamente, muestra un mensaje en el 
                campo de texto textbox_row y reinicia los campos de texto.
                Si algun valor no es correcto, muestra un mensaje 
                en el campo de texto textbox_row y en el campo de texto correspondiente.
                Si el cliente no se actualiza correctamente, muestra un mensaje en el
                campo de texto textbox_row.

        Args:
            e (ft.ControlEvent): Evento click de los botones
        """

        cliente = Cliente()
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        logging.info(f'ID: {self.tb_id.value}')

        # Accion de button_delete
        if e.control == self.button_delete:
            logging.info(f'[{date} (Search)] - Boton presionado: Eliminar')
            if cliente.delete(self.tb_id.value) == 200:
                logging.info(
                    f'[{date} (Search)] - Cliente eliminado correctamente')
                self.textbox_row.value = f"""El cliente {self.tb_name.value.strip()} {self.tb_lastName.value.strip()} ha sido eliminado con exito"""
                self.restart_fields()
            else:
                logging.info(
                    f'[{date} (Search)] - Cliente NO pudo ser eliminado')
                self.textbox_row.value = f"""El cliente {self.tb_name.value.strip()} {self.tb_lastName.value.strip()} NO PUDO SER ELIMINADO"""
                self.textbox_row.color = ft.colors.RED

        # Accion de button_update
        elif e.control == self.button_update:
            logging.info(f'[{date} (Search)] - Boton presionado: Actualizar')
            if self.is_blank():
                self.textbox_row.value = "No puede haber campos vacios"
                self.textbox_row.color = ft.colors.RED

            else:
                if self.check_email(self.tb_email.value):
                    self.textbox_row.value = "El email no es valido"
                    self.textbox_row.color = ft.colors.RED
                    self.tb_email.counter_text = "Ingrese un email valido"
                    self.tb_email.counter_style = ft.TextStyle(
                        color=ft.colors.RED)

                elif self.tb_dni.value.isnumeric() == False:
                    self.textbox_row.value = "El DNI debe ser un numero"
                    self.textbox_row.color = ft.colors.RED
                    self.tb_dni.counter_text = "Ingrese un DNI valido"
                    self.tb_dni.counter_style = ft.TextStyle(
                        color=ft.colors.RED)

                elif self.validate_phone(self.tb_phone.value):
                    self.textbox_row.value = "El numero de telefono NO es valido"
                    self.textbox_row.color = ft.colors.RED
                    self.tb_phone.counter_text = "Ingrese un numero de telefono valido"
                    self.tb_phone.counter_style = ft.TextStyle(
                        color=ft.colors.RED)

                else:
                    self.data = json.dumps({
                        "id": int(self.tb_id.value),
                        "name": self.tb_name.value,
                        "lastName": self.tb_lastName.value,
                        "address": self.tb_address.value,
                        "city": self.tb_city.value,
                        "zipCode": self.tb_zipcode.value,
                        "dni": int(self.tb_dni.value),
                        "phone": self.tb_phone.value,
                        "email": self.tb_email.value
                    })
                    logging.info(
                        f'[{date} (Search)] - Datos a actualizar: {self.data}')

                    if cliente.update(self.tb_id.value, self.data) == 200:
                        logging.info(
                            f'[{date} (Search)] - Cliente actualizado correctamente\n{self.data}'
                        )
                        self.textbox_row.value = f"""El cliente {self.tb_name.value.strip()} {self.tb_lastName.value.strip()} ha sido actualizado con exito"""
                        self.restart_fields()
                    else:
                        logging.info(
                            f'[{date} (Search)] - Cliente NO pudo ser actualizado'
                        )
                        self.textbox_row.value = f"""El cliente {self.tb_name.value.strip()} {self.tb_lastName.value.strip()} NO PUDO SER ACTUALIZADO"""
                        self.textbox_row.color = ft.colors.RED

        else:
            # Accion de button_search
            logging.info(f'[{date} (Search)] - Boton presionado: Buscar')
            if cliente.get_by_id(self.tb_id.value) == 200:
                self.textbox_row.value = ""
                self.tb_name.value = cliente.name.strip()
                self.tb_lastName.value = cliente.lastName.strip()
                self.tb_address.value = cliente.address.strip()
                self.tb_city.value = cliente.city.strip()
                self.tb_zipcode.value = cliente.zipCode.strip()
                self.tb_dni.value = str(cliente.dni).strip()
                self.tb_phone.value = cliente.phone.strip()
                self.tb_email.value = cliente.email.strip()
                self.tb_id.read_only = True
                self.tb_name.read_only = False
                self.tb_lastName.read_only = False
                self.tb_address.read_only = False
                self.tb_city.read_only = False
                self.tb_zipcode.read_only = False
                self.tb_dni.read_only = False
                self.tb_phone.read_only = False
                self.tb_email.read_only = False
                self.button_update.disabled = False
                self.button_delete.disabled = False
                self.button_restart_fields.disabled = False
                logging.info(
                    f'''[{date} (Search)] - Cliente encontrado: 
                        {cliente.name.strip()}
                        {cliente.lastName.strip()}
                        {cliente.address.strip()}
                        {cliente.city.strip()}
                        {cliente.zipCode.strip()}
                        {str(cliente.dni).strip()}
                        {cliente.phone.strip()}
                        {cliente.email.strip()}
                    '''
                )
            else:
                logging.info(f'[{date} (Search)] - Cliente NO encontrado')
                self.textbox_row.value = f"""El cliente codigo {self.tb_id.value.strip()} NO PUDO SER ENCONTRADO"""
                self.textbox_row.color = ft.colors.RED

        Thread(target=self.clear_textbox).start()
        self.update()
