from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import requests
API_KEY = "d03df81fa6320b1f7fbb33c667d4e3c6"
app = FastAPI()
# here in directory you'll pass folder name where your html code present
templates = Jinja2Templates(directory="templates")

@app.get("/{city}")
async def home(request: Request, city: str):
    try:
        response = dict(requests.get(url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}").json())
        city_name = response["name"]
        temperature = round(response["main"]["temp"] - 273.15, 2)
        temp_feels_like = round(response["main"]["feels_like"] - 273.15, 2)
        description = response["weather"][0]["description"]
        return templates.TemplateResponse("home.html", {
            "request": request,
            "city_name": city_name,
            "temperature": temperature,
            "temp_feels_like": temp_feels_like,
            "description": description
        })
    except:
        return templates.TemplateResponse("error.html", {"request": request, "city": city})