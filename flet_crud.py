import flet as ft
import sqlite3

# sqllite start
# commands database strings:
sql_costumer = '''
    CREATE TABLE IF NOT EXISTS customer (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT);
'''
#insert data in column 'name'
sql_insert = '''
    INSERT INTO customer (name) VALUES (?)
'''

# create a table in database
def create_table():
    try:
        con = sqlite3.connect("data.db")
        cursor = con.cursor()
        
        cursor.execute(sql_costumer)
        
        con.commit()
    except con.DatabaseError as error:
        print("Database error", error)
    finally:
        if con:
            con.close()

# check if table was created
def get_all_table():
    try:
        con = sqlite3.connect("data.db")
        cursor = con.cursor()
        
        res = cursor.execute("SELECT * FROM customer")
        # print(res.fetchall())
        return res.fetchall()
    except con.DatabaseError as error:
        print("Database error", error)
        return None
    finally:
        if con:
            con.close()

# insert data in table
def insert_data(name):
    try:
        con = sqlite3.connect("data.db")
        cursor = con.cursor()
        
        cursor.execute(
            sql_insert,
            [name]
        )
        con.commit()
    except con.DatabaseError as error:
        print("Database error", error)
    finally:
        if con:
            con.close()

# remove data from table
def delete_data(identifier, by_name=True):
    try:
        con = sqlite3.connect("data.db")
        cursor = con.cursor()
        
        if by_name:
            cursor.execute(
                "DELETE FROM customer WHERE name = ?",
                [identifier]
            )
        else:
            cursor.execute(
                "DELETE FROM customer WHERE id = ?",
                [identifier]
            )
        con.commit()
    except con.DatabaseError as error:
        print("Database error", error)
    finally:
        if con:
            con.close()

# get id by name
def get_id_by_name(name):
    try:
        con = sqlite3.connect("data.db")
        cursor = con.cursor()
        
        cursor.execute("SELECT id FROM customer WHERE name = ?", [name])
        result = cursor.fetchone()
        return result[0] if result else None # ternary python operator
    except con.DatabaseError as error:
        print("Database error", error)
        return None
    finally:
        if con:
            con.close()

# update data in table
def update_data(id, new_name):
    try:
        con = sqlite3.connect("data.db")
        cursor = con.cursor()
        
        cursor.execute(
            "UPDATE customer SET name = ? WHERE id = ?",
            (new_name, id)
        )
        con.commit()
    except con.DatabaseError as error:
        print("Database error", error)
    finally:
        if con:
            con.close()

create_table()
# delete_data("Andre", by_name=True)
# insert_data("Rafael")
# x = get_all_table()
# print(x)
# y = get_id_by_name("Rafael")
# print(y)



# sqlite3 database end


# start flet code 

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
    
    
    
    def listTile_items(row: list):
        show_column.controls.append(
            ft.ListTile(
                shape=ft.RoundedRectangleBorder(radius=10),
                bgcolor_activated=ft.Colors.BLUE_300,
                leading=ft.Icon(
                    name=ft.Icons.PERSON,
                    color=ft.Colors.WHITE30,
                    size=30,
                ),
                bgcolor=ft.Colors.BLACK45,
                title=ft.Text("ID: " + str(row[0])),
                title_text_style=ft.TextStyle(size=10, color=ft.Colors.BLUE_300),
                subtitle=ft.Text("Name: " + row[1]),
                subtitle_text_style=ft.TextStyle(size=15, color=ft.Colors.BLUE_300),
                trailing= ft.PopupMenuButton(
                    icon_color=ft.Colors.RED,
                    items=[
                        ft.PopupMenuItem(
                            icon=ft.Icons.DELETE,
                            text="Delete",
                            on_click=popup_delete_alert_open,
                        ),
                        ft.PopupMenuItem(
                            icon=ft.Icons.EDIT,
                            text="Edit",
                        ),
                    ],
                ),
            )
        )
    
    def show_all_data():
        rows = get_all_table()
        for row in rows:
            listTile_items(row)
    
    def add_data(e):
        data = field_add_data.content.controls[0].value
        if not len(data.strip()) == 0: # check if data has only spaces or is empty
            insert_data(data) # insert data in database
            field_add_data.content.controls[0].value = "" # clear field after insert data
            listTile_items([get_id_by_name(data), data]) # insert data in list
            popup_add_data_close(e)
    
    def popup_add_data_open(e):
        e.control.page.overlay.append(popup_add_data)
        popup_add_data.open = True
        e.control.page.update()

    def popup_add_data_close(e): 
        popup_add_data.open = False
        e.control.page.update()

    def delete_item(e):
        item_name=e.control.parent.parent.subtitle.value[6:]
        show_column.controls.remove(e.control.parent.parent)
        delete_data(item_name, by_name=True)
        page.update()
    
    def popup_delete_alert_open(e):
        e.control.page.overlay.append(popup_delete_alert)
        popup_delete_alert.open = True
        e.control.page.update()
    
    def popup_delete_alert_close(e): 
        popup_delete_alert.open = False
        e.control.page.update()

    main_title = ft.Container(
        content=ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.VerticalAlignment.CENTER,
            controls=[
                ft.Text(
                    value="CRUD COM SQLITE",
                    size=16,
                    color=ft.Colors.BLUE_300,
                    # bgcolor=ft.Colors.WHITE12,
                    weight=ft.FontWeight.W_500,
                ),    
                ft.IconButton(
                    icon=ft.Icons.ADD_CIRCLE_OUTLINE,
                    icon_color=ft.Colors.BLUE_300,
                    alignment=ft.alignment.center,
                    padding=0,
                    on_click=popup_add_data_open,
                    
                )
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
    
    show_column = ft.Column(
        scroll = ft.ScrollMode.ALWAYS,
        expand = True,
        alignment=ft.MainAxisAlignment.START,        
    )
    
    field_add_data = ft.Container(
        content=ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.TextField(
                    label="Enter data:",
                    height=35,
                    width=150,
                    text_size=12,
                    border_radius=10,
                    border_color=ft.Colors.TRANSPARENT,
                    color=ft.Colors.BLUE_300,
                    label_style=ft.TextStyle(size=14, color=ft.Colors.WHITE24),
                    on_submit=add_data,
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
    
    
    popup_add_data=ft.AlertDialog(
        modal=True,
        title=ft.Text("Insert a new data", size=12),
        content=field_add_data,
        actions=[
            ft.TextButton("Insert", on_click=add_data),            
            ft.TextButton("Cancel", on_click=popup_add_data_close),
        ]
    )
    
    popup_delete_alert=ft.AlertDialog(
        modal=True,
        title=ft.Text("Delete", size=12),
        content=ft.Text("Are you sure you want to delete this item?"),
        actions=[
            ft.TextButton("Yes", on_click=delete_item),
            ft.TextButton("No", on_click=popup_delete_alert_close),
        ]
    )
    
    show_all_data()
    
    page.add(
        # teste,
        # teste_txt,
        main_title,
        # field_add_data,
        # remove_button,
        show_column,
    )
    
    
    page.update()



ft.app(main)