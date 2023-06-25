# AppZendesk


APP para envío masivo de tickets mediante conexión a la API de Zendesk.


## 0 - Instalar librerías del proyecto.

Luego de clonar el repo, instalar las librerias del proyecto ejecutando en la consola el archivo "requirements.txt".

```
pip install -r requirements.txt
```

Mediante pyinstaller, correr la siguiente linea:

```
pyinstaller --noconfirm --onefile --windowed --name "AppZendesk" --add-data "C:/Users/{RUTA AL PROYECTO}/AppZendesk/CTkMessagebox;CTkMessagebox/" --add-data "C:/Users/{RUTA AL PROYECTO}/AppZendesk/CTkScrollableDropdown;CTkScrollableDropdown/" --collect-all customtkinter -w "C:/Users/{RUTA AL PROYECTO}/AppZendesk/main.py"

```




## 1 - Seleccionar ID's de usuarios a contactar

<div align="center">
    <img src="imagenes/uno.png" alt="Texto alternativo de la imagen">
</div>

## 2 - Copiar y pegar ID's

Se deben copiar (ctl + c) y pegar (ctl + v) todos los ID's separados por una coma (,). Notar que el último registro no debe tener una coma, pues la aplicación no permitirá realizar la carga si no se elimina. 
<div align="center">
    <img src="imagenes/dos.png" alt="Texto alternativo de la imagen">
</div>


## 3 - Presionar el botón "Cargar ID's"


Luego de cumplir el paso anterior, es necesario presionar el botón para cargar los usuarios. Mediante una advertencia se notificará la carga exitosa de los ID´s.

<div align="center">
    <img src="imagenes/tres.png" alt="Texto alternativo de la imagen">
</div>



## 4 - Seleccionar agente que notificará


Mediante la primera caja superior del costado derecho, es posible hacer doble click y desplazarse por la lista para seleccionar al Agente que emitirá la comunicación.

<div align="center">
    <img src="imagenes/cuatro.png" alt="Texto alternativo de la imagen">
</div>

## 5 - Seleccionar producto


Mediante la selección del producto se podrá activar el formulario que clasifica el tipo de comunicación dentro de la plataforma Zendesk.

<div align="center">
    <img src="imagenes/cinco.png" alt="Texto alternativo de la imagen">
</div>

## 6 - Escribir asunto y mensaje


En cada caja es posible definir el asunto y el mensaje que se transmitirá a los usuarios.

<div align="center">
    <img src="imagenes/Interfaz (blanca).png" alt="Texto alternativo de la imagen">
</div>


## 7 - Aceptar y enviar


Comenzará el proceso de notificación, para luego dejar en la carpeta un excel que tendrá el detalle de cada notificación realizada para efectos de seguimiento.

<div align="center">
    <img src="imagenes/seis.png" alt="Texto alternativo de la imagen">
</div>


## Anexo

La APP debe tener en la misma carpeta los archivos "agentes.json" y "usuarios_zendesk.json". Estos archivos deben generarse de la siguiente forma, considerando como insumo el archvo "json_usuarios.json" descargado de la API:

```
from tqdm import tqdm
import pandas as pd

# Obtener la lista de usuarios
users = zenpy_client.users()

data = []
# Recorrer todos los usuarios con barra de progreso
with tqdm(total=len(users), desc="Procesando usuarios") as pbar:
    # Recorrer cada usuario
    for user in users:
        data.append(user.to_dict())  # Convertir el usuario a un diccionario y agregarlo a la lista

        # Actualizar la barra de progreso
        pbar.update(1)

# Guardar la lista de usuarios en el archivo JSON
with open("json_usuarios.json", "w") as file:
    json.dump(data, file, indent=2)

# Leer el archivo JSON como un DataFrame
df_users = pd.read_json("json_usuarios.json")

# Imprimir el DataFrame
print(df_users)

```

Luego leer el archivo mediante las siguientes lineas:

```
df_users = pd.read_json("json_usuarios.json")

df_users[["id","name","email"]].to_json("usuarios_zendesk.json")
df_users[df_users['role'] == 'agent'][["id", "name", "email"]].to_json("agentes.json", orient='records')
```
