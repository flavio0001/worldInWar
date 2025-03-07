from mover import Mover

class Player(Mover):
    """Classe para representar um jogador no jogo."""
    
    players = []  # Lista global de jogadores

    def __init__(self, nome, x=0, y=0, z=0, velocidade=1.0):
        """Inicializa um jogador com nome, posição e status."""
        super().__init__(x, y, z, velocidade)
        self.nome = nome
        self.vida = 100
        self.energia = 100
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

    def interagir(self, objeto):
        """Simula interação com objetos do jogo."""
        print(f"{self.nome} interagiu com {objeto}!")

    def status(self):
        """Exibe o status atual do jogador."""
        return f"{self.nome} | Vida: {self.vida} | Energia: {self.energia} | Posição: ({self.x}, {self.y}, {self.z})"

# Testando a classe
if __name__ == "__main__":
    jogador1 = Player("Guerreiro", 0, 0, 0)
    jogador2 = Player("Mago", 10, 5, 0)

    print(jogador1.status())
    jogador1.mover("norte")
    jogador1.mover("leste", "correr")
    jogador1.interagir("Baú Antigo")
    print(jogador1.status())

    print(jogador2.status())
    Player.remove_player("Mago")
    print(Player.players)  # Verifica lista após remoção
