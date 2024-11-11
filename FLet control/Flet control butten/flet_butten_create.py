import flet as ft

def main(page: ft.page):
    btn = ft.ElevatedButton("Click me!")
    page.add(btn)

ft.app(main)