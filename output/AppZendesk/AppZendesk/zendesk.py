# Configurar las credenciales de la API de Zendesk
user = "pfcha_staff@anid.cl"
token = "aiUPPMqY5pFcSSNt5UpUx2vIFlaAuI6GgOdoHKCR"

##########################################################################################
import requests

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
##########################################################################################

usuarios = resultados

# Definir los datos del agente
agente = result

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

json_response = []
##########################################################################################
# Enviar una solicitud para crear cada ticket
ticket_url = "https://conicytoirs.zendesk.com/api/v2/tickets.json"

for ticket_data in tickets:
    response = requests.post(ticket_url, auth=(user + "/token", token), json=ticket_data)
    if response.status_code == 201:
        print("Ticket creado correctamente.", response.status_code)
    else:
        print("Error al crear el ticket. Código de respuesta:", response.status_code)
        print("Respuesta del servidor:", response.json())
    json_response.append(response.json())

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

