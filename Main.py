import serial
#from cassandra.cluster import Cluster

ser = serial.Serial('COM4', baudrate = 9600, timeout = 1)
#cluster = Cluster() """Cluster(['192.168.0.1', '192.168.0.2']), 127.0.0.1 default"""
#session = cluster.connect('mykeyspace') """la bd"""

arduinoData = ser.readline()

while True:

    arduinoData = int(ser.readline())
    print(arduinoData)

 #   session.execute(
  #      """
   #     INSERT INTO data(distance, timestamp)
    #    VALUES (%s, toTimestamp(now())
     #   """,
      #  (arduinoData, ))
    ser.flush()
