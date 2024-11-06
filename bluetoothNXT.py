import nxt
import nxt.locator 
import nxt.brick
import time
import pygame


r = 2.75
L = 17
OmegaL = 0
OmegaR = 0 
Vxg = 0
TETAg = 0
started = False

def run_bob():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE and started == False:
                started = True
                bob = nxt.locator.find(host="00:16:53:09:72:DE")
                bob.start_program("Bob6.rxe")
                MotorLeft = bob.get_motor(nxt.motor.Port.B)
                MotorRight = bob.get_motor(nxt.motor.Port.C)

def separa_elementos(vetor):
    numeros = vetor.strip("()").split(", ")
    numeros = [int(num) for num in numeros]
    return numeros

def diferential_cinematic():
    data = []
    Fposition_left = 0
    Fposition_right = 0
    vetorL = MotorLeft.get_tacho().__str__()
    vetorR = MotorRight.get_tacho().__str__()
    Iposition_left = separa_elementos(vetorL)
    Iposition_right = separa_elementos(vetorR)
    to = time.clock_gettime_ns(time.CLOCK_REALTIME)
    
    for i in range(0,10):
        Fposition_left += separa_elementos(vetorL)
        Fposition_right += separa_elementos(vetorR)
        time.sleep(0.1)
    tf = time.clock_gettime_ns(time.CLOCK_REALTIME)
    OmegaL = (Fposition_left[2] - Iposition_left[2])/(tf-to)
    OmegaR = (Fposition_right[2] - Iposition_right[2])/(tf-to)
    Vxg = (((r*OmegaR)/2) + ((r*OmegaL)/2))
    TETAg = (((r*OmegaR)/2*L) - ((r*OmegaL)/2*L))
    data.append(Vxg)
    data.append(TETAg)
    return data



pygame.init()
x = 100
y = 100
info = pygame.display.Info()
w_display = info.current_w
h_display = info.current_h
workspace_horizontal = w_display/(2.7)
workspace_vertical = h_display/(1.8)
screen = pygame.display.set_mode([w_display,h_display],pygame.FULLSCREEN)

def draw_workspace():

    base_line_distance = 0.38
    housing_line_distance = 0.75

    recharge_line = base_line_distance * workspace_horizontal
    warehouse_line = (2.7 - base_line_distance) * workspace_horizontal
    pygame.draw.line(screen,(0, 0, 0), (recharge_line, 0), (recharge_line, h_display), width=5)
    pygame.draw.line(screen,(0, 0, 0), (warehouse_line, 0), (warehouse_line, h_display), width=5)


    housing_horizontal = housing_line_distance * workspace_horizontal
    housing_vertical = housing_line_distance * workspace_vertical
    pygame.draw.rect(screen,(0, 0, 0), pygame.Rect(housing_horizontal, 0, 150,150), width=5)
    pygame.draw.rect(screen,(0, 0, 0), pygame.Rect((2*housing_horizontal), 0, 150,150), width=5)
    pygame.draw.rect(screen,(0, 0, 0), pygame.Rect(housing_horizontal, housing_vertical, 150,150), width=5)
    pygame.draw.rect(screen,(0, 0, 0), pygame.Rect((2*housing_horizontal), housing_vertical, 150,150), width=5)
    pygame.draw.rect(screen,(0, 0, 0), pygame.Rect(housing_horizontal, (2*housing_vertical), 150,150), width=5)
    pygame.draw.rect(screen,(0, 0, 0), pygame.Rect((2*housing_horizontal), (2*housing_vertical), 150,150), width=5)

def bob_6_new_testament_two_point_0(x,y):
    bod_diameter = 0.085*workspace_horizontal
    pygame.draw.circle(screen, (255, 0, 0), (x, y), bod_diameter)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running == False

    run_bob()
    screen.fill((255, 255, 255))
    
    draw_workspace()
    bob_6_new_testament_two_point_0(x,y)
    G = diferential_cinematic()
    if(G[1] != 0){
        y += G[0]
    }else{
        x += G[0]
    }
    pygame.display.flip()



pygame.quit()