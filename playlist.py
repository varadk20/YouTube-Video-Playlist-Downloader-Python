import os
from PyQt6.QtWidgets import QFileDialog, QMessageBox
from pytube import Playlist, YouTube


def convert_seconds_to_minutes(seconds):
    return seconds // 60, seconds % 60


def download_playlist(self):
    url = self.entry.text()
    if not url:
        self.show_error("Error", "Please enter a valid YouTube playlist URL.")
        return

    try:
        playlist = Playlist(url)
        download_path = QFileDialog.getExistingDirectory(self, "Select Directory")
        if download_path:
            for video in playlist.video_urls:
                try:
                    yt = YouTube(video)
                    stream = yt.streams.get_highest_resolution()
                    filename = stream.default_filename
                    os.path.join(download_path, filename)
                    stream.download(output_path=download_path)
                except Exception as e:
                    self.show_warning("Warning", f"Error downloading {video.title}: {str(e)}")

            self.show_info("Success", f"Playlist downloaded successfully to {download_path}")
        else:
            self.show_warning("Warning", "Download canceled.")
    except Exception as e:
        self.show_error("Error", f"An error occurred: {str(e)}")


def preview_playlist(self):
    url = self.entry.text()
    if not url:
        self.show_error("Error", "Please enter a valid YouTube playlist URL.")
        return

    try:
        playlist = Playlist(url)
        playlist_info = ""
        for video_url in playlist.video_urls:
            try:
                yt = YouTube(video_url)
                title = yt.title
                duration_seconds = yt.length
                duration_minutes, remaining_seconds = convert_seconds_to_minutes(duration_seconds)
                playlist_info += f"Title: {title}\nDuration: {duration_minutes} minutes {remaining_seconds} seconds\n\n"
            except Exception as e:
                self.show_warning("Warning", f"Error accessing video information: {str(e)}")

        # Open a dialog window to display playlist information
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Information)
        msg_box.setWindowTitle("Playlist Preview")
        msg_box.setText(playlist_info)
        msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg_box.exec()

        self.show_info("Success", "Playlist preview information displayed successfully.")
    except Exception as e:
        self.show_error("Error", f"An error occurred: {str(e)}")
