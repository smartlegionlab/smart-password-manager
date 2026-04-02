# Smart Password Manager Web <sup>v1.3.2</sup>

---

> Note: This is a production-ready password manager. For academic research on the underlying security paradigms, see [The Pointer-Based Security Paradigm](https://doi.org/10.5281/zenodo.17204738), [Local Data Regeneration Paradigm](https://doi.org/10.5281/zenodo.17264327)

---

[![GitHub top language](https://img.shields.io/github/languages/top/smartlegionlab/smart-password-manager)](https://github.com/smartlegionlab/smart-password-manager)
[![GitHub license](https://img.shields.io/github/license/smartlegionlab/smart-password-manager)](https://github.com/smartlegionlab/smart-password-manager/blob/master/LICENSE)
[![GitHub release](https://img.shields.io/github/v/release/smartlegionlab/smart-password-manager)](https://github.com/smartlegionlab/smart-password-manager/)
[![GitHub stars](https://img.shields.io/github/stars/smartlegionlab/smart-password-manager?style=social)](https://github.com/smartlegionlab/smart-password-manager/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/smartlegionlab/smart-password-manager?style=social)](https://github.com/smartlegionlab/smart-password-manager/network/members)

## 🌐 Web-Based Smart Password Management

Smart Password Manager (web version).

> **Powered by** [smartpasslib](https://github.com/smartlegionlab/smartpasslib) - The core library for deterministic password generation.

Your passwords don't need to be stored because they were never created—they already exist as mathematically valid data waiting to be discovered.

---

## 🚀 Quick Start

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

## 🎨 Interface Preview

![Web Interface](https://github.com/smartlegionlab/smart-password-manager/raw/master/data/images/smart_password_manager.png)
*Modern web interface for smart password management*

## 🏗️ Architecture

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

## 🔄 Smart Password Ecosystem

This web application is part of a comprehensive suite:

### 🖥️ Desktop Applications
- [**Desktop Manager**](https://github.com/smartlegionlab/smart-password-manager-desktop) - Cross-platform desktop application

### 🛠️ Console Tools
- [**CLI PassGen**](https://github.com/smartlegionlab/clipassgen/) - Command-line password generator
- [**CLI PassMan**](https://github.com/smartlegionlab/clipassman/) - Console-based password manager

### 💡 Core Technology
- [**SmartPassLib**](https://github.com/smartlegionlab/smartpasslib) - Core password generation library


## 📜 License

BSD 3-Clause License

Copyright (c) 2025, Alexander Suvorov

---

## 📄 Legal Disclaimer

**COMPLETE AND ABSOLUTE RELEASE FROM ALL LIABILITY**

**SOFTWARE PROVIDED "AS IS" WITHOUT ANY WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND NONINFRINGEMENT.**

The copyright holder, contributors, and any associated parties **EXPLICITLY DISCLAIM AND DENY ALL RESPONSIBILITY AND LIABILITY** for:

1. **ANY AND ALL DATA LOSS**: Complete or partial loss of passwords, accounts, credentials, cryptographic keys, or any data whatsoever
2. **ANY AND ALL SECURITY INCIDENTS**: Unauthorized access, data breaches, account compromises, theft, or exposure of sensitive information
3. **ANY AND ALL FINANCIAL LOSSES**: Direct, indirect, incidental, special, consequential, or punitive damages of any kind
4. **ANY AND ALL OPERATIONAL DISRUPTIONS**: Service interruptions, account lockouts, authentication failures, or denial of service
5. **ANY AND ALL IMPLEMENTATION ISSUES**: Bugs, errors, vulnerabilities, misconfigurations, or incorrect usage
6. **ANY AND ALL LEGAL OR REGULATORY CONSEQUENCES**: Violations of laws, regulations, compliance requirements, or terms of service
7. **ANY AND ALL PERSONAL OR BUSINESS DAMAGES**: Reputational harm, business interruption, loss of revenue, or any other damages
8. **ANY AND ALL THIRD-PARTY CLAIMS**: Claims made by any other parties affected by software usage

**USER ACCEPTS FULL AND UNCONDITIONAL RESPONSIBILITY**

By installing, accessing, or using this software in any manner, you irrevocably agree that:

- You assume **ALL** risks associated with software usage
- You bear **SOLE** responsibility for secret phrase management and security
- You accept **COMPLETE** responsibility for all testing and validation
- You are **EXCLUSIVELY** liable for compliance with all applicable laws
- You accept **TOTAL** responsibility for any and all consequences
- You **PERMANENTLY AND IRREVOCABLY** waive, release, and discharge all claims against the copyright holder, contributors, distributors, and any associated entities

**NO WARRANTY OF ANY KIND**

This software comes with **ABSOLUTELY NO GUARANTEES** regarding:
- Security effectiveness or cryptographic strength
- Reliability or availability
- Fitness for any particular purpose
- Accuracy or correctness
- Freedom from defects or vulnerabilities

**NOT A SECURITY PRODUCT OR SERVICE**

This is experimental software. It is not:
- Security consultation or advice
- A certified cryptographic product
- A guaranteed security solution
- Professional security software
- Endorsed by any security authority

**FINAL AND BINDING AGREEMENT**

Usage of this software constitutes your **FULL AND UNCONDITIONAL ACCEPTANCE** of this disclaimer. If you do not accept **ALL** terms and conditions, **DO NOT USE THE SOFTWARE.**

**BY PROCEEDING, YOU ACKNOWLEDGE THAT YOU HAVE READ THIS DISCLAIMER IN ITS ENTIRETY, UNDERSTAND ITS TERMS COMPLETELY, AND ACCEPT THEM WITHOUT RESERVATION OR EXCEPTION.**

---

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

