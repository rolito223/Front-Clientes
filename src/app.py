"""Esta aplicacion es el front end de la api Clientes
Pretende ser un CRUD multiplataforma de clientes
"""
import flet as ft


def main(page: ft.Page) -> None:
    """Funcion principal de la aplicacion
    Los campos que manejan los endpoints son:
    {
        "id": 0,
        "name": "string",
        "lastName": "string",
        "address": "string",
        "city": "string",
        "zipCode": "string",
        "dni": 0,
        "phone": "string",
        "email": "string"
    }
    Los endpoints de la api son:
    [GET]/api/Clientes Obtiene todos los clientes
    [GET]/api/Clientes/{id} Obtiene un cliente por id
    [POST]/api/Clientes Crea un nuevo cliente
    [PUT]/api/Clientes/{id} Actualiza un cliente
    [DELETE]/api/Clientes/{id} Elimina un cliente
    """
    page.title = "Clientes"
    page.description = "CRUD de clientes"
    page.language = "es"
    page.author = "Raul Andres Orlando"
    page.keywords = "CRUD, clientes, api"

    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def button_clicked(e):
        t.value = f"""Textboxes values are:  
                    '{tb_name.value}'
                    '{tb_lastName.value}'
                    '{tb_address.value}'
                    '{tb_city.value}'
                    '{tb_zipcode.value}'
                    '{tb_dni.value}'
                    '{tb_phone.value}'
                    '{tb_email.value}'
                """
        page.update()

    t = ft.Text()

    tb_id = ft.TextField(
        label="ID",
        value="0"
    )

    tb_name = ft.TextField(
        label="Nombre",
        value="",
        capitalization=ft.TextCapitalization.WORDS,
        keyboard_type=ft.KeyboardType.NAME,
        hint_text="Ingrese su nombre",
    )

    tb_lastName = ft.TextField(
        label="Read-only",
        read_only=True,
        value="Last name"
    )

    tb_address = ft.TextField(
        label="With placeholder",
        hint_text="Please enter text here"
    )

    tb_city = ft.TextField(
        label="With an icon",
        icon=ft.icons.EMOJI_EMOTIONS
    )

    tb_zipcode = ft.TextField(
        label="With an icon",
        icon=ft.icons.EMOJI_EMOTIONS
    )

    tb_dni = ft.TextField(
        label="Nombre",
        value="",
        capitalization=ft.TextCapitalization.WORDS
    )

    tb_phone = ft.TextField(
        label="Nombre",
        value="",
        capitalization=ft.TextCapitalization.WORDS
    )

    tb_email = ft.TextField(
        label="Nombre",
        value="",
        capitalization=ft.TextCapitalization.WORDS
    )

    b = ft.ElevatedButton(
        text="Submit",
        on_click=button_clicked
    )

    ft.ResponsiveRow([
        ft.Column(
            col={"sm": 12, "md": 6, "lg": 4, "xl": 3},
            controls=[
                ft.Text("Column 1"),
                t,
                tb_id,
                tb_name,
                tb_lastName,
                tb_address,
                tb_city,
                tb_zipcode,
                tb_dni,
                tb_phone,
                tb_email,
                b
            ]),
    ], alignment=ft.MainAxisAlignment.CENTER)

    page.add(
        tb_name,
        tb_lastName,
        tb_address,
        tb_city,
        tb_zipcode,
        tb_dni,
        tb_phone,
        tb_email,
        b,
        t,
    )


ft.app(target=main, port=5000, view=ft.WEB_BROWSER)
