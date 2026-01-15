# Setup Instructions

## Django Backend Setup

### Step 1: Install Django and Dependencies

```bash
cd backend
pip install -r requirements.txt
```

If you don't have pip, install it first or use:
```bash
pip3 install -r requirements.txt
```

### Step 2: Run Database Migrations

```bash
cd backend
python3 manage.py migrate
```

### Step 3: Create Admin User

```bash
python3 manage.py createsuperuser
```

When prompted, enter:
- Username: `muktesh` (or your choice)
- Email: (optional, press Enter to skip)
- Password: `*Hacker4636*` (or your choice)

### Step 4: Start Django Server

```bash
cd backend
python3 manage.py runserver 8001
```

Keep this terminal open - the Django server must be running.

### Step 5: Start Frontend Server (in a NEW terminal)

```bash
cd /Users/pradyumna/company
python3 -m http.server 8002
```

## Access Points

- **Frontend Website:** http://localhost:8002
- **Django Admin Panel:** http://localhost:8001/admin
- **Backend API:** http://localhost:8001/api/contact/

## Viewing Contact Messages

1. Go to http://localhost:8001/admin/
2. Login with your superuser credentials
3. Click "Contact Messages" under the "CONTACT" section
4. View all submitted messages

## Troubleshooting

### Error: Django not installed
```bash
pip3 install Django==4.2.7 django-cors-headers==4.3.1
```

### Error: Port 8001 already in use
Change the port:
```bash
python3 manage.py runserver 8003
```
Then update `script.js` line 241 to use port 8003 instead of 8001.

### Error: 404 Not Found
- Make sure Django server is running on port 8001
- Make sure you've run migrations: `python3 manage.py migrate`
- Check browser console for specific error messages

### Error: CORS error
- Make sure both servers are running
- Frontend: http://localhost:8002
- Backend: http://localhost:8001

