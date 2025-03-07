import pygame
import accessible_output2.outputs  
from input_manager import InputManager  

class Player:
    def __init__(self, input_manager):
        self.input_manager = input_manager
        self.output = accessible_output2.outputs.auto.Auto()

    def atualizar(self):
        if self.input_manager.tecla_pressionada("pular"):
            self.output.speak("O personagem pulou.")
        
        if self.input_manager.tecla_pressionada("andar_frente"):
            self.output.speak("O personagem andou para frente.")

        if self.input_manager.tecla_pressionada("andar_direita"):
            self.output.speak("O personagem andou para direita.")

pygame.init()
tela = pygame.display.set_mode((800, 600))
input_manager = InputManager()
player = Player(input_manager)

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    input_manager.atualizar()
    player.atualizar()
    
    pygame.display.flip()

pygame.quit()
