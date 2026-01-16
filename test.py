import sys
import shutil
import os
from pathlib import Path
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, 
                             QVBoxLayout, QWidget, QFileDialog, QMessageBox)

class ImportWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Importateur de Fichiers")
        self.resize(300, 150)

        # Configuration du dossier de destination
        self.dossier_destination = Path("./imports")
        self.dossier_destination.mkdir(exist_ok=True) # Crée le dossier s'il n'existe pas

        # Interface
        self.bouton_import = QPushButton("Importer des fichiers")
        self.bouton_import.clicked.connect(self.importer_fichiers)

        layout = QVBoxLayout()
        layout.addWidget(self.bouton_import)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def importer_fichiers(self):
        from PySide6.QtWidgets import QFileDialog, QApplication
        import sys
        dialog = QFileDialog()
        dialog.setWindowTitle("Sélectionner fichiers ou dossiers")
        dialog.setFileMode(QFileDialog.Directory) # Permet de sélectionner des dossiers
        dialog.setOption(QFileDialog.DontUseNativeDialog, True) # Utilise l'interface Qt (plus flexible)

        # Cette option permet de sélectionner n'importe quel élément dans la vue
        if dialog.exec():
            selections = dialog.selectedFiles()
            print(f"Éléments sélectionnés : {selections}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImportWindow()
    window.show()
    sys.exit(app.exec())