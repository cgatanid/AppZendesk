import tkinter
from tkinter import ttk
import customtkinter
import CTkScrollableDropdown
from CTkScrollableDropdown import *
from CTkTable import *
from CTkMessagebox import CTkMessagebox

customtkinter.set_appearance_mode("light") #"system", "dark" y "light"
customtkinter.set_default_color_theme("dark-blue") # Themes: "blue" (standard), "green", "dark-blue"

import json

# Abrir el archivo JSON
with open('agentes.json', 'r') as json_file:
    agentes = json.load(json_file)

values = [item['name'] for item in agentes]

import pandas as pd
# Convertir el JSON a DataFrame
df_agentes = pd.read_json('agentes.json')
dic_agentes = df_agentes.to_dict(orient='records')
df_usuarios = pd.read_json('usuarios_zendesk.json')
dic_usuarios = df_usuarios.to_dict(orient='records')

# pyinstaller --noconfirm --onedir --windowed --name "AppZendesk" -F main.py --collect-all customtkinter -w
# pyinstaller --noconfirm --onefile --windowed --name "AppZendesk" --add-data "C:/Users/aparedes/PycharmProjects/AppZendesk/agentes.json;." --add-data "C:/Users/aparedes/PycharmProjects/AppZendesk/usuarios_zendesk.json;." --add-data "C:/Users/aparedes/PycharmProjects/AppZendesk/CTkMessagebox;CTkMessagebox/" --add-data "C:/Users/aparedes/PycharmProjects/AppZendesk/CTkScrollableDropdown;CTkScrollableDropdown/" --collect-all customtkinter -w "C:/Users/aparedes/PycharmProjects/AppZendesk/main.py"

class ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Progreso del envío de Tickets")
        self.geometry("400x200")

        self.label = customtkinter.CTkLabel(self, text="Progreso del envío")
        self.label.pack(padx=20, pady=20)

        self.progressbar = customtkinter.CTkProgressBar(self)
        self.progressbar.pack(pady=20)
        self.progressbar.set(0)

    def test(self, n):
        self.progressbar.start()

        for x in range(n):
            progress_percentage = (x / n) * 100  # Calcular el porcentaje de progreso actual
            self.progressbar.set(progress_percentage)  # Actualizar la barra de progreso con el porcentaje

            self.update_idletasks()

        self.progressbar.stop()

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        # configure window
        self.title("Zendesk Envío de Tickets Masivos")
        self.geometry(f"{1320}x{700}")

        # configure grid layout
        self.grid_columnconfigure((0,1,2), weight=1)
        self.grid_rowconfigure((0,1,2,3), weight=1)

        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self,
                                                               values=["60%", "70%", "80%", "90%", "100%", "110%",
                                                                       "120%", "130%", "140%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=5, column=0, padx=60, pady=(20, 20), sticky="w")
        self.scaling_optionemenu.set("100%")


        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self,
                                                                       values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=5, column=0, padx=60, pady=(20, 20), sticky="e")
        self.appearance_mode_optionemenu.set("Dark")



        # ········································· USUARIOS  ·················································

        carga_frame = customtkinter.CTkFrame(self)
        carga_frame.grid(row=0, column=0, rowspan=3, padx=10, pady=5, sticky="nsew")

        carga_label = customtkinter.CTkLabel(carga_frame, text="Ingresar ID's separados por coma (,)")
        carga_label.pack(side="top")


        def button_event():
            print("button pressed")

        self.textbox_carga = customtkinter.CTkTextbox(carga_frame, width=420, height=100)
        self.textbox_carga.pack(padx=10, pady=10, expand=True, fill="both")

        def buscar_por_id(usuarios, ids):
            resultados = [usuario for usuario in usuarios if usuario.get('id') in ids]
            return resultados

        def leer_ids():
            ids_buscados = self.textbox_carga.get("0.0", "end-1c")
            #ids_lista = [int(id) for id in ids_buscados.split(',')]
            ids_lista = []

            try:
                ids_lista = [int(id) for id in ids_buscados.split(',')]
            except ValueError:
                print("Error: Los ID's ingresados no son válidos.")
                def show_error_1():
                    # Show some error message
                    CTkMessagebox(title="Error",
                                  message="No ha ingresado ID's correctamente o los valores no son de tipo numérico. Revise la lista ingresada, asegurandose de: (i) que los ID's deben ser identificadores válidos para cada usuario en Zendesk, (ii) que todos los ID's estén separados por una coma a excepción del ultimo valor y (iii) que los valores ingresados sean de tipo numérico, dado que la lista no debe contener letras.",
                                  icon="cancel")
                show_error_1()

            print(ids_lista)

            print(ids_lista)
            def buscar_por_id(usuarios, ids):
                resultados = [usuario for usuario in usuarios if usuario.get('id') in ids]
                return resultados

            resultados = buscar_por_id(dic_usuarios, ids_lista)

            if len(resultados) != len(ids_lista):
                print("len lista resultados:", len(resultados), "| len lista ingresada:", len(ids_lista))
                def show_error():
                    # Show some error message
                    CTkMessagebox(title="Error", message="Algunos ID's ingresados no son válidos. Revise la lista ingresada, asegurandose de: (i) que los ID's deben ser identificadores válidos para cada usuario en Zendesk, (ii) que todos los ID's estén separados por una coma a excepción del ultimo valor y (iii) que los valores ingresados sean de tipo numérico, dado que la lista no debe contener letras.", icon="cancel")
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
                    CTkMessagebox(title="Felicitaciones",message=f"Se ha incorporado a la lista  de notificación masiva un total de {index} usuarios",
                                  icon="check", option_1="Muy bien")
                show_checkmark()

            #resultados = pd.DataFrame(resultados)
            #print(resultados)
            #for _, row in resultados.iterrows():
            #    val = (row['name'], row['email'])
            #    self.treeview.insert('', 'end', text=str(row['id']), values=val)


        self.cargar = customtkinter.CTkButton(carga_frame, text="Cargar ID's", command=leer_ids)
        self.cargar.pack(padx=10, pady=10)

        # ········································· USUARIOS TABLA  ·················································
        tabla_frame = customtkinter.CTkFrame(self)
        tabla_frame.grid(row=3, column=0, rowspan=2, padx=10, pady=5, sticky="nsew")

        tabla_label = customtkinter.CTkLabel(tabla_frame, text="Usuarios a notificar")
        tabla_label.pack(side="top")

        # Scrollbar
        self.scrollbar = ttk.Scrollbar(tabla_frame)
        #self.scrollbar.grid(row=3, column=0, rowspan=4, sticky="ne")
        # self.scrollbar.place(x=1250, y=290)

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
        self.entry_0.grid(row=0, column=1, columnspan=2, padx=10, pady=10, sticky="ew")

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
        ticket_forms = [
            {
                'ticket_form_id': 360003496052,
                'ticket_form_name': 'SCH-Trámites Generales Becarios Depto. Formación Capital Humano',
                'fields': [
                    {'field_id': 360012823751, 'field_name': 'Estado'},
                    {'field_id': 360012823811, 'field_name': 'Grupo'},
                    {'field_id': 360012823831, 'field_name': 'Agente asignado'},
                    {'field_id': 9648003197972, 'field_name': 'Ticket status'},
                    {'field_id': 4416517088276, 'field_name': 'ID Mesa Antigua'},
                    {'field_id': 360049147651, 'field_name': 'SCH-Productos gestión de becarios'},
                    {'field_id': 360012823711, 'field_name': 'Asunto'},
                    {'field_id': 360012823731, 'field_name': 'Descripción'},
                    {'field_id': 360012823791, 'field_name': 'Prioridad'},
                    {'field_id': 360049098492, 'field_name': 'Folio'},
                    {'field_id': 1900002772607, 'field_name': 'RUN'},
                    {'field_id': 1900002772667, 'field_name': 'Gestión en Departamento de Apoyo'},
                    {'field_id': 360049147671, 'field_name': 'TED asociado'},
                    {'field_id': 360049098472, 'field_name': 'Resolución asociada'},
                    {'field_id': 360049147691, 'field_name': 'Prepara TED'},
                    {'field_id': 1900002772647, 'field_name': 'Apoyo administrativo'},
                    {'field_id': 5739531550740, 'field_name': 'SCH-N° de ticket en mesa de ayuda Depto de Apoyo Antigua'},
                    {'field_id': 1900002772627, 'field_name': 'ActivaTracking'}
                ]
            },
            {
                'ticket_form_id': 4417337313172,
                'ticket_form_name': 'SCH-Trámites generales Depto. Financiero',
                'fields': [
                    {'field_id': 360012823751, 'field_name': 'Estado'},
                    {'field_id': 360012823811, 'field_name': 'Grupo'},
                    {'field_id': 360012823831, 'field_name': 'Agente asignado'},
                    {'field_id': 9648003197972, 'field_name': 'Ticket status'},
                    {'field_id': 360012823711, 'field_name': 'Asunto'},
                    {'field_id': 360012823731, 'field_name': 'Descripción'},
                    {'field_id': 360012823791, 'field_name': 'Prioridad'},
                    {'field_id': 4417350044052, 'field_name': 'SCH-Productos del Depto. Financiero'}
                ]
            },
            {
                'ticket_form_id': 4416360583956,
                'ticket_form_name': 'SCH-Trámites Generales Depto. Inserción',
                'fields': [
                    {'field_id': 360012823751, 'field_name': 'Estado'},
                    {'field_id': 360012823811, 'field_name': 'Grupo'},
                    {'field_id': 360012823831, 'field_name': 'Agente asignado'},
                    {'field_id': 9648003197972, 'field_name': 'Ticket status'},
                    {'field_id': 7947034060308, 'field_name': 'SCH-Productos del Depto. Inserción'},
                    {'field_id': 360012823711, 'field_name': 'Asunto'},
                    {'field_id': 360012823731, 'field_name': 'Descripción'},
                    {'field_id': 360012823791, 'field_name': 'Prioridad'},
                    {'field_id': 360048882892, 'field_name': 'Folio / Código de Proyecto *'},
                    {'field_id': 7972026531476, 'field_name': 'SCH-Instrumento Inserción'},
                    {'field_id': 7972091141268, 'field_name': 'SCH-Convocatoria'},
                    {'field_id': 1900002772667, 'field_name': 'Gestión en Departamento de Apoyo'},
                    {'field_id': 360049147671, 'field_name': 'TED asociado'}
                ]
            }
        ]
        values_1 = [ticket_forms[0]['ticket_form_name'], ticket_forms[1]['ticket_form_name'], ticket_forms[2]['ticket_form_name']]

        def combobox_callback(choice):
            print("combobox dropdown clicked:", choice)

        default_1 = customtkinter.StringVar(value="Seleccionar tipo de producto")
        self.optionmenu_1 = customtkinter.CTkComboBox(self, width=640, command=combobox_callback, variable=default_1)
        self.optionmenu_1.grid(row=1, column=1, columnspan=2, padx=10, pady=10, sticky="ew")
        CTkScrollableDropdown(self.optionmenu_1, values=values_1, justify="left", height=700)


        #······································ ESTADO DEL TICKET ·················································

        def radiobutton_event():
            print("radiobutton toggled, current value:", radio_var.get())

        estado_frame = customtkinter.CTkFrame(self)
        estado_frame.grid(row=2, column=1, padx=10, pady=5, sticky="nsew")

        estado_label = customtkinter.CTkLabel(estado_frame, text="Estado del ticket")
        estado_label.pack(side="top", expand=True, fill="both")

        radio_var = tkinter.IntVar(value=0)

        self.segemented_button_var = customtkinter.StringVar(value="Cerrado")
        self.segemented_button = customtkinter.CTkSegmentedButton(estado_frame,
                                                                  values=["Cerrado", "Abierto", "Pendiente", "En espera"],
                                                                  variable=self.segemented_button_var)
        self.segemented_button.pack(side="left", padx=10, pady=10, expand=True, fill="both")

        # ································ PRIORIDAD DEL TICKET ·················································

        prioridad_frame = customtkinter.CTkFrame(self)
        prioridad_frame.grid(row=2, column=2, padx=10, pady=5, sticky="nsew")
        prioridad_label = customtkinter.CTkLabel(prioridad_frame, text="Tipo de Prioridad")
        prioridad_label.pack(side="top", expand=True, fill="both")

        self.segemented_button_var_1 = customtkinter.StringVar(value="Normal")
        self.segemented_button_var_1 = customtkinter.CTkSegmentedButton(prioridad_frame,
                                                                        values=["Normal", "Alta", "Urgente", "Baja"],
                                                                        variable=self.segemented_button_var_1)
        self.segemented_button_var_1.pack(side="right", padx=10, pady=10, expand=True, fill="both")

        #····································· ASUNTO DEL MENSAJE ··········································

        self.entry = customtkinter.CTkEntry(self, placeholder_text="Escribir asunto del mensaje", width=750)
        self.entry.grid(row=3, column=1, columnspan=2, padx=10, pady=10, sticky="ew")
        #self.entry.place(x=100, y=270)

        # ········································ MENSAJE ·················································
        # create textbox
        self.textbox = customtkinter.CTkTextbox(self, width=800, height=300)

        self.textbox.grid(row=4, column=1, columnspan=2, padx=10, pady=10, sticky="nsew")

        self.textbox.insert("0.0","Insertar mensaje")
        self.textbox_carga.insert("0.0", "Cargar ID's")

        def envio():
            print("button pressed")
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

        self.button = customtkinter.CTkButton(self, text="Limpiar", command=borrar)
        self.button.grid(row=5, column=1, padx=20, pady=10)
        self.button_1 = customtkinter.CTkButton(self, text="Enviar Tickets", command=envio)
        self.button_1.grid(row=5, column=2, padx=20, pady=10)
        self.toplevel_window = None

        def open_toplevel():
            if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
                self.toplevel_window = ToplevelWindow(self)  # create window if its None or destroyed
            else:
                self.toplevel_window.focus()  # if window exists focus it

        def ask_question():
            # get yes/no answers

            ids_buscados = self.textbox_carga.get("0.0", "end-1c")
            # ids_lista = [int(id) for id in ids_buscados.split(',')]
            ids_lista = []

            try:
                ids_lista = [int(id) for id in ids_buscados.split(',')]
            except ValueError:
                print("Error: Los ID's ingresados no son válidos.")

                def show_error_1():
                    # Show some error message
                    CTkMessagebox(title="Error",
                                  message="No ha ingresado ID's correctamente o los valores no son de tipo numérico. Revise la lista ingresada, asegurandose de: (i) que los ID's deben ser identificadores válidos para cada usuario en Zendesk, (ii) que todos los ID's estén separados por una coma a excepción del ultimo valor y (iii) que los valores ingresados sean de tipo numérico, dado que la lista no debe contener letras.",
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
                    print("enviando")
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
                            if form['ticket_form_name'] == ticket_form_name:
                                return form['ticket_form_id']
                        return None

                    nombre_formulario = producto
                    ticket_form_id = buscar_ticket_form_id(forms, nombre_formulario)
                    print("ID de Producto encontrado:", ticket_form_id)

                    def buscar_fields_por_form_id(forms, ticket_form_id):
                        for form in forms:
                            if form.get('ticket_form_id') == ticket_form_id:
                                return form.get('fields', [])
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
                            item['value'] = item.pop('field_name')

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
                    ##########################################################################################

                    usuarios = resultados

                    # Definir los datos del agente
                    agente = result[0]
                    print(agente)

                    cuerpo = mensaje
                    ##########################################################################################
                    # Crear la lista de datos de los tickets
                    tickets = []
                    for usuario in usuarios:
                        ticket_data = {
                            "ticket": {
                                'tags': 'notificacion_masiva_sch',  # a crear por el tito
                                "requester_id": usuario["id"],
                                "submitter_id": agente["id"],
                                "assignee_id": agente["id"],
                                "subject": asunto,
                                "raw_subject": asunto,
                                "comment": {"body": cuerpo},
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
                    json_response = []
                    ##########################################################################################
                    # Enviar una solicitud para crear cada ticket
                    ticket_url = "https://conicytoirs.zendesk.com/api/v2/tickets.json"

                    open_toplevel()

                    for i, ticket_data in enumerate(tickets, start=1):
                        response = requests.post(ticket_url, auth=(user + "/token", token), json=ticket_data)
                        if response.status_code == 201:
                            print("Ticket creado correctamente.", response.status_code)
                        else:
                            print("Error al crear el ticket. Código de respuesta:", response.status_code)
                            print("Respuesta del servidor:", response.json())
                        json_response.append(response.json())
                        print(i)
                        self.toplevel_window.test(i)

                    print("completado")
                    ############################################################################################
                    import pandas as pd

                    # Obtener la respuesta como objeto JSON
                    # Guardar las respuestas en un archivo JSON
                    with open("responses.json", "w") as file:
                        json.dump(json_response, file)

                    # Convertir el JSON en un DataFrame
                    df = pd.json_normalize(json_response)
                    df.to_excel("Seguimiento_tickets.xlsx", index=False)
                    ######################################END COLAB##############################################

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
