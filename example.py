import flet as ft
from color_selector import ColorSelector


def main(page: ft.Page):
    color_selector = ColorSelector()

    page.add(
        ft.ElevatedButton(
            bgcolor='#1fa8f5',
            on_click=color_selector.open_dialog
        )
    )


if __name__ == '__main__':
    ft.app(target=main)
