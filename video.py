from PyQt6.QtWidgets import QFileDialog, QMessageBox
from pytube import YouTube
import os


def convert_seconds_to_minutes(seconds):
    return seconds // 60, seconds % 60


def download_single_video(self):
    url = self.entry.text()
    if not url:
        self.show_error("Error", "Please enter a valid YouTube URL.")
        return

    try:
        yt = YouTube(url)
        download_path = QFileDialog.getExistingDirectory(self, "Select Directory")
        if download_path:
            stream = yt.streams.get_highest_resolution()
            filename = stream.default_filename
            os.path.join(download_path, filename)
            stream.download(output_path=download_path)

            self.show_info("Success", f"Video downloaded successfully to {download_path}")
        else:
            self.show_warning("Warning", "Download canceled.")
    except Exception as e:
        self.show_error("Error", f"An error occurred: {str(e)}")


def preview_video(self):
    url = self.entry.text()
    if not url:
        self.show_error("Error", "Please enter a valid YouTube URL.")
        return

    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        file_path = stream.download()

        # Get video information
        title = yt.title
        duration_seconds = yt.length
        duration_minutes, remaining_seconds = convert_seconds_to_minutes(duration_seconds)

        # Open a dialog window to display video information
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Information)
        msg_box.setWindowTitle("Video Preview")
        msg_box.setText(f"Title: {title}\nDuration: {duration_minutes} minutes {remaining_seconds} seconds")
        msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg_box.exec()

        # Remove the downloaded file after viewing information
        os.remove(file_path)

        self.show_info("Success", "Video preview information displayed successfully.")
    except Exception as e:
        self.show_error("Error", f"An error occurred: {str(e)}")



