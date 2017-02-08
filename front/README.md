# Piclodio frontend

This part of the project is written with Angular JS 2 and  was generated with [angular-cli](https://github.com/angular/angular-cli) version 1.0.0-beta.30.

## Installation

### Pre requisite

Install nodejs 6.x
```bash
curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -
sudo apt-get install -y nodejs
node --version
```

Install NPM
```bash
sudo apt-get install npm
```

Install angular CLI
```bash
sudo npm install -g @angular/cli
```

Clone the project
```bash
git clone https://github.com/Sispheor/angular2_poc.git
```

Install dependencies
```bash
cd project_sources
sudo npm install
```

### Run a development server

Run the developement server
```bash
ng serve --host 0.0.0.0
```
Navigate to `http://serer_ip:4200/`. The app will automatically reload if you change any of the source files.


### Run a prod server

Install apache web server
```bash
sudo apt-get install apache2
```

Build the project to genertate static files
```bash
ng build --prod --aot
```

The last command wil generate a "dist" folder. Place it in the apache web server and give all right to the Apache user
```bash
sudo cp -R dist/ /var/www/piclodio3
sudo chown -R apache2: /var/www/piclodio3
```

Disable the default vHost files

Create a vHost for piclodio, create a file `/etc/apache2/sites-available/piclodio.conf` with the following content
```bash
<VirtualHost *:80>

        DocumentRoot /var/www/piclodio3

        <Directory /var/www/piclodio3>
                Order allow,deny
                Allow from all
                AllowOverride All
        </Directory>

        ErrorLog ${APACHE_LOG_DIR}/piclodio.log
        CustomLog ${APACHE_LOG_DIR}/access.piclodio.log combined

</VirtualHost>
```

Active the vHost and reload the web server
```bash
sudo a2ensite piclodio
sudo service apache2 reload
```



