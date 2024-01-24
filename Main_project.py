import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QColorDialog, QInputDialog
from PyQt5.QtGui import QPainter, QPen, QPixmap, QColor, QIcon
from PyQt5.QtCore import Qt, QPoint
from PIL import Image
import sqlite3
from project import Ui_Paint


class Paint(QMainWindow, Ui_Paint):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.connection = sqlite3.connect('history_drawings.sqlite')
        cur = self.connection.cursor()
        cur.execute('''DELETE FROM draws''')

        self.can_draw = False
        self.eraser_on = False
        self.canvas_color_const = False
        self.file_name, self.w, self.h = None, None, None

        self.pen_width = 5
        self.pen_color = QColor(0, 0, 0)
        self.canvas_color = QColor(255, 255, 255)

        canvas = Image.new('RGB', (self.size().width(), self.size().height()), self.canvas_color.getRgb())
        canvas.save('picture.png')
        self.canvas = QPixmap('picture.png')

        self.drawings = []
        self.pen_options = []
        self.bd_pen_options = []
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Paint')
        self.setWindowIcon(QIcon('paint_logo.png'))

        self.btn_pen_color.clicked.connect(self.set_pen_color)
        self.btn_pen_color.setShortcut("Ctrl+P")
        self.btn_canvas_color.clicked.connect(self.set_canvas_color)
        self.btn_canvas_color.setShortcut("Ctrl+C")

        self.btn_set_image.clicked.connect(self.set_image)
        self.btn_set_image.setShortcut("Ctrl+K")
        self.btn_pen_width.clicked.connect(self.set_pen_width)
        self.btn_pen_width.setShortcut("Ctrl+W")

        self.btn_eraser_width.clicked.connect(self.set_eraser_width)
        self.btn_eraser_width.setShortcut("Ctrl+E")
        self.btn_eraser.clicked.connect(self.set_eraser)
        self.btn_eraser.setShortcut("Ctrl+L")

        self.btn_back.clicked.connect(self.back)
        self.btn_back.setShortcut("Ctrl+Z")
        self.btn_forward.clicked.connect(self.forward)
        self.btn_forward.setShortcut("Ctrl+Right")

        self.btn_clear.clicked.connect(self.clear_canvas)
        self.btn_return.clicked.connect(self.return_drawing)

        self.btn_save.clicked.connect(self.save_image)
        self.btn_save.setShortcut("Ctrl+S")

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), self.canvas)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            if self.w:
                canvas = Image.open('picture.png')
                im = Image.open(self.file_name)
                im = im.resize((int(self.w), int(self.h)))
                self.file_name, self.w, self.h = None, None, None

                canvas.paste(im, (event.pos().x(), event.pos().y()))
                canvas.save('picture.png')
                self.canvas = QPixmap('picture.png')

            canvas = Image.open('picture.png')
            canvas = canvas.resize((self.size().width(), self.size().height()))
            canvas.save('picture.png')
            self.canvas = QPixmap('picture.png')

            painter = QPainter(self.canvas)
            for i in range(len(self.drawings)):
                painter.setPen(self.pen_options[i])
                for coords in self.drawings[i]:
                    painter.drawLine(*coords)
            self.update()

            self.drawings.append([])
            self.can_draw = True
            self.last_point = event.pos()

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.LeftButton and self.can_draw:
            painter = QPainter(self.canvas)
            painter.setPen(QPen(self.pen_color, self.pen_width, Qt.SolidLine))
            painter.drawLine(self.last_point, event.pos())

            self.drawings[-1].append((self.last_point, event.pos()))
            self.last_point = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton and self.can_draw:
            self.pen_options.append(QPen(self.pen_color, self.pen_width, Qt.SolidLine))
            self.can_draw = False

    def set_pen_color(self):
        if self.eraser_on:
            self.set_eraser()
        color = QColorDialog.getColor()
        if color.isValid():
            self.pen_color = color
            self.btn_pen_color.setStyleSheet(
                '''background-color: rgb{}; border-radius: 30px;'''.format(color.getRgb()[:3]))

    def set_canvas_color(self):
        if not self.canvas_color_const:
            color = QColorDialog.getColor()
            if color.isValid():
                self.canvas_color = color
                canvas = Image.new('RGB', (self.size().width(), self.size().height()), self.canvas_color.getRgb())
                canvas.save('picture.png')
                self.canvas = QPixmap('picture.png')

                painter = QPainter(self.canvas)
                for i in range(len(self.drawings)):
                    painter.setPen(self.pen_options[i])
                    for coords in self.drawings[i]:
                        painter.drawLine(*coords)
                self.btn_canvas_color.setStyleSheet(
                    '''background-color: rgb{}; border-radius: 30px;'''.format(color.getRgb()[:3]))
                self.update()

    def set_pen_width(self):
        if self.eraser_on:
            self.set_eraser()
        width, ok_pressed = QInputDialog.getInt(self, "Pen", "Enter pen width:", self.pen_width, 1, 100, 1)
        if ok_pressed:
            self.pen_width = width
            self.btn_pen_width.setText(str(self.pen_width))

    def set_eraser_width(self):
        if self.eraser_on:
            width, ok_pressed = QInputDialog.getInt(self, "Pen", "Enter pen width:", self.pen_width, 1, 100, 1)
            if ok_pressed:
                self.pen_width = width
                self.btn_eraser_width.setText(str(self.pen_width))

    def set_eraser(self):
        if not self.eraser_on:
            if self.canvas_color_const:
                self.pen_parameters = (self.pen_width, self.pen_color)
                self.pen_width, self.pen_color = 50, self.canvas_color
                self.eraser_on = True
            else:
                answer, ok_pressed = QInputDialog.getItem(self, "Ластик", "Вы больше не сможете изменять цвет холста",
                                                          ("Продолжить", "Отмена"), 0, False)
                if ok_pressed:
                    if answer == 'Продолжить':
                        self.pen_parameters = (self.pen_width, self.pen_color)
                        self.pen_width, self.pen_color = 50, self.canvas_color
                        self.canvas_color_const = True
                        self.eraser_on = True
        else:
            self.pen_width, self.pen_color = self.pen_parameters
            self.eraser_on = False

    def set_image(self):
        if self.canvas_color_const:
            self.file_name = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '',
                                                         'Все файлы (*);;Картинка (*.jpg);;Картинка (*.png)')[0]
            if self.file_name:
                im_size, ok_pressed = QInputDialog.getText(self, "Картинка",
                                                           '''Введите размер картинки в формате: ширина, высота
После нажмите на экране туда, где хотите разместить картинку''')
                if ok_pressed:
                    self.w, self.h = im_size.split(',')[0], im_size.split(',')[1]
        else:
            answer, ok_pressed = QInputDialog.getItem(self, "Картинка", "Вы больше не сможете изменять цвет холста",
                                                      ("Продолжить", "Отмена"), 0, False)
            if ok_pressed:
                self.canvas_color_const = True
                self.file_name = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '',
                                                             'Все файлы (*);;Картинка (*.jpg);;Картинка (*.png)')[0]
                if self.file_name:
                    im_size, ok_pressed = QInputDialog.getText(self, "Картинка",
                                                               '''Введите размер картинки в формате: ширина, высота
После нажмите на экране туда, где хотите разместить картинку''')
                    if ok_pressed:
                        self.w, self.h = im_size.split(',')[0], im_size.split(',')[1]

    def back(self):
        if self.drawings:
            d = []
            for cords in self.drawings[-1]:
                x1, y1, x2, y2 = cords[0].x(), cords[0].y(), cords[1].x(), cords[1].y()
                lines = f'{x1},{y1},{x2},{y2}'
                d.append(lines)
            d = ';;;'.join(d)

            query = f"INSERT INTO draws(drawings) VALUES ('{d}')"
            cur = self.connection.cursor()
            cur.execute(query)
            self.connection.commit()

            self.bd_pen_options.append(self.pen_options[-1])
            del self.drawings[-1]
            del self.pen_options[-1]

            self.canvas = QPixmap('picture.png')
            painter = QPainter(self.canvas)
            for i in range(len(self.drawings)):
                painter.setPen(self.pen_options[i])
                for coords in self.drawings[i]:
                    painter.drawLine(*coords)
            self.update()

    def forward(self):
        cur = self.connection.cursor()
        d = cur.execute('SELECT drawings FROM draws').fetchall()
        if d and self.bd_pen_options:
            d = d[-1][0].split(';;;')
            a = []
            for cords in d:
                x1, y1, x2, y2 = [int(i) for i in cords.split(',')]
                line = (QPoint(x1, y1), QPoint(x2, y2))
                a.append(line)

            self.drawings.append(a)
            self.pen_options.append(self.bd_pen_options[-1])
            del self.bd_pen_options[-1]
            cur.execute('''DELETE FROM draws 
            WHERE id = (SELECT MAX(id) FROM draws);''')
            self.connection.commit()

            self.canvas = QPixmap('picture.png')
            painter = QPainter(self.canvas)
            for i in range(len(self.drawings)):
                painter.setPen(self.pen_options[i])
                for coords in self.drawings[i]:
                    painter.drawLine(*coords)
            self.update()

    def clear_canvas(self):
        if self.drawings:
            cur = self.connection.cursor()
            cur.execute('DELETE FROM draws')
            self.connection.commit()
            for draw in self.drawings:
                d = []
                for cords in draw:
                    x1, y1, x2, y2 = cords[0].x(), cords[0].y(), cords[1].x(), cords[1].y()
                    lines = f'{x1},{y1},{x2},{y2}'
                    d.append(lines)
                d = ';;;'.join(d)

                query = f"INSERT INTO draws(drawings) VALUES ('{d}')"
                cur.execute(query)
                self.connection.commit()

            self.bd_pen_options = self.pen_options[:]
            self.drawings.clear()
            self.pen_options.clear()
            self.canvas = QPixmap('picture.png')
            self.update()

    def return_drawing(self):
        cur = self.connection.cursor()
        d = cur.execute('SELECT drawings FROM draws').fetchall()

        if d and self.bd_pen_options:
            for i in d:
                i = i[0].split(';;;')
                a = []
                for cords in i:
                    x1, y1, x2, y2 = [int(i) for i in cords.split(',')]
                    line = (QPoint(x1, y1), QPoint(x2, y2))
                    a.append(line)
                self.drawings.append(a)

            self.pen_options += self.bd_pen_options[:]
            self.bd_pen_options.clear()
            cur.execute('DELETE FROM draws')
            self.connection.commit()

            self.canvas = QPixmap('picture.png')
            painter = QPainter(self.canvas)
            for i in range(len(self.drawings)):
                painter.setPen(self.pen_options[i])
                for coords in self.drawings[i]:
                    painter.drawLine(*coords)
            self.update()

    def save_image(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Сохранить рисунок", "", "PNG (*.png);;JPEG (*.jpg *.jpeg)")
        if file_path:
            self.canvas.save(file_path)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Paint()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
