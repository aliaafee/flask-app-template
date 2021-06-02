import os

from app import create_app
from config import config


if __name__ == "__main__":
	wsgi_app = create_app(
		config[os.getenv('FLASK_CONFIG') or 'default']
	)

	wsgi_app.run()

