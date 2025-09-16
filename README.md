# Smart Password Manager Web <sup>v1.1.1</sup>

[![GitHub top language](https://img.shields.io/github/languages/top/smartlegionlab/smart-password-manager)](https://github.com/smartlegionlab/smart-password-manager)
[![GitHub license](https://img.shields.io/github/license/smartlegionlab/smart-password-manager)](https://github.com/smartlegionlab/smart-password-manager/blob/master/LICENSE)
[![GitHub release](https://img.shields.io/github/v/release/smartlegionlab/smart-password-manager)](https://github.com/smartlegionlab/smart-password-manager/)
[![GitHub stars](https://img.shields.io/github/stars/smartlegionlab/smart-password-manager?style=social)](https://github.com/smartlegionlab/smart-password-manager/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/smartlegionlab/smart-password-manager?style=social)](https://github.com/smartlegionlab/smart-password-manager/network/members)

## 🌐 Web-Based Smart Password Management

A professional Django-based web application for managing and generating smart passwords with deterministic cryptography. Provides a comprehensive web interface for secure password management.

> **Powered by** [smartpasslib](https://github.com/smartlegionlab/smartpasslib) - The core library for deterministic password generation

## 🌟 Key Features

- 🌐 **Web-Based Interface** - Access your password manager from any device
- 🔒 **Zero Password Storage** - Passwords generated on-demand, never stored in database
- 🎨 **Responsive Design** - Works seamlessly on desktop and mobile devices
- 📁 **Project Organization** - Organize credentials by projects and categories
- 🔍 **Advanced Search** - Quickly find and manage your login information
- ⚡ **Real-Time Generation** - Instant password generation with cryptographic security

## 🌌 The Paradox at the Core

This tool embodies a beautiful cryptographic paradox: **perfect reproducibility meets complete unpredictability**. 

The system is both:
- **Perfectly reproducible** - Identical inputs (login + secret phrase) will always generate the exact same password, every time, on any device
- **Completely unpredictable** - Without the exact inputs, the output is computationally impossible to guess or reverse-engineer

This paradox is powered by deterministic cryptography - the same revolutionary concept explored in our foundational articles:
- [**The Password That Never Was**](https://dev.to/smartlegionlab/the-password-that-never-was-how-to-access-secrets-that-were-always-there-smart-password-library-4h16) - How passwords emerge from mathematical space rather than being created
- [**Chrono-Library Messenger**](https://dev.to/smartlegionlab/i-created-a-messenger-that-doesnt-send-any-data-heres-how-it-works-4ecp) - The cryptographic framework enabling this paradigm
- [**Messages That Have Always Been With Us**](https://dev.to/smartlegionlab/the-magic-of-messages-that-have-always-been-with-us-48gp) - Philosophical foundation of pre-existing information

Your passwords don't need to be stored because they were never created - they already exist as mathematical certainties, waiting to be discovered through the correct combination of login and secret phrase.

---

## 🚀 Quick Start

### Prerequisites
- **Python 3.8+** 
- **PostgreSQL** (recommended) or SQLite
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

## 🎨 Interface Preview

![Web Interface](https://github.com/smartlegionlab/smart-password-manager/raw/master/data/images/smart_password_manager.png)
*Modern web interface for smart password management*

## 🏗️ Architecture

### Technology Stack
- **Backend**: Django 5.2+
- **Database**: PostgreSQL (recommended) or SQLite
- **Frontend**: HTML5, CSS3, JavaScript
- **Security**: SHA3-512, deterministic cryptography
- **Task Queue**: Celery with Redis (optional)

### Database Configuration
Default development credentials:
- **User**: postgres
- **Password**: postgres
- **Database**: smart_password_manager_db
- **Host**: localhost
- **Port**: 5432

## 🔄 Smart Password Ecosystem

This web application is part of a comprehensive suite:

### 🖥️ Desktop Applications
- [**Desktop Manager**](https://github.com/smartlegionlab/smart-password-manager-desktop) - Cross-platform desktop application

### 🛠️ Console Tools
- [**CLI PassGen**](https://github.com/smartlegionlab/clipassgen/) - Command-line password generator
- [**CLI PassMan**](https://github.com/smartlegionlab/clipassman/) - Console-based password manager

### 🤖 Mobile Integration
- [**Telegram Bot**](https://t.me/smartpasswordmanagerbot) - Mobile password management

### 💡 Core Technology
- [**SmartPassLib**](https://github.com/smartlegionlab/smartpasslib) - Core password generation library

## 🛡️ Security Features

- **No Password Storage** - Credentials generated on-demand
- **PostgreSQL Security** - Enterprise-grade database security
- **Django Security** - Built-in protection against common vulnerabilities
- **Cryptographic Security** - SHA3-512 and system entropy
- **Environment Variables** - Secure configuration management

## 📖 Related Resources

Learn about the technology behind this application:
- [**The Password That Never Was**](https://dev.to/smartlegionlab/the-password-that-never-was-how-to-access-secrets-that-were-always-there-smart-password-library-4h16) - Technical foundation
- [**SmartPassLib Documentation**](https://github.com/smartlegionlab/smartpasslib) - Core library documentation

## 🚀 Production Deployment

For production deployment, consider:
- Using PostgreSQL with secure credentials
- Setting `DEBUG=False`
- Using environment-specific settings
- Configuring proper SSL/TLS certificates
- Setting up backup strategies

## 🐛 Issue Reporting

Found a bug or have a feature request? Please [create an issue](https://github.com/smartlegionlab/smart-password-manager/issues) on GitHub.

## 💻 Development

### Development Setup with PyCharm
- Database user: `postgres`
- Database password: `postgres`
- Configure PostgreSQL data source in PyCharm

### Testing
```bash
# Run tests
python manage.py test

# Run with coverage
coverage run manage.py test
coverage report
```

## 📜 License

BSD 3-Clause License

Copyright (c) 2025, Alexander Suvorov

```
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
```

## 🌟 Professional Web-Based Password Management

Experience enterprise-grade password management with the security of deterministic cryptography and the convenience of web accessibility.

**Ready to deploy?** [Get started](https://github.com/smartlegionlab/smart-password-manager) with the web version of our smart password ecosystem.

---

*Explore more professional tools at [Smart Legion Lab](https://github.com/smartlegionlab)*
