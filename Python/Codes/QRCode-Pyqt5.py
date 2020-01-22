from PyQt5 import QtCore,QtGui,QtWidgets
from pygame2 import UIs
import sys,qdarkstyle
class UI(object):
    def Form(self,window):
        window.setWindowTitle('QRCode')
        # Theme css Dark You can Delete if you want backup Default
        window.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
        # Size Window by Disable edit size window
        window.setFixedSize(500,500)
        # file css for size font label and button  look the file if you want know the code css
        s = open('css/style.css', 'r')
        sread = s.read()
        # Create Button for Click Create the QRCode
        self.btn = QtWidgets.QPushButton(window)
        self.btn.setText('تحويل')
        self.btn.setGeometry(150, 400, 200, 40)
        self.btn.setStyleSheet(sread)
        # Line for Enter Word
        self.line = QtWidgets.QLineEdit(window)
        self.line.setGeometry(140,60,200,30)
        # Label  Only
        self.s = QtWidgets.QLabel(window)
        self.s.setStyleSheet(sread)
        self.s.setText('ادخل كلمة للتحويل')
        # This label for Show the Image after Change QRCode
        self.lbp = QtWidgets.QLabel(window)
        self.lbp.setGeometry(100,100,300,300)
        self.s.setGeometry(0,10,500,30)
        self.s.setAlignment(QtCore.Qt.AlignCenter)
        s.close()
        # Connect Button if user Click button execute Function qr()
        self.btn.clicked.connect(self.qr)
    # Create Function qr for Changed the QRCode
    def qr(self):
        # Librarys qrcode for QRCode Image and Library for Give Image QRCode Name Number Random
        import qrcode,random
        # Take the letters from Line
        make = self.line.text()
        # Random Number for Name Image
        ran = random.randrange(999)
        # Print, You can delete it
        print(ran)
        # Make QRCode from Line
        qr = qrcode.make(make) # Word Changed from QLineEdit()
        qr.save('image/{}.png'.format(ran)) # Name Photo QRCode After Changed Text
        self.phot = QtGui.QPixmap('image/{}.png'.format(ran))  # Name Photo to Show By QLabel()
        self.lbp.setPixmap(self.phot) # Show Photo
if __name__=='__main__':
    # And End the for Run The Software.
    app = QtWidgets.QApplication(sys.argv)
    form = QtWidgets.QMainWindow()
    ui = UI()
    ui.Form(form)
    form.show()
    sys.exit(app.exec_())





