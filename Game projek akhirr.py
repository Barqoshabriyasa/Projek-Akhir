import pygame
from pygame import mixer
from pygame import *
# Inisialisasi Pygame
pygame.init()
mixer.init()
#counter
error_counter = 0
succes_counter = 0
level = 1

# Ukuran layar
screen = pygame.display.set_mode((900, 500)) #layar/scene
display.set_caption("Clicker Game")

#label
myfont = pygame.font.Font("D:\VSCODE LABIRIN\ByteBounce.ttf", 35, )
myfont1 = pygame.font.Font("D:\VSCODE LABIRIN\ByteBounce.ttf", 50, )


#fungsi label
def draw_text(text, font, text_col, x, y):
    img = myfont.render(text, True, text_col)
    screen.blit(img, (x, y))

#upload audio
audio = mixer.Sound(r"D:\VSCODE LABIRIN\game lingkaran.mp3")
error = mixer.Sound(r"D:\VSCODE LABIRIN\error lingkaran.mp3")
succes = (r"D:\VSCODE LABIRIN\thumbs up.jpeg")

# Warna
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
# Posisi dan ukuran kotak
circle_pos = [200, 270]  
circle_pos2 = [700,270]
circle_pos3 = [700,270]
#circle_pos3 = [300,155]
circle_color = RED
circle_color2 = BLUE
circle_radius = 30
circle_radius2 = 30
circle_radius3 = 30
circle_color3 = BLUE
# Kecepatan gerakan kotak
circle_speedx = 3
circle_speedy = 3
# Fungsi untuk memeriksa apakah kotak diklik
def is_circle_clicked(pos, circle_pos, circle_radius):
    x, y = pos #tentukan posisinya
    circle_x, circle_y = circle_pos
    distance = ((x- circle_x)**2 + (y - circle_y)**2) ** 0.5
    circle_width, circle_height = circle_pos
    return distance <= circle_radius
def is_circle_clicked2(pos, circle_pos2, circle_radius2):
    x, y = pos #tentukan posisinya
    circle_x, circle_y = circle_pos2
    distance = ((x- circle_x)**2 + (y - circle_y)**2) ** 0.5
    circle_width, circle_height = circle_pos2
    return distance <= circle_radius2
def is_circle_clicked3(pos, circle_pos3, circle_radius3):
    x, y = pos #tentukan posisinya
    circle_x, circle_y = circle_pos3
    distance = ((x- circle_x)**2 + (y - circle_y)**2) ** 0.5
    circle_width, circle_height = circle_pos3
    return distance <= circle_radius2
# Loop utama
running = True
clock = pygame.time.Clock()  # Untuk mengatur frame rate
while running:
    screen.fill((WHITE))     # Mengisi layar dengan warna putih
    label = str( succes_counter)
    levell = str(level)
    draw_text((label), myfont, (0,0,0),850,5)
    draw_text((levell), myfont, (0,0,0),90,5)
    draw_text("Score", myfont, (0,0,0),750,5)
    draw_text("Clicker Game", myfont1, (0,0,0),350,5)
    draw_text("Level", myfont, (0,0,0),5,5)

    click = pygame.event.get()


    for event in click: #mengatur supaya game selalu berjalan
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if is_circle_clicked(event.pos, circle_pos, circle_radius):
                mixer.Sound.play(audio)
                # Ganti warna kotak saat diklik
                circle_color  = GREEN if circle_color == RED else RED if circle_color== BLUE else BLUE if circle_color == GREEN else GREEN
                succes_counter += 1
            elif is_circle_clicked2(event.pos, circle_pos2, circle_radius2):
                mixer.Sound.play(audio)
                # Ganti warna kotak saat diklik
                circle_color2  = GREEN if circle_color2 == RED else RED if circle_color2 == BLUE else BLUE if circle_color2 == GREEN else GREEN
                succes_counter += 1
            elif is_circle_clicked3(event.pos, circle_pos3, circle_radius3):
                    mixer.Sound.play(audio)
                    # Ganti warna kotak saat diklik
                    circle_color3  = GREEN if circle_color3 == RED else RED if circle_color3== BLUE else BLUE if circle_color3 == GREEN else GREEN
                    succes_counter += 1
            else:
                    mixer.Sound.play(error)
                    succes_counter -= 1
    if succes_counter <= -10 :
        
        screen.fill(WHITE)   
        draw_text("Game Over", myfont, (RED),375,230)
        circle_speedy = 0
        circle_speedx = 0
        circle_color = WHITE
        circle_color2 = WHITE
    if succes_counter > 5:
        circle_speedx = circle_speedx+ 1
        circle_speedy = circle_speedy+ 1
        succes_counter = 0
        level += 1
    if level > 1:
        pygame.draw.circle(screen, circle_color3, (circle_pos3), circle_radius3)
        for event in click: #mengatur supaya game selalu berjalan
            if event.type == pygame.MOUSEBUTTONDOWN:
                if is_circle_clicked3(event.pos, circle_pos3, circle_radius3):
                    mixer.Sound.play(audio)
                    # Ganti warna kotak saat diklik
                    circle_color3  = GREEN if circle_color3 == RED else RED if circle_color3== BLUE else BLUE if circle_color3 == GREEN else GREEN
                    succes_counter += 1

            
            
            
                        
                

    # Update posisi kotak
    circle_pos[0] += circle_speedx
    circle_pos[1] += circle_speedy

    circle_pos2 [0] -= circle_speedx
    circle_pos2[1] -= circle_speedy
 
    circle_pos3 [0] -= circle_speedx
    circle_pos3[1] += circle_speedy




    
    # Pantulkan kotak jika mencapai tepi layar
    if circle_pos[0] - circle_radius <= 0 or circle_pos[0] + circle_radius >= 1000:
        circle_speedx = -circle_speedx
    if circle_pos[1] - circle_radius <= 40 :#or circle_pos[1] + circle_radius > 2700:
        circle_speedy = -circle_speedy
    if circle_pos2[0] - circle_radius2 <= 0 or circle_pos2[0] + circle_radius2 >= 1000:
        circle_speedx = -circle_speedx
    if circle_pos2[1] - circle_radius2 <= 40  :# or circle_pos[1] + circle_radius2 >= 700:
        circle_speedy = -circle_speedy



    # Menggambar kotak
    pygame.draw.circle(screen, circle_color, circle_pos, circle_radius)
    pygame.draw.circle(screen, circle_color2, circle_pos2, circle_radius2)


    # Update layar
    pygame.display.flip()
     
    # Batasi frame rate
    clock.tick(60)

# Keluar dari Pygame

