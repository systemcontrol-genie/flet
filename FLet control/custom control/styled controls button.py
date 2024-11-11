import flet as ft

class MyButten(ft.ElevatedButton):
    def __init__(self, text, on_click):
        super().__init__()
        self.bgcolor = ft.colors.ORANGE_300
        self.color  = ft.colors.GREEN_800
        self.text= text
        self.on_click = on_click

def main(page:ft.Page):
    
    def ok_clicked(e):
        print("OK clicked")
    
    def cancel_clicked(e):
        print("Cancel clicked")

    page.add(
        MyButten(text = "OK", on_click = ok_clicked),
        MyButten(text = "Cencel", on_click =cancel_clicked),
    )

ft.app(main)