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
        self.ui.S_P_Button01.clicked.connect(lambda: self.browse_file(self.ui.S_P_LineEdit01))
        self.ui.pushButton_3.clicked.connect(lambda: self.ssh_and_rsync())

    def browse_file(self,path):
        directory =  QFileDialog.getOpenFileName(self,"Pick A Directory")
        if directory:
            try:
                path.setText(directory)
            except:
                pass

    def create_command(self):
        sourcePath = self.ui.S_P_LineEdit01.text()
        destPath = self.ui.D_P_LineEdit01.text()
        username = self.ui.UserName_LineEdit.text()
        destLocation = self.ui.D_M_01.currentText()
        source = sourcePath
        dest = username + "@" + destLocation + ":" + destPath
        command = ("rsync -rpvgotP" + " " + source + " " + dest)
        return command

    def ssh_and_rsync(self):
        command = self.create_command()
        sourceComp = self.ui.S_M_01.currentText()
        user = self.ui.UserName_LineEdit.text()
        userPass, okay = QInputDialog.getText(self,'Password','Enter your password',QLineEdit.Password)
        client = SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.client.AutoAddPolicy())
        print (str(sourceComp))
        client.connect( str(sourceComp), username=str(user), password=str(userPass))

        with SSHClientInteraction(client) as interact:
            interact.expect(PROMPT)

            interact.send(command)
            interact.expect(PROMPT)
            cmd_output_uname = interact.current_output_clean
            print(cmd_output_uname)

            client.close()



def main():
    app = QApplication(sys.argv)
    w = AppWindow()
    w.show()
    sys.exit(app.exec_())

if __name__ == '__main__':            
    main()                              



