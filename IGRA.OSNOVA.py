import pygame
import random
pygame.init()


#-|-|-|-|-|-|-|-|Т-Е-Х-И-Ч-Е-С-К-И-Е|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|


#Устанавливаю размер окна
width = 1366
height = 706

#Создаём окно
display = pygame.display.set_mode((width, height))
pygame.display.set_caption('')

#Создаём фпс
fps = pygame.time.Clock()

#Загружаем иконку игры
icon = pygame.image.load('icon1.png')
pygame.display.set_icon(icon)


#-|-|-|-|-|-|-|-|Д-О-Б-А-В-Л-Е-Н-И-Е  О-Б-Ъ-Е-К-Т-О-В  И  И-Х  К-О-О-Р-Д-И-Н-А-Т|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|


#Загружаем фон
fon = pygame.image.load('fon.jpg')

#Загружаем картинку бегемота
chel = [pygame.image.load('Hippo.png')]

#Загружаем картинки падающих объектов
jrat = [pygame.image.load('fish_2.png'), pygame.image.load('fish_1.png'), pygame.image.load('fish_3.png'), pygame.image.load('fish_4.png')]

#Загружаем картиинку жизней 
heart_1 = pygame.image.load('heart_1.png')
heart_05 = pygame.image.load('heart_0.5.png')
heart_0 = pygame.image.load('heart_0.png')
heart = [heart_1, heart_05, heart_0]

#Загружаем картинки птиц и присваиваем им начальные координаты
y_bird = 75 + 30 * random.choice(range(0, 6))
x_bird = - 600

birds_1_1 = [pygame.image.load('bird_1_0.png'), pygame.image.load('bird_1_1.png'), pygame.image.load('bird_1_2.png'), pygame.image.load('bird_1_1.png')]
birds_1_2 = [pygame.transform.flip(birds_1_1[0], True, False), pygame.transform.flip(birds_1_1[1], True, False), pygame.transform.flip(birds_1_1[2], True, False), pygame.transform.flip(birds_1_1[1], True, False)]
birds_2_1 = [pygame.image.load('bird_2_0.png'), pygame.image.load('bird_2_1.png'), pygame.image.load('bird_2_2.png'), pygame.image.load('bird_2_1.png')]
birds_2_2 = [pygame.transform.flip(birds_2_1[0], True, False), pygame.transform.flip(birds_2_1[1], True, False), pygame.transform.flip(birds_2_1[2], True, False), pygame.transform.flip(birds_2_1[1], True, False)]
birds_3_1 = [pygame.image.load('bird_3_0.png'), pygame.image.load('bird_3_1.png'), pygame.image.load('bird_3_2.png'), pygame.image.load('bird_3_1.png')]
birds_3_2 = [pygame.transform.flip(birds_3_1[0], True, False), pygame.transform.flip(birds_3_1[1], True, False), pygame.transform.flip(birds_3_1[2], True, False), pygame.transform.flip(birds_3_1[1], True, False)]
birds = [[birds_1_1, birds_1_2], [birds_2_1, birds_2_2], [birds_3_1, birds_3_2]]

#Начальные координаты бегемота
x_chel = 24
y_chel = 535

#Начальные кооординаты рыб
x_fish = 84 + 220 * random.choice(range(0, 6))
y_fish = -124


#-|-|-|-|-|-|-|-|Д-О-П-О-Л-Н-И-Т-Е-Л-Ь-Н-Ы-Е  П-Е-Р-Е-М-Е-Н-Н-Ы-Е|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|


#Переменная счёта
score = 0

#Переменная скорости, с которой падают фрукты
speed = 3

#Переменная задержки при нажатия кнопок управления бегемотом
zaderj = 0

#Для получения направления птицы
fl1 = 0
#Для рандомной смены картинок рыб
fl2 = 0
#Задержка на нажатие кнопок передвижения
fl3 = True
#Для смены картинок сердец
fl4 = 0
#Для смены положения крыльев птицы (раз в 4 тика)
fl5 = 0
#Для рандомной смены картинок птиц
fl6 = 0


#-|-|-|-|-|-|-|-|Д-О-Б-А-В-Л-Е-Н-И-Е  Ф-У-Н-К-Ц-И-Й|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|


#Функция написания текста
def print_text(message, x, y, font_color = (0, 0, 0), font_type = 'shrift_3.ttf', font_size = 30):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    display.blit(text, (x, y))

#Функция рисования сердечек
def blit_heart(img_1, img_2, img_3):
    display.blit(img_1, (40, 40))  
    display.blit(img_2, (74, 40))
    display.blit(img_3, (108, 40))

#Функция паузы
def pause():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        print_text('Нажмите ENTER, чтобы продолжить', (width - 19 * 30) // 2, (height - 30) // 2)
        pygame.display.update()         
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            paused = False
        if keys[pygame.K_ESCAPE]:
            paused = False
            game = False


#-|-|-|-|-|-|-|-|О-С-Н-О-В-Н-О-Й  Ц-И-К-Л|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|


#Делаем основной цикл
def run_game():  
    global x_chel, y_chel, fl1, fl2, fl3, fl4, fl5, fl6, chel, x_fish, y_fish, speed, zaderj, score, x_bird, y_bird
    game = True
    while game == True:
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 quit()

        #Добавление фона
        display.blit(fon, (0, 0))

        #Птицы
        if x_bird > - 400 and fl1 == 0:
            x_bird -= 2
            if fl5 != 3:
                fl5 += 0.25
            else:
                fl5 = 0
            display.blit(birds[fl6][1][int(fl5)], (x_bird, y_bird))   
        else:
            fl1 = 1
        if x_bird < 1766 and fl1 == 1:
            x_bird += 2
            if fl5 != 3:
                fl5 += 0.25
            else:
                fl5 = 0
            display.blit(birds[fl6][0][int(fl5)], (x_bird, y_bird))
        else:
            fl1 = 0
        if x_bird == - 400 or x_bird == 1766:
            y_bird = 75 + 100 * random.choice(range(0, 6))
            fl6 = random.choice(range(0, 3))
            
        #Прорисовка бегемота
        display.blit(chel[0], (x_chel, y_chel))  
        
        #Строка счёта в левом верхнем углу
        print_text((f'Ваш счёт {score}'), 10, 5)

        #Прорисовка сердечек
        if fl4 == 0:
            blit_heart(heart[0], heart[0], heart[0])
        if fl4 == 1:
            blit_heart(heart[0], heart[0], heart[1])
        if fl4 == 2:
            blit_heart(heart[0], heart[0], heart[2])
        if fl4 == 3:
            blit_heart(heart[0], heart[1], heart[2])
        if fl4 == 4:
            blit_heart(heart[0], heart[2], heart[2])
        if fl4 == 5:
            blit_heart(heart[1], heart[2], heart[2])
        if fl4 == 6:
            blit_heart(heart[2], heart[2], heart[2])
            y_bird = 75 + 30 * random.choice(range(0, 6))
            x_bird = - 600
            speed = 3
            paused = True
            while paused:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        quit()
                print_text((f'Ваш счёт {score}'), 10, 5)
                print_text(f'Вы проиграли, ваш счёт: {score}', 450, 330)
                print_text('Нажмите ENTER чтобы начать заново', 400, 380)
                pygame.display.update()

                keys = pygame.key.get_pressed()
                if keys[pygame.K_RETURN]:
                    score = 0
                    fl4 = 0
                    y_fish = -124
                    x_fish = 84 + 220 * random.choice(range(0, 6))
                    pygame.display.update()
                    paused = False
                if keys[pygame.K_ESCAPE]:
                    paused = False
                    game = False

        #Прорисовка падающего объекта      
        display.blit(jrat[fl2], (x_fish, y_fish))
        
        #Съедание падающего объекта
        if x_chel + 60 == x_fish and y_fish <= 521 and y_fish >= 507:
            if fl2 != 3:
                score += 10
            else:
                fl4 += 1
            y_fish = -124
            x_fish = 84 + 220 * random.choice(range(0, 6))
            fl2 = random.choice(range(0, 4))

        #Добавляем задержку по передвижению бегемота, поскольку при использовании pygame.time.delay() 
        #задержка идёт на всю программу, по этому падающий объект зависает в воздухе
        if zaderj == 8:
            fl3 == True
            zaderj = 0
        
        #Перемещение бегемота
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d] and x_chel + 220 <= 1343 and zaderj == 0:
            x_chel += 220
            fl3 = False
        if keys[pygame.K_a] and x_chel - 220 >= 23 and zaderj == 0:
            x_chel -= 220
            fl3 = False
        
        #Элемент задержки нажатия клавиш передвижения бегемота
        if fl3 == False:
            zaderj += 1
        
        #Изменение скорости падающего объекта
        if speed < 14:
            speed += 1/1000
        else:
            speed = 14
        
        if y_fish < 850:
            y_fish += speed
        else:
            if fl2 == 3:
                fl4 = fl4
            else:
                fl4 += 1
            y_fish = -124
            x_fish = 84 + 220 * random.choice(range(0, 6))
            fl2 = random.choice(range(0, 4))
            
        #Проверка на паузу
        if keys[pygame.K_p]:
            pause()

        #Проверка на выход
        if keys[pygame.K_ESCAPE]:
            game = False

        #Задаём fps
        fps.tick(60)

        pygame.display.update()

run_game()