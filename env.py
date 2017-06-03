import os
from os.path import join, dirname
from dotenv import load_dotenv

MANDATORY_ENV_VARIABLES = ["DATABASE_URL", "SERIAL_PORT"]
environment = {}

class EnvironmentSetupError(Exception):
	pass

try: 
	dotenv_path = join(dirname(__file__), '.env')
	if not load_dotenv(dotenv_path):
		raise EnvironmentSetupError("Missing dotenv file in root directory")

	for variable in MANDATORY_ENV_VARIABLES:
		if os.environ.has_key(variable):
				environment[variable] = os.environ.get(variable)
		else:
			raise EnvironmentSetupError("Environment variable " + variable + " must be defined")
except Exception as e:
	print "EnvironmentSetupException:", e
