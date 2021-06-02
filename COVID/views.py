from django.shortcuts import render
from bs4 import BeautifulSoup
from selenium import webdriver
import requests

#WEBSCRAPING
def scraping():
    page = requests.get("https://www.worldometers.info/coronavirus/")
    soup = BeautifulSoup(page.content,'html.parser')
    data = soup.find_all(class_="maincounter-number")
    data_values=[]
    for i in data:
        data_values.append(i.span.string)
    return data_values

# Create your views here.
def home(request):
    while True:
        data_values=scraping()
        cases = data_values[0]
        recovered = data_values[1]
        death = data_values[2]
        return render(request,'home.html',{'data':data_values})