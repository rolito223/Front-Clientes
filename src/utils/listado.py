from flet import *
import flet as ft
import json
import logging
from datetime import datetime
import os
from threading import Thread
from time import sleep

from utils.api_cliente import Cliente


class TabContentListar(ft.UserControl):
    """
        Clase que contiene el contenido de la pestaña de busqueda
    Args:
        ft (_type_): _description_
    """

    def __init__(self):
        """
            Constructor de la clase TabContentListar
        """
        super().__init__()
        self.title = "Crear Clientes"
        self.description = "CRUD de clientes"
        self.language = "es"
        self.author = "Raul Andres Orlando"
        self.keywords = "CRUD, clientes, api"

        self.vertical_alignment = ft.MainAxisAlignment.CENTER

        self.textbox_row = ft.Text()

        self.contenedor_lista = ft.DataTable(
            columns=[
                ft.DataColumn(
                    ft.Text(
                        'ID', size=14, weight=ft.FontWeight.BOLD
                    )
                ),
                ft.DataColumn(
                    ft.Text(
                        'Nombre', size=14,
                        weight=ft.FontWeight.BOLD
                    )
                ),
                ft.DataColumn(
                    ft.Text(
                        'Apellido', size=14,
                        weight=ft.FontWeight.BOLD
                    )
                ),
                ft.DataColumn(
                    ft.Text(
                        'Direccion', size=14,
                        weight=ft.FontWeight.BOLD
                    )
                ),
                ft.DataColumn(
                    ft.Text(
                        'Ciudad', size=14,
                        weight=ft.FontWeight.BOLD
                    )
                ),
                ft.DataColumn(
                    ft.Text(
                        'Codigo Postal', size=14,
                        weight=ft.FontWeight.BOLD
                    )
                ),
                ft.DataColumn(
                    ft.Text(
                        'DNI', size=14, weight=ft.FontWeight.BOLD
                    )
                ),
                ft.DataColumn(
                    ft.Text(
                        'Telefono', size=14,
                        weight=ft.FontWeight.BOLD
                    )
                ),
                ft.DataColumn(
                    ft.Text(
                        'Email', size=14,
                        weight=ft.FontWeight.BOLD
                    )
                )
            ],
            column_spacing=20,
            horizontal_margin=10
        )

        self.button_search = ft.FloatingActionButton(
            icon=ft.icons.SEARCH_OUTLINED,
            bgcolor=ft.colors.BLUE_500,
            on_click=self.button_clicked
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
                        self.button_search, self.textbox_row
                    ]
                ),
                ft.Row(
                    controls=[
                        self.contenedor_lista
                    ],
                    scroll=ft.ScrollMode.AUTO
                )
            ],
            spacing=20,
            scroll=ft.ScrollMode.AUTO,
            alignment=MainAxisAlignment.CENTER
        )
        self.contenedor = ft.Container(
            col={"sm": 24, "md": 12, "lg": 8, "xl": 10},
            content=fields,
            padding=20,
            margin=ft.margin.only(top=20),
            border_radius=15,
            border=ft.border.all(2, ft.colors.BLACK),
            bgcolor=ft.colors.GREY_900,
            alignment=alignment.top_center
        )
        return (
            ft.ResponsiveRow(
                [self.contenedor],
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER
            )
        )

    def clear_textbox(self) -> None:
        """
            Limpia el contenido del textbox_row
        """
        sleep(10)
        self.textbox_row.value = ""
        self.textbox_row.color = ft.colors.WHITE
        self.update()

    def button_clicked(self, e: ft.ControlEvent) -> None:
        """
            Maneja los eventos click de los botones:

        button_search:
            Lista todos los clientes existentes con sus respectivas propiedades.
        Args:
            e (ft.ControlEvent): Evento click de los botones
        """

        cliente = Cliente()
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        logging.info(f'Solicitud de listado de clientes')

        # Accion de button_search
        logging.info(f'[{date} (Search)] - Boton presionado: Buscar')
        if cliente.get_all() == 200:
            self.contenedor_lista.rows.clear()
            self.textbox_row.value = ""
            for data in cliente.data:
                self.contenedor_lista.rows.append(
                    ft.DataRow(
                        [
                            ft.DataCell(
                                ft.Text(
                                    str(data['id']),
                                    size=12, selectable=True
                                )
                            ),
                            ft.DataCell(
                                ft.Text(
                                    data['name'], size=12, selectable=True
                                )
                            ),
                            ft.DataCell(
                                ft.Text(
                                    data['lastName'],
                                    size=12, selectable=True
                                )
                            ),
                            ft.DataCell(
                                ft.Text(
                                    data['address'],
                                    size=12, selectable=True
                                )
                            ),
                            ft.DataCell(
                                ft.Text(
                                    data['city'], size=12, selectable=True
                                )
                            ),
                            ft.DataCell(
                                ft.Text(
                                    data['zipCode'],
                                    size=12, selectable=True
                                )
                            ),
                            ft.DataCell(
                                ft.Text(
                                    str(data['dni']),
                                    size=12, selectable=True
                                )
                            ),
                            ft.DataCell(
                                ft.Text(
                                    data['phone'], size=12,
                                    selectable=True
                                )
                            ),
                            ft.DataCell(
                                ft.Text(
                                    data['email'], size=12,
                                    selectable=True
                                )
                            )
                        ]
                    )
                )

            logging.info(
                f'[{date} (Search)] - Listado generado: {len(cliente.data)} clientes')
        else:
            logging.info(f'[{date} (Search)] - Error al listar clientes')
            self.textbox_row.value = f'*** ERROR AL LISTAR CLIENTES ***'
            self.textbox_row.color = ft.colors.RED

        Thread(target=self.clear_textbox).start()
        self.update()
