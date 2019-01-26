Smart Home
===================
## Description
[Smart Home](https://github.com/jakhax/smart-home.git) 
This is a raspberry pi based smart-home that can be used to control devices and get data from sensors e.g light bulbs, fans, air conditioner, humidity & temp sensors, home media system.

The main aim of the project was to create a smart home system thats lets you to easily add more devices to your home without having to rewrite your code or change your circuit design.

## Getting started

### Requirements
This project was created on a debian linux platform but should work on other unix based[not limited to] systems.
* Tested on Debian Linux
* Python3
* node 10.2.0 and npm 6.3.0
* angular cli 6.0.0

### Cloning the repository
```bash
git clone https://github.com/jakhax/smart-home.git && cd smart-home
```

### Setting up Angular

#### Install node packages
- This part should be preferably done on your PC and not on the Pi as it is painfully slow to compile angular packages on the raspberry pi.
```bash
cd front-end
npm install
ng serve
```
#### Edit django-rest api endpoint
* Edit environment.ts(.prod.ts in production) `apiEndPoint` to your django-rest endpoint, in this case the IP address of your Raspberry Pi.

#### Build for production
* Build your app with `npm run build:prod`

<img src="media/smart-rooms.png"  alt="Smart Home Interface" width="600" height="300">

## Setting up the Django server on the raspberry pi
- First clone the project to your Raspberry Pi

#### Creating a virtual environment

```bash
python3 -m virtualenv virtual
source virtual/bin/activate
```

#### Installing dependencies
```bash
pip3 install -r requirements
```

#### Prepare environmet variables
For this project you will need the following configurations plus email setup for email registration hmac verification.
```bash
DEBUG=True
SECRET_KEY=SECRET_KEY

ALLOWED_HOSTS=.localhost,.127.0.0.1,testserver,.ngrok.io
CORS_ORIGIN_WHITELIST=127.0.0.1:4200,localhost:4200

JWT_EXPIRATION_DAYS=7
DATABASE_URL=postgres://user:password@127.0.0.1:5432/database

IS_PI=False
WEATHER_API_KEY=WEATHER_API_KEY
```
#### Database migrations

```bash
python manage.py migrate
```
#### Running the server 
```bash
python manage.py runserver
```

#### Running the tests
```bash
python manage.py test
```

#### weather api

- Get a weather api key from [Darksky](https://darksky.net)

## Cordova build android

* Assuming you have android sdk(preferably through android studio), java and gradle installed.
* Install cordova with npm `npm install -g cordova`
* Create a cordova project `cordova create mobile`
* At this point you can copy contents of the `dist` folder created when you build the angular app and replace them with the contents of the `www` folder in the cordova project folder, you can also uses a system link.
* Add or edit the `<base href>` tag in `index.html` to `<base href="./">` since we will using a file path and not a url
* Add android , `cordova platform add android`
* Connect your android device via usb, enable usb-debugging then run `cordova run android`, it should run the app in your device.

## Getting started

### To be documented
1. Adding GPIO pins, devices and device types to the Database via django admin.
2. Suggestions on physical connections and builds.

## Contributing

- Git clone [https://github.com/jakhax/smart-home.git](https://github.com/jakhax/smart-home.git) 
- Make the changes.
- Write your tests.
- If everything is OK. push your changes and make a pull request.

## License ([MIT License](http://choosealicense.com/licenses/mit/))

This project is licensed under the MIT Open Source license, (c) [Smart Home](https://github.com/jakhax/smart-home.git)
