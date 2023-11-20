from flet import *
import flet as ft
import json
import logging
from datetime import datetime
import os

from utils.api_cliente import Cliente


class TabContentCreate(ft.UserControl):
    """
        Formulario de creacion de clientes
    """

    def __init__(self):
        """
            Constructor de la clase TabContentCreate
        """
        super().__init__()
        self.title = "Crear Clientes"
        self.description = "CRUD de clientes"
        self.language = "es"
        self.author = "Raul Andres Orlando"
        self.keywords = "CRUD, clientes, api"

        self.vertical_alignment = ft.MainAxisAlignment.CENTER

        self.textbox_row = ft.Text()

        self.dlgalert = ft.AlertDialog(title=ft.Text(
            "Hello, you!"), on_dismiss=lambda e: print("Dialog dismissed!"))

        # self.tb_id = ft.TextField(
        #     label="ID",
        #     hint_text="0",
        #     bgcolor='#1a1c1e'
        # )

        self.tb_name = ft.TextField(
            label="Nombre",
            value="",
            capitalization=ft.TextCapitalization.WORDS,
            keyboard_type=ft.KeyboardType.NAME,
            hint_text="Ingrese su nombre",
            bgcolor='#1a1c1e'
        )

        self.tb_lastName = ft.TextField(
            label="Apellido",
            value="",
            capitalization=ft.TextCapitalization.WORDS,
            keyboard_type=ft.KeyboardType.NAME,
            hint_text="Ingrese su apellido",
            bgcolor='#1a1c1e'
        )

        self.tb_address = ft.TextField(
            label="Domicilio",
            value="",
            capitalization=ft.TextCapitalization.WORDS,
            keyboard_type=ft.KeyboardType.STREET_ADDRESS,
            hint_text="Ingrese su domicilio",
            bgcolor='#1a1c1e'
        )

        self.tb_city = ft.TextField(
            label="Ciudad",
            value="",
            capitalization=ft.TextCapitalization.WORDS,
            keyboard_type=ft.KeyboardType.NAME,
            hint_text="Ciudad de residencia",
            bgcolor='#1a1c1e'
        )

        self.tb_zipcode = ft.TextField(
            label="Codigo Postal",
            value="",
            capitalization=ft.TextCapitalization.CHARACTERS,
            keyboard_type=ft.KeyboardType.TEXT,
            hint_text="Codigo postal",
            bgcolor='#1a1c1e'
        )

        self.tb_dni = ft.TextField(
            label="DNI",
            value="",
            keyboard_type=ft.KeyboardType.NUMBER,
            hint_text="Ingrese su numero de DNI",
            bgcolor='#1a1c1e',
            on_change=self.blank_error
        )

        self.tb_phone = ft.TextField(
            label="Telefono",
            capitalization=ft.TextCapitalization.NONE,
            keyboard_type=ft.KeyboardType.PHONE,
            hint_text="Ingrese su numero de telefono",
            bgcolor='#1a1c1e',
            on_change=self.blank_error
        )

        self.tb_email = ft.TextField(
            label="E-Mail",
            value="",
            keyboard_type=ft.KeyboardType.EMAIL,
            hint_text="Ingrese su correo electronico",
            bgcolor='#1a1c1e',
            on_change=self.blank_error
        )

        self.button_submit = ft.ElevatedButton(
            content=ft.Row(
                [
                    ft.Icon(name=ft.icons.SAVE_OUTLINED, color="BLACK87"),
                    ft.Text(
                        "Guardar",
                        font_family="ARIAL",
                        style=ft.TextThemeStyle.HEADLINE_SMALL,
                        color=ft.colors.BLACK
                    )
                ],
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
            ),

            bgcolor=ft.colors.BLUE_500,
            style=ft.ButtonStyle(
                side={
                    ft.MaterialState.DEFAULT: ft.BorderSide(3, ft.colors.BLACK),
                    ft.MaterialState.HOVERED: ft.BorderSide(1, ft.colors.BLACK),
                },
                elevation={"pressed": 0, "": 5},
                animation_duration=500
            ),
            on_click=self.button_clicked
        )

    def build(self) -> ft.Control:
        """
            Construye el formulario de creacion de clientes
        Returns:
            ft.Control: Formulario de creacion de clientes
        """

        fields = ft.Column(
            controls=[
                ft.Divider(height=10, color='#212121'),
                ft.Row(
                    controls=[ft.Text(
                        "INGRESE LOS DATOS DEL CLIENTE",
                        font_family="ARIAL",
                        style=ft.TextThemeStyle.TITLE_LARGE,
                        color=ft.colors.WHITE,
                        max_lines=3,
                        overflow=ft.TextOverflow.ELLIPSIS,
                        text_align=ft.TextAlign.CENTER
                    )],
                    alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                    wrap=True
                ),
                ft.Row(
                    controls=[
                        self.textbox_row,
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
                    controls=[self.button_submit],
                    alignment=ft.MainAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER
                ),
                ft.Divider(height=20, color='#212121')
            ],
            spacing=20,
            scroll=ft.ScrollMode.AUTO
        )
        contenedor = ft.Container(
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
                [contenedor],
                alignment=ft.MainAxisAlignment.CENTER
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
            Chequea si hay campos vacios en el formulario

        Returns:
            bool: True si hay campos vacios, False caso contrario
        """
        if self.tb_address.value == "" or self.tb_city.value == "" or self.tb_dni.value == "" or self.tb_email.value == "" or self.tb_lastName.value == "" or self.tb_name.value == "" or self.tb_phone.value == "" or self.tb_zipcode.value == "":
            return True

    def check_email(self, email: str) -> bool:
        """
            Chequea si el email es valido
        Args:
            email (str): Email a validar
        Returns:
            bool: True si el email es invalido, False caso contrario
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
            phone (str): Numero de telefono a validar

        Returns:
            bool: True si el numero de telefono es invalido, False caso contrario
        """

        if (len(phone) >= 10) and (len(phone) <= 13) and (phone.isnumeric()):
            return False
        else:
            return True

    def limpiar_datos(self) -> None:
        """
            Limpia los campos de texto del formulario
        """
        self.tb_name.value = ""
        self.tb_lastName.value = ""
        self.tb_address.value = ""
        self.tb_city.value = ""
        self.tb_zipcode.value = ""
        self.tb_dni.value = ""
        self.tb_phone.value = ""
        self.tb_email.value = ""

    def button_clicked(self, e: ft.ControlEvent) -> None:
        """
            Maneja el evento click del boton button_submit:
                Se encarga de validar los campos y enviar los datos a la api.
                Si algun campo esta vacio, se muestra un mensaje de error en
                el textbox_row.
                Si algun campo no cumple con el formato requerido, se muestra un
                mensaje de error en el textbox_row y en el campo correspondiente.

                Si la respuesta dela api es 201, el cliente fue creado con exito y se
                muestra un mensaje de exito en el textbox_row con el nombre y apellido 
                del cliente y su id.
                Caso contrario, se muestra un mensaje de error en el textbox_row.
        Args:
            e (ft.ControlEvent): Evento click del boton submit
        """

        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        logging.info(f'[{date} (Create)] - Boton presionado: Guardar')
        if self.is_blank():
            self.textbox_row.value = "No puede haber campos vacios"
            self.textbox_row.color = ft.colors.RED

        else:
            if self.check_email(self.tb_email.value):
                self.textbox_row.value = "El email no es valido"
                self.textbox_row.color = ft.colors.RED
                self.tb_email.counter_text = "Ingrese un email valido"
                self.tb_email.counter_style = ft.TextStyle(color=ft.colors.RED)

            elif self.tb_dni.value.isnumeric() == False:
                self.textbox_row.value = "El DNI debe ser un numero"
                self.textbox_row.color = ft.colors.RED
                self.tb_dni.counter_text = "Ingrese un DNI valido"
                self.tb_dni.counter_style = ft.TextStyle(color=ft.colors.RED)

            elif self.validate_phone(self.tb_phone.value):
                self.textbox_row.value = "El numero de telefono NO es valido"
                self.textbox_row.color = ft.colors.RED
                self.tb_phone.counter_text = "Ingrese un numero de telefono valido"
                self.tb_phone.counter_style = ft.TextStyle(color=ft.colors.RED)

            else:
                logging.info(
                    f'[{date} (Create)] - Datos validados correctamente')
                logging.info(f'[{date} (Create)] - Enviando datos a la api')
                cliente = Cliente()

                data = json.dumps({
                    "name": self.tb_name.value,
                    "lastName": self.tb_lastName.value,
                    "address": self.tb_address.value,
                    "city": self.tb_city.value,
                    "zipCode": self.tb_zipcode.value,
                    "dni": int(self.tb_dni.value),
                    "phone": self.tb_phone.value,
                    "email": self.tb_email.value
                })
                logging.info(f'[{date} (Create)] - Datos enviados: {data}')
                if cliente.create(data) == 201:
                    self.textbox_row.value = f"""El cliente {self.tb_name.value.strip()} {self.tb_lastName.value.strip()} (ID: {cliente.id}) ha sido creado con exito"""
                    logging.info(
                        f'[{date} (Create)] - Cliente creado con exito')
                    self.limpiar_datos()

                else:
                    logging.info(
                        f'[{date} (Create)] - Error al crear el cliente')
                    self.textbox_row.value = f"""El cliente {self.tb_name.value.strip()} {self.tb_lastName.value.strip()} NO PUDO SER CREADO"""
                    self.textbox_row.color = ft.colors.RED

        self.update()
