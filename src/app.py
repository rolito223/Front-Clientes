import flet as ft
import logging

from utils.create import TabContentCreate
# from utils.icons import TabContentIcon

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

    def change_theme(e):
        """
        Summary:
            Cambia el tema de la aplicacion
        Args:
            e (ControlEvent): evento de control
        """
        page.theme_mode = "light" if page.theme_mode == "dark" else "dark"
        theme_icon_button.selected = not theme_icon_button.selected
        page.update()

    # Inicio del renderizado de la aplicacion

    theme_icon_button = ft.IconButton(
        ft.icons.DARK_MODE,
        selected=False,
        selected_icon=ft.icons.LIGHT_MODE,
        icon_size=35,
        tooltip="change theme",
        on_click=change_theme,
        style=ft.ButtonStyle(
            color={"": ft.colors.BLACK, "selected": ft.colors.WHITE}, ),
    )

    create = TabContentCreate()

    tabs = ft.Tabs(
        expand=True,
        scrollable=True,
        selected_index=0,
        tabs=[
            ft.Tab(
                text="",
                content=create,
                icon=ft.icons.SEARCH_OUTLINED
            ),
            ft.Tab(
                text="Alta",
                content=create,
                icon=ft.icons.CREATE_OUTLINED
            ),
            ft.Tab(
                text="Actualizar",
                content=create,
                icon=ft.icons.UPDATE_OUTLINED
            ),
            ft.Tab(
                text="Eliminar",
                content=create,
                icon=ft.icons.DELETE_FOREVER_OUTLINED
            )
        ]
    )

    page.add(tabs)

    page.update()


ft.app(
    target=main,
    route_url_strategy="path",
    view=ft.WEB_BROWSER,
    assets_dir="assets"
)
