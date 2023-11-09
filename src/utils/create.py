from flet import *
import flet as ft


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

        self.tb_id = ft.TextField(
            label="ID",
            hint_text="0",
            bgcolor='#1a1c1e'
        )

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
            value="",
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
            # color=ft.colors.BLACK87,
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

        # self.add(
        #     self.tb_name,
        #     self.tb_lastName,
        #     self.tb_address,
        #     self.tb_city,
        #     self.tb_zipcode,
        #     self.tb_dni,
        #     self.tb_phone,
        #     self.tb_email,
        #     self.button_submit,
        #     self.textbox_row,
        # )

        self.update()

    def button_clicked(self, e: ft.ControlEvent):
        e.page.textbox_row.value = f"""Textboxes values are:
                    '{self.tb_name.value}'
                    '{self.tb_lastName.value}'
                    '{self.tb_address.value}'
                    '{self.tb_city.value}'
                    '{self.tb_zipcode.value}'
                    '{self.tb_dni.value}'
                    '{self.tb_phone.value}'
                    '{self.tb_email.value}'
                """
        self.update()


if __name__ == '__main__':
    def main(page: ft.Page):
        page.add(TabContentCreate())

    ft.app(main)
