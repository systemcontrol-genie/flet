import flet as ft

def main(page: ft.Page):
    def butten_clicked(e):
        output_text.value = f"Dropdown value is: {color_dropdown.value}"
        page.update()
    
    output_text = ft.Text()
    submit_btn = ft.ElevatedButton(text="submit", on_click=butten_clicked)
    color_dropdown = ft.Dropdown(
        width=100,
        options=[
            ft.dropdown.Option("Red"),
            ft.dropdown.Option("Green"),
            ft.dropdown.Option("Blue"),
        ]
   )
    page.add(color_dropdown, submit_btn, output_text)

ft.app(main)