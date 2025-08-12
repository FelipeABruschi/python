RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 5

velocidade = 70
local_carro = 100

if velocidade > RADAR_1:
    if local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE):
        print("carro multado")

