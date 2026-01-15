# Django Backend Setup

## Quick Start

### 1. Install Dependencies

```bash
cd backend
pip install -r requirements.txt
```

Or if using virtual environment:

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Run Migrations

```bash
python manage.py migrate
```

### 3. Create Superuser (for admin panel)

```bash
python manage.py createsuperuser
```

Enter your admin credentials when prompted.

### 4. Start the Django Server

```bash
python manage.py runserver 8001
```

The backend will run on `http://localhost:8001`

### 5. Start Frontend Server (in another terminal)

```bash
cd /Users/pradyumna/company
python3 -m http.server 8002
```

## Access Points

- **Frontend:** http://localhost:8002
- **Backend API:** http://localhost:8001
- **Django Admin:** http://localhost:8001/admin

## Viewing Messages

1. Go to http://localhost:8001/admin/
2. Login with your superuser credentials
3. Click on "Contact Messages" under the "CONTACT" section
4. View all submitted contact forms

Messages are also printed in the Django terminal when received.

## API Endpoints

- **Contact Form:** POST http://localhost:8001/api/contact/
- **Newsletter:** POST http://localhost:8001/api/newsletter/

## Troubleshooting

### Port Already in Use
If port 8001 is in use, change it:
```bash
python manage.py runserver 8003
```
Then update the API URL in `script.js` to use port 8003.

### CORS Errors
Make sure both servers are running:
- Frontend: http://localhost:8002
- Backend: http://localhost:8001

Both ports are configured in `settings.py` under `CORS_ALLOWED_ORIGINS`.

