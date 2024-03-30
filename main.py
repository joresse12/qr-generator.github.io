import sys
from PyQt6.QtWidgets  import QApplication, QMainWindow
from qrCodeUI import  Ui_MainWindow


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())

# # # img = qrcode.make("EvMa23aMTi")
# # # img.save("myQrCode.png")

# # Informations du réseau Wi-Fi
# wifi_ssid = "W701V-9"
# wifi_password = "EvMa23aMTi"
# wifi_security = "WPA"  # Sécurité WiFi, peut être WEP, WPA, ou sans fil

# # Création de la chaîne de configuration WiFi pour le QR code
# wifi_config = f"WIFI:T:{wifi_security};S:{wifi_ssid};P:{wifi_password};;"

# # create the qr-code
# qr = qrcode.QRCode(
#     version=1,
#     error_correction=qrcode.constants.ERROR_CORRECT_L,
#     box_size=10,
#     border=4,
# )
# qr.add_data(wifi_config)
# qr.make(fit=True)

# # generate Qr code image
# img = qr.make_image(fill_color="black", back_color="white")

# # image saving
# img.save("myWifiQRCode.png")
