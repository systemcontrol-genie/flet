import flet as ft

def main(page: ft.page):
    t = ft.Text()
    page.add(
        ft.Row(controls=[
            ft.Text("A"),
            ft.Text("B"),
            ft.Text("C")
        ])
    )

ft.app(main)
