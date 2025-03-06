import os

# Define a pasta de mapas com caminho dinâmico
BASE_MAPA_PATH = os.path.join(os.path.dirname(__file__), "mapas")

class Mapa:
    def __init__(self, arquivo):
        """Carrega um mapa de um arquivo .mp"""
        self.nome = None
        self.max_x = 0
        self.max_y = 0
        self.max_z = 0
        self.plataformas = []
        self.bordas = []
        self.textos = []
        self.escadas = []

        self.carregar_mapa(arquivo)

    def carregar_mapa(self, arquivo):
        """Lê e processa um arquivo de mapa"""
        caminho = os.path.join(BASE_MAPA_PATH, arquivo)

        if not os.path.exists(caminho):
            raise FileNotFoundError(f"❌ ERRO: Arquivo de mapa '{arquivo}' não encontrado em {BASE_MAPA_PATH}")

        with open(caminho, "r", encoding="utf-8") as f:
            linhas = f.readlines()

        for linha in linhas:
            linha = linha.strip()
            if not linha or linha.startswith("#"):  
                continue  # Ignora comentários e linhas vazias

            partes = linha.split(":")
            tipo = partes[0]

            if tipo == "map":
                self.nome = partes[1]

            elif tipo == "maxx":
                self.max_x = int(partes[1])

            elif tipo == "maxy":
                self.max_y = int(partes[1])

            elif tipo == "maxz":
                self.max_z = int(partes[1])

            elif tipo == "p":  # Plataforma (piso)
                min_y, max_y, min_x, max_x, tipo_plataforma = partes[1:6]
                self.plataformas.append({
                    "min_y": int(min_y), "max_y": int(max_y),
                    "min_x": int(min_x), "max_x": int(max_x),
                    "tipo": tipo_plataforma
                })

            elif tipo == "border":  # Borda
                min_y, max_y, min_x, max_x, min_z, max_z, tipo_borda = partes[1:8]
                self.bordas.append({
                    "min_y": int(min_y), "max_y": int(max_y),
                    "min_x": int(min_x), "max_x": int(max_x),
                    "min_z": int(min_z), "max_z": int(max_z),
                    "tipo": tipo_borda
                })

            elif tipo == "text":  # Texto/Zona
                min_y, max_y, min_x, max_x, min_z, max_z, descricao = partes[1:8]
                self.textos.append({
                    "min_y": int(min_y), "max_y": int(max_y),
                    "min_x": int(min_x), "max_x": int(max_x),
                    "min_z": int(min_z), "max_z": int(max_z),
                    "descricao": descricao
                })

            elif tipo == "escada":  # Escada
                min_y, max_y, min_x, max_x, min_z, max_z, tipo_escada = partes[1:8]
                self.escadas.append({
                    "min_y": int(min_y), "max_y": int(max_y),
                    "min_x": int(min_x), "max_x": int(max_x),
                    "min_z": int(min_z), "max_z": int(max_z),
                    "tipo": tipo_escada
                })

    def obter_tipo_de_piso(self, x, y):
        """Verifica o tipo de piso na posição do jogador."""
        for plataforma in self.plataformas:
            if plataforma["min_x"] <= x <= plataforma["max_x"] and plataforma["min_y"] <= y <= plataforma["max_y"]:
                return plataforma["tipo"]  # Retorna o tipo do piso encontrado
        return None  # Nenhum piso encontrado

    def verificar_colisao(self, x, y, z):
        """Verifica se um ponto (x, y, z) colide com uma borda."""
        for borda in self.bordas:
            if borda["min_x"] <= x <= borda["max_x"] and \
               borda["min_y"] <= y <= borda["max_y"] and \
               borda["min_z"] <= z <= borda["max_z"]:
                return True  # Colisão detectada
        return False  # Nenhuma colisão

    def obter_texto_zona(self, x, y, z):
        """Retorna a descrição da zona onde o jogador está."""
        for texto in self.textos:
            if texto["min_x"] <= x <= texto["max_x"] and \
               texto["min_y"] <= y <= texto["max_y"] and \
               texto["min_z"] <= z <= texto["max_z"]:
                return texto["descricao"]
        return None  # Nenhuma zona encontrada
