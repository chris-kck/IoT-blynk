import spidev # To communicate with SPI devices

# Start SPI connection

spi = spidev.SpiDev() # Created an SPI object
spi.open(0,0) #opened the SPI protocol

# Read MCP3008 data
def analogInput(channel):
  spi.max_speed_hz = 1350000	#spi clock speed
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
  return data

# Scaling data to voltage
def Volts(data):
  volts = (data * 3.3) / float(1023)
  volts = round(volts, 2) # Round off to 2 dp
  return volts
 
# Scaling data to temperature.
def Temp(data):
  temp = ((data * 330)/float(1023))-50
  temp = round(temp)
  return temp
  #temp_degrees = Temp(analogInput(1))

print(Temp(analogInput(1)))
