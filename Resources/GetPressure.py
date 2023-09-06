import smbus2
import time
import datetime
import Logging

from config import Config_Log

class Lps25hsensor:
    address = 0x5d

    PRESS_OUT_XL = 0x28
    PRESS_OUT_L = 0x29
    PRESS_OUT_H = 0x2A

    TEMP_OUT_L = 0x2B
    TEMP_OUT_H = 0x2C

    def __init__(self, smbus_addr=1):
        self.bus = smbus2.SMBus(smbus_addr)

    def setup(self):
        try:
            self.bus.write_i2c_block_data(self.address, 0x00, [])
        except OSError as e:
            print(e)

            time.sleep(0.1)

    def read_pressure(self):
        try:
            self.bus.write_i2c_block_data(self.address, 0x20, [0x90])
        except OSError as e:
            print(e)

        time.sleep(0.1)

        XL = self.read_i2c_block(self.PRESS_OUT_XL)
        L = self.read_i2c_block(self.PRESS_OUT_L)
        H = self.read_i2c_block(self.PRESS_OUT_H)

        pressure = (
                (H << 16) | (L << 8) | XL
        )
        pressure = pressure / 4096
        return pressure

    def read_temp(self):
        try:
            self.bus.write_i2c_block_data(self.address, 0x20, [0x90])
        except OSError as e:
            print(e)

        time.sleep(0.1)

        TL = self.read_i2c_block(self.TEMP_OUT_L)
        TH = self.read_i2c_block(self.TEMP_OUT_H)

        temp = (
                (TH << 8) | TL
        )
        temp = binary_to_twos_complement(temp)
        temp = 42.5 + (temp / 480)
        return temp

    def read_i2c_block(self, register):
        blocks = self.bus.read_i2c_block_data(self.address, register, 1)
        return blocks[0]


def hPa_to_MPa(hPa):
    return hPa / 10000


def Mpa_to_Altimeter(MPa):
    P = MPa
    P0 = 0.101325

    altitude = 44330 * (1 - ((P / P0) ** (1000 / 5255)))

    return altitude


def binary_to_twos_complement(binary_value):
    binary_str = str(bin(binary_value))[2:]

    if binary_str[0] == '0':
        return int(binary_str, 2)
    else:
        inverted = ''
        for bit in binary_str:
            if bit == '0':
                inverted += "1"
            else:
                inverted += "0"
        val = int(inverted, 2)
        val += 1
        val *= -1
        return val

def Get_Pressure():
    sensor = Lps25hsensor(1)
    sensor.setup()

    hPa = sensor.read_pressure()
    temp = sensor.read_temp()

    MPa = hPa_to_MPa(hPa)
    alt = Mpa_to_Altimeter(MPa)
    
    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')

    Text = "Timestamp is {}\nAltimeter : {}\nTemperature : {}\n\n".format(timestamp, alt, temp)
    #print("Get Pressure at {}".format(Text))
    Logging.log_sensor(Text)
    

if __name__ == '__main__':
    sensor = Lps25hsensor(1)
    sensor.setup()

    hPa = sensor.read_pressure()
    temp = sensor.read_temp()

    MPa = hPa_to_MPa(hPa)
    alt = Mpa_to_Altimeter(MPa)
    
    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')

    Text = "Timestamp is {}\nAltimeter : {}\nTemperature : {}\n\n".format(timestamp, alt, temp)
    #print("Get Pressure at {}".format(timestamp))
    #print(Text)
