import pygame

class InputManager:
    def __init__(self):
        self.teclas_pressionadas = {}
        self.comandos = {
            "pular": pygame.K_SPACE,
            "andar_frente": pygame.K_UP,
            "andar_direita": pygame.K_RIGHT,
        }

    def atualizar(self):
        self.teclas_pressionadas = pygame.key.get_pressed()

    def tecla_pressionada(self, comando):
        if comando in self.comandos:
            return self.teclas_pressionadas[self.comandos[comando]]
        return False
