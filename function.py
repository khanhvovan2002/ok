from main import*

class UIFunctions(MainWindow):
    def toggleMenu(self, maxWidth, enable):
        if enable:
            width = self.ui.Left_Menu.width()
            maxExtend = maxWidth
            standard = 60

            if width == 60:
                widthExtended = maxExtend
            else:
                widthExtended = standard


            self.animation = QPropertyAnimation(self.ui.Left_Menu, b"minimumWidth")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.start()
            
