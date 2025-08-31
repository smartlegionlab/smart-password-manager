# Smart Password Manager <sup>v0.0.2</sup>

---

## PostgreSQL

### Installation

```bash
# Install PostgreSQL
sudo pacman -S postgresql

# Initialize database cluster
sudo su - postgres -c "initdb --locale en_US.UTF-8 -D '/var/lib/postgres/data'"

# Start and enable PostgreSQL service
sudo systemctl start postgresql
sudo systemctl enable postgresql

# Access PostgreSQL shell
sudo -u postgres psql
```

### Database Configuration

#### Development Setup (using default postgres user)

```sql
CREATE DATABASE smart_password_manager_db
    OWNER postgres
    ENCODING 'UTF-8'
    LC_COLLATE 'en_US.UTF-8'
    LC_CTYPE 'en_US.UTF-8'
    TEMPLATE template0;
```

#### If you need to delete the test database first

```sql
REVOKE CONNECT ON DATABASE smart_password_manager_db FROM PUBLIC;
DROP DATABASE smart_password_manager_db;
```

#### Install PostgreSQL Python adapter
```bash
pip install psycopg2-binary
```

## Environment Configuration

### Secret Key Generation

Generate a secure secret key:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### Environment Variables

Create `.env` file in project root:

#### Development Configuration
```ini
# Core Settings
DJANGO_ENV=development
SECRET_KEY=your-generated-secret-key
DEBUG=True

# Database Settings (using default postgres user)
DB_NAME=smart_password_manager_db
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=localhost
DB_PORT=5432

# Redis/Celery Settings
REDIS_URL=redis://localhost:6379/1
CELERY_BROKER_URL=redis://localhost:6379/0
CELERY_RESULT_BACKEND=redis://localhost:6379/0

DEBUG_TOOLBAR_ENABLED=True
```

***

## Project Setup

```bash
# Clone repository
git clone https://github.com/smart_legion_lab/smart-password-manager-web.git
cd smart-password-manager-web

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Database migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser
```

## Running the Application

### Development Mode
```bash
# Start Django development server
python manage.py runserver
```

Access the application at: [http://localhost:8000](http://localhost:8000)


## Pycharm

User and password for DB is: user (postgres); password (postgres).

***

## 📜 Licensing

This project is offered under a dual-licensing model.

### 🆓 Option 1: BSD 3-Clause License (for Non-Commercial Use)
This license is **free of charge** and allows you to use the software for:
- Personal and educational purposes
- Academic research and open-source projects
- Evaluation and testing

**Important:** Any use by a commercial organization or for commercial purposes 
(including internal development and prototyping) requires a commercial license.

### 💼 Option 2: Commercial License (for Commercial Use)
A commercial license is **required** for:
- Integrating this software into proprietary products
- Using it in internal operations within a company
- SaaS and hosted services that incorporate this software
- Obtaining priority support and indemnification

**To obtain a commercial license,** please contact us directly at:  
📧 **smartlegiondev@gmail.com**
