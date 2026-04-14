import serial
import time

BAUD = 115200
PORTAS = ['/dev/ttyUSB0', '/dev/ttyUSB1', '/dev/ttyACM0']

ser = None

for porta in PORTAS:
    try:
        ser = serial.Serial(porta, BAUD, timeout=1, dsrdtr=False, rtscts=False)
        print(f"✅ Conectado em {porta}")
        time.sleep(2)  # dá tempo pro ESP32 inicializar
        break
    except Exception as e:
        print(f"⚠️ Não consegui abrir {porta}: {e}")

if ser is None:
    print("❌ Nenhuma porta serial disponível.")
    exit(1)

# Loop de leitura
with ser:
    while True:
        linha = ser.readline().decode(errors='ignore').strip()
        if linha:
            print(linha)
