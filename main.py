import tkinter
from tkinter import ttk
import customtkinter
import CTkScrollableDropdown
from CTkScrollableDropdown import *
from CTkTable import *
from CTkMessagebox import CTkMessagebox
import time
import pandas as pd
from tqdm import tqdm
from zenpy import Zenpy
import json
import requests
import datetime
import os

customtkinter.set_appearance_mode("light") #"system", "dark" y "light"
customtkinter.set_default_color_theme("dark-blue") # Themes: "blue" (standard), "green", "dark-blue"

# Verificar la existencia de la carpeta "Fuente"
carpeta_fuente = "Fuente"
if not os.path.exists(carpeta_fuente):
    os.makedirs(carpeta_fuente)
    print(f"Carpeta '{carpeta_fuente}' creada correctamente.")

# Verificar la existencia de la carpeta "Excel"
carpeta_excel = "Excel"
if not os.path.exists(carpeta_excel):
    os.makedirs(carpeta_excel)
    print(f"Carpeta '{carpeta_excel}' creada correctamente.")

# Verificar la existencia de la carpeta "Seguimiento"
carpeta_seguimiento = "Seguimiento"
if not os.path.exists(carpeta_seguimiento):
    os.makedirs(carpeta_seguimiento)
    print(f"Carpeta '{carpeta_seguimiento}' creada correctamente.")

# Abrir el archivo JSON
with open('Fuente/agentes_zendesk.json', 'r') as json_file:
    agentes = json.load(json_file)

values = [item['name'] for item in agentes]

# Convertir el JSON a DataFrame
df_agentes = pd.read_json('Fuente/agentes_zendesk.json')
dic_agentes = df_agentes.to_dict(orient='records')
df_usuarios = pd.read_json('Fuente/usuarios_zendesk.json')
dic_usuarios = df_usuarios.to_dict(orient='records')

# Leer el archivo JSON
with open('Fuente/formularios_zendesk.json', 'r') as file:
    data = json.load(file)

# Acceder a la lista de formularios
json_ticket_forms = data['ticket_forms']  # luego en la variable ticket_forms usa para tener todos los formularios

# Filtrar los formularios cuyo título comienza con 'SCH'
filtered_forms = [formulario for formulario in json_ticket_forms if formulario['form_title'].startswith(
    'SCH')]  # Aqui, lo que està pasando es que como se define luego en el boton los valores que puede tomar, solo se mostraran los de la SCH, pero si se deja sin comentario la de abajo, se estarian desplegando todos los formularios
# filtered_forms = [formulario for formulario in json_ticket_forms if formulario['form_title']]

def cargar_todo():
    # Abrir el archivo JSON
    with open('Fuente/agentes_zendesk.json', 'r') as json_file:
        agentes = json.load(json_file)

    values = [item['name'] for item in agentes]

    # Convertir el JSON a DataFrame
    df_agentes = pd.read_json('Fuente/agentes_zendesk.json')
    dic_agentes = df_agentes.to_dict(orient='records')
    df_usuarios = pd.read_json('Fuente/usuarios_zendesk.json')
    dic_usuarios = df_usuarios.to_dict(orient='records')

    # Leer el archivo JSON
    with open('Fuente/formularios_zendesk.json', 'r') as file:
        data = json.load(file)

    # Acceder a la lista de formularios
    json_ticket_forms = data['ticket_forms']  # luego en la variable ticket_forms usa para tener todos los formularios

    # Filtrar los formularios cuyo título comienza con 'SCH'
    filtered_forms = [formulario for formulario in json_ticket_forms if formulario['form_title'].startswith(
        'SCH')]  # Aqui, lo que està pasando es que como se define luego en el boton los valores que puede tomar, solo se mostraran los de la SCH, pero si se deja sin comentario la de arriba, se estarian desplegando todos los formularios
    # filtered_forms = [formulario for formulario in json_ticket_forms if formulario['form_title']]
    def checkmark():
        # Show some positive message with the checkmark icon
        CTkMessagebox(title="Felicitaciones",
                      message=f"Se realizó la descarga y actualización de los archivos.",
                      icon="check", option_1="Muy bien")

    checkmark()
    print("Carga Completa")

# pyinstaller --noconfirm --onefile --console --name "AppZendesk" -F main.py --collect-all customtkinter -w
# pyinstaller --noconfirm --onefile --windowed --name "AppZendesk" --add-data "C:/Users/aparedes/PycharmProjects/AppZendesk/agentes_zendesk.json;." --add-data "C:/Users/aparedes/PycharmProjects/AppZendesk/usuarios_zendesk.json;." --add-data "C:/Users/aparedes/PycharmProjects/AppZendesk/CTkMessagebox;CTkMessagebox/" --add-data "C:/Users/aparedes/PycharmProjects/AppZendesk/CTkScrollableDropdown;CTkScrollableDropdown/" --collect-all customtkinter -w "C:/Users/aparedes/PycharmProjects/AppZendesk/main.py"
# pyinstaller --noconfirm --onefile --windowed --name "AppZendeskV5" --add-data "C:/Users/aparedes/PycharmProjects/AppZendesk/CTkMessagebox;CTkMessagebox/" --add-data "C:/Users/aparedes/PycharmProjects/AppZendesk/CTkScrollableDropdown;CTkScrollableDropdown/" --collect-all customtkinter -w "C:/Users/aparedes/PycharmProjects/AppZendesk/main.py"
# pyinstaller --noconfirm --onefile --console --name "APP Zendesk (Console)" --upx-dir "C:/Users/aparedes/PycharmProjects/AppZendesk/upx-4.0.2-win64" --add-data "CTkMessagebox;CTkMessagebox/" --add-data "CTkScrollableDropdown;CTkScrollableDropdown/" --collect-all customtkinter  main.py
# pyinstaller --noconfirm --onefile --console --name "APP Zendesk (Console)" --add-data "CTkMessagebox;CTkMessagebox/" --add-data "CTkScrollableDropdown;CTkScrollableDropdown/" --collect-all customtkinter  main.py

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        # configure window
        self.title("Zendesk Envío de Tickets Masivos")
        self.geometry(f"{1320}x{720}")


        # configure grid layout
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure((1,2,3), weight=1)
        self.grid_rowconfigure((0,1,2,3), weight=1)

        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self,
                                                               values=["60%", "70%", "80%", "90%", "100%", "110%",
                                                                       "120%", "130%", "140%", "150%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=5, column=0, columnspan=2, padx=60, pady=(20, 20), sticky="w")
        self.scaling_optionemenu.set("100%")

        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self,
                                                                       values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=5, column=0, columnspan=2, padx=60, pady=(20, 20), sticky="e")
        self.appearance_mode_optionemenu.set("Light")

        # ········································· BOTONES ACTUALIZACION ·················································
        def usuarios():
            self.progressbar.set(0)
            msg = CTkMessagebox(title="Confirmar descarga/actualización de usuarios",
                                message="Se iniciará la descarga de usuarios desde Zendesk API. Este proceso tomará unos minutos (7 a 10) para crear/actualizar dos archivos en la carpeta fuente: (i) 'Fuente/usuarios_zendesk.json' y (ii) 'Excel/Usuarios [dia-mes-año] [hora.minuto].xlsx'.",
                                icon="question", option_1="Aceptar", option_2="Cancelar")
            response = msg.get()
            if response == "Aceptar":
                zenpy_client = Zenpy(domain='zendesk.com', subdomain='conicytoirs', email="pfcha_staff@anid.cl", token='aiUPPMqY5pFcSSNt5UpUx2vIFlaAuI6GgOdoHKCR')
                # Obtener la lista de usuarios
                users = zenpy_client.users()
                data = []
                # Recorrer todos los usuarios con barra de progreso
                for index, user in enumerate(tqdm(users, desc="Procesando usuarios", unit='user'), start=1):
                    data.append(user.to_dict())  # Convertir el usuario a un diccionario y agregarlo a la lista
                    if index == len(users):
                        # Guardar la lista de usuarios en el archivo JSON
                        with open("Fuente/json_usuarios.json", "w") as file:
                            json.dump(data, file, indent=2)
                        # Leer el archivo JSON como un DataFrame
                        df_users = pd.read_json("Fuente/json_usuarios.json")

                        # Convertir datetimes a timezone-unaware
                        df_users["created_at"] = df_users["created_at"].dt.tz_convert(None)
                        df_users["last_login_at"] = df_users["last_login_at"].dt.tz_convert(None)
                        df_users["updated_at"] = df_users["updated_at"].dt.tz_convert(None)

                        # Expandir el diccionario 'user_fields' en columnas individuales
                        df_users = pd.concat(
                            [df_users.drop(['user_fields'], axis=1), df_users['user_fields'].apply(pd.Series)],
                            axis=1)

                        # Obtener la fecha y hora actual
                        fecha_actual = datetime.datetime.now().strftime("%d-%m-%Y")
                        hora_actual = datetime.datetime.now().strftime("%H.%M")
                        # Obtener la cantidad de registros en el DataFrame
                        total_rows = len(df_users)
                        # Generar el nombre del archivo de Excel
                        nombre_archivo = f"Excel/Usuarios [{fecha_actual}] [{hora_actual}] [{total_rows} registros].xlsx"

                        # Guardar el DataFrame resultante en un archivo de Excel y Json
                        df_users.to_excel(nombre_archivo, index=False)
                        df_users[["id", "name", "email"]].to_json("Fuente/usuarios_zendesk.json")

                    # Actualizar la barra de progreso
                    self.progressbar.set(index / len(users))
                    self.update()  # Actualizar la interfaz gráfica

                print("Descarga Exitosa")
                cargar_todo()
            else:
                print("Cancelado")
                return

        def agentes():
            self.progressbar.set(0)
            msg = CTkMessagebox(title="Confirmar descarga/actualización de agentes",
                                message="Se iniciará la descarga de agentes desde Zendesk API. Este proceso tomará unos minutos para crear/actualizar dos archivos en la carpeta fuente: (i) 'Fuente/agentes_zendesk.json' y (ii) 'Excel/Agentes [dia-mes-año] [hora.minuto].xlsx'.",
                                icon="question", option_1="Aceptar", option_2="Cancelar")
            response = msg.get()
            if response == "Aceptar":
                zenpy_client = Zenpy(domain='zendesk.com', subdomain='conicytoirs', email="pfcha_staff@anid.cl",
                                     token='aiUPPMqY5pFcSSNt5UpUx2vIFlaAuI6GgOdoHKCR')

                #agents = zenpy_client.search("role:admin role:agent", type='user', sort_by='name', sort_order='desc')
                agents = zenpy_client.search("role:admin role:agent", type='user')
                data = []
                for index, agent in enumerate(tqdm(agents, desc="Procesando agentes", unit='agent'), start=1):
                    data.append(agent.to_dict())

                    if index == len(agents):
                        # Guardar la lista de usuarios en el archivo JSON
                        with open("Fuente/agentes_zendesk.json", "w") as file:
                            json.dump(data, file, indent=2)
                        # Leer el archivo JSON como un DataFrame
                        df_agents = pd.read_json("Fuente/agentes_zendesk.json")

                        # Convertir datetimes a timezone-unaware
                        df_agents["created_at"] = df_agents["created_at"].dt.tz_convert(None)
                        df_agents["last_login_at"] = df_agents["last_login_at"].dt.tz_convert(None)
                        df_agents["updated_at"] = df_agents["updated_at"].dt.tz_convert(None)

                        # Obtener la fecha y hora actual
                        fecha_actual = datetime.datetime.now().strftime("%d-%m-%Y")
                        hora_actual = datetime.datetime.now().strftime("%H.%M")
                        # Obtener la cantidad de registros en el DataFrame
                        total_rows = len(df_agents)
                        # Generar el nombre del archivo de Excel
                        nombre_archivo = f"Excel/Agentes [{fecha_actual}] [{hora_actual}] [{total_rows} registros].xlsx"

                        # Guardar el DataFrame resultante en un archivo de Excel y Json
                        df_agents.to_excel(nombre_archivo, index=False)
                        df_agents[df_agents['role'] != 'end-user'][["id", "name", "email"]].to_json(
                            "Fuente/agentes_zendesk.json", orient='records')

                    # Actualizar la barra de progreso
                    self.progressbar.set(index / len(agents))
                    self.update()  # Actualizar la interfaz gráfica
                print("Descarga Exitosa")
                cargar_todo()
            else:
                print("Cancelado")
                return


        def formularios():
            self.progressbar.set(0)
            msg = CTkMessagebox(title="Confirmar descarga/actualización de formularios",
                                message="Se iniciará la descarga de formularios desde Zendesk API. Este proceso tomará unos minutos para crear/actualizar dos archivos en la carpeta fuente: (i) 'Fuente/formularios_zendesk.json' y (ii) 'Excel/Formularios [dia-mes-año] [hora.minuto].xlsx'.",
                                icon="question", option_1="Aceptar", option_2="Cancelar")
            response = msg.get()
            if response == "Aceptar":
                # Configurar las credenciales de la API de Zendesk
                user = "pfcha_staff@anid.cl"
                token = "aiUPPMqY5pFcSSNt5UpUx2vIFlaAuI6GgOdoHKCR"
                url_forms = "https://conicytoirs.zendesk.com/api/v2/ticket_forms.json"

                data = {"ticket_forms": []}
                max_retries1 = 3
                retries1 = 0

                while retries1 < max_retries1:
                    try:
                        response = requests.get(url_forms, auth=(user + "/token", token))
                        if response.status_code == 200:
                            ticket_forms = response.json()["ticket_forms"]
                            for index, form in enumerate(tqdm(ticket_forms, desc="Procesando formularios", unit='form'),
                                                         start=1):
                                form_data = {
                                    "form_id": form["id"],
                                    "form_title": form["name"],
                                    "form_fields": []
                                }
                                for field_id in form['ticket_field_ids']:
                                    url = 'https://conicytoirs.zendesk.com/api/v2/ticket_fields/{}.json'
                                    max_retries2 = 3
                                    retries2 = 0

                                    while retries2 < max_retries2:
                                        try:
                                            response_field = requests.get(url.format(field_id),
                                                                          auth=(user + "/token", token))
                                            response_field.raise_for_status()

                                            if response_field.status_code == 200:
                                                field_data = response_field.json()['ticket_field']
                                                field_name = field_data['title']
                                                form_data["form_fields"].append({
                                                    "field_id": field_id,
                                                    "field_title": field_name
                                                })
                                                break  # Salir del bucle while si la solicitud fue exitosa

                                            elif response_field.status_code == 429:
                                                seconds_to_wait = int(response.headers["Retry-After"])
                                                print("Api transfer rate sobrepasada. Esperar:", seconds_to_wait,
                                                      "segundos.")
                                                time.sleep(seconds_to_wait)
                                                retries1 += 1
                                                if retries2 == max_retries2:
                                                    field_data = response_field.json()['ticket_field']
                                                    field_name = "field_data['title']"
                                                    form_data["form_fields"].append({
                                                        "field_id": "field_id",
                                                        "field_title": "field_name"})
                                            else:
                                                print('Error al obtener el campo con ID {}: {}'.format(field_id,
                                                                                                       response_field.status_code))
                                                time.sleep(3)
                                                retries2 += 1
                                                if retries2 == max_retries2:
                                                    field_data = response_field.json()['ticket_field']
                                                    field_name = "field_data['title']"
                                                    form_data["form_fields"].append({
                                                        "field_id": "field_id",
                                                        "field_title": "field_name"})

                                        except requests.exceptions.SSLError:
                                            print('Error SSL. Reintentando la solicitud...')
                                            retries2 += 1
                                            time.sleep(3)  # Esperar 3 segundos antes de reintentar

                                data["ticket_forms"].append(form_data)
                                self.progressbar.set(index / len(ticket_forms))
                                self.update()

                            break  # Salir del bucle while si la solicitud fue exitosa

                        elif response.status_code == 429:
                            seconds_to_wait = int(response.headers["Retry-After"])
                            print("Api transfer rate sobrepasada. Esperar:", seconds_to_wait, "segundos.")
                            time.sleep(seconds_to_wait)
                            retries1 += 1

                        else:
                            print("Error al obtener los formularios. Código de estado:", response.status_code)
                            time.sleep(3)
                            retries1 += 1

                    except requests.exceptions.SSLError:
                        print('Error SSL. Reintentando la solicitud...')
                        retries1 += 1
                        time.sleep(3)  # Esperar 3 segundos antes de reintentar

                # Guardar los datos en un archivo JSON
                with open('Fuente/formularios_zendesk.json', "w") as file:
                    json.dump(data, file)

                # Leer el archivo JSON
                with open('Fuente/formularios_zendesk.json', 'r') as file:
                    data = json.load(file)

                # Aplanar los diccionarios en columnas del DataFrame
                df = pd.json_normalize(data, 'ticket_forms', errors='ignore')
                df = df.explode('form_fields')
                df = pd.concat([df.drop(['form_fields'], axis=1), df['form_fields'].apply(pd.Series)], axis=1)

                # Obtener la fecha y hora actual
                fecha_actual = datetime.datetime.now().strftime("%d-%m-%Y")
                hora_actual = datetime.datetime.now().strftime("%H.%M")
                # Obtener la cantidad de registros en el DataFrame
                total_rows = len(df)
                # Generar el nombre del archivo de Excel
                nombre_archivo = f"Excel/Formularios [{fecha_actual}] [{hora_actual}] [{total_rows} registros].xlsx"

                df.to_excel(nombre_archivo, index=False)
                print("Descarga Exitosa")
                cargar_todo()
            else:
                print("Cancelado")
                return


        update_frame = customtkinter.CTkFrame(self)
        update_frame.grid(row=0, column=0, rowspan=3, padx=10, pady=5, sticky="nsew")

        update_label = customtkinter.CTkLabel(update_frame, text="Actualización")
        update_label.pack(side="top")

        self.update_usuarios = customtkinter.CTkButton(update_frame, text="Usuarios", command=usuarios)
        self.update_usuarios.pack(side="top", padx=10, pady=10, expand=True, fill="both")

        self.update_agentes = customtkinter.CTkButton(update_frame, text="Agentes", command=agentes)
        self.update_agentes.pack(padx=10, pady=10, expand=True, fill="both")

        self.update_formularios = customtkinter.CTkButton(update_frame, text="Formularios", command=formularios)
        self.update_formularios.pack(side="bottom", padx=10, pady=10, expand=True, fill="both")


        # ········································· USUARIOS  ·················································


        carga_frame = customtkinter.CTkFrame(self)
        carga_frame.grid(row=0, column=1, rowspan=3, padx=10, pady=5, sticky="nsew")

        carga_label = customtkinter.CTkLabel(carga_frame, text="Ingresar ID's")
        carga_label.pack(side="top")

        self.textbox_carga = customtkinter.CTkTextbox(carga_frame, width=150, height=100)
        self.textbox_carga.pack(padx=10, pady=10, expand=True, fill="both")

        def buscar_por_id(usuarios, ids):
            resultados = [usuario for usuario in usuarios if usuario.get('id') in ids]
            return resultados

        def leer_ids():
            ###################################################
            self.treeview.delete(*self.treeview.get_children())
            ids_buscados = self.textbox_carga.get("0.0", "end-1c")
            print(ids_buscados)
            try:
                ids_lista = ids_buscados.strip().splitlines()
                ids_lista = list(map(int, [item for sublist in ids_lista for item in sublist.split()]))
                print("OK")
            except ValueError:
                try:
                    ids_lista = [int(id) for id in ids_buscados.split(',')]
                    print("OK 2")
                except ValueError:
                    try:
                        ids_lista = ids_buscados.replace(" ", "")
                        ids_lista = ids_lista.split(",")
                        ids_lista = list(map(int, [item for sublist in ids_lista for item in sublist.split()]))
                        print("OK 3")
                    except ValueError:
                        def show_error_1():
                            # Show some error message
                            CTkMessagebox(title="Error",
                                          message="No ha ingresado ID's correctamente o los valores no son de tipo numérico. Revise la lista ingresada, asegurandose de: (i) que los ID's deben ser identificadores válidos para cada usuario en Zendesk, (ii) que todos los ID's estén separados por una coma o un espacio y (iii) que los valores ingresados sean de tipo numérico, dado que la lista no debe contener letras.",
                                          icon="cancel")
                        show_error_1()
                        return

            if ids_lista == []:
                def show_error_id_vacio():
                    # Show some error message
                    CTkMessagebox(title="Error",
                                  message="No ha ingresado la lista de ID's",
                                  icon="cancel")

                show_error_id_vacio()
                return

            print(ids_lista)
            print(len(ids_lista))

            def buscar_por_id(usuarios, ids):
                resultados = [usuario for usuario in usuarios if usuario.get('id') in ids]
                return resultados

            resultados = buscar_por_id(dic_usuarios, ids_lista)

            if len(resultados) != len(ids_lista):
                print("len lista resultados:", len(resultados), "| len lista ingresada:", len(ids_lista))
                def show_error():
                    # Show some error message
                    CTkMessagebox(title="Error", message="Algunos ID's ingresados no son válidos. Revise la lista ingresada, asegurandose de: (i) que los ID's deben ser identificadores válidos para cada usuario en Zendesk, (ii) que todos los ID's estén separados por una coma o un espacio y (iii) que los valores ingresados sean de tipo numérico, dado que la lista no debe contener letras.", icon="cancel")
                show_error()
            elif (len(resultados) == 0) & (len(ids_lista) == 0):
                print("len lista resultados:", len(resultados), "| len lista ingresada:", len(ids_lista))
                return
            else:
                print(resultados)
                for index, result in enumerate(resultados, start=1):
                    val = (result['id'], result['name'], result['email'])
                    self.treeview.insert('', 'end', text=str(index), values=val)

                def show_checkmark():
                    # Show some positive message with the checkmark icon
                    CTkMessagebox(title="Felicitaciones",message=f"Se ha incorporado a la lista de notificación masiva un total de {index} usuarios",
                                  icon="check", option_1="Muy bien")
                show_checkmark()

        self.cargar = customtkinter.CTkButton(carga_frame, text="Cargar ID's", command=leer_ids)
        self.cargar.pack(padx=10, pady=10)

        # ········································· USUARIOS TABLA  ·················································
        tabla_frame = customtkinter.CTkFrame(self)
        tabla_frame.grid(row=3, column=0, columnspan=2, rowspan=2, padx=10, pady=5, sticky="nsew")

        tabla_label = customtkinter.CTkLabel(tabla_frame, text="Usuarios a notificar")
        tabla_label.pack(side="top")

        # Scrollbar
        self.scrollbar = ttk.Scrollbar(tabla_frame)
        #self.scrollbar.grid(row=3, column=0, rowspan=4, sticky="ne")
        #self.scrollbar.place(x=1250, y=290)

        # Treeview
        self.treeview = ttk.Treeview(
            tabla_frame,
            selectmode="browse",
            yscrollcommand=self.scrollbar.set,
            columns=(0, 3),
            height=16,
        )
        self.treeview.pack(padx=20, pady=10, expand=True, fill="both")

        self.scrollbar.config(command=self.treeview.yview)

        # Define columns
        self.treeview['columns'] = ('id', 'name', 'email')

        # Format columns
        self.treeview.column('#0', width=40)
        self.treeview.column('id', width=100)
        self.treeview.column('name', width=150)
        self.treeview.column('email', width=150)

        # Create headings
        self.treeview.heading('#0', text='n', anchor="center")
        self.treeview.heading('id', text='id', anchor="center")
        self.treeview.heading('name', text='name', anchor="center")
        self.treeview.heading('email', text='email', anchor="center")


        #········································· AGENTES ····················································
        # Attach to Entry
        default = customtkinter.CTkLabel(self, text="Seleccionar Agente")

        self.entry_0 = customtkinter.CTkEntry(self, width=640)
        self.entry_0.grid(row=0, column=2, columnspan=2, padx=10, pady=10, sticky="ew")

        self.selected_value = tkinter.StringVar()

        CTkScrollableDropdown(self.entry_0, values=values, command=lambda e: self.entry_0.delete(0, tkinter.END) or self.entry_0.insert(0, e),
                              autocomplete=True, justify="left")

        #self.scrollable_dropdown = CTkScrollableDropdown(self.entry_0, values=values, variable=self.selected_value,
         #                                                autocomplete=True, justify="left")

        #def combobox_callback(choice):
        #    print("combobox dropdown clicked:", choice)

        #default = customtkinter.StringVar(value="Seleccionar Agente")
        #self.optionmenu = customtkinter.CTkOptionMenu(self, width=640, command=combobox_callback, variable=default)
        #self.optionmenu.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        #CTkScrollableDropdown(self.optionmenu, values=values, justify="left")

        #········································ PRODUCTOS ·················································
        #ticket_forms = filtered_forms # Solo las de SCH
        ticket_forms = json_ticket_forms # Todas

        # Obtener solo los nombres de los formularios filtrados
        ticket_form_names = [formulario['form_title'] for formulario in filtered_forms]

        default_1 = customtkinter.StringVar(value="Seleccionar tipo de producto")
        def combobox_callback(choice):
            print("combobox dropdown clicked:", str(self.optionmenu_1.get()))

        self.optionmenu_1 = customtkinter.CTkComboBox(self, width=640, command=combobox_callback, variable=default_1)
        self.optionmenu_1.grid(row=1, column=2, columnspan=2, padx=10, pady=10, sticky="ew")
        CTkScrollableDropdown(self.optionmenu_1, values=ticket_form_names, justify="left", height=700)

        #······································ ESTADO DEL TICKET ·················································

        estado_frame = customtkinter.CTkFrame(self)
        estado_frame.grid(row=2, column=2, padx=10, pady=5, sticky="nsew")

        estado_label = customtkinter.CTkLabel(estado_frame, text="Estado del ticket")
        estado_label.pack(side="top", expand=True, fill="both")

        def obtener_valor_estado(valor):
            valor_seleccionado = self.segemented_button_var.get()
            print(str(valor_seleccionado))

        self.segemented_button_var = customtkinter.StringVar(value="Cerrado")
        self.segemented_button = customtkinter.CTkSegmentedButton(estado_frame,
                                                                  values=["Cerrado", "Abierto", "Pendiente", "En espera"],
                                                                  variable=self.segemented_button_var,
                                                                  command=obtener_valor_estado)
        self.segemented_button.pack(side="left", padx=10, pady=10, expand=True, fill="both")

        # ································ PRIORIDAD DEL TICKET ·················································

        prioridad_frame = customtkinter.CTkFrame(self, width=400)
        prioridad_frame.grid(row=2, column=3, padx=10, pady=5, sticky="nsew")
        prioridad_label = customtkinter.CTkLabel(prioridad_frame, text="Tipo de prioridad")
        prioridad_label.pack(side="top", expand=True, fill="both")
        def obtener_valor_prioridad(valor):
            valor_seleccionado = self.segemented_button_var_1.get()
            print(str(valor_seleccionado))

        self.segemented_button_var_1 = customtkinter.StringVar(value="Normal")
        self.segemented_button_var_1 = customtkinter.CTkSegmentedButton(prioridad_frame,
                                                                        values=["Normal", "Alta", "Urgente", "Baja"],
                                                                        variable=self.segemented_button_var_1,
                                                                        command=obtener_valor_prioridad)
        self.segemented_button_var_1.pack(side="right", padx=10, pady=10, expand=True, fill="both")

        #····································· ASUNTO DEL MENSAJE ··········································

        self.entry = customtkinter.CTkEntry(self, placeholder_text="Escribir asunto del mensaje", width=750)
        self.entry.grid(row=3, column=2, columnspan=2, padx=10, pady=10, sticky="ew")
        #self.entry.place(x=100, y=270)

        # ········································ MENSAJE ·················································
        # create textbox
        self.textbox = customtkinter.CTkTextbox(self, width=800, height=300)

        self.textbox.grid(row=4, column=2, columnspan=2, padx=10, pady=10, sticky="nsew")

        self.textbox.insert("0.0","{}, {}:\n\nEscribir/copiar aquí el resto del mensaje. La primera línea es un encabezado que automaticamente asignara el siguiente string: Buenos días/tardes/noches (automático dependiendo de la hora a la que se genere el ticket) y el nombre del usuario:.\n\nDe todas formas, es posible borrarlo y escribir cualquier mensaje, solo debes considerar que si se mantienen los dos corchetes en la primera línea, la apertura del mensaje será automática. Otro punto importante es que si se deja la primera línea, no deben existir otros corchetes iguales dentro del mensaje.")
        self.textbox_carga.insert("0.0", "")

        def envio():
            print("button pressed")
            self.progressbar.set(0)
            ask_question()

        def borrar():
            self.entry_0.delete('0', 'end')
            self.optionmenu_1.set("")
            self.segemented_button.set("Cerrado")
            self.segemented_button_var_1.set("Normal")
            self.entry.delete('0', 'end')
            self.textbox.delete('1.0', 'end')
            self.textbox_carga.delete('1.0', 'end')
            self.treeview.delete(*self.treeview.get_children())
            self.progressbar.set(0)

        self.button = customtkinter.CTkButton(self, text="Limpiar", command=borrar)
        self.button.grid(row=5, column=2, padx=20, pady=10)
        self.button_1 = customtkinter.CTkButton(self, text="Enviar Tickets", command=envio)
        self.button_1.grid(row=5, column=3, padx=20, pady=10)
        self.progressbar = customtkinter.CTkProgressBar(self, height=16)
        self.progressbar.grid(row=6, column=0, columnspan=4, padx=20, pady=10, sticky="nsew")
        self.progressbar.configure(progress_color='green')

        self.progressbar.set(0)

        def ask_question():
            # get yes/no answers

            ids_buscados = self.textbox_carga.get("0.0", "end-1c")
            ids_lista = []

            try:
                ids_lista = ids_buscados.strip().splitlines()
                ids_lista = list(map(int, [item for sublist in ids_lista for item in sublist.split()]))
            except ValueError:
                try:
                    ids_lista = [int(id) for id in ids_buscados.split(',')]
                except ValueError:
                    try:
                        ids_lista = ids_buscados.replace(" ", "")
                        ids_lista = ids_lista.split(",")
                        ids_lista = list(map(int, [item for sublist in ids_lista for item in sublist.split()]))
                    except ValueError:
                        def show_error_1():
                            # Show some error message
                            CTkMessagebox(title="Error",
                                          message="No ha ingresado ID's correctamente o los valores no son de tipo numérico. Revise la lista ingresada, asegurandose de: (i) que los ID's deben ser identificadores válidos para cada usuario en Zendesk, (ii) que todos los ID's estén separados por una coma o un espacio y (iii) que los valores ingresados sean de tipo numérico, dado que la lista no debe contener letras.",
                                          icon="cancel")
                        show_error_1()
                        return

            resultados = buscar_por_id(dic_usuarios, ids_lista)
            print("Usuarios a contactar:", resultados)

            if len(self.entry_0.get()) != 0 and len(self.optionmenu_1.get()) != 0 and len(self.entry.get()) != 0 and len(self.textbox.get("1.0", "end-1c")) != 0 and len(resultados) !=0:

                msg = CTkMessagebox(title="Confirmar envío", message="Deseas dar inicio al envío masivo de Tickets por Zendesk API",
                                    icon="question", option_1="Aceptar", option_2="Cancelar")
                response = msg.get()

                if response == "Aceptar":
                    print("Enviando")
                    forms = ticket_forms.copy()
                    agente = self.entry_0.get()
                    print("Agente ingresado:", agente)

                    def buscar_por_name(usuarios, agente):
                        result = [usuario for usuario in usuarios if usuario.get('name') in agente]
                        return result

                    result = buscar_por_name(dic_agentes, agente)
                    print("Agente resultado:", result)

                    producto = self.optionmenu_1.get()
                    print("Producto ingresado:", producto)

                    def buscar_ticket_form_id(forms, ticket_form_name):
                        for form in forms:
                            if form['form_title'] == ticket_form_name:
                                return form['form_id']
                        return None

                    nombre_formulario = producto
                    ticket_form_id = buscar_ticket_form_id(forms, nombre_formulario)
                    print("ID de Producto encontrado:", ticket_form_id)

                    def buscar_fields_por_form_id(forms, ticket_form_id):
                        for form in forms:
                            if form.get('form_id') == ticket_form_id:
                                return form.get('form_fields', [])
                        return []

                    fields = buscar_fields_por_form_id(forms, ticket_form_id)
                    print("Campos:", fields)
                    print("tickets forms", forms)
                    fields_api = fields.copy()
                    print("copia:", fields_api)
                    for item in fields_api:
                        if 'id' not in item:
                            item['id'] = item.pop('field_id')

                    for item in fields_api:
                        if 'value' not in item:
                            item['value'] = item.pop('field_title')

                    for item in fields_api:
                        if item['id'] == 360049147651:
                            item['value'] = 'notifica_uso_exclusivo'
                        else:
                            item['value'] = ''

                    print("fields para api:", fields_api)

                    estado = self.segemented_button.get()
                    print("Estado de ticket ingresado:", estado)

                    def transformar_estado(estado):
                        if estado == "Cerrado":
                            estado = "closed"
                        elif estado == "Abierto":
                            estado = "open"
                        elif estado == "Pendiente":
                            estado = "pending"
                        elif estado == "En espera":
                            estado = "on-hold"
                        return estado

                    estado = transformar_estado(estado)
                    print("Estado en inglés:", estado)

                    prioridad = self.segemented_button_var_1.get()
                    print("Prioridad ingresada:", prioridad)

                    def transformar_prioridad(prioridad):
                        if prioridad == "Normal":
                            prioridad = "normal"
                        elif prioridad == "Alta":
                            prioridad = "high"
                        elif prioridad == "Urgente":
                            prioridad = "urgent"
                        elif prioridad == "Baja":
                            prioridad = "low"
                        return prioridad

                    prioridad = transformar_prioridad(prioridad)
                    print("Prioridad en inglés:", prioridad)

                    asunto = self.entry.get()
                    print("Asunto:", asunto)
                    mensaje = self.textbox.get("1.0", "end-1c")
                    print("Mensaje:", mensaje)

                    # Configurar las credenciales de la API de Zendesk
                    user = "pfcha_staff@anid.cl"
                    token = "aiUPPMqY5pFcSSNt5UpUx2vIFlaAuI6GgOdoHKCR"

                    ######################################COLAB##############################################
                    import requests
                    print("ID FORMULARIO:", ticket_form_id)
                    url = f'https://conicytoirs.zendesk.com/api/v2/ticket_forms/{ticket_form_id}.json'

                    data = {
                        'ticket_form': {
                            'active': True
                        }
                    }

                    response = requests.put(url, json=data, auth=(user + "/token", token))

                    if response.status_code == 200:
                        print('Formulario activado exitosamente.')
                    else:
                        print('Error al activar el formulario:', response.status_code)

                        def show_warning_api():
                            # Show some retry/cancel warnings
                            msg = CTkMessagebox(title="Advertencia", message=f"No se pudo establecer la conexión con la API para la activación del formulario Nombre: {nombre_formulario} e ID: {ticket_form_id}.",
                                                icon="warning", option_1="Cancel")

                            if msg.get() == "Cancel":
                                return
                            else:
                                return
                        show_warning_api()

                    ############################## Lectura usuarios y mensaje ################################
                    usuarios = resultados

                    # Definir los datos del agente
                    agente = result[0]
                    print(agente)

                    cuerpo = mensaje
                    ##########################################################################################
                    # Crear la lista de datos de los tickets
                    tickets = []
                    for usuario in usuarios:
                        # Obtener la hora actual
                        hora_actual = datetime.datetime.now().time()
                        # Determinar si es mañana, tarde o noche
                        if hora_actual < datetime.time(12):
                            saludo = "Buenos días"
                        elif hora_actual < datetime.time(18):
                            saludo = "Buenas tardes"
                        else:
                            saludo = "Buenas noches"
                        ticket_data = {
                            "ticket": {
                                'tags': 'notificacion_masiva_sch',  # a crear por el tito
                                "requester_id": usuario["id"],
                                "submitter_id": agente["id"],
                                "assignee_id": agente["id"],
                                "subject": asunto,
                                "raw_subject": asunto,
                                "comment": {"body": cuerpo.format(saludo, usuario["name"].title())},
                                # "comment": {"body": cuerpo, "public": False},
                                # "actions": [{'field': 'notification_user',
                                #             'value': [
                                #                'requester_id',
                                #                '[Subdirección de Capital Humano ANID] {{ticket.title}}',
                                #                "Estimado(a) Usuario(a).\n\n"
                                #                "Te informamos que esta notificación se ha generado bajo el número de ticket N° {{ticket.id}}.\n\n"
                                #                "Por favor, no des respuesta a este correo electrónico, puedes ingresar al portal de Ayuda ANID <a href='https://ayuda.anid.cl/hc/es/requests'>https://ayuda.anid.cl/hc/es/requests</a>), para revisar el historial de tus actividades.\n\n"
                                #                "Muchas gracias,\n\n"
                                #                "Equipo Ayuda ANID\n"
                                #                "Agencia Nacional de Investigación y Desarrollo - ANID\n"
                                #                "Twitter: [@AnidInforma](https://twitter.com/AnidInforma)\n"
                                #                "__________________________\n\n"
                                #                "{{ticket.comments_formatted}}"]}],
                                "ticket_form_id": ticket_form_id,
                                "custom_fields": fields_api,
                                "priority": prioridad,
                                "status": estado,
                                # "audit.events": [{
                                #    'type': 'Notification',
                                #    'via': {
                                #        'channel': 'rule',
                                #        'source': {
                                #            'from': {'deleted': False, 'title': 'Notificar al solicitante sobre solicitud recibida (Consulta)', 'revision_id': 1},
                                #            'rel': 'trigger'
                                #        }
                                #    },
                                #    'subject': '[Solicitud recibida]',
                                #    'body': "Estimado(a) Usuario(a).\n\n"
                                #            "Te informamos que esta notificación se ha generado bajo el número de ticket N° {ticket_id}.\n\n"
                                #            "Por favor, no des respuesta a este correo electrónico, puedes ingresar al portal de Ayuda ANID "
                                #            "<a href='https://ayuda.anid.cl/hc/es/requests'>https://ayuda.anid.cl/hc/es/requests</a>), "
                                #            "para revisar el historial de tus actividades.\n\n"
                                #            "Muchas gracias,\n\n"
                                #            "Equipo Ayuda ANID\n"
                                #            "Agencia Nacional de Investigación y Desarrollo - ANID\n"
                                #            "Twitter: [@AnidInforma](https://twitter.com/AnidInforma)\n"
                                #            "__________________________\n\n"
                                #            "{{ticket.comments_formatted}}"
                                #            }],
                                # 'external_id': None,
                                # 'via.channel': 'api',
                                # 'source.rel': None,
                                # 'type': 'incident',
                                # 'recipient': None,
                                # 'organization_id': None,
                                # 'group_id': 360022158932,
                                # 'collaborator_ids': [],
                                # 'followers_ids': [],
                                # "collaborators": usuario["email"],
                                # "email_cc_ids": [],
                                # 'forum_topic_id': None,
                                # 'problem_id': None,
                                # 'has_incidents': False,
                                # 'is_public': False,
                                # 'due_at': None,
                                # 'tags': ['ticket_sch'],
                                # 'satisfaction_rating.score': 'unoffered',
                                # 'sharing_agreement_ids': [],
                                # 'followup_ids': [],
                                # 'ticket_form_id': 360001687811,
                                # 'brand_id': 360001686831,
                                # 'allow_channelback': False,
                                # 'allow_attachments': True,
                                # 'from_messaging_channel': False,
                                # 'fields': {"id": '', 'value': ''}
                            }
                        }
                        tickets.append(ticket_data)
                    print("Tickets:", tickets)
                    ##########################################################################################
                    # Enviar una solicitud para crear cada ticket
                    json_response = []

                    ticket_url = "https://conicytoirs.zendesk.com/api/v2/tickets.json"

                    max_attempts = 3  # Número máximo de intentos permitidos por ticket

                    for i, ticket_data in enumerate(tickets, start=1):
                        print(ticket_data)
                        attempts = 0
                        while attempts < max_attempts:
                            try:
                                response = requests.post(ticket_url, auth=(user + "/token", token), json=ticket_data)
                                if response.status_code == 201:
                                    print("Ticket creado correctamente.", response.status_code)
                                    json_response.append(response.json())
                                    break  # Se ha creado el ticket, se sale del bucle while
                                elif response.status_code == 429:
                                    seconds_to_wait = int(response.headers["Retry-After"])
                                    print("API transfer rate sobrepasada. Esperar:", seconds_to_wait, "segundos.")
                                    time.sleep(seconds_to_wait)
                                    attempts += 1
                                    if attempts == max_attempts:
                                        print("Se ha alcanzado el número máximo de intentos para el ticket:", i)
                                        json_response.append(response.json())
                                else:
                                    print("Error al crear el ticket. Código de respuesta:", response.status_code)
                                    print("Respuesta del servidor:", response.json())
                                    json_response.append(response.json())
                                    break  # Se ha producido un error, se sale del bucle while
                            except requests.exceptions.SSLError:
                                print('Error SSL. Reintentando la solicitud...')
                                attempts += 1
                                time.sleep(3)  # Esperar 3 segundos antes de reintentar

                        self.progressbar.set(i / len(tickets))
                        self.progressbar.get()
                        self.update()

                    self.progressbar.stop()

                    print("completado")
                    ############################################################################################
                    import pandas as pd

                    # Obtener la fecha y hora actual
                    fecha_actual = datetime.datetime.now().strftime("%d-%m-%Y")
                    hora_actual = datetime.datetime.now().strftime("%H.%M")
                    # Obtener el número diferenciador basado en len(tickets)
                    numero_diferenciador = len(tickets)

                    # Guardar las respuestas en un archivo JSON
                    with open(f"Seguimiento/responses [{fecha_actual}] [{hora_actual}].json", "w") as file:
                        json.dump(json_response, file)

                    # Generar el nombre del archivo de Excel
                    nombre_archivo = f"Seguimiento/Seguimiento tickets [{fecha_actual}] [{hora_actual}] [{numero_diferenciador} tickets].xlsx"

                    # Convertir el JSON en un DataFrame
                    df = pd.json_normalize(json_response)
                    # Guardar el DataFrame en el archivo de Excel
                    df.to_excel(nombre_archivo, index=False)

                    ######################################END COLAB##############################################
                    def show_finish():
                        # Show some error message
                        CTkMessagebox(title="Felicitaciones",
                                      message=f"Se ha logrado enviar un total de {len(tickets)} tickets mediante Zendesk API. En la carpeta en donde se aloja la APP se ha generado el archivo 'Seguimiento_tickets.xlsx', para verificar el detalle de cada envío.",
                                      icon="check")
                    show_finish()
                else:
                    print("Cancelado")
                    return

            else:
                def show_error_2():
                    # Show some error message
                    CTkMessagebox(title="Error", message="Algunos de los campos requeridos para comenzar con el envío estan vacíos. Revise: (i) la selección del agente que enviará el mensaje, (ii) la selección del producto, (iii) escribir el asunto del mensaje y (iv) escribir el cuerpo del mensaje para la notificación.", icon="cancel")
                show_error_2()

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")

if __name__ == "__main__":
    app = App()
    app.mainloop()
