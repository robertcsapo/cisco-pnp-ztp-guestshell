"""
HTTP Service to download Python script
"""
from flask import Flask, request, send_from_directory, render_template
from threading import Thread
import provision

unique_device = {}
app = Flask(__name__)
""" Settings """
PORT="8000"
HOST="0.0.0.0"

@app.route("/")
def hello():
    return "Cisco Custom ZTP provisioning - Made by rcsapo@cisco.com"

@app.route('/ztp.py', methods=["GET"])
def ztp_file():
    print(request.headers)
    ztp_device = request.remote_addr
    if ztp_device in unique_device:
        print("Duplicate of device %s" % ztp_device)
        unique_device.pop(ztp_device, None)
    else:
        print("New device %s" % ztp_device)
        unique_device[ztp_device] = ztp_device
        t = Thread(target=provision.ztp, args=(request.remote_addr,))
        t.start()
    return app.send_static_file('ztp.py')

if __name__ == "__main__":
    app.run(host=HOST,port=PORT)
