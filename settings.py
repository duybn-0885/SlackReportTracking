import os
import environ

root = environ.Path(__file__)
env = environ.Env()
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
environ.Env.read_env(env_file=os.path.join(BASE_DIR, '.env'))

DATABASE_URL = env.db('DATABASE_URL')
JIRA_API_TOKEN = env('JIRA_API_TOKEN')
JIRA_USER = env('JIRA_USER')
JIRA_URL = env('JIRA_URL')
