import os
import pygame
import random

class SoundMap:
    def __init__(self):
        pygame.mixer.init()  # Inicia o mixer do pygame

        self.sounds_folder = r"D:\program\área de testes\worldInWar\WW\src\cliente\assets\sounds\pisos"
        self.sounds = {}

        self.load_sounds()

    def load_sounds(self):
        """Carrega os sons dos diferentes tipos de piso."""
        if not os.path.exists(self.sounds_folder):
            raise FileNotFoundError(f"Pasta de sons não encontrada: {self.sounds_folder}")

        for tipo_piso in os.listdir(self.sounds_folder):
            caminho_piso = os.path.join(self.sounds_folder, tipo_piso)
            if os.path.isdir(caminho_piso):  # Só pega diretórios
                self.sounds[tipo_piso] = [
                    os.path.join(caminho_piso, file)
                    for file in os.listdir(caminho_piso)
                    if file.endswith(".ogg")
                ]

    def play_step_sound(self, tipo_piso):
        """Toca um som de passo baseado no tipo de piso."""
        if tipo_piso in self.sounds and self.sounds[tipo_piso]:
            sound_file = random.choice(self.sounds[tipo_piso])  # Escolhe um aleatório
            pygame.mixer.Sound(sound_file).play()
        else:
            print(f"⚠️ Nenhum som encontrado para o piso: {tipo_piso}")

