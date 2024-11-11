import flet as ft

def main(page):
    def add_clicked(e):
        page.add(ft.Checkbox(label=new_task.value))
        new_task.value = ""
        new_task.focus()
        new_task.update()
    
    new_task = ft.TextField(hint_text="what's needs to doen?", width=300)
    page.add(ft.Row([new_task , ft.ElevatedButton("add", on_click=add_clicked)]))

ft.app(main)