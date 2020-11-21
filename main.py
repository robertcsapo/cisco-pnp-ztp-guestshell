"""
HTTP Service to download Python script
"""
from threading import Thread
from flask import Flask, request
import provision


unique_device = {}
app = Flask(__name__)
""" Settings """
PORT = 8000
HOST = "0.0.0.0"

__app__ = "cisco-pnp-ztp-guestshell"
__version__ = "1.1"
__maintainer__ = "rcsapo@cisco.com"
__url__ = "https://github.com/robertcsapo/cisco-pnp-ztp-guestshell"


@app.route("/")
def hello():
    """ Display app information """
    return "{} version {} - made by {} \n source {}".format(
        __app__, __version__, __maintainer__, __url__
    )


@app.route("/ztp.py", methods=["GET"])
def ztp_file():
    """ Offer ZTP Python file to Cisco IOS-XE device """
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
    return app.send_static_file("ztp.py")


if __name__ == "__main__":
    app.run(host=HOST, port=PORT, threaded=True, debug=False)
