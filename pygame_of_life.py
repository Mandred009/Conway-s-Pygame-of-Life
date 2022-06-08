import pygame

# Initializing Pygame
pygame.init()

# Creating display
window_width=1500
window_height=850
display_surface=pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption("Pygame Of Life")

# Setting FPS and clock
fps=20
clock=pygame.time.Clock()

# Loading the music
pygame.mixer.music.load('HinaCC0_004_Sound-of-passion.mp3')

# Function to lay tiles
def Tile(x,y,tiletype):
    if(tiletype==0):
        image=pygame.draw.rect(display_surface,(0,0,0),(x,y,14,14))
    elif(tiletype==1):
        image=pygame.draw.rect(display_surface,(255,255,255),(x,y,14,14))

# Function to exchange value of maps
def looper():
    for i in range(1,len(tile_map)-1):
        for j in range(1,len(tile_map[i])-1):
            tile_map[i][j]=tile_copy[i][j]

# The function which checks for the logic in Conways game of life
def lifecheck():
    for i in range(1, len(tile_map) - 1):
        sum=0
        for j in range(1, len(tile_map[i]) - 1):
                sum= tile_map[i - 1][j - 1] + tile_map[i - 1][j] + tile_map[i - 1][j + 1] + tile_map[i][j - 1] + tile_map[i][j + 1] + tile_map[i + 1][j - 1] + tile_map[i + 1][j] + tile_map[i + 1][j + 1]
                if sum==3 and tile_map[i][j]==0:
                    tile_copy[i][j]=1
                if (sum==2 or sum==3) and tile_map[i][j]==1:
                    tile_copy[i][j]=1
                elif (sum<2 or sum>3) and tile_map[i][j]==1:
                    tile_copy[i][j]=0
                Tile(j * 15, i * 15, tile_copy[i][j])

#def deathcheck():
    for i in range(1,len(tile_map)-1):
        sum=0
        for j in range(1,len(tile_map[i])-1):
                sum=tile_map[i-1][j-1]+tile_map[i-1][j]+tile_map[i-1][j+1]+tile_map[i][j-1]+tile_map[i][j+1]+tile_map[i+1][j-1]+tile_map[i+1][j]+tile_map[i+1][j+1]
                if sum==3 and tile_map[i][j]==0:
                    tile_copy[i][j]=1
                Tile(j * 15, i * 15, tile_copy[i][j])

# Tile map
tile_map=[]
tile_copy=[]

# Creating Tile Map
for i in range(0,window_height//15):
    l=[]
    for j in range(0,window_width//15):
        l.append(0)
    tile_map.append(l)

# Creating overlay mirror tile map
for i in range(0,window_height//15):
    l2=[]
    for j in range(0,window_width//15):
        l2.append(0)
    tile_copy.append(l2)

# Placing tiles
for i in range(len(tile_map)):
    for j in range(len(tile_map[i])):
        if tile_map[i][j]==1:
            Tile(j * 15, i * 15, 1)
        else:
            Tile(j * 15, i * 15, 0)

# Main game loop
running=True
input=True

# Play Music
pygame.mixer.music.play(-1,0.0)

while(running):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

        # Selecting live cells with mouse as input
        if event.type==pygame.MOUSEBUTTONDOWN and input:
            mouse_x=event.pos[0]
            mouse_y=event.pos[1]
            tile_map[mouse_y//15][mouse_x//15]=1
            tile_copy[mouse_y // 15][mouse_x // 15] = 1
            Tile((mouse_x//15)*15,(mouse_y//15)*15,1)

        # Press enter to start the simulation
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_KP_ENTER:
                input=False
    if input==False:
        lifecheck()
        looper()
    pygame.display.update()
    clock.tick(fps)

pygame.quit()