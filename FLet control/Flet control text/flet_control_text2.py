import flet as ft
import time

def main(page: ft.page):

    page.add(ft.Row(controls=[
        ft.TextField(label="your name"),
        ft.ElevatedButton(text='say my name!')
    ])
    )
ft.app(main)