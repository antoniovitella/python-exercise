import random
import string
def genera_password(lunghezza):
    caratteri = string.ascii_letters + string.digits
    password =''.join(random.choice (caratteri) for _ in range(lunghezza))
    return password
lunghezza_password = 12 # Puoi cambiare la lunghezza della password qui
nuova_password = genera_password(lunghezza_password)
print("La tua nuova password casuale è:",nuova_password)