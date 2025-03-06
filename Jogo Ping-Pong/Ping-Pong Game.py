import tkinter as tk

# Configurações da janela
LARGURA = 800
ALTURA = 600

# Configurações da raquete e da bola
RAQUETE_LARGURA = 10
RAQUETE_ALTURA = 100
BOLA_TAMANHO = 20

# Velocidades iniciais (reduzidas)
VELOCIDADE_RAQUETE = 20
VELOCIDADE_BOLA_X = 3  # Velocidade horizontal reduzida
VELOCIDADE_BOLA_Y = 3  # Velocidade vertical reduzida

# Função para mover a raquete para cima
def mover_raquete_cima(event):
    # Obtém as coordenadas atuais da raquete esquerda
    x1, y1, x2, y2 = canvas.coords(raquete_esquerda)
    if y1 > 0:  # Verifica se a raquete não está no topo
        canvas.move(raquete_esquerda, 0, -VELOCIDADE_RAQUETE)

    # Obtém as coordenadas atuais da raquete direita
    x1, y1, x2, y2 = canvas.coords(raquete_direita)
    if y1 > 0:  # Verifica se a raquete não está no topo
        canvas.move(raquete_direita, 0, -VELOCIDADE_RAQUETE)

# Função para mover a raquete para baixo
def mover_raquete_baixo(event):
    # Obtém as coordenadas atuais da raquete esquerda
    x1, y1, x2, y2 = canvas.coords(raquete_esquerda)
    if y2 < ALTURA:  # Verifica se a raquete não está na base
        canvas.move(raquete_esquerda, 0, VELOCIDADE_RAQUETE)

    # Obtém as coordenadas atuais da raquete direita
    x1, y1, x2, y2 = canvas.coords(raquete_direita)
    if y2 < ALTURA:  # Verifica se a raquete não está na base
        canvas.move(raquete_direita, 0, VELOCIDADE_RAQUETE)

# Função para mover a bola
def mover_bola():
    global VELOCIDADE_BOLA_X, VELOCIDADE_BOLA_Y

    # Movimentação da bola
    canvas.move(bola, VELOCIDADE_BOLA_X, VELOCIDADE_BOLA_Y)

    # Coordenadas da bola
    bola_x1, bola_y1, bola_x2, bola_y2 = canvas.coords(bola)

    # Verifica colisão com as bordas superior e inferior
    if bola_y1 <= 0 or bola_y2 >= ALTURA:
        VELOCIDADE_BOLA_Y *= -1  # Inverte a direção vertical

    # Verifica colisão com as raquetes
    raquete_esquerda_coords = canvas.coords(raquete_esquerda)
    raquete_direita_coords = canvas.coords(raquete_direita)

    if (bola_x1 <= RAQUETE_LARGURA and raquete_esquerda_coords[1] < bola_y2 and raquete_esquerda_coords[3] > bola_y1) or \
       (bola_x2 >= LARGURA - RAQUETE_LARGURA and raquete_direita_coords[1] < bola_y2 and raquete_direita_coords[3] > bola_y1):
        VELOCIDADE_BOLA_X *= -1  # Inverte a direção horizontal

    # Verifica se a bola saiu da tela (ponto para o jogador)
    if bola_x1 <= 0 or bola_x2 >= LARGURA:
        reiniciar_bola()

    # Repete a função após 10ms
    janela.after(10, mover_bola)

# Função para reiniciar a bola no centro
def reiniciar_bola():
    global VELOCIDADE_BOLA_X, VELOCIDADE_BOLA_Y
    canvas.coords(bola, LARGURA // 2 - BOLA_TAMANHO // 2, ALTURA // 2 - BOLA_TAMANHO // 2,
                  LARGURA // 2 + BOLA_TAMANHO // 2, ALTURA // 2 + BOLA_TAMANHO // 2)
    VELOCIDADE_BOLA_X *= -1  # Inverte a direção horizontal

# Criação da janela
janela = tk.Tk()
janela.title("Ping Pong")

# Criação do canvas (área de desenho)
canvas = tk.Canvas(janela, width=LARGURA, height=ALTURA, bg="black")
canvas.pack()

# Criação das raquetes
raquete_esquerda = canvas.create_rectangle(0, ALTURA // 2 - RAQUETE_ALTURA // 2,
                                           RAQUETE_LARGURA, ALTURA // 2 + RAQUETE_ALTURA // 2, fill="white")
raquete_direita = canvas.create_rectangle(LARGURA - RAQUETE_LARGURA, ALTURA // 2 - RAQUETE_ALTURA // 2,
                                          LARGURA, ALTURA // 2 + RAQUETE_ALTURA // 2, fill="white")

# Criação da bola
bola = canvas.create_oval(LARGURA // 2 - BOLA_TAMANHO // 2, ALTURA // 2 - BOLA_TAMANHO // 2,
                          LARGURA // 2 + BOLA_TAMANHO // 2, ALTURA // 2 + BOLA_TAMANHO // 2, fill="white")

# Configuração dos controles
janela.bind("<w>", mover_raquete_cima)
janela.bind("<s>", mover_raquete_baixo)
janela.bind("<Up>", mover_raquete_cima)
janela.bind("<Down>", mover_raquete_baixo)

# Inicia o movimento da bola
mover_bola()

# Inicia o loop principal da interface gráfica
janela.mainloop()