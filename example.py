import flet as ft
from color_selector import ColorSelector


def main(page: ft.Page):
    # page.theme_mode = 'dark'

    color_selector = ColorSelector(on_color=lambda color: print(color))

    page.add(
        ft.ElevatedButton(
            bgcolor='#1fa8f5',
            on_click=color_selector.open_dialog
        ),
        ft.ElevatedButton(
            bgcolor='#aa88f5',
            on_click=color_selector.open_dialog
        )
    )


if __name__ == '__main__':
    ft.app(target=main)
