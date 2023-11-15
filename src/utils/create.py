from flet import *
import flet as ft
import json

from utils.models import Cliente


class TabContentCreate(ft.UserControl):
    def __init__(self):
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
            capitalization=ft.TextCapitalization.NONE,
            keyboard_type=ft.KeyboardType.NUMBER,
            hint_text="Ingrese su numero de DNI",
            bgcolor='#1a1c1e'
        )

        self.tb_phone = ft.TextField(
            label="Telefono",
            capitalization=ft.TextCapitalization.NONE,
            keyboard_type=ft.KeyboardType.PHONE,
            hint_text="Ingrese su numero de telefono",
            bgcolor='#1a1c1e'
        )

        self.tb_email = ft.TextField(
            label="E-Mail",
            value="",
            keyboard_type=ft.KeyboardType.EMAIL,
            hint_text="Ingrese su correo electronico",
            bgcolor='#1a1c1e'
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

    def build(self):
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

    def validate_numbers(number: str, args):
        if not number.isnumeric():
            return True

    def open_dlg(self, e):
        e.page.dialog = self.dlgalert
        self.dlgalert.open = True
        e.page.update()

    def button_clicked(self, e: ft.ControlEvent):
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
        if cliente.create(data) == 201:
            self.textbox_row.value = f"""El cliente {self.tb_name.value.strip()} {self.tb_lastName.value.strip()} (ID: {cliente.id}) ha sido creado con exito"""
            self.tb_name.value = ""
            self.tb_lastName.value = ""
            self.tb_address.value = ""
            self.tb_city.value = ""
            self.tb_zipcode.value = ""
            self.tb_dni.value = ""
            self.tb_phone.value = ""
            self.tb_email.value = ""
        else:
            self.textbox_row.value = f"""El cliente {self.tb_name.value.strip()} {self.tb_lastName.value.strip()} NO PUDO SER CREADO"""

        self.update()
