import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QMessageBox


class MainWindow(QtWidgets.QMainWindow):
    from video import download_single_video, preview_video
    from playlist import download_playlist, preview_playlist

    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('mainwindow.ui', self)

        self.download_single_button.clicked.connect(self.download_single_video)
        self.download_playlist_button.clicked.connect(self.download_playlist)
        self.preview_button.clicked.connect(self.preview_video)
        self.preview_playlist_button.clicked.connect(self.preview_playlist)

    def show_error(self, title, message):
        self.show_message_box(QMessageBox.Icon.Critical, title, message)

    def show_warning(self, title, message):
        self.show_message_box(QMessageBox.Icon.Warning, title, message)

    def show_info(self, title, message):
        self.show_message_box(QMessageBox.Icon.Information, title, message)

    def show_message_box(self, icon, title, message):
        msg_box = QMessageBox()
        msg_box.setIcon(icon)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)

        # Set a specific style sheet for the message box
        msg_box.setStyleSheet("QMessageBox { background-color: white; }")

        msg_box.exec()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())
