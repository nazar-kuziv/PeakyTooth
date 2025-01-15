import os
import shutil

from PySide6.QtCore import QSize, QMargins
from PySide6.QtGui import QPainter, QPageLayout
from PySide6.QtPdf import QPdfDocument, QPdfDocumentRenderOptions
from PySide6.QtPdfWidgets import QPdfView
from PySide6.QtPrintSupport import QPrinter, QPrintDialog
from PySide6.QtWidgets import QWidget, QVBoxLayout, QMessageBox, QDialog, QHBoxLayout, QFileDialog

from controller.controller_pdf import ControllerPdf
from view.widget.button_base import ButtonBase


class ScreenPdf(QWidget):
    def __init__(self, appointment_id):
        super().__init__()

        self.appointment_id = appointment_id

        try:
            self.controller = ControllerPdf(self, appointment_id)
        except Exception as e:
            print(f'An error occurred while creating controller: {str(e)}')
            self.show_error('Can not create pdf')
            self.deleteLater()
            return

        self.setWindowTitle('Appointment PDF')
        self.setMinimumSize(950, 750)

        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(20, 20, 20, 20)
        self.main_layout.setSpacing(15)

        # Layout na przyciski
        self.buttons_layout = QHBoxLayout()
        self.buttons_layout.setContentsMargins(0, 0, 0, 0)  # Brak dodatkowych marginesów
        self.buttons_layout.setSpacing(10)  # Minimalny odstęp między przyciskami

        # Przycisk "Send to Patient"
        self.send_button = ButtonBase('Send to Patient')
        self.send_button.setFixedSize(140, 40)
        self.send_button.setStyleSheet("""
            QPushButton {
                background-color: #007ACC;
                color: white;
                border-radius: 5px;
                font-weight: bold;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #005A9E;
            }
            QPushButton:pressed {
                background-color: #004080;
            }
        """)
        self.send_button.clicked.connect(self.ask_patient_again_about_sending)
        self.buttons_layout.addWidget(self.send_button)

        # Przycisk "Print PDF"
        self.printer_button = ButtonBase('Print PDF')
        self.printer_button.setFixedSize(140, 40)
        self.printer_button.setStyleSheet("""
            QPushButton {
                background-color: #28A745;
                color: white;
                border-radius: 5px;
                font-weight: bold;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #218838;
            }
            QPushButton:pressed {
                background-color: #1E7E34;
            }
        """)
        self.printer_button.clicked.connect(self.print_pdf)
        self.buttons_layout.addWidget(self.printer_button)

        # Przycisk "Save PDF"
        self.save_as_button = ButtonBase('Save PDF')
        self.save_as_button.setFixedSize(140, 40)
        self.save_as_button.setStyleSheet("""
            QPushButton {
                background-color: #FF8C00;
                color: white;
                border-radius: 5px;
                font-weight: bold;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #FF7F50;
            }
            QPushButton:pressed {
                background-color: #CD5B45;
            }
        """)
        self.save_as_button.clicked.connect(self.save_pdf)
        self.buttons_layout.addWidget(self.save_as_button)

        # Dodanie przycisków do głównego layoutu
        self.main_layout.addLayout(self.buttons_layout, stretch=0)

        if self.show_pdf() is None:
            self.show_error('Can not create pdf')
            self.deleteLater()
            return

    def show_pdf(self):
        try:
            self.pdf_file_path = self.controller.get_pdf_path()
        except Exception as e:
            print(f'An error occurred while showing pdf: {str(e)}')
            self.show_error('Can not create pdf')
            self.deleteLater()
            return None

        self.documentPDF = QPdfDocument()
        self.documentPDF.load(self.pdf_file_path)
        self.viewPDF = QPdfView()
        self.viewPDF.setPageMode(QPdfView.PageMode.MultiPage)
        self.viewPDF.setDocument(self.documentPDF)
        self.viewPDF.setStyleSheet("""
            QPdfView {
                border: 1px solid #ddd;
                background-color: #f2f2f2;
            }
        """)
        self.main_layout.addWidget(self.viewPDF)

        return True

    def print_pdf(self):

        # noinspection PyUnresolvedReferences
        printer = QPrinter(QPrinter.HighResolution)

        printer.setFullPage(True)
        # noinspection PyUnresolvedReferences
        printer.setPageMargins(QMargins(0, 0, 0, 0), QPageLayout.Millimeter)
        prev_dial = QPrintDialog(printer)

        # noinspection PyUnresolvedReferences
        if prev_dial.exec_() == QDialog.Accepted:
            painter = QPainter(printer)
            options = QPdfDocumentRenderOptions()
            # noinspection PyUnresolvedReferences
            target_rect = printer.pageRect(QPrinter.DevicePixel)
            image_size = QSize(int(target_rect.width()), int(target_rect.height()))
            document_pdf = QPdfDocument()
            document_pdf.load(self.pdf_file_path)
            image = document_pdf.render(0, image_size, options)
            painter.drawImage(target_rect, image)
            painter.end()

    def save_pdf(self):
        file_name = QFileDialog.getSaveFileName(self, "Save as", os.path.expanduser('~') + "/Documents/", "Pdf Files (*.pdf)")
        if file_name[0]:
            try:
                shutil.copyfile(self.pdf_file_path, file_name[0])
                self.show_success("PDF saved successfully.")
            except Exception as e:
                print(f'An error occurred while saving the pdf: {str(e)}')
                self.show_error('Can not save pdf')

    def ask_patient_again_about_sending(self):
        # noinspection PyUnresolvedReferences
        reply = QMessageBox.question(self, 'Send PDF', 'Do you want to send the PDF to the patient?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        # noinspection PyUnresolvedReferences
        if reply == QMessageBox.Yes:
            self.controller.send_pdf_to_patient()

    def show_error(self, error):
        QMessageBox.critical(self, 'Error', str(error))

    def show_success(self, message):
        QMessageBox.information(self, 'Success', message)
