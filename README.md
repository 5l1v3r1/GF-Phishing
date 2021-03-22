# Hacking-GF


**ONLY DOWNLOAD IT HERE, DO NOT TRUST OTHER PLACES.**

This is the official and only repository of the Hacking-GF project.

Written by: Ridel Saavedra Flores - GitHub: [@shakarr](https://github.com/shakarr)

DISCLAIMER: This is only for testing purposes and can only be used where strict consent has been given. Do not use this for illegal purposes, period.

Please read the LICENSE for the licensing of Hacking-GF.

# Features

* Generates a fake pages to capture passwords
* Adds Targets Info to the the fake page
* Sends SPOOFED emails with an SMTP you provide
* Uses NGROK to make the fake pages accessible world wide
* Grabs Victims IP addresses and does an IP lookup

### AVAILABLE PAGES

|Available Pages|Mobile Support|
|:---|:---:|
|Grand Fantasia|1|

## Tested on

* Windows 10 
* Windows 7

# Requirements

## Windows

- python3.5
- XAMPP
- Chromedriver
- NGROK
- PHP(default in XAMPP installation)

# Installation and Configuration

## Windows
**1. Download the repository**
```cmd
$ git clone https://github.com/shakarr/GF-Phishing.git
$ cd GF-Phishing
$ pip3 install -r requirements.txt
```
**NOTE**
you need to have "git" installed to use "git clone". Here [how to install git in windows](https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Instalaci%C3%B3n-de-Git)

**2. Download Chromedriver**

Go to the official [google](https://sites.google.com/a/chromium.org/chromedriver/downloads) page and download it according to your google version and unzip it in the GF-Phishing folder

**3. Download ngrok**

Go to the official [ngrok](https://ngrok.com/download) page and download it and unzip it in the GF-Phishing folder

**4. Install python3.5**

Go to the official [python](https://www.python.org/downloads/release/python-350/) page, download the installer and follow the installation instructions

**5. Install XAMPP**

Go to the official [xampp](https://www.apachefriends.org/es/index.html) page, download the installer and follow the installation instructions

**NOTE**

Is important that the installation folder be C:\