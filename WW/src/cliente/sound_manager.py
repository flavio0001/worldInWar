import pygame
import os

# Caminho base dos arquivos de áudio
BASE_SOUND_PATH = r"D:\program\área de testes\worldInWar\WW\src\cliente\assets\sounds"

class SoundManager:
    def __init__(self):
        """Inicializa o mixer do pygame e configura o volume padrão."""
        pygame.mixer.init()
        self.music_volume = 0.5  # Volume da música (0.0 a 1.0)
        self.sound_volume = 0.7  # Volume dos efeitos sonoros (0.0 a 1.0)

    def play_music(self, filename, loop=True):
        """Toca uma música de fundo em loop."""
        music_path = os.path.join(BASE_SOUND_PATH, "music", filename)
        if os.path.exists(music_path):
            pygame.mixer.music.load(music_path)
            pygame.mixer.music.set_volume(self.music_volume)
            pygame.mixer.music.play(-1 if loop else 0)
            print(f"[INFO] Tocando música: {music_path}")
        else:
            print(f"[ERRO] Arquivo de música não encontrado: {music_path}")

    def stop_music(self):
        """Para a música atual."""
        pygame.mixer.music.stop()
        print("[INFO] Música parada.")

    def play_sound(self, category, filename):
        """Toca um efeito sonoro específico."""
        sound_path = os.path.join(BASE_SOUND_PATH, category, filename)
        if os.path.exists(sound_path):
            sound = pygame.mixer.Sound(sound_path)
            sound.set_volume(self.sound_volume)
            sound.play()
            print(f"[INFO] Tocando som: {sound_path}")
        else:
            print(f"[ERRO] Arquivo de som não encontrado: {sound_path}")

    def set_music_volume(self, volume):
        """Ajusta o volume da música."""
        self.music_volume = max(0.0, min(1.0, volume))
        pygame.mixer.music.set_volume(self.music_volume)
        print(f"[INFO] Volume da música ajustado para: {self.music_volume}")

    def set_sound_volume(self, volume):
        """Ajusta o volume dos efeitos sonoros."""
        self.sound_volume = max(0.0, min(1.0, volume))
        print(f"[INFO] Volume dos efeitos sonoros ajustado para: {self.sound_volume}")

# Teste rápido (remova este bloco ao integrar no menu.py)
if __name__ == "__main__":
    sound_manager = SoundManager()
    sound_manager.play_music("m1.ogg")
    input("Pressione Enter para testar os sons...")
    sound_manager.play_sound("menu", "menu.flac")
    input("Pressione Enter para testar o som de confirmação...")
    sound_manager.play_sound("menu", "enter.flac")
    input("Pressione Enter para parar a música...")
    sound_manager.stop_music()
