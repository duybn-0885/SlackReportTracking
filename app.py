import logging
from flask import Flask, jsonify, request, redirect, send_from_directory

from services.get_ticket_information import get_spent_time


app = Flask(__name__)


@app.route('/service/healthcheck', methods=['get'])
def health_check():
    return (jsonify({'message': 'alive'}), 200, {'Content-Type': 'application/json'})


@app.route('/service/get_log_time', methods=['get'])
def get_log_time():
    """
    param:
        - user_email(string)
        - date_log(string)
    """
    logging.info('--------------------------Start get log time---------------------------------')
    user_email = request.args.get('user_email')
    date_log = request.args.get('date_log')
    total_log_time = _convert_time_standard_time(get_spent_time(user_email, date_log))
    message = 'Total log time of %s in %s is %s'%(user_email, date_log, total_log_time)

    return (jsonify({'message': message}), 200, {'Content-Type': 'application/json'})


def _convert_time_standard_time(log_time):
    hour = int(log_time / 3600)
    minute = int(log_time % 3600 / 60)

    return '%sh%sm'%(hour, minute)
