# Smart Password Manager Web <sup>v1.3.6</sup>

---

> Note: This is a production-ready password manager. For academic research on the underlying security paradigms, see [The Pointer-Based Security Paradigm](https://doi.org/10.5281/zenodo.17204738), [Local Data Regeneration Paradigm](https://doi.org/10.5281/zenodo.17264327)

---

[![GitHub top language](https://img.shields.io/github/languages/top/smartlegionlab/smart-password-manager)](https://github.com/smartlegionlab/smart-password-manager)
[![GitHub license](https://img.shields.io/github/license/smartlegionlab/smart-password-manager)](https://github.com/smartlegionlab/smart-password-manager/blob/master/LICENSE)
[![GitHub release](https://img.shields.io/github/v/release/smartlegionlab/smart-password-manager)](https://github.com/smartlegionlab/smart-password-manager/)
[![GitHub stars](https://img.shields.io/github/stars/smartlegionlab/smart-password-manager?style=social)](https://github.com/smartlegionlab/smart-password-manager/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/smartlegionlab/smart-password-manager?style=social)](https://github.com/smartlegionlab/smart-password-manager/network/members)

## Web-Based Smart Password Management

Smart Password Manager (web version).

> **Powered by** [smartpasslib](https://github.com/smartlegionlab/smartpasslib) - The core library for deterministic password generation.

Your passwords don't need to be stored because they were never created—they already exist as mathematically valid data waiting to be discovered.

---

## Quick Start

### Prerequisites
- **Python 3.8+** 
- **PostgreSQL**
- **Redis** (for Celery tasks, optional)

### Installation

#### 1. Install PostgreSQL
```bash
# Arch Linux
sudo pacman -S postgresql

# Ubuntu/Debian
sudo apt-get install postgresql postgresql-contrib

# Initialize database cluster (Arch Linux)
sudo su - postgres -c "initdb --locale en_US.UTF-8 -D '/var/lib/postgres/data'"
sudo systemctl start postgresql
sudo systemctl enable postgresql
```

#### 2. Project Setup
```bash
# Clone repository
git clone https://github.com/smartlegionlab/smart-password-manager.git
cd smart-password-manager

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Install PostgreSQL adapter
pip install psycopg2-binary
```

#### 3. Database Configuration
```sql
-- Access PostgreSQL shell
sudo -u postgres psql

-- Create database
CREATE DATABASE smart_password_manager_db
    OWNER postgres
    ENCODING 'UTF-8'
    LC_COLLATE 'en_US.UTF-8'
    LC_CTYPE 'en_US.UTF-8'
    TEMPLATE template0;
```

#### 4. Environment Configuration
Create `.env` file in project root:
```ini
# Core Settings
DJANGO_ENV=development
SECRET_KEY=your-generated-secret-key-here
DEBUG=True

# Database Settings
DB_NAME=smart_password_manager_db
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=localhost
DB_PORT=5432

# Optional: Redis/Celery Settings
REDIS_URL=redis://localhost:6379/1
CELERY_BROKER_URL=redis://localhost:6379/0
```

Generate secret key:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

#### 5. Database Migration & Setup
```bash
# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic
```

#### 6. Run Development Server
```bash
python manage.py runserver
```

Access the application at: [http://localhost:8000](http://localhost:8000)
Admin interface: [http://localhost:8000/admin](http://localhost:8000/admin)

## Interface Preview

![Web Interface](https://github.com/smartlegionlab/smart-password-manager/raw/master/data/images/smart_password_manager.png)
*Modern web interface for smart password management*

## Architecture

### Technology Stack
- **Backend**: Django 5.2+
- **Database**: PostgreSQL
- **Frontend**: HTML5, CSS3, JavaScript
- **Task Queue**: Celery with Redis (optional)

### Database Configuration
Default development credentials:
- **User**: postgres
- **Password**: postgres
- **Database**: smart_password_manager_db
- **Host**: localhost
- **Port**: 5432

## Smart Password Ecosystem

This web application is part of a comprehensive suite:

### Desktop Applications
- [**Desktop Manager**](https://github.com/smartlegionlab/smart-password-manager-desktop) - Cross-platform desktop application

### Console Tools
- [**CLI PassGen**](https://github.com/smartlegionlab/clipassgen/) - Command-line password generator
- [**CLI PassMan**](https://github.com/smartlegionlab/clipassman/) - Console-based password manager

### Core Technology
- [**SmartPassLib**](https://github.com/smartlegionlab/smartpasslib) - Core password generation library


## License

BSD 3-Clause License

Copyright (©) 2025, Alexander Suvorov

