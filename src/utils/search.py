from flet import *
import flet as ft
import json

from utils.models import Cliente


class TabContentSearch(ft.UserControl):
    def __init__(self):
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
            read_only=True
        )

        self.tb_phone = ft.TextField(
            label="Telefono",
            capitalization=ft.TextCapitalization.NONE,
            keyboard_type=ft.KeyboardType.PHONE,
            bgcolor='#1a1c1e',
            read_only=True
        )

        self.tb_email = ft.TextField(
            label="E-Mail",
            value="",
            keyboard_type=ft.KeyboardType.EMAIL,
            bgcolor='#1a1c1e',
            read_only=True
        )

        self.button_search = ft.ElevatedButton(
            content=ft.Row(
                [
                    ft.Icon(name=ft.icons.SEARCH_OUTLINED, color="BLACK87"),
                    ft.Text(
                        "Buscar",
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

        self.button_update = ft.ElevatedButton(
            content=ft.Row(
                [
                    ft.Icon(name=ft.icons.UPDATE_OUTLINED, color="BLACK87"),
                    ft.Text(
                        "Actualizar",
                        font_family="ARIAL",
                        style=ft.TextThemeStyle.HEADLINE_SMALL,
                        color=ft.colors.BLACK
                    )
                ],
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
            ),
            disabled=True,
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

        self.button_delete = ft.ElevatedButton(
            content=ft.Row(
                [
                    ft.Icon(name=ft.icons.DELETE_OUTLINE, color="#FF3333"),
                    ft.Text(
                        "Eliminar",
                        font_family="ARIAL",
                        style=ft.TextThemeStyle.HEADLINE_SMALL,
                        color=ft.colors.BLACK
                    )
                ],
                disabled=True,
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
            ),

            bgcolor=ft.colors.YELLOW_400,
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
                        self.button_delete
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
                alignment=ft.MainAxisAlignment.CENTER
            )
        )

    def restart_fields(self):
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

    def button_clicked(self, e: ft.ControlEvent):
        cliente = Cliente()
        if e.control == self.button_delete:
            if cliente.delete(self.tb_id.value) == 200:
                print(e, "Cliente eliminado correctamente")
                self.textbox_row.value = f"""El cliente {self.tb_name.value.strip()} {self.tb_lastName.value.strip()} ha sido eliminado con exito"""
                self.restart_fields()
            else:
                self.textbox_row.value = f"""El cliente {self.tb_name.value.strip()} {self.tb_lastName.value.strip()} NO PUDO SER ELIMINADO"""

        elif e.control == self.button_update:
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
            if cliente.update(self.tb_id.value, self.data) == 200:
                self.textbox_row.value = f"""El cliente {self.tb_name.value.strip()} {self.tb_lastName.value.strip()} ha sido actualizado con exito"""
                self.restart_fields()
            else:
                self.textbox_row.value = f"""El cliente {self.tb_name.value.strip()} {self.tb_lastName.value.strip()} NO PUDO SER ACTUALIZADO"""

        else:
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
            else:
                self.textbox_row.value = f"""El cliente codigo {self.tb_id.value.strip()} NO PUDO SER ENCONTRADO"""

        self.update()
