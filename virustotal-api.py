import hashlib
from virus_total_apis import PublicApi
import os
import time

API_KEY = '' #registrate para obtener la propia api
api = PublicApi(API_KEY)

with open("archivo.txt", "rb") as file:
    file_hash = hashlib.md5(file.read()).hexdigest()
response = api.get_file_report(file_hash) 

if response["response_code"] == 200: #if si el escaneo fue éxitoso
    if response["results"]["positives"] > 30:
        print("ARCHIVO MALICIOSO DETECTADO, analisis hecho por más de 30 antivirus") 
        time.sleep(3)
        print("Procedemos a eliminar el archivo")
        os.remove('virus.exe')
    else:
        print("Menos de 30 antivirus lo han detectado")    
else: 
    print("No ha podido obtenerse el análisis del archivo")


