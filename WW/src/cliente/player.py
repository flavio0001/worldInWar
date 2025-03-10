from mover import Mover

class Player(Mover):
    """Classe para representar um jogador no jogo."""
    
    players = []  # Lista global de jogadores

    def __init__(self, nome, mapa, sound_map, x=0, y=0, z=0, velocidade=1.0):
        """Inicializa um jogador com nome, posição e status."""
        super().__init__(x, y, z, velocidade)
        self.nome = nome
        self.vida = 100
        self.energia = 100
        self.mapa = mapa
        self.sound_map = sound_map
        self.id = len(Player.players)  # ID único do jogador
        Player.players.append(self)  # Adiciona à lista global

    @classmethod
    def get_player(cls, nome):
        """Retorna um jogador pelo nome, se existir."""
        for player in cls.players:
            if player.nome == nome:
                return player
        return None

    @classmethod
    def remove_player(cls, nome):
        """Remove um jogador da lista global."""
        for player in cls.players:
            if player.nome == nome:
                cls.players.remove(player)
                print(f"Jogador {nome} removido.")
                return True
        return False

    def mover(self, direcao, tipo_movimento="andar"):
        """Move o jogador e ajusta energia conforme a ação."""
        if self.energia <= 0:
            print(f"{self.nome} está cansado e não pode se mover!")
            return
        
        deslocamento = self.calcular_deslocamento(tipo_movimento)

        if tipo_movimento == "correr":
            self.energia -= 10  # Correr gasta mais energia
            deslocamento *= 2  
        elif tipo_movimento == "rastejar":
            self.energia -= 2  

        super().mover(direcao, tipo_movimento)

        if tipo_movimento == "andar":
            self.energia = min(self.energia + 5, 100)  # Regenera energia

        print(f"Nova posição de {self.nome}: ({self.x}, {self.y}, {self.z}) | Energia: {self.energia}")

        self.tocar_som_passo()  # Chama a função de som aqui

    def interagir(self, objeto):
        """Simula interação com objetos do jogo."""
        print(f"{self.nome} interagiu com {objeto}!")

    def status(self):
        """Exibe o status atual do jogador."""
        return f"{self.nome} | Vida: {self.vida} | Energia: {self.energia} | Posição: ({self.x}, {self.y}, {self.z})"

    def falar_coordenadas(self):
        return f"Posição: {self.x}, {self.y}, {self.z}"

    def falar_zona(self, mapa=None):
        if mapa:
            return mapa.get_texto_zona(self.x, self.y, self.z)
        return "Zona desconhecida"

    def tocar_som_passo(self):
        """Toca o som do piso correto quando o jogador anda."""
        if self.mapa and self.sound_map:
            tipo_piso = self.mapa.obter_tipo_de_piso(self.x, self.y)
            if tipo_piso:
                self.sound_map.play_step_sound(tipo_piso)
            else:
                print("⚠️ Nenhum piso detectado para tocar som.")
        else:
            print("⚠️ O jogador não tem um mapa ou sistema de som associado.")
