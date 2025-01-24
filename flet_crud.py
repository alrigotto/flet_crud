import flet as ft
import sqlite3


# database connection

connection = sqlite3.connect("data.db", check_same_thread=False)
cursor = connection.cursor()

# create table in database

def create_table():
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS costumers (id INTEGER PRIMARY KEY
        AUTOINCREMENT, name TEXT)
        
        """
    )
    
create_table()   

def main(page: ft.Page):
    page.title = "CRUD COM SQLITE"
    page.window.height=600
    page.window.width=300
    page.window.min_width=300
    # page.horizontal_alignment = "CENTER"
    # page.vertical_alignment = "CENTER"
    
    # def on_resized(e):
    #     page.add(ft.Text(f"Janela redimensionada para {e.width}x{e.height}"))
    # page.on_resized = on_resized
    
    def add_data(e):
        cursor.execute(
            "INSERT INTO costumers (name) VALUES (?)",
            [field_add_data.content.controls[0].value]
        )
        connection.commit()
        
    def show_data(e):
        cursor.execute("SELECT * FROM costumers")
        rows = cursor.fetchall()
        # print(rows)
        for row in rows:
            page.add(ft.Text(f"ID: {row[0]}, Name: {row[1]}"))
        page.update()
    
    # def show_data(e):
    #     page.add(ft.Text(field_add_data.content.controls[0].value))
    #     field_add_data.content.controls[0].value = ""
    #     page.update()
    
    main_title = ft.Container(
        content=ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Icon(
                    name=ft.Icons.FORMAT_LIST_NUMBERED_RTL,
                    color=ft.Colors.BLUE_300,
                ),
                ft.Text(
                    value="CRUD COM SQLITE",
                    size=16,
                    color=ft.Colors.BLUE_300,
                    # bgcolor=ft.Colors.WHITE12,
                    weight=ft.FontWeight.W_500,
                ),    
            ],
        ),
        margin=5,
        padding=5,
        alignment=ft.alignment.center,
        bgcolor=ft.Colors.WHITE12,
        width=page.on_resized,
        height=40,
        border_radius=10,
    )
    
    field_add_data = ft.Container(
        content=ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.TextField(
                    label="Enter data:",
                    height=35,
                    width=200,
                    text_size=15,
                    border_radius=10,
                    border_color=ft.Colors.TRANSPARENT,
                    color=ft.Colors.BLUE_300,
                    label_style=ft.TextStyle(size=15, color=ft.Colors.WHITE24),
                    
                    # hint_text="dsdssdd",
                    # hover_color=ft.Colors.RED,
                    # bgcolor=ft.Colors.WHITE12,
                ),
                ft.IconButton(
                    icon=ft.Icons.CHECK_CIRCLE_OUTLINE_ROUNDED,
                    icon_color=ft.Colors.BLUE_300,
                    on_click=add_data,
                    
                ),
            ],
        ),
        margin=5,
        padding=5,
        alignment=ft.alignment.center,
        bgcolor=ft.Colors.WHITE12,
        width=page.on_resized,
        height=50,
        border_radius=10,
    )
    
    show_button = ft.Button(text="Show data", on_click=show_data)
    
    page.add(
        # teste,
        # teste_txt,
        main_title,
        field_add_data,
        show_button,
    )
    
    
    page.update()



ft.app(main)