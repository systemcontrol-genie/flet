import flet as ft

def main(page: ft.page):
    t = ft.Text(value='Hello , world' , color="green")
    page.controls.append(t)
    page.update()
ft.app(main)