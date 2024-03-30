import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt6.QtGui import QPixmap, QImage
from qrCodeUI import Ui_MainWindow
from PIL.ImageQt import ImageQt
import qrcode


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.generate_btn.clicked.connect(self.generate_qr)
        self.ui.download_btn.clicked.connect(self.save_as_pdf)

    def generate_qr(self):
        
        wifi_password = self.ui.passwd_line.text()
        wifi_ssid = self.ui.lineEdit.text()
        
        wifi_security = "WPA"  # Sécurité WiFi, peut être WEP, WPA, ou sans fil

        # Création de la chaîne de configuration WiFi pour le QR code
        wifi_config = f"WIFI:T:{wifi_security};S:{wifi_ssid};P:{wifi_password};;"

        # Création du QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(wifi_config)
        qr.make(fit=True)

        # Génération de l'image du QR code
        img = qr.make_image(fill_color="black", back_color="white")

        # Conversion de l'image PIL en QImage
        qimage = ImageQt(img)
        
        pixmap = QPixmap.fromImage(qimage)
        # Afficher le QR code dans votre interface graphique (vous devez ajouter un QLabel à votre fichier .ui pour afficher l'image)
        
        self.ui.qr_place.setPixmap(pixmap)
        self.ui.qr_place.setScaledContents(True)
        
        # store the QR code image for later use
        self.qr_image = img
        
    def save_as_pdf(self):
        if hasattr(self, 'qr_image'):
            file_path, _ = QFileDialog.getSaveFileName(self, "Save QR Code as PDF", "", "PDF File (*.pdf)")
            
            if file_path:
                # Save the QR code image as a PDF
                self.qr_image.save(file_path, "PDF", resolution=100.0)

        
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
