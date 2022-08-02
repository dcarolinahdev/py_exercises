from datetime import datetime
import pytz

bogota_tmz = pytz.timezone("America/Bogota")
bogota_date = datetime.now(bogota_tmz)
print("Bogotá: ", bogota_date.strftime("%d/%m/%Y %H:%M:%S %p"))

cdmx_tmz = pytz.timezone("America/Mexico_City")
cdmx_date = datetime.now(cdmx_tmz)
print("Mexico: ", cdmx_date.strftime("%d/%m/%Y %H:%M:%S %p"))

caracas_tmz = pytz.timezone("America/Caracas")
caracas_date = datetime.now(caracas_tmz)
print("Caracas:", caracas_date.strftime("%d/%m/%Y %H:%M:%S %p"))