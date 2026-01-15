# import qrcode

# Wi-Fi details
ssid = "Yourwifiname"
password = "yourpass"
encryption = "WPA"   # Options: WEP, WPA, or leave empty for no password
hidden = "true"      # "true" if hidden, "false" or omit if visible

# Format according to Wi-Fi QR standard
wifi_config = f"WIFI:T:{encryption};S:{ssid};P:{password};H:{hidden};;"

# Generate QR code
# qr = qrcode.make(wifi_config)

# Save as image
# qr.save("wifi_qr.png")
