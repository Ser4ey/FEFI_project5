from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QVBoxLayout, QWidget, QPushButton

def on_button_click():
    text = line_edit.text()  # Получаем текст из QLineEdit
    print(f"Введен текст: {text}")

app = QApplication([])

window = QMainWindow()
central_widget = QWidget()
window.setCentralWidget(central_widget)
layout = QVBoxLayout(central_widget)

line_edit = QLineEdit()
layout.addWidget(line_edit)

button = QPushButton("Получить текст")
button.clicked.connect(on_button_click)  # Соединяем сигнал clicked с обработчиком

layout.addWidget(button)

window.show()

app.exec()