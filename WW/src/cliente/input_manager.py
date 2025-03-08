import pygame

class InputManager:
    def __init__(self):
        self.comandos = {
            "menu_sair": pygame.K_ESCAPE,
            "menu_cima": pygame.K_UP,
            "menu_baixo": pygame.K_DOWN,
            "menu_selecionar": pygame.K_RETURN,
            "cima": pygame.K_UP,
            "baixo": pygame.K_DOWN,
            "esquerda": pygame.K_LEFT,
            "direita": pygame.K_RIGHT,
            "girar_esquerda": pygame.K_a,
            "girar_direita": pygame.K_d,
            "virar180_frente": (pygame.K_LALT, pygame.K_w),
            "virar180_tras": (pygame.K_LALT, pygame.K_s),
            "falar_coordenadas": pygame.K_c,
            "falar_zona": pygame.K_b
        }
        
        self.teclas_pressionadas = {}
        self.teclas_ativadas = set()
    
    def atualizar(self, eventos):
        self.teclas_pressionadas = pygame.key.get_pressed()
        self.teclas_ativadas.clear()
        
        for event in eventos:
            if event.type == pygame.KEYDOWN:
                self.teclas_ativadas.add(event.key)
    
    def tecla_pressionada(self, comando):
        if comando in self.comandos:
            return self.teclas_pressionadas[self.comandos[comando]]
        return False
    
    def tecla_ativada(self, comando):
        if comando in self.comandos:
            return self.comandos[comando] in self.teclas_ativadas
        return False

    def tecla_combinada_ativada(self, comando):
        if comando in self.comandos:
            alt, tecla = self.comandos[comando]
            return pygame.key.get_pressed()[alt] and pygame.key.get_pressed()[tecla]
        return False
