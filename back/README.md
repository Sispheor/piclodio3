# Piclodio 3 backend

## Development installation

System packages
```
sudo apt install sqlite3
```

Create a dedicated python env
```
cd back
virtualenv venv -p python3.7
source venvtest/bin/activate
```

Install python packages
```
pip3 install -r requirements.txt
```

## Run dev server

```
python3 manage.py runserver
```

# Run tests

```
python3 manage.py test
```

## Production server

Switch the server to prod mode by editing the file `back/piclodio3/settings.py` and update the line that correspond to the debug
```python
DEBUG = False
```

Run the prod server
```
gunicorn --bind 0.0.0.0:8000 piclodio3.wsgi:application
```

### Automatically at each startup with systemd (Prod)

Create and open a Systemd service file for Gunicorn with sudo privileges in your text editor:
```bash
sudo nano /etc/systemd/system/gunicorn.service
```

Place the following content (update the WorkingDirectory path depending on your installation)
```bash
[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=pi
Group=pi
WorkingDirectory=/home/pi/piclodio3/back
ExecStart=gunicorn --bind 0.0.0.0:8000 piclodio3.wsgi:application

[Install]
WantedBy=multi-user.target
```

We can now start the Gunicorn service we created and enable it so that it starts at boot:
```bash
sudo systemctl daemon-reload
sudo systemctl start gunicorn
sudo systemctl enable gunicorn
```

The backend API should now be accessible on the port 8000 of the server.
