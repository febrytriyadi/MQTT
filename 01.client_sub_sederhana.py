# import paho mqtt
import paho.mqtt.client as mqtt

# import time for sleep()
import time

#adsfsafdsafsafasf######################################
def on_message(client, userdata, message):
    # print pesan
    print("message received ",str(message.payload.decode("utf-8")))
########################################
    
# buat callback on_message; jika ada pesan
#client.on_message=on_message
# buat definisi nama broker yang akan digunakan
broker="192.168.100.102"

# buat client baru bernama P1
print("creating new instance")
client = mqtt.Client("P1")

# kaitkan callback on_message ke client
client.on_message=on_message

# buat koneksi ke broker
print("connecting to broker")
client.connect(broker)


# jalankan loop client
client.loop_start()

# client melakukan subsribe ke topik 1
print("Subscribing to topic","waktu")
client.subscribe("waktu")

# loop forever
while True:
    # berikan waktu tunggu 1 detik 
    time.sleep(1)

#stop loop
client.loop_stop()
