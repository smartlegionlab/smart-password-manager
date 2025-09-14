# Smart Password Manager <sup>v1.0.1</sup>

---

Smart Password Manager web version.

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

## 📜 License & Disclaimer

This project is licensed under the **GNU Affero General Public License v3.0 (AGPLv3)**.

- You are free to use, modify, and distribute this software.
- **However, if you modify this software and run it as a hosted service (e.g., a web app), you MUST make the full source code of your modified version available to your users under the same license.**
- The full license text can be found in the [LICENSE](LICENSE) file.

### ⚠️ Important Disclaimer

> **THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.**
>
> *(This is a summary of the full disclaimer, which is legally binding and located in sections 15 and 16 of the AGPLv3 license).*

For commercial use that is not compatible with the AGPLv3 terms (e.g., including this software in a proprietary product without disclosing the source code), a **commercial license** is required. Please contact me at [smartlegiondev@gmail.com](mailto:smartlegiondev@gmail.com) to discuss terms.