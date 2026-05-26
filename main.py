import machine
import dht
import time

# Configuração
sensor_dht = dht.DHT22(machine.Pin(15))
pino_vibracao = machine.ADC(machine.Pin(34)) 
pino_vibracao.atten(machine.ADC.ATTN_11DB)
led_alerta = machine.Pin(2, machine.Pin.OUT)

print("Sistema de Monitoramento de Motores Iniciado...")

while True:
    try:
        sensor_dht.measure()
        temp = sensor_dht.temperature()
        vibracao = pino_vibracao.read()
        
        print(f"Temp: {temp}C | Vibração: {vibracao}")

        # Limites de Alerta
        if temp > 50 or vibracao > 3000:
            led_alerta.value(1)
            print("!!! ALERTA DE FALHA !!!")
        else:
            led_alerta.value(0)

        time.sleep(2)
    except:
        print("Erro na leitura")