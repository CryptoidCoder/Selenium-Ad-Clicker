# Selenium-Web-Clicker

## A Web-Scraper running in docker that utilizes the Mysterium Network to browse while being undetected

>This project aims to navigate the web while randomizing user agents and ip's. The brilliance of it comes from the Mysterium network. 
>This allows us to use non-commercial ip's as a Virtual Private Netowrk. When clicking on websites from a known VPN/Proxy websites often just block them. 
>That is where Mysterium Comes in allowing people to have a decentralized VPN.

## Part one: Mysterium

>The wallet is what will be paying the individuals who run the servers we are connecting to.
>You will need to download the Mysterium-Desktop app and make a wallet so you can import your private key into Selenium-Web-Clicker
>Then export the wallet and put the string and password in docker-compose.yml

## Part two: Test Site

>You will need to make a Linux server on a VPS and hook a domain up to it. 
>Making the necessary changes to the index.html file to reflect your test. 
>Then build and run the docker container as follows (making sure you are in the same directory):
    
    docker build -t ad_site .
    docker run -d -p 80:80 ad_site

## Part three: Web Bot

>The last part is the web clicker and this one should run locally. The ad_bot uses two containers; 
>The first is a Mysterium node (which we do not need to edit), and the second is a Selenium web-scraper.
>You will need to change some of the code in  ad_bot.py. 
>You will need to change the URL to whatever domain you made for the Ad_site.

    Docker build -t ad_bot .
    docker-compose up

## All set you should start earing money wherever you set-up your ad network. 

> [Big thanks to CryptoidCoder for helping me with this project](https://cryptoidcoder.github.io/Coding-Website/landing)
