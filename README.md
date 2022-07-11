# GEONYC

Side by side UI for BigApple, GeoClient, and Esri Locator

## Pre-Install

Install BigApple package

https://github.com/cchendoitt/bigapple

## Installation

git clone https://github.com/cchendoitt/geonyc

on workstation command line
  
  > cd geonyc

  > pip install -r requirements.txt
  
  > flask run

  open browser with url http://localhost:5000 

## Optional 

To hot deploy:

  > set FLASK_APP=app.py
  
  > set FLASK_ENV=development
  
  > flask run

To make local host IP available for others view:

  > flask run --host=0.0.0.0
