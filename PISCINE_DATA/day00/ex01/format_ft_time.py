from datetime import date #bibliotheque dont j importe seulement ce dont j ai besoin
import time

today_date = date.today() 
scientific_time = time.time()

print("Seconds since January 1, 1970:", time.time(), " or ", "{:e}". format(scientific_time) ,"in scientific notation")
print(today_date.strftime("%B %d %Y"))