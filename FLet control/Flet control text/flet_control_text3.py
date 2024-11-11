import flet as ft

def main(page: ft.page):
    first_name = ft.TextField()
    last_name = ft.TextField()
    #first_name.disabled = True
    #last_name.disabled = True
    #page.add(first_name, last_name)
    c = ft.Column(controls=[first_name, last_name])
    c.disabled = True
    page.add(c)

ft.app(main)