"""
File: my_drawing.py
Name: Philip Kuo
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect, GPolygon, GLine, GLabel, GArc
from campy.graphics.gwindow import GWindow


def main():
    """
    Title: Brain explosion
    這是一個GArc地獄，原本想畫一個想code想到頭腦爆炸的畫面，畫完才發現使用太多GLine導致無法上色索性放棄
    """
    window = GWindow(width=1500, height=843.75, title='Brain explosion')
    head_ur = GArc(700, 700, 0, 90, x=600, y=200)
    # head_ur.filled = True
    # head_ur.fill_color = 'navy'
    window.add(head_ur)
    head_ul = GArc(800, 800, 90, 90, x=580, y=200)
    # head_ul.filled = True
    # head_ul.fill_color = 'navy'
    window.add(head_ul)
    head_lr = GArc(1000, 1200, 270, 90, x=450, y=75)
    # head_lr.filled = True
    # head_lr.fill_color = 'navy'
    window.add(head_lr)
    chin = GArc(120, 90, 180, 120, x=635, y=633, )
    # chin.filled = True
    # chin.fill_color = 'navy'
    window.add(chin)
    nose_up_line = GLine(580, 400, 590, 405)
    window.add(nose_up_line)
    nose_up_arc = GArc(150, 150, 320, 130, x=550, y=405, )
    window.add(nose_up_arc)
    nose_mid_line = GLine(593, 551, 617, 505)
    window.add(nose_mid_line)
    nose_low_arc = GArc(20, 20, 120, 160, x=590, y=550, )
    window.add(nose_low_arc)
    nose_low_line = GLine(597, 569, 670, 569)
    window.add(nose_low_line)
    face_up = GArc(650, 650, 168, 53, x=590, y=300)
    window.add(face_up)
    face_low = GLine(610, 570, 635, 657)
    window.add(face_low)
    ear_low = GArc(600, 600, 290, 70, x=760, y=280)
    window.add(ear_low)
    ear_up = GArc(60, 100, 20, 170, x=901, y=402)
    window.add(ear_up)
    eye_right_up = GArc(38, 20, 340, 150, x=585, y=420)
    window.add(eye_right_up)
    eye_right_low = GArc(40, 20, 160, 160, x=590, y=426)
    window.add(eye_right_low)
    eye_left_up = GArc(200, 200, 30, 70, x=640, y=440)
    window.add(eye_left_up)
    eye_left_low = GArc(150, 150, 210, 70, x=680, y=420)
    window.add(eye_left_low)
    eye_lower_left = GArc(600, 600, 210, 35, x=670, y=360)
    window.add(eye_lower_left)
    eye_lower_right = GArc(600, 600, 300, 30, x=520, y=360)
    window.add(eye_lower_right)
    mouth_up = GLine(630, 600, 690, 610)
    window.add(mouth_up)
    mouth_mid = GArc(200, 30, 180, 90, x=630, y=600)
    window.add(mouth_mid)
    mouth_low = GLine(640, 620, 670, 625)
    window.add(mouth_low)
    brain1 = GOval(10, 10, x=680, y=330)
    window.add(brain1)
    brain2 = GOval(30, 30, x=680-10, y=330-10)
    window.add(brain2)
    brain3 = GOval(50, 50, x=680 - 20, y=330 - 20)
    window.add(brain3)
    brain4 = GOval(70, 70, x=680 - 30, y=330 - 30)
    window.add(brain4)
    brain5 = GOval(90, 90, x=680 - 40, y=330 - 40)
    window.add(brain5)
    brain6 = GOval(110, 110, x=680 - 50, y=330 - 50)
    window.add(brain6)
    brain7 = GOval(130, 130, x=680 - 60, y=330 - 60)
    window.add(brain7)
    brain8 = GOval(150, 150, x=680 - 70, y=330 - 70)
    window.add(brain8)
    brain9 = GOval(170, 170, x=680 - 80, y=330 - 80)
    window.add(brain9)
    body_r = GArc(200, 200, 180, 70, x=906, y=500)
    window.add(body_r)
    body_r2 = GLine(926, 590, 1150, 800)
    window.add(body_r2)
    body_m = GLine(702, 676, 750, 800)
    window.add(body_m)
    body_l = GArc(300, 300, 100, 100, x=568, y=600)
    window.add(body_l)
    body_l2 = GArc(600, 600, 120, 50, x=552, y=700)
    window.add(body_l2)
    shot1 = GPolygon()
    shot1.add_vertex((800, 400))
    shot1.add_vertex((900, 900))
    shot1.add_vertex((920, 900))
    shot1.filled = True
    shot1.fill_color = 'aliceblue'
    window.add(shot1)
    shot2 = GPolygon()
    shot2.add_vertex((850, 450))
    shot2.add_vertex((1600, 700))
    shot2.add_vertex((1500, 720))
    shot2.filled = True
    shot2.fill_color = 'beige'
    window.add(shot2)
    shot3 = GPolygon()
    shot3.add_vertex((830, 420))
    shot3.add_vertex((1600, 600))
    shot3.add_vertex((1500, 610))
    shot3.filled = True
    shot3.fill_color = 'blueviolet'
    window.add(shot3)
    shot4 = GPolygon()
    shot4.add_vertex((870, 400))
    shot4.add_vertex((1600, 400))
    shot4.add_vertex((1500, 410))
    shot4.filled = True
    shot4.fill_color = 'chocolate'
    window.add(shot4)
    shot5 = GPolygon()
    shot5.add_vertex((750, 350))
    shot5.add_vertex((1600, 200))
    shot5.add_vertex((1500, 230))
    shot5.filled = True
    shot5.fill_color = 'cyan'
    window.add(shot5)
    shot6 = GPolygon()
    shot6.add_vertex((800, 300))
    shot6.add_vertex((1600, 10))
    shot6.add_vertex((1500, 30))
    shot6.filled = True
    shot6.fill_color = 'darkorange'
    window.add(shot6)
    shot7 = GPolygon()
    shot7.add_vertex((750, 250))
    shot7.add_vertex((900, -30))
    shot7.add_vertex((950, -60))
    shot7.filled = True
    shot7.fill_color = 'darkseagreen'
    window.add(shot7)
    shot8 = GPolygon()
    shot8.add_vertex((680, 250))
    shot8.add_vertex((710, -30))
    shot8.add_vertex((700, -60))
    shot8.filled = True
    shot8.fill_color = 'darkviolet'
    window.add(shot8)
    shot9 = GPolygon()
    shot9.add_vertex((670, 270))
    shot9.add_vertex((610, -30))
    shot9.add_vertex((600, -60))
    shot9.filled = True
    shot9.fill_color = 'dodgerblue'
    window.add(shot9)
    shot10 = GPolygon()
    shot10.add_vertex((630, 300))
    shot10.add_vertex((410, -30))
    shot10.add_vertex((400, -60))
    shot10.filled = True
    shot10.fill_color = 'gainsboro'
    window.add(shot10)
    shot11 = GPolygon()
    shot11.add_vertex((650, 370))
    shot11.add_vertex((110, -30))
    shot11.add_vertex((150, -60))
    shot11.filled = True
    shot11.fill_color = 'green'
    window.add(shot11)
    shot12 = GPolygon()
    shot12.add_vertex((630, 380))
    shot12.add_vertex((-110, 30))
    shot12.add_vertex((-150, 60))
    shot12.filled = True
    shot12.fill_color = 'indianred'
    window.add(shot12)
    shot13 = GPolygon()
    shot13.add_vertex((680, 380))
    shot13.add_vertex((-110, 600))
    shot13.add_vertex((-150, 700))
    shot13.filled = True
    shot13.fill_color = 'lavenderblush'
    window.add(shot13)
    shot14 = GPolygon()
    shot14.add_vertex((620, 390))
    shot14.add_vertex((-110, 400))
    shot14.add_vertex((-150, 450))
    shot14.filled = True
    shot14.fill_color = 'lightcyan'
    window.add(shot14)

    # brain10 = GArc(190, 190, 330, 90, x=680-50, y=330-50)
    # brain10.filled = True
    # brain10.fill_color = 'red'
    # window.add(brain10)




    # eye_right_up = GArc(100, 50, 0, 180, x=600, y=600)
    # window.add(eye_right_up)


if __name__ == '__main__':
    main()
