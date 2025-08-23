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

2. Create a virtual environment and activate it(optional if using pycharm, because the virtual env will activated along with project creation):

```bash
python -m venv env
source env/bin/activate  
```

3. Install the dependencies:

```bash
pip install -r requirements.txt
```

4. Create django secret key
   
To run and access the billing page, create a secret using the command:

```bash
   python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```
   
Create a secret variable named "SECRET_KEY" and append the randomly generated secret string with the prefix "django-insecure-" in social_network/settings.py file


5. Run the development server:

```bash
docker-compose up --build
```

6. Access the application:

- Log In: `http://127.0.0.1:8000/`
# chatapp
