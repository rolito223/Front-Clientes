import flet as ft
import logging
from datetime import datetime
import os

from utils.create import TabContentCreate
from utils.search import TabContentSearch


def main(page: ft.Page):
    """
        Renderiza la aplicacion y maneja los eventos de la misma.
    Librerias:
        Se utiliza la libreria flet para renderizar la aplicacion.
        El backend de la aplicacion es una api rest desarrollada en .net core.
        Se utiliza la libreria requests para realizar las peticiones a la api.
        Se utiliza la libreria logging para guardar los logs de la aplicacion.
        Se utiliza la libreria datetime para el manejo de fechas.

    Eventos:
        El evento on_window_event se utiliza para agregar una confirmacion 
        al salir de la aplicacion.

        El evento on_exit_button_click se utiliza para agregar una confirmacion al presionar
        el boton exit_button (Solo version de escritorio y mobile).

        El evento yes_click del boton de confirmacion se utiliza para cerrar la aplicacion.

        El evento no_click del boton de confirmacion se utiliza para cerrar el dialogo de confirmacion.

        El evento on_click del boton de github se utiliza para abrir el repositorio
        en el navegador.

    Vistas:
        TabContentCreate: Vista para el tab de alta de clientes.

        TabContentSearch: Vista para el tab de busqueda de clientes.

        Por defecto se muestra la pestaña TabContentSearch.

        Appbar: Encabezado de la aplicacion con el titulo, el acceso al repositorio y
        el boton de salir(Solo version de escritorio y mobile).

    Endpoints:

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
    # Chequeo que exista el path, caso contrario lo creo
    os.path.exists(
        f'{os.path.abspath("logs")}'
    ) or os.mkdir(
        f'{os.path.abspath("logs")}'
    )

    logging.basicConfig(
        format='%(levelname)s:%(message)s',
        filename=f'{os.path.abspath("logs")}\{datetime.now().strftime("%Y-%m-%d")}.log',
        filemode='a',
        level=logging.INFO
    )

    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    logging.info(f'[{date} (Main)] - Inicio de la aplicacion')

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
        logging.info(f'[{date} (Main)] - Cierre de la aplicacion')
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

    def on_exit_button_click(e):
        page.dialog = confirm_dialog
        confirm_dialog.open = True
        page.update()

    exit_button = ft.IconButton(
        icon=ft.icons.EXIT_TO_APP,
        icon_color=ft.colors.YELLOW_ACCENT,
        on_click=lambda e: on_exit_button_click(e),
        tooltip="Salir"
    )

    page.appbar = ft.AppBar(
        title=ft.Text(
            "CRUD Clientes",
            color="white",
            size=20
        ),
        center_title=True,
        bgcolor="blue",
        actions=[exit_button],
        leading_width=40,
        leading=ft.IconButton(
            icon=ft.icons.CODE,
            icon_color=ft.colors.YELLOW_ACCENT,
            on_click=lambda e: page.launch_url(
                "https://github.com/rolito223/Front-Clientes"),
            tooltip="Ir al repositorio"
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
    # view=ft.WEB_BROWSER,  # Permite abrir la aplicacion en el navegador
    assets_dir="assets"
)
