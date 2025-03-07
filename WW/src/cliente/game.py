import pygame
import accessible_output2.outputs.auto
from input_manager import InputManager
from time import sleep

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

        # Configuração do sistema de voz
        self.last_spoken = ""
        self.speak_delay = 0
        
        # Estado do jogo
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


    def run(self):
        self.speak("Jogo iniciado. Pressione ESC para o menu de saída.")

        while self.running:
            # Coletar eventos
            eventos = pygame.event.get()
            
            # Processar eventos de fechamento da janela
            for event in eventos:
                if event.type == pygame.QUIT:
                    self.running = False
            
            # Atualizar o gerenciador de entrada
            self.input_manager.atualizar(eventos)
            
            # Atualizar contador de delay da fala
            if self.speak_delay > 0:
                self.speak_delay -= 1
            
            # Gerenciar estados do jogo
            if self.state == "game":
                # Processamento do jogo principal
                if self.input_manager.tecla_ativada("menu_sair"):
                    self.show_exit_menu()
                    
            elif self.state == "exit_menu":
                # Processamento do menu de saída
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

            # Renderização
            pygame.display.flip()
            self.clock.tick(self.fps)

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()