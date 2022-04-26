# Selenium-Ad-Clicker

## A Web-Scraper running in docker that utilizes the Mysterium Network to click ads while being undetected

>This project aims to click your own ads and make money. The brilliance of it comes from the Mysterium network. 
>This allows us to use non-commercial ip's as VPNs'. When clicking on an ad from a known VPN/Proxy ad networks often >just block them therefore earning nothing. 
>That is where Mysterium Comes in allowing people to have a decentralized VPN.

## Part one: Mysterium

>The wallet is what will be paying the individuals who run the servers we are connecting to.
>You will need to download the Mysterium-Desktop app and make a wallet and import some tokens into it.
>Then export the wallet and put the string and password in docker-compose.yml

## Part two: Ad Site

>You will need to make a Linux server on a VPS and hook a domain up to it. 
>Making the necessary changes to the index.html file to reflect your ad. 
>Then build and run the docker container as follows (making sure you are in the same directory):
    
    docker build -t ad_site .
    docker run -d -p 80:80 ad_site

## Part three: Ad Bot

>The last part is the ad clicker and this one should run locally. The ad_bot uses two containers; 
>The first is a Mysterium node (which we do not need to edit), and the second is a Selenium web-scraper.
>You will need to change some of the code in  ad_bot.py. 
>You will need to change the URL to whatever domain you made for the Ad_site.

    Docker build -t ad_bot .
    docker-compose up

## All set you should start earing money wherever you set-up your ad network. 

> [Big thanks to CryptoidCoder for helping me with this project](https://cryptoidcoder.github.io/Coding-Website/landing)