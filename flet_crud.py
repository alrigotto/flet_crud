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
        show_column.controls.clear()
        page.update()
        show_data()
    
    
    show_column = ft.Column(
        scroll = ft.ScrollMode.ALWAYS,
        expand = True,
        alignment=ft.MainAxisAlignment.START,        
    )
    
    def show_data():
        cursor.execute("SELECT * FROM costumers")
        rows = cursor.fetchall()
        for row in rows:
            show_column.controls.append(ft.ListTile(
                trailing=ft.IconButton(
                    icon=ft.Icons.DELETE,
                    icon_color=ft.Colors.RED,
                    # on_click=lambda e: remove_data(row[0]),
                ),
                shape=ft.RoundedRectangleBorder(radius=10),
                bgcolor_activated=ft.Colors.BLUE_300,
                leading=ft.Icon(
                    name=ft.Icons.PERSON,
                    color=ft.Colors.WHITE30,
                    size=45,
                ),
                bgcolor=ft.Colors.BLACK45,
                title=ft.Text("ID: " + str(row[0])),
                title_text_style=ft.TextStyle(size=8, color=ft.Colors.BLUE_300),
                subtitle=ft.Text("Name: " + row[1]),
                subtitle_text_style=ft.TextStyle(size=15, color=ft.Colors.BLUE_300),
                )
            )
        page.update()
    
    
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
        margin=0,
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
        margin=0,
        padding=5,
        alignment=ft.alignment.center,
        bgcolor=ft.Colors.WHITE12,
        width=page.on_resized,
        height=50,
        border_radius=10,
    )
    
    
    
    # remove_button = ft.Button(text="remove", on_click=remove_elm)
    show_data()
    
    page.add(
        # teste,
        # teste_txt,
        main_title,
        field_add_data,
        # remove_button,
        show_column,
    )
    
    
    # page.update()



ft.app(main)