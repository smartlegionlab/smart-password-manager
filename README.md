# Smart Password Manager <sup>v1.0.1</sup>

---

Smart Password Manager web version.

---

![GitHub top language](https://img.shields.io/github/languages/top/smartlegionlab/smart-password-manager)
[![GitHub](https://img.shields.io/github/license/smartlegionlab/smart-password-manager)](https://github.com/smartlegionlab/smart-password-manager/blob/master/LICENSE)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/smartlegionlab/smart-password-manager)](https://github.com/smartlegionlab/smart-password-manager/)
[![GitHub Repo stars](https://img.shields.io/github/stars/smartlegionlab/smart-password-manager?style=social)](https://github.com/smartlegionlab/smart-password-manager/)
[![GitHub watchers](https://img.shields.io/github/watchers/smartlegionlab/smart-password-manager?style=social)](https://github.com/smartlegionlab/smart-password-manager/)
[![GitHub forks](https://img.shields.io/github/forks/smartlegionlab/smart-password-manager?style=social)](https://github.com/smartlegionlab/smart-password-manager/)

---

![LOGO](https://github.com/smartlegionlab/smart-password-manager/raw/master/data/images/smart_password_manager.png)

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
git clone https://github.com/smart_legion_lab/smart-password-manager.git
cd smart-password-manager

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

*And check out the implementation that makes this possible:*

- [Smart Password Library on GitHub](https://github.com/smartlegionlab/smartpasslib)
- [Smart Password Library on PyPi](https://pypi.org/project/smartpasslib/)

- [Chrono-Library Messenger](https://github.com/smartlegionlab/chrono-library-messenger)
- [Console Smart Password Generator on GitHub](https://github.com/smartlegionlab/clipassgen)
- [Console Smart Password Manager on GitHub](https://github.com/smartlegionlab/clipassman)
- [Smart Password Manager Desktop version GitHub](https://github.com/smartlegionlab/smart-password-manager-desktop)

- [Article on dev.to: The Password That Never Was: How to Access Secrets That Were Always There. Smart Password Library. 🔐](https://dev.to/smartlegionlab/the-password-that-never-was-how-to-access-secrets-that-were-always-there-smart-password-library-4h16)

---

## 📜 License & Disclaimer

BSD 3-Clause License

Copyright (c) 2025, Alexander Suvorov

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
