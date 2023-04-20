from PIL import Image, ImageEnhance, ImageFilter
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QHBoxLayout, QVBoxLayout, QFileDialog, QMainWindow, QDialog, QLineEdit, QLabel
from PyQt5.QtGui import QPixmap, QIntValidator, QIcon

app = QApplication([])

class Window(QWidget):

    #Image saver
    def SaveIMG(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self,"Save Image", "", "Image Files (*.jpg)", options=options)
        if file_name:
            self.fin_edit_img.save(file_name)



    #Zobracovač náhledového obrázku
    def ShowIMG(self):
        big_org_img = Image.open(self.file_name)
        smol_org_img = big_org_img.resize((250,250), Image.LANCZOS)
        smol_org_img.save("C:/Users/Petr/Documents/Projekty/Python/Images_&_Text_files/pychletoulozim.jpg")
        pixmap = QPixmap("C:/Users/Petr/Documents/Projekty/Python/Images_&_Text_files/pychletoulozim.jpg")
        self.smol_org_img.setPixmap(pixmap)
        self.bt_con.setEnabled(True)
    


    #Image opener
    def OpenIMG(self):
        
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "Image Files (*.png *.jpg *.bmp *.webp *.gif)", options=options)
        if file_name:
            self.file_name = file_name
            self.ShowIMG()



    #CL -> BW convertor
    def ToGray(self):
        self.popup.close()
        big_org_img = Image.open(self.file_name)
        gray_image = big_org_img.convert("L")
        self.fin_edit_img = gray_image
        smol_gray_image = gray_image.resize((250,250), Image.LANCZOS)
        smol_gray_image.save("C:/Users/Petr/Documents/Projekty/Python/Images_&_Text_files/fasteditimg.jpg")
        pixmap = QPixmap("C:/Users/Petr/Documents/Projekty/Python/Images_&_Text_files/fasteditimg.jpg")
        self.smol_con_img.setPixmap(pixmap)
        self.bt_save.setEnabled(True)
        self.bt_con.setEnabled(True)
    


    #Contrast Backend
    def Contrast_Backend(self):
        context = self.ctrinp.text()
        ctrnum = int(context)
        if ctrnum > 100:
            return
        self.ctrwin.close()
        big_org_img = Image.open(self.file_name)
        contrast_enhancer = ImageEnhance.Contrast(big_org_img)
        big_ctr_img = contrast_enhancer.enhance(ctrnum)
        self.fin_edit_img = big_ctr_img
        smol_ctr_img = big_ctr_img.resize((250,250), Image.LANCZOS)
        smol_ctr_img.save("C:/Users/Petr/Documents/Projekty/Python/Images_&_Text_files/fasteditimg.jpg")
        pixmap = QPixmap("C:/Users/Petr/Documents/Projekty/Python/Images_&_Text_files/fasteditimg.jpg")
        self.smol_con_img.setPixmap(pixmap)
        self.bt_save.setEnabled(True)
        self.bt_con.setEnabled(True)


    #Contrast window
    def Contrast_Window(self):
        self.popup.close()
        self.ctrwin = QWidget()

        #Info Text
        self.ctrinftxt = QLabel("Input numbers 1-100")
        self.ctrinftxt.setAlignment(Qt.AlignCenter)

        onlyint = QIntValidator()
        onlyint.setRange(1, 100)
        #Contrast Input
        self.ctrinp = QLineEdit()
        self.ctrinp.setValidator(onlyint)

        #Save button
        self.bt_ctr_save = QPushButton("Save", self)
        self.bt_ctr_save.clicked.connect(self.Contrast_Backend)


        #Rozložení okna
        CTRhbox = QHBoxLayout()

        CTRvbox = QVBoxLayout()
        CTRvbox.addLayout(CTRhbox)
        CTRvbox.addWidget(self.ctrinftxt)
        CTRvbox.addWidget(self.ctrinp)
        CTRvbox.addWidget(self.bt_ctr_save)

        #Final Settings
        self.ctrwin.setWindowTitle("Contrast Settings")
        self.ctrwin.setLayout(CTRvbox)
        self.ctrwin.show()



    #Rotator Backend
    def Rotator_Backend(self):
        self.rtrwin.close()
        rotdeg = int(self.rotinp.text())
        big_org_img = Image.open(self.file_name)
        big_rot_img = big_org_img.rotate(rotdeg, expand=True)
        self.fin_edit_img = big_rot_img
        smol_rot_img = big_rot_img.resize((250,250), Image.LANCZOS)
        smol_rot_img.save("C:/Users/Petr/Documents/Projekty/Python/Images_&_Text_files/fasteditimg.jpg")
        pixmap = QPixmap("C:/Users/Petr/Documents/Projekty/Python/Images_&_Text_files/fasteditimg.jpg")
        self.smol_con_img.setPixmap(pixmap)
        self.bt_save.setEnabled(True)
        self.bt_con.setEnabled(True)
        


    #Rotator Window
    def Rotator_Window(self):
        self.popup.close()
        self.rtrwin = QWidget()

        #Save button
        self.bt_rot_save = QPushButton("Save", self)
        self.bt_rot_save.clicked.connect(self.Rotator_Backend)

        #Info text
        self.rotinftxt = QLabel("Input numbers 0-360")
        self.rotinftxt.setAlignment(Qt.AlignCenter)
        
        #Degrees input
        self.rotinp = QLineEdit()
        self.rotinp.setValidator(QIntValidator(0, 360))

        #Rozložení okna 
        RTRhbox = QHBoxLayout()

        RTRvbox = QVBoxLayout()
        RTRvbox.addLayout(RTRhbox)
        RTRvbox.addWidget(self.rotinftxt)
        RTRvbox.addWidget(self.rotinp)
        RTRvbox.addWidget(self.bt_rot_save)

        #Final Settings
        self.rtrwin.setWindowTitle("Rotation Settings")
        self.rtrwin.setLayout(RTRvbox)
        self.rtrwin.show()


    
    #Blur Backend
    def Blur_Backend(self):
        self.blrwin.close()
        blrnum = int(self.blrinp.text())
        big_org_img = Image.open(self.file_name)
        big_blr_img = big_org_img.filter(ImageFilter.GaussianBlur(radius=blrnum))
        self.fin_edit_img = big_blr_img
        smol_blr_img = big_blr_img.resize((250,250), Image.LANCZOS)
        smol_blr_img.save("C:/Users/Petr/Documents/Projekty/Python/Images_&_Text_files/fasteditimg.jpg")
        pixmap = QPixmap("C:/Users/Petr/Documents/Projekty/Python/Images_&_Text_files/fasteditimg.jpg")
        self.smol_con_img.setPixmap(pixmap)
        self.bt_save.setEnabled(True)
        self.bt_con.setEnabled(True)


    #Blur Window
    def Blur_Window(self):
        self.popup.close()
        self.blrwin = QWidget()

        #Save button
        self.bt_blr_save = QPushButton("Save", self)
        self.bt_blr_save.clicked.connect(self.Blur_Backend)

        #Info Text
        self.blrinftxt = QLabel("Input numbers 1-100")
        self.blrinftxt.setAlignment(Qt.AlignCenter)

        #Blur Input
        self.blrinp = QLineEdit()
        self.blrinp.setValidator(QIntValidator(1, 100))

        #Rozložení okna
        BLRhbox = QHBoxLayout()

        BLRvbox = QVBoxLayout()
        BLRvbox.addLayout(BLRhbox)
        BLRvbox.addWidget(self.blrinftxt)
        BLRvbox.addWidget(self.blrinp)
        BLRvbox.addWidget(self.bt_blr_save)

        #Final Settings
        self.blrwin.setWindowTitle("Blur Settings")
        self.blrwin.setLayout(BLRvbox)
        self.blrwin.show()



    #Flip Sides
    def Flip_Sides(self):
        self.popup.close()
        big_org_img = Image.open(self.file_name)
        big_flip_img = big_org_img.transpose(Image.FLIP_LEFT_RIGHT)
        self.fin_edit_img = big_flip_img
        smol_flip_img = big_flip_img.resize((250,250), Image.LANCZOS)
        smol_flip_img.save("C:/Users/Petr/Documents/Projekty/Python/Images_&_Text_files/fasteditimg.jpg")
        pixmap = QPixmap("C:/Users/Petr/Documents/Projekty/Python/Images_&_Text_files/fasteditimg.jpg")
        self.smol_con_img.setPixmap(pixmap)
        self.bt_save.setEnabled(True)
        self.bt_con.setEnabled(True)

    def ToJPG(self):
        self.popup.close()
        big_org_img = Image.open(self.file_name)
        smol_org_img = big_org_img.resize((250,250), Image.LANCZOS)
        smol_org_img.save("C:/Users/Petr/Documents/Projekty/Python/Images_&_Text_files/fasteditimg.jpg")
        pixmap = QPixmap("C:/Users/Petr/Documents/Projekty/Python/Images_&_Text_files/fasteditimg.jpg")
        self.smol_con_img.setPixmap(pixmap)
        self.bt_save.setEnabled(True)
        self.bt_con.setEnabled(True)


    #Pop-Up Window s možnostmi
    def PopUpWindow(self):
        self.popup = QWidget()

        self.bt_con.setEnabled(False)

        #Button na CL->BW
        self.bt_gray = QPushButton("To B&W", self)
        self.bt_gray.clicked.connect(self.ToGray)

        #Button na Contrast
        self.bt_contrast = QPushButton("Change Contrast", self)
        self.bt_contrast.clicked.connect(self.Contrast_Window)

        #Button na Rotate
        self.bt_rotate = QPushButton("Rotate Image", self)
        self.bt_rotate.clicked.connect(self.Rotator_Window)

        #Button na FS
        self.bt_flip = QPushButton("Flip Sides", self)
        self.bt_flip.clicked.connect(self.Flip_Sides)
        
        #Button na JPG
        self.bt_jpg = QPushButton("To JPG", self)
        self.bt_jpg.clicked.connect(self.ToJPG)

        #Button na Blur
        self.bt_blur = QPushButton("Blur", self)
        self.bt_blur.clicked.connect(self.Blur_Window)


        #Rozložení okna
        POPhbox1 = QHBoxLayout()
        POPhbox1.addWidget(self.bt_gray)
        POPhbox1.addWidget(self.bt_contrast)
        POPhbox1.addWidget(self.bt_rotate)

        POPhbox2 = QHBoxLayout()
        POPhbox2.addWidget(self.bt_flip)
        POPhbox2.addWidget(self.bt_jpg)
        POPhbox2.addWidget(self.bt_blur)

        POPvbox = QVBoxLayout()
        POPvbox.addLayout(POPhbox1)
        POPvbox.addLayout(POPhbox2)

        #Finální nastavení
        self.popup.setWindowTitle("Option Selection")
        self.popup.setLayout(POPvbox)
        self.popup.show()


    #Main Window
    def __init__(self):
        super(Window, self).__init__()
        
        
        #Button na otevření obrázku
        self.bt_open = QPushButton("Open Picture", self)
        self.bt_open.clicked.connect(self.OpenIMG)

        #Button na konverzi
        self.bt_con = QPushButton("Options", self)
        self.bt_con.clicked.connect(self.PopUpWindow)
        self.bt_con.setEnabled(False)

        #Button na save
        self.bt_save = QPushButton("Save Picture", self)
        self.bt_save.clicked.connect(self.SaveIMG)
        self.bt_save.setEnabled(False)

        #Originální image
        self.smol_org_img = QLabel(self)
        self.smol_org_img.setFixedSize(250, 250)

        #Converted image 
        self.smol_con_img = QLabel(self)
        self.smol_con_img.setFixedSize(250, 250)

        #Rozložení okna
        hbox = QHBoxLayout()
        hbox.addWidget(self.bt_open)
        hbox.addWidget(self.bt_con)
        hbox.addWidget(self.bt_save)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addWidget(self.smol_org_img)
        vbox.addWidget(self.smol_con_img)
        
        #Finální nastavení
        self.setWindowTitle("Image Editor")
        self.setLayout(vbox)
        self.show()


Window = Window()
Window.show()
app.exec_()