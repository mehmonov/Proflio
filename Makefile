
setup-dev:
	virtualenv venv
	. venv/bin/activate && pip install --upgrade pip
	. venv/bin/activate && pip install -r requirements/dev.txt

setup-prod:
	virtualenv venv
	. venv/bin/activate && pip install --upgrade pip
	. venv/bin/activate && pip install -r requirements/prod.txt

setup-test:
	virtualenv venv
	. venv/bin/activate && pip install --upgrade pip
	. venv/bin/activate && pip install -r requirements/test.txt

mg:
	. venv/bin/activate && python manage.py migrate

collectstatic:
	. venv/bin/activate && python manage.py collectstatic --noinput

test:
	. venv/bin/activate && python manage.py test