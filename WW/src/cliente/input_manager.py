import pygame

class InputManager:
    def __init__(self):
        # Dicionário simplificado para mapear comandos para teclas
        self.comandos = {
            "menu_sair": pygame.K_ESCAPE,
            "menu_cima": pygame.K_UP,
            "menu_baixo": pygame.K_DOWN,
            "menu_selecionar": pygame.K_RETURN
        }
        
        # Armazenar estado atual das teclas
        self.teclas_pressionadas = {}
        self.teclas_ativadas = set()
    
    def atualizar(self, eventos):
        # Obter estado de todas as teclas
        self.teclas_pressionadas = pygame.key.get_pressed()
        
        # Limpar teclas ativadas a cada frame
        self.teclas_ativadas.clear()
        
        # Processar eventos para identificar teclas ativadas
        for event in eventos:
            if event.type == pygame.KEYDOWN:
                self.teclas_ativadas.add(event.key)
    
    def tecla_pressionada(self, comando):
        """Verifica se uma tecla está sendo pressionada continuamente"""
        if comando in self.comandos:
            return self.teclas_pressionadas[self.comandos[comando]]
        return False
    
    def tecla_ativada(self, comando):
        """Verifica se uma tecla acabou de ser pressionada neste frame"""
        if comando in self.comandos:
            return self.comandos[comando] in self.teclas_ativadas
        return False