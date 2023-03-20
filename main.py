import sys
from PyQt5.QtCore import  Qt
from PyQt5.QtGui import QPainter, QPen,QCursor
from PyQt5.QtWidgets import QApplication, QMainWindow
from screeninfo import get_monitors


class Canvas(QMainWindow):
    def __init__(self):
        super().__init__()
        self.drawing = False
        self.clear=False
        self.initUI()
        self.line=[]
        self.start_pos=[0,0]
        self.end_pos=[0,0]


    def initUI(self):
        self.monitor = get_monitors()[0]
        # self.setCursor(Qt.WaitCursor)
        self.resize(self.monitor.width, self.monitor.height)
        self.setWindowFlags(Qt.FramelessWindowHint)
        # window的bug问题 导致的如果使用WA_TranslucentBackground的话一定是需要FramelessWindowHint 否则会出现窗口黑屏的问题
        self.setAttribute(Qt.WA_TranslucentBackground)

    def paintEvent(self,event):
        if self.drawing==True:
            painter = QPainter(self)
            # 开始绘制
          #  print("kaishi huitu")
            painter.begin(self)
            # 设置画笔颜色
            pen=QPen()
            pen.setColor(Qt.red)  # 设置画笔颜色为红色
            pen.setStyle(Qt.SolidLine)  # 设置画笔颜色为正常直线
            pen.setWidth(10)  # 设置画笔宽度
            painter.setPen(pen)

            # 设置绘制内容、绘制区域、对齐方式
            ## 窗口大小

            y1=self.start_pos[1]
            y2= self.end_pos[1]

            y_end=y1+(y2-y1)/0.236

            y3=y1+(y_end-y1)*0.382
            y4=y1+(y_end-y1)*0.5
            y5=y1+(y_end-y1)*0.618
            y6=y1+(y_end-y1)*0.786

            for i in (y1,y2,y3,y4,y5,y6,y_end):
                painter.drawLine(0, round(i), self.monitor.width,round(i))
              #  print(i)
            ## 这里是逐点绘制

            # 结束绘制

            painter.end()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_S:
            self.start_pos[0]=            QCursor.pos().x()
            self.start_pos[1]=            QCursor.pos().y()
          #  print(self.start_pos)
            self.update()

        if event.key() == Qt.Key_E:
            self.end_pos[0]=            QCursor.pos().x()
            self.end_pos[1]=            QCursor.pos().y()
          #  print(self.end_pos)
            self.update()

        if event.key()== Qt.Key_P:
            self.drawing=True
            self.update()

        if event.key()== Qt.Key_C:
            self.drawing=False
            self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Canvas()
    window.show()
    sys.exit(app.exec_())
