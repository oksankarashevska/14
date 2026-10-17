from PyQt6.QtWidgets import QMainWindow, QFrame, QGridLayout, QVBoxLayout, QHBoxLayout, QLabel
from modules.app import app
from PyQt6.QtCore import Qt

main_window = QMainWindow()
WIDTH_WINDOW = 800
HEIGHT_WINDOW = 600

primary_screen = app.primaryScreen()
screen_size = primary_screen.size()
width_screen = screen_size.width()
height_screen = screen_size.height()

main_window.setGeometry(
    (width_screen // 2) - (WIDTH_WINDOW // 2), 
    (height_screen // 2) - (HEIGHT_WINDOW // 2), 
    WIDTH_WINDOW, HEIGHT_WINDOW)

frame_0 = QFrame(parent= main_window)
frame_0.setStyleSheet("background-color: black")
frame_0.setFixedSize(400, 200)

layout_0 = QVBoxLayout()
frame_0.setLayout(layout_0)

label_1 = QLabel(text = "SPACE CONTROL", parent = frame_0)
label_1.setStyleSheet("font-size: 30px; color: white")

layout_0.addWidget(label_1)

# layout_0.setAlignment(Qt.AlignmentFlag.AlignLeft)

frame_1 = QFrame(parent= main_window)
frame_1.setStyleSheet("background-color: black")
frame_1.setFixedSize(WIDTH_WINDOW, HEIGHT_WINDOW)

frame_2 = QFrame(parent= frame_1)
frame_2.setStyleSheet("background-color: red")
frame_2.setFixedSize(100, 100)

frame_3 = QFrame(parent= frame_1)
frame_3.setStyleSheet("background-color: green")
frame_3.setFixedSize(100, 100)

frame_4 = QFrame(parent= frame_1)
frame_4.setStyleSheet("background-color: blue")
frame_4.setFixedSize(100, 100)

frame_5 = QFrame(parent= frame_1)
frame_5.setStyleSheet("background-color: grey")
frame_5.setFixedSize(400, 200)

label_2 = QLabel(text = "SYSTEM ONLINE", parent = frame_5)
label_2.setStyleSheet("font-size: 20px; color: white")

frame_6 = QFrame(parent= frame_1)
frame_6.setStyleSheet("background-color: white")
frame_6.setFixedSize(400, 60)

label_3 = QLabel(text = "ENGINE  RADAR  NAVIGATION", parent = frame_6)
label_3.setStyleSheet("font-size: 10px;  color: black")

main_layout = QVBoxLayout()
frame_1.setLayout(main_layout)

main_layout.setContentsMargins(0, 0, 0, 0)
main_layout.setSpacing(0) 

main_layout.setAlignment(Qt.AlignmentFlag.AlignBottom)

layout_kvadrat = QHBoxLayout()
layout_kvadrat.setContentsMargins(100, 10, 0, 10) 
layout_kvadrat.setSpacing(120) 

layout_kvadrat.addWidget(frame_2) 
layout_kvadrat.addWidget(frame_4) 
layout_kvadrat.addWidget(frame_3) 
main_layout.addWidget(frame_0)     
main_layout.addWidget(frame_5)  
main_layout.addLayout(layout_kvadrat)
main_layout.addWidget(frame_6) 

