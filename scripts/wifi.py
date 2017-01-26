import network

def do_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect("My ASUS", "6e5b0c29a9e1")
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())
