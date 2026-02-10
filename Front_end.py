import streamlit as st
import requests
import json
st.title('Mobile Price Prediction',text_alignment='center')
Release_year = st.number_input('Year of Launch',min_value=2016,max_value=2026,step=1)
Brand = st.selectbox("Select Company",['Apple','Google','Motorola','Nothing','Oneplus','Oppo','Realme','Samsung','Vivo','Xiaomi'])
if Brand =='Apple':
    Apple=1
    google=0
    Motorola=0
    Nothing=0
    Oneplus=0
    Oppo=0
    Realme=0
    Samsung=0
    Vivo=0
    Xiaomi=0
elif Brand =='Google':
    Apple=0
    google=1
    Motorola=0
    Nothing=0
    Oneplus=0
    Oppo=0
    Realme=0
    Samsung=0
    Vivo=0
    Xiaomi=0  
elif Brand =='Motorola':
    Apple=0
    google=0
    Motorola=1
    Nothing=0
    Oneplus=0
    Oppo=0
    Realme=0
    Samsung=0
    Vivo=0
    Xiaomi=0 
elif Brand =='Nothing':
    Apple=0
    google=0
    Motorola=0
    Nothing=1
    Oneplus=0
    Oppo=0
    Realme=0
    Samsung=0
    Vivo=0
    Xiaomi=0  
elif Brand =='Oneplus':
    Apple=0
    google=0
    Motorola=0
    Nothing=0
    Oneplus=1
    Oppo=0
    Realme=0
    Samsung=0
    Vivo=0
    Xiaomi=0           
elif Brand =='Oppo':
    Apple=0
    google=0
    Motorola=0
    Nothing=0
    Oneplus=0
    Oppo=1
    Realme=0
    Samsung=0
    Vivo=0
    Xiaomi=0    
elif Brand =='Realme':
    Apple=0
    google=0
    Motorola=0
    Nothing=0
    Oneplus=0
    Oppo=0
    Realme=1
    Samsung=0
    Vivo=0
    Xiaomi=0 
elif Brand =='Samsung':
    Apple=0
    google=0
    Motorola=0
    Nothing=0
    Oneplus=0
    Oppo=0
    Realme=0
    Samsung=1
    Vivo=0
    Xiaomi=0      
elif Brand =='Vivo':
    Apple=0
    google=0
    Motorola=0
    Nothing=0
    Oneplus=0
    Oppo=0
    Realme=0
    Samsung=0
    Vivo=1
    Xiaomi=0   
else:
    Apple=0
    google=0
    Motorola=0
    Nothing=0
    Oneplus=0
    Oppo=0
    Realme=0
    Samsung=0
    Vivo=0
    Xiaomi=1   
if Brand=='Apple':
    Ram_GB = 8
    Storage = st.pills('Storage Size',[128,256,512,1024])
elif Brand=='Samsung':
    Ram_GB = st.pills('Ram Size',[8,12])
    Storage = st.pills('Storage Size',[128,256,512,1024])
elif Brand=='Google':
    Ram_GB = st.pills('Ram Size',[12,16])
    Storage = st.pills('Storage Size',[128,256,512])
elif Brand=='Oneplus' or Brand=='Xiaomi':
    Ram_GB = st.pills('Ram Size',[8,12,16,24]) 
    Storage = st.pills('Storage Size',[128,256,512])
elif Brand=='Nothing' or Brand=='Motorola' or Brand=='Realme':
    Ram_GB = st.pills('Ram Size',[8,12,16])
    Storage = st.pills('Storage Size',[64,128,256])
else:
    Ram_GB = st.pills('Ram Size',[4,6,8,12,16])
    Storage = st.pills('Storage Size',[32,64,128,256])
screen_size = st.number_input('Screen Size',min_value=5.8,max_value=7.0,step=0.2)
refresh_rate = st.selectbox('Refresh_rate',[60,90,120])
camera = st.pills('Camera MP',[12,16,48,50,64,108])
if Release_year>2022:
    _5G = 'Yes'
else:
    _5G = st.selectbox('5G Support',['Yes','No'])
    Support_5G = 1 if _5G=='Yes' else 0
if Brand=='Apple':
    Proccessor = st.selectbox('Select Proccessor',['Apple_Bionic'])
elif Brand=='Google':
    Proccessor = st.selectbox('Select Proccessor',['Tensor'])
elif Brand=='Samsung':
    Proccessor = st.selectbox('Select Proccessor',['Snapdragon','Exynos']) 
else:
    Proccessor = st.selectbox('Select Proccessor',['Snapdragon','Dimensity'])             
if Proccessor =="Apple_Bionic":
    Apple_Bionic=1
    Dimensity=0
    Exynos=0
    Snapdragon=0
    Tensor=0
elif Proccessor =='Dimensity':
    Apple_Bionic=0
    Dimensity=1
    Exynos=0
    Snapdragon=0
    Tensor=0   
elif Proccessor =='Exynos':
    Apple_Bionic=0
    Dimensity=0
    Exynos=1
    Snapdragon=0
    Tensor=0
elif Proccessor == 'Snapdragon':
    Apple_Bionic=0
    Dimensity=0
    Exynos=0
    Snapdragon=1
    Tensor=0 
else:
    Apple_Bionic=0
    Dimensity=0
    Exynos=0
    Snapdragon=0
    Tensor=1   
if Brand=='Apple':
    Battery = 4000
elif Brand=='Google':
    Battery = 4500    
else:
    Battery = st.selectbox("Select Battery Size",['3500','4000','4500','5000','5500','6000'])   
if Battery == '3500':
    Battery_enc = 1
elif Battery == '4000':
    Battery_enc = 2
elif Battery == '4500':
    Battery_enc = 3
elif Battery == '5000':
    Battery_enc = 4
elif Battery == '5500':
    Battery_enc = 5
else:
    Battery_enc = 6
Screen_t = st.selectbox("Select Screen Type",['LCD','AMOLED','OLED'])  
if Screen_t == 'LCD':
    Screen_type = 1
elif Screen_t == 'AMOLED':
    Screen_type = 2
else:
    Screen_type = 3
#X_test = [[Release_year,Ram_GB,Storage,screen_size,refresh_rate,camera,Support_5G,Apple,Motorola,Nothing,Oneplus,Oppo,Realme,Samsung,Vivo,Xiaomi,Apple_Bionic,Dimensity,Exynos,Snapdragon,Tensor,Battery_enc,Screen_type]]           
if st.button("SUBMIT"):
    obj1 = json.dumps({"Release_year":int(Release_year),"Ram_GB":int(Ram_GB),"Storage":int(Storage),"screen_size":float(screen_size),"refresh_rate":int(refresh_rate),"camera":int(camera),"Support_5G":int(Support_5G),"Apple":int(Apple),"google":int(google),"Motorola":int(Motorola),"Nothing":int(Nothing),"Oneplus":int(Oneplus),"Oppo":int(Oppo),"Realme":int(Realme),"Samsung":int(Samsung),"Vivo":int(Vivo),"Xiaomi":int(Xiaomi),"Apple_Bionic":int(Apple_Bionic),"Dimensity":int(Dimensity),"Exynos":int(Exynos),"Snapdragon":int(Snapdragon),"Tensor":int(Tensor),"Battery_enc":int(Battery_enc),"Screen_type":int(Screen_type)})
    url = 'http://127.0.0.1:8000/predict'
    response = requests.post(url = url,data=obj1)
    output = json.loads(response.text)
    st.success(output["predicted_Price"])                      