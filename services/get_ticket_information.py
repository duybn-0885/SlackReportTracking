import requests
from requests.auth import HTTPBasicAuth
import json
from datetime import datetime

from settings import JIRA_API_TOKEN, JIRA_USER, JIRA_URL
from databases.db_connector import DbConnector


ticket_id_or_key = 'DY-504'
auth = HTTPBasicAuth(JIRA_USER, JIRA_API_TOKEN)
headers = {
   'Accept': 'application/json'
}


def get_ticket_change_log(ticket_id_or_key):
    ticket_url = JIRA_URL + ticket_id_or_key + '/changelog'
    response = requests.request(
        'GET',
        ticket_url,
        headers=headers,
        auth=auth
    )

    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(',', ': '))


def get_spent_time(user_email, date=datetime.today().strftime('%Y-%m-%d')):
    total_log_time = 0
    ticket_change_log = get_ticket_change_log('DY-504')
    change_log_values = ticket_change_log['values']

    for change_log_value in reversed(change_log_values):
        author = change_log_value['author']
        items = change_log_value['items']

        if change_log_value['created'].split('T')[0] == date and author['emailAddress'] == user_email:
            items = change_log_value['items']
            for item in items:
                if item['field'] == 'timespent':
                    total_log_time += int(item['to']) - int(item['from'])

    return total_log_time
