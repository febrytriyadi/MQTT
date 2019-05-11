# import paho
import paho.mqtt.client as mqtt

# definsi broker yang digunakan
broker = "192.168.100.102"

# buat client bernama P1
print("creating new instance")
client = mqtt.Client("P1")

# client terkoneksi ke broker
print("connecting to broker")
client.connect(broker)

# print "baca file"
print ("read file")

# buka file surf.jpg
my_file=open("surf.jpg",'rb')
# baca semua isi file
fileContent = my_file.read()
byteArr = bytes(fileContent)
client.publish("poto",byteArr)
print("publish foto")

client.loop_stop()

 

# ubah file dalam bentuk byte gunakan fungsi byte()


# publish dengan topik photo dan data dipublish adalah file


# client loop mulai


# tutup file
