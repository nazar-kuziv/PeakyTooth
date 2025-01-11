import os
import shutil

from PySide6.QtCore import QSize, QMargins
from PySide6.QtGui import QPainter, QPageLayout, Qt
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

        self.buttons_layout = QHBoxLayout()
        self.buttons = QWidget(self)
        self.buttons.setFixedHeight(60)
        self.buttons_layout.addStretch(1)
        self.buttons.setLayout(self.buttons_layout)
        self.main_layout.addWidget(self.buttons)

        self.send_button = ButtonBase('Send to patient')
        self.send_button.clicked.connect(self.ask_patient_again_about_sending)
        self.send_button.setFixedWidth(120)
        # noinspection PyUnresolvedReferences
        self.buttons_layout.addWidget(self.send_button, alignment=Qt.AlignRight)

        self.printer_button = ButtonBase('Print Pdf')
        self.printer_button.clicked.connect(self.print_pdf)
        self.printer_button.setFixedWidth(140)
        # noinspection PyUnresolvedReferences
        self.buttons_layout.addWidget(self.printer_button, alignment=Qt.AlignRight)

        self.save_as_button = ButtonBase('Save')
        self.save_as_button.clicked.connect(self.save_pdf)
        self.save_as_button.setFixedWidth(160)
        # noinspection PyUnresolvedReferences
        self.buttons_layout.addWidget(self.save_as_button, alignment=Qt.AlignRight)

        if self.show_pdf() is None:
            self.show_error('Can not create pdf')
            self.deleteLater()
            return

        self.show()

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
        file_name = QFileDialog.getSaveFileName(self, "Save as", os.path.expanduser('~') + "/Documents/",
                                                "Pdf Files (*.pdf)")
        if file_name[0]:
            try:
                shutil.copyfile(self.pdf_file_path, file_name[0])
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
        QMessageBox.critical(self, 'Error', error)

    def show_success(self, message):
        QMessageBox.information(self, 'Success', message)