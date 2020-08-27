from flask import Flask, jsonify, request, redirect, send_from_directory
from flask_cors import cross_origin

from services.get_ticket_information import get_spent_time

app = Flask(__name__)

@app.route('/service/healthcheck', methods=['get'])
@cross_origin
def health_check():
    return (jsonify({'message': 'alive'}), 200, {'Content-Type': 'application/json'})


@app.route('/service/get_log_time', methods=['get'])
@cross_origin
def get_log_time():
    """
    param:
        - user_email(string)
        - date_log(string)
    """
    logging.info('--------------------------Start get log time---------------------------------')
    user_email = request.args.get('user_email')
    date_log = request.args.get('date_log')
    total_log_time = get_spent_time(user_email, date_log)

    logging.info('Spent_time_of_user: #{user_email} in #{date_log} is #{total_log_time}')
