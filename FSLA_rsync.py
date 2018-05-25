import sys
import os
import subprocess
from PyQt5.QtWidgets import QMainWindow, QApplication,QFileDialog,QMessageBox,QInputDialog,QLineEdit
from FSLA_rsyncGUI import Ui_MainWindow


from paramiko import SSHClient
from paramiko_expect import SSHClientInteraction
import paramiko
import getpass




PROMPT = ".*\$\s+"


class AppWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        self.ui.UserName_LineEdit.setText(os.getlogin())
        #activator for S_P button? 
        self.ui.S_P_Button01.clicked.connect(lambda: self.browse_file(self.ui.S_P_LineEdit01))
        self.ui.D_P_Button01.clicked.connect(lambda: self.browse_dest(self.ui.D_P_LineEdit01))
        self.ui.pushButton_3.clicked.connect(lambda: self.ssh_and_rsync())

    def browse_file(self,path):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')
        if fname[0]:
            self.ui.S_P_LineEdit01.setText(fname[0])

    def browse_dest(self,path):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')
        if fname[0]:
            self.ui.D_P_LineEdit01.setText(fname[0])
        
   
    def create_command(self):
        sourcePath = self.ui.S_P_LineEdit01.text()
        destPath = self.ui.D_P_LineEdit01.text()
        username = self.ui.UserName_LineEdit.text()
        destLocation = self.ui.D_M_01.currentText()
        source = sourcePath

        self.testPath(sourcePath)
        self.testPath(destPath)

        dest = username + "@" + destLocation + ":" + destPath
        command = ("rsync -rpvgotP" + " " + source + " " + dest)
        self.warningPopup(command)
        return command

    def testPath(self, path):
        path = str(path)
        for i in range (0, len(path)):
            value = int(ord(path[i]))
            if value != 95 and (value < 45 or (value > 57 and value < 65) or (value > 90 and value < 97) or value >127):
                self.warningPopup("Invalid Characters found!")

    def warningPopup(self,msg):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setInformativeText(msg)
        msgBox.exec()

    def commPopup(self,msg):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setInformativeText(msg)
        msgBox.exec()

    def ssh_and_rsync(self):
        command = self.create_command()
        sourceComp = self.ui.S_M_01.currentText()
        user = self.ui.UserName_LineEdit.text()
        userPass, okay = QInputDialog.getText(self,'Password','Enter your password',QLineEdit.Password)
        client = SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.client.AutoAddPolicy())
        print (str(sourceComp))

        try:
            client.connect( str(sourceComp), username=str(user), password=str(userPass))

            with SSHClientInteraction(client) as interact:
                interact.expect(PROMPT)

                interact.send(command)
                interact.expect(PROMPT)
                cmd_output_uname = interact.current_output_clean
                print(cmd_output_uname)

                client.close()
        except:
            self.warningPopup("Something went wrong when connecting. Make sure you entered your credentials correctly.")


def main():
    app = QApplication(sys.argv)
    w = AppWindow()
    w.show()
    sys.exit(app.exec_())

if __name__ == '__main__':            
    main()                              



