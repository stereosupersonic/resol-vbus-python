import os

# configure kind of connection "lan", "serial" or "stdin"
connection = "lan"
#connection = "serial"
#connection = "stdin"

# only used for "lan"
address = ("192.168.1.86", 7053)
vbus_pass = "vbus"

# only used for "serial"
# port = "/dev/ttyAMA0"
# baudrate = 9600

# specify Resol specs file
spec_file = os.path.dirname(__file__) + '/spec/DeltaSolM.json'

# expected amount of different source packets (see spec_file)
expected_packets = 1

# should json data field contain units?
use_units = True

debug = False

# Temperatur Sensor 1 = tkol => kollekoren temperatur
# Temperatur Sensor 2 = TSPu => Temp. Schichtenspeicher oben
# Temperatur Sensor 3 => nicht in betrieb
# Temperatur Sensor 4 = TSP2u => Temp. Schichtenspeicher unten
# Temperatur Sensor 5=> ??? evtl.  "34.9 °C",
# Temperatur Sensor 9=> ??? evtl. "26.8 °C",
# Temperatur Sensor 11 => Temp. aussen  "9.1 °C",


# 24.02.2023 19:02 Holzofen vor ca 1h an
  # "DeltaSol M [Regler]": {
  #   "Temperatur Sensor 1": "7.4 °C",
  #   "Temperatur Sensor 2": "64.5 °C",

  #   "Temperatur Sensor 4": "26.7 °C",
  #   "Temperatur Sensor 5": "63.9 °C",

  #   "Temperatur Sensor 9": "46.3 °C",

  #   "Temperatur Sensor 11": "8.2 °C",
