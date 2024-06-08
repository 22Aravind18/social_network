# Social Networking Application

A simple social networking application built using Django and Django Rest Framework.

## Installation

### Prerequisites

- Python 3.8+
- Docker (for containerization)

### Steps

1. Clone the repository:

```bash
git clone https://github.com/22Aravind18/social_network.git
cd social_network
```

2. Create a virtual environment and activate it:

```bash
python -m venv env
source env/bin/activate  
```

3. Install the dependencies:

```bash
pip install -r requirements.txt
```

4. Apply the migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create a superuser:

```bash
python manage.py createsuperuser
```

6. Run the development server:

```bash
python manage.py runserver
```

7. Access the application:

- Log In: `http://127.0.0.1:8000/login/`
