import pygame
import accessible_output2.outputs.auto
from input_manager import InputManager
from time import sleep
from player import Player  
from map import Map  

class Game:
    def __init__(self):
        pygame.init()
        self.width, self.height = 800, 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("WorldInWar")
        self.running = True
        self.clock = pygame.time.Clock()
        self.output = accessible_output2.outputs.auto.Auto()
        self.fps = 60
        self.input_manager = InputManager()
        self.player = Player("Jogador1")
        self.mapa = Map("brasilândia.mp")
        print(f"Nome do mapa: {self.mapa.name}")
        print(f"Tamanho: X={self.mapa.max_x}, Y={self.mapa.max_y}, Z={self.mapa.max_z}")
        print(f"Zonas de texto: {self.mapa.zonas_texto}")
        print(f"Bordas X: {self.mapa.bordas_x}")
        print(f"Bordas Y: {self.mapa.bordas_y}")
        print(f"Plataformas: {self.mapa.plataformas}")



        self.last_spoken = ""
        self.speak_delay = 0
        
        self.state = "game"

    def speak(self, text):
        if text != self.last_spoken or self.speak_delay <= 0:
            self.output.speak(text, interrupt=True)
            self.last_spoken = text
            self.speak_delay = 10

    def show_exit_menu(self):
        self.speak("Deseja sair?")
        sleep(0.5)

        self.state = "exit_menu"
        self.exit_options = ["Sim", "Não"]
        self.selected_index = 1

    def processar_input(self, eventos):
        self.input_manager.atualizar(eventos)

        if self.input_manager.tecla_pressionada("cima"):
            self.player.mover("norte")
        elif self.input_manager.tecla_pressionada("baixo"):
            self.player.mover("sul")
        elif self.input_manager.tecla_pressionada("esquerda"):
            self.player.mover("oeste")
        elif self.input_manager.tecla_pressionada("direita"):
            self.player.mover("leste")

        if self.input_manager.tecla_ativada("girar_esquerda"):
            self.player.mover("oeste")
        elif self.input_manager.tecla_ativada("girar_direita"):
            self.player.mover("leste")

        if self.input_manager.tecla_combinada_ativada("virar180_frente"):
            self.player.mover("180")
        elif self.input_manager.tecla_combinada_ativada("virar180_tras"):
            self.player.mover("180")

        if self.input_manager.tecla_ativada("falar_coordenadas"):
            self.speak(self.player.falar_coordenadas())

        if self.input_manager.tecla_ativada("falar_zona"):
            self.speak(self.player.falar_zona(self.mapa))

    def run(self):
        self.speak("Jogo iniciado. Pressione ESC para o menu de saída.")

        while self.running:
            eventos = pygame.event.get()
            
            for event in eventos:
                if event.type == pygame.QUIT:
                    self.running = False
            
            self.input_manager.atualizar(eventos)
            self.processar_input(eventos)

            if self.speak_delay > 0:
                self.speak_delay -= 1
            
            if self.state == "game":
                if self.input_manager.tecla_ativada("menu_sair"):
                    self.show_exit_menu()
                    
            elif self.state == "exit_menu":
                if self.input_manager.tecla_ativada("menu_cima") or self.input_manager.tecla_ativada("menu_baixo"):
                    self.selected_index = 1 - self.selected_index
                    self.speak(f"{self.exit_options[self.selected_index]}")

                elif self.input_manager.tecla_ativada("menu_selecionar"):
                    if self.selected_index == 0:
                        self.speak("Saindo do jogo")
                        sleep(0.5)
                        self.running = False
                    else:
                        self.speak("Retornando ao jogo")
                        self.state = "game"

                elif self.input_manager.tecla_ativada("menu_sair"):
                    self.speak("Retornando ao jogo")
                    self.state = "game"

            pygame.display.flip()
            self.clock.tick(self.fps)

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()
