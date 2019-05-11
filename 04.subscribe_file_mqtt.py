# gunakan library paho
import paho.mqtt.client as mqtt

# gunakan library time
import time

# buat callback pada saat ada pesan masuk
###########################################
def on_message(client, userdata, message):
    with open("iris.jpg", "wb") as x:        
        x.write(message.payload)
        x.close()
        print("Downloaded")
    # tulis hasil file yang didapat bernama "iris.jpg"
    
##########################################
        
# definisikan broker yang akan digunakan
broker="192.168.100.102"

# buat client P2 
print("creating new instance")
client = mqtt.Client("P2")
client.on_message=on_message
# koneksi P2 ke broker
print("connecting to broker")
client.connect(broker)

# P2 subcribe ke topik "photo"
print("Subscribing to topic","photo")
client.loop_start()
client.subscribe("poto")

# callback diaktifkan


#client.loop_forever()
while True:
    client.loop(15)
    time.sleep(2)

#stop loop
client.loop_stop()