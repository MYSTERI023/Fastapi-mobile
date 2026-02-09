from fastapi import FastAPI
from pydantic import BaseModel
import pickle

final_model = pickle.load(open('final_MPP.pkl','rb'))
scaler = pickle.load(open('scaled_value.pkl','rb'))
class Mobile(BaseModel):
    Release_year:int
    Ram_GB:int
    Storage:int
    screen_size:float
    refresh_rate:int
    camera:int
    Support_5G:int
    Apple:int
    google:int
    Motorola:int
    Nothing:int
    Oneplus:int
    Oppo:int
    Realme:int
    Samsung:int
    Vivo:int
    Xiaomi:int
    Apple_Bionic:int
    Dimensity:int
    Exynos:int
    Snapdragon:int
    Tensor:int
    Battery_enc:int
    Screen_type:int

Mobile_app = FastAPI()

@Mobile_app.get('/')
def hello():
    return{'message':'hello'}

@Mobile_app.post('/predict')
def predict(Mob:Mobile):
    q = [[Mob.Release_year,Mob.Ram_GB,Mob.Storage,Mob.screen_size,Mob.refresh_rate,Mob.camera,Mob.Support_5G,Mob.Apple,Mob.google,Mob.Motorola,Mob.Nothing,Mob.Oneplus,Mob.Oppo,Mob.Realme,Mob.Samsung,Mob.Vivo,Mob.Xiaomi,Mob.Apple_Bionic,Mob.Dimensity,Mob.Exynos,Mob.Snapdragon,Mob.Tensor,Mob.Battery_enc,Mob.Screen_type]]
    q_scaled = scaler.transform(q)
    yp = final_model.predict(q_scaled)[0]
    value = round(yp,2)
    return {'predicted_Price':value}