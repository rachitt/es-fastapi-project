import pickle
from pydantic import BaseModel
from fastapi import FastAPI
import json

app=FastAPI()
class model_input(BaseModel):
    HomePlanet: int
    CryoSleep: int
    Cabin: int
    Destination: int
    Age: float
    VIP:int
    RoomService:float
    FoodCourt:float
    ShoppingMall:float
    Spa:float
    VRDeck:float

model=pickle.load(open('Spaceship_kaggle.sav','rb'))
@app.get("/")
@app.post('/spaceship_ss')
def prediction(input_parameters: model_input):
    input_data=input_parameters.json()
    input_dictionary=json.loads(input_data)
    
    hp=input_dictionary['HomePlanet']
    cs=input_dictionary['CryoSleep']
    cab=input_dictionary['Cabin']
    dest=input_dictionary['Destination']
    age=input_dictionary['Age']
    vp=input_dictionary['VIP']
    rs=input_dictionary['RoomService']
    fc=input_dictionary['FoodCourt']
    sm=input_dictionary['ShoppingMall']
    sp=input_dictionary['Spa']
    vrd=input_dictionary['VRDeck']
    
    input_list=[hp,cs,cab,dest,age,vp,rs,fc,sm,sp,vrd]
    prediction=model.predict([input_list])
    
    if prediction[0] ==0:
        print("Transported:False")
    else:
        print("Transported:True")
    
    
