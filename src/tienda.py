from flet import AppBar, ElevatedButton, Page, Text, View, colors


def tienda(page):
    View(
        '/',
        [
            AppBar(
                title=Text('App Flet'),
                bgcolor=colors.SURFACE_VARIANT
            ),
            ElevatedButton(
                'Visitar la tienda',
                on_click=lambda _: page.go('/tienda')
            )
        ]
    )
