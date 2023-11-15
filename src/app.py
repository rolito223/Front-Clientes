import flet as ft
import logging

from utils.create import TabContentCreate
from utils.search import TabContentSearch


logger = logging.log(logging.DEBUG, "/logs/mainmenu.log")


def main(page: ft.Page):
    """Menu main de la aplicacion
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
    logging.info("Iniciando mainmenu.py")

    # Encabezado de la aplicacion

    page.title = "CRUD Clientes"
    page.theme_mode = "dark"
    page.vertical_alignment = "start"
    page.horizontal_alignment = "center"
    page.window_width = 800
    page.window_height = 1000
    # page.window_maximized = True

    # Permite agregar una confirmacion al salir de la aplicacion
    def window_event(e):
        if e.data == "close":
            page.dialog = confirm_dialog
            confirm_dialog.open = True
            page.update()

    page.window_prevent_close = True
    page.on_window_event = window_event

    def yes_click(e):
        page.window_destroy()

    def no_click(e):
        confirm_dialog.open = False
        page.update()

    confirm_dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("Se requiere confirmacion", size=12),
        content=ft.Text("Realmente desea salir de la aplicacion?"),
        actions=[
            ft.ElevatedButton("Si", on_click=yes_click),
            ft.OutlinedButton("No", on_click=no_click),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    restart_button = ft.IconButton(
        ft.icons.REFRESH,
        icon_size=35,
        tooltip="restart app",
        on_click=lambda e: page.reload(),
        style=ft.ButtonStyle(
            color=ft.colors.WHITE,
        ),
    )

    page.appbar = ft.AppBar(
        title=ft.Text(
            "CRUD Clientes",
            color="white",
            size=20
        ),
        center_title=True,
        bgcolor="blue",
        actions=[restart_button],
        leading_width=40,
        leading=ft.IconButton(
            icon=ft.icons.CODE,
            icon_color=ft.colors.YELLOW_ACCENT,
            on_click=lambda e: page.launch_url(
                "https://github.com/rolito223/Front-Clientes"),
            tooltip="View Code"
        )
    )

    create = TabContentCreate()
    search = TabContentSearch()

    tabs = ft.Tabs(
        expand=True,
        scrollable=True,
        selected_index=0,
        tabs=[
            ft.Tab(
                text="",
                content=search,
                icon=ft.icons.SEARCH_OUTLINED
            ),
            ft.Tab(
                text="Alta",
                content=create,
                icon=ft.icons.CREATE_OUTLINED
            )
        ]
    )

    page.add(tabs)

    page.update()


ft.app(
    target=main,
    route_url_strategy="path",
    # view=ft.WEB_BROWSER,
    assets_dir="assets"
)
