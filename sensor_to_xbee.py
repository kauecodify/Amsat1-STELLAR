import time
import board
import busio
from adafruit_bmp280 import Adafruit_BMP280_I2C
import serial

i2c = busio.I2C(board.SCL, board.SDA)
bmp280 = Adafruit_BMP280_I2C(i2c)

xbee_serial = serial.Serial('/dev/ttyUSB0', 9600)

def send_data(data):
    xbee_serial.write(data.encode('utf-8'))

def main():
    while True:
        temperature = bmp280.temperature
        pressure = bmp280.pressure
        
        message = f"Temperatura: {temperature:.2f} C, Pressão: {pressure:.2f} hPa"

        send_data(message)

        print(message)

        time.sleep(10)

if __name__ == "__main__":
    main()
