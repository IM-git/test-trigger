import os
import dotenv


dotenv.load_dotenv('.env')
LOGIN = os.environ['LOGIN']
PASSWORD = os.environ['PASSWORD']
ASANA_TOKEN = os.environ['ASANA_TOKEN']
GIT_TOKEN = os.environ['GIT_TOKEN']
TEAMCITY_TOKEN = os.environ['TEAMCITY_TOKEN']

