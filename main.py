import serial
import sys
from rgbmatrix import RGBMatrix, RGBMatrixOptions

# Setup the serial port to receive data
baudrate = 115200
port = ""
ser = serial.Serial(port, baudrate, timeout=1)

# Setup the RGB matrix
options = RGBMatrixOptions()
options.rows = 32
options.cols = 64
options.chain_length = 1
options.parallel = 1
options.hardware_mapping = "adafruit-hat-pwm"
options.gpio_slowdown = 0
options.pwm_bits = 7

matrix = RGBMatrix(options=options)


with ser as ser_port:
    try:
        while True:
            if ser_port.in_waiting > 0:
                data = ser_port.readline().decode("utf-8").strip()
                match data:
                    case "yellow_flag":
                        matrix.Fill(255, 0, 255)
                    case "blue_flag":
                        matrix.Fill(0, 255, 0)
                    case "green_flag":
                        matrix.Fill(0, 0, 255)
                    case "white_flag":
                        matrix.Fill(255, 255, 255)
                    case "black_flag":
                        matrix.fill(0, 0, 0)
    except KeyboardInterrupt:
        matrix.Clear()
        ser.close()
        sys.exit(0)
