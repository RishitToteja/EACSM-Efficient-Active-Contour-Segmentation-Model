import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog
from PyQt5.QtGui import QPixmap, QPainter, QPen
from PyQt5.QtCore import Qt
import segment
import pandas as pd

class CreateDatasetWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Create Dataset")
        self.current_index = 0
        self.images = []
        self.pointsLeft = []
        self.pointsRight = []
        self.side = 0
        self.df = pd.DataFrame(
            columns=["Patient_No", "Point1", "Point2", "Point3", "Point4", "Point5", "Point6", "Point7", "Point8",
                     "Point9", "Point10", "Point11", "Point12"])

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        self.image_label = QLabel(self)
        layout.addWidget(self.image_label)

        self.select_images_btn = QPushButton("Select Images", self)
        self.select_images_btn.clicked.connect(self.select_images)
        layout.addWidget(self.select_images_btn)

        self.next_btn = QPushButton("Next", self)
        self.next_btn.clicked.connect(self.next_image)
        layout.addWidget(self.next_btn)

        self.segment_btn = QPushButton("Segment", self)
        self.segment_btn.clicked.connect(self.segment)
        layout.addWidget(self.segment_btn)
        self.segment_btn.hide()

        self.otherSideBtn = QPushButton("Mark Points for Other Side", self)
        self.otherSideBtn.clicked.connect(self.otherSide)
        layout.addWidget(self.otherSideBtn)
        self.otherSideBtn.hide()

        self.toCsvBtn = QPushButton("Generate Dataset in CSV", self)
        self.toCsvBtn.clicked.connect(self.dataToCsv)
        layout.addWidget(self.toCsvBtn)
        self.toCsvBtn.hide()


    def select_images(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFiles)
        file_dialog.setNameFilter("Images (*.png *.jpg *.jpeg)")
        if file_dialog.exec_():
            selected_files = file_dialog.selectedFiles()
            self.images = selected_files
            self.show_image()
            self.select_images_btn.hide()
            self.segment_btn.show()
            self.otherSideBtn.show()
            self.toCsvBtn.show()

    def show_image(self):
        if self.images:
            image_path = self.images[self.current_index]
            self.image_label.setPixmap(QPixmap(image_path).scaled(612, 733))
            self.image_label.mousePressEvent = self.getPos

    def getPos(self, event):
        x = event.pos().x()
        y = event.pos().y()

        if(self.side==1):
            self.pointsRight.append((x, y))
        else:
            self.pointsLeft.append((x, y))

        self.plot_points(x, y)

    def plot_points(self, x, y):
        pixmap = self.image_label.pixmap()
        if pixmap:
            image = pixmap.toImage()
            if x >= 0 and x < image.width() and y >= 0 and y < image.height():
                # Draw 'x' mark on the image
                painter = QPainter(pixmap)
                painter.setPen(QPen(Qt.red, 2))  # Set pen color and width
                painter.drawLine(x - 5, y, x + 5, y)  # Draw horizontal line
                painter.drawLine(x, y - 5, x, y + 5)  # Draw vertical line
                painter.end()

                # Update the image label with the modified pixmap
                self.image_label.setPixmap(pixmap)

    def next_image(self):
        print("Current INDEX IS - {}".format(self.current_index))
        self.current_index += 1
        if(self.current_index>=len(self.images)):
            self.dataToCsv()
        self.show_image()
        self.side=0
        self.pointsLeft = []
        self.pointsRight = []

    def segment(self):
        image_path = self.images[self.current_index]
        pno = "segmented_img_{}".format(self.current_index)
        output_pth = "segmented_imgs/"+pno+".jpg"
        print(self.images)
        self.images.insert(self.current_index+1, output_pth)
        print(self.images)

        boundaryPoints = segment.getContour(self.pointsLeft, self.pointsRight, image_path, output_pth)
        p_no = "segmented_img_{}"
        self.df.loc[self.current_index] = [pno] + boundaryPoints


    def otherSide(self):
        self.side = 1
        self.image_label.clear()  # Clear the image_label
        self.show_image()  # Re-display the image without the red marks

    def dataToCsv(self):
        self.df.to_csv("dataset.csv")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CreateDatasetWindow()
    window.show()
    sys.exit(app.exec_())
