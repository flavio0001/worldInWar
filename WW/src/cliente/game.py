import pygame
import accessible_output2.outputs.auto
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
        
        # Configurações para evitar duplicação de leituras
        self.last_spoken = ""
        self.speak_delay = 0

    def speak(self, text):
        """Função para falar texto evitando repetições rápidas do mesmo texto"""
        if text != self.last_spoken or self.speak_delay <= 0:
            self.output.speak(text, interrupt=True)
            self.last_spoken = text
            self.speak_delay = 10  # Frames até permitir a repetição do mesmo texto
    
    def show_exit_menu(self):
        self.speak("Deseja sair?")
        sleep(0.5)  # Pequena pausa para melhor compreensão
        
        menu_running = True
        options = ["Sim", "Não"]
        selected_index = 1
        
        # Anúncio inicial da opção selecionada
        self.speak(f"{options[selected_index]}")
        
        while menu_running:
            # Diminui o contador de delay de fala, se houver
            if self.speak_delay > 0:
                self.speak_delay -= 1
                
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    return

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        # Alternar entre as opções apenas com setas para cima/baixo
                        selected_index = 1 - selected_index
                        self.speak(f"{options[selected_index]}")
                        
                    elif event.key == pygame.K_RETURN:
                        if selected_index == 0:  # Sim
                            self.speak("Saindo do jogo")
                            sleep(0.5)  # Dar tempo para o leitor de tela terminar
                            self.running = False
                            return
                        else:  # Não
                            self.speak("Retornando ao jogo")
                            menu_running = False
                            
                    elif event.key == pygame.K_ESCAPE:
                        # Sair do menu com ESC
                        self.speak("Retornando ao jogo")
                        menu_running = False
                        
            # Atualiza a tela e mantém o frame rate
            pygame.display.flip()
            self.clock.tick(self.fps)

    def run(self):
        self.speak("Jogo iniciado. Pressione ESC para o menu de saída.")
        
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.show_exit_menu()
                    # Aqui você adicionará outras teclas e funcionalidades do jogo

            # Aqui você irá atualizar a lógica do jogo, como movimento do jogador, etc.
            
            # Atualiza a tela e mantém o frame rate
            pygame.display.flip()
            self.clock.tick(self.fps)

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()