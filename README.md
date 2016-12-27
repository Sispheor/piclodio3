# Piclodio3

## Back end
This part of the project is written Django Rest framework.

### Development platform

#### Install dev environment (Ubuntu 16.04)
Install the framwork
```
sudo pip install Django==1.10.4
sudo pip install djangorestframework==3.5.3
sudo pip install django-cors-headers==1.3.1
```



## Front end

This part of the project is written with Angular JS 2 and  was generated with [angular-cli](https://github.com/angular/angular-cli) version 1.0.0-beta.22-1.

### Development platform

#### Install dev environment (Ubuntu 16.04)

Install nodejs 6.x
```
curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -
sudo apt-get install -y nodejs
node --version
```

Install NPM
```
sudo apt-get install npm
```

Install angular CLI
```
sudo npm install -g angular-cli
```

Clone the project
```
git clone https://github.com/Sispheor/angular2_poc.git
```

Install dependencies
```
cd project_sources
sudo npm install
```

#### Development server

Run the developement server
```
ng serve --host 0.0.0.0
```
Navigate to `http://serer_ip:4200/`. The app will automatically reload if you change any of the source files.

### Code scaffolding

Run `ng generate component component-name` to generate a new component. You can also use `ng generate directive/pipe/service/class`.

### Build

Run `ng build` to build the project. The build artifacts will be stored in the `dist/` directory. Use the `-prod` flag for a production build.

### Running unit tests

Run `ng test` to execute the unit tests via [Karma](https://karma-runner.github.io).

### Running end-to-end tests

Run `ng e2e` to execute the end-to-end tests via [Protractor](http://www.protractortest.org/).
Before running the tests make sure you are serving the app via `ng serve`.
