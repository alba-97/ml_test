## Mutant API

### Instalación

Clona el repositorio:

```bash
git clone https://github.com/alba-97/ml_test.git
cd ml_test
```

Crea un archivo .env y coloca la SECRET_KEY

```bash
SECRET_KEY=123456
```

Instala las dependencias

```bash
pip install -r requirements.txt
```

Corre las migraciones de la DB

```bash
python manage.py migrate
```

Corre el proyecto

```bash
python manage.py runserver
```

El proyecto se ejecutará en [http://localhost:8000](http://localhost:8000).
