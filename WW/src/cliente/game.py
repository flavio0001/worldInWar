import pygame
import accessible_output2.outputs  

class Game:
    def __init__(self):
        pygame.init()
        self.width, self.height = 800, 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("WorldInWar")
        self.running = True
        self.output = accessible_output2.outputs.Auto()

    def show_exit_menu(self):
        menu_running = True
        options = ["Sim", "Não"]
        selected_index = 0  

        while menu_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        selected_index = 1 - selected_index  
                        self.output.speak(options[selected_index])  

                    if event.key == pygame.K_RETURN:
                        if selected_index == 0:  
                            pygame.quit()
                            exit()
                        else:
                            menu_running = False  

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.show_exit_menu()  

            pygame.display.flip()

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()
