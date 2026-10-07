import serial
import sys
from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image, ImageDraw, ImageFont

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
canvas = matrix.CreateFrameCanvas()

image = Image.new("RGB", (64, 32))
draw = ImageDraw.Draw(image)
text_font = ImageFont.load("")
box = text_font.getbbox("0")
char_width = box[2] - box[0]
char_height = box[3] - box[1]

text_x = 32 + ((32 - char_width) // 2)
text_y = ((32 - char_height) // 2) - box[1]


with ser as ser_port:
    try:
        while True:
            if ser_port.in_waiting > 0:
                data = ser_port.readline().decode("utf-8").strip()
                data_split = data.split(",")
                flag_color = data_split[0].strip()
                gear = data_split[1].strip()

                canvas.Clear()
                match flag_color:
                    case "yellow_flag":
                        # canvas.Fill(255, 0, 255)
                        draw.rectangle([0, 0, 31, 31], fill=(255, 0, 255))
                    case "blue_flag":
                        # canvas.Fill(0, 255, 0)
                        draw.rectangle([0, 0, 31, 31], fill=(2, 255, 0))
                    case "green_flag":
                        # canvas.Fill(0, 0, 255)
                        draw.rectangle([0, 0, 31, 31], fill=(0, 0, 255))
                    case "white_flag":
                        # canvas.Fill(255, 255, 255)
                        draw.rectangle([0, 0, 31, 31], fill=(255, 255, 255))
                    case "black_flag":
                        # canvas.fill(0, 0, 0)
                        draw.rectangle([0, 0, 31, 31], fill=(0, 0, 0))

                draw.text((text_x, text_y), gear, fill=(255, 255, 255), font=text_font)
                canvas.SetImage(image)
                canvas = matrix.SwapOnVSync(canvas)
    except KeyboardInterrupt:
        matrix.Clear()
        ser.close()
        sys.exit(0)
