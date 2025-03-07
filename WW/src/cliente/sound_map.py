import os

class Map:
    def __init__(self, filename):
        """Inicializa o mapa a partir de um arquivo .mp."""
        self.name = None
        self.max_x = 0
        self.max_y = 0
        self.max_z = 0
        self.max_text = ""
        
        # Estruturas do mapa
        self.plataformas = []
        self.bordas_x = []
        self.bordas_y = []
        self.portas = []
        self.escadas = []
        self.zonas_texto = []
        self.elementos = []
        
        # Carregar o mapa
        self.load_map(filename)
    
    def load_map(self, filename):
        """Carrega os dados do mapa de um arquivo .mp"""
        path = os.path.join("src", "cliente", "mapas", filename)
        
        if not os.path.exists(path):
            raise FileNotFoundError(f"Arquivo {path} não encontrado!")
            
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue  # Ignorar linhas vazias e comentários
                    
                parts = line.split(":")
                tipo = parts[0]
                
                # Configurações gerais
                if tipo == "map":
                    self.name = parts[1]
                elif tipo == "maxx":
                    self.max_x = int(parts[1])
                elif tipo == "maxy":
                    self.max_y = int(parts[1])
                elif tipo == "maxz":
                    self.max_z = int(parts[1])
                elif tipo == "max_text":
                    self.max_text = parts[1]
                    
                # Plataformas
                elif tipo == "p":
                    min_y, max_y, min_x, max_x, tipo_piso = parts[1:6]
                    self.plataformas.append({
                        "min_x": int(min_x), "max_x": int(max_x),
                        "min_y": int(min_y), "max_y": int(max_y),
                        "tipo": tipo_piso
                    })
                    
                # Bordas
                elif tipo == "borderx":
                    min_x, max_x, nome = parts[1:4]
                    self.bordas_x.append({
                        "min_x": int(min_x), "max_x": int(max_x),
                        "nome": nome
                    })
                elif tipo == "bordery":
                    min_y, max_y, nome = parts[1:4]
                    self.bordas_y.append({
                        "min_y": int(min_y), "max_y": int(max_y),
                        "nome": nome
                    })
                    
                # Portas
                elif tipo == "door":
                    min_x, max_x, min_y, max_y, nome = parts[1:6]
                    self.portas.append({
                        "min_x": int(min_x), "max_x": int(max_x),
                        "min_y": int(min_y), "max_y": int(max_y),
                        "nome": nome
                    })
                    
                # Escadas
                elif tipo == "escada":
                    min_x, max_x, min_y, max_y, min_z, max_z, tipo_escada = parts[1:8]
                    self.escadas.append({
                        "min_x": int(min_x), "max_x": int(max_x),
                        "min_y": int(min_y), "max_y": int(max_y),
                        "min_z": int(min_z), "max_z": int(max_z),
                        "tipo": tipo_escada
                    })
                    
                # Zonas de texto
                elif tipo == "text":
                    min_x, max_x, min_y, max_y, min_z, max_z, texto = parts[1:8]
                    self.zonas_texto.append({
                        "min_x": int(min_x), "max_x": int(max_x),
                        "min_y": int(min_y), "max_y": int(max_y),
                        "min_z": int(min_z), "max_z": int(max_z),
                        "texto": texto
                    })
                    
                # Elementos (sons, efeitos)
                elif tipo == "e":
                    min_x, max_x, min_y, max_y, min_z, max_z, nome = parts[1:8]
                    self.elementos.append({
                        "min_x": int(min_x), "max_x": int(max_x),
                        "min_y": int(min_y), "max_y": int(max_y),
                        "min_z": int(min_z), "max_z": int(max_z),
                        "nome": nome
                    })
    
    def verificar_colisao(self, x, y, z):
        """Verifica se há uma barreira nas coordenadas (x, y, z)."""
        # Verificar bordas no eixo X
        for borda in self.bordas_x:
            if borda["min_x"] <= x <= borda["max_x"]:
                return True, borda["nome"]
                
        # Verificar bordas no eixo Y
        for borda in self.bordas_y:
            if borda["min_y"] <= y <= borda["max_y"]:
                return True, borda["nome"]
                
        return False, None
    
    def verificar_porta(self, x, y):
        """Verifica se o jogador está em uma porta."""
        for porta in self.portas:
            if (porta["min_x"] <= x <= porta["max_x"] and 
                porta["min_y"] <= y <= porta["max_y"]):
                return True, porta["nome"]
        return False, None
    
    def verificar_escada(self, x, y, z):
        """Verifica se o jogador está em uma escada."""
        for escada in self.escadas:
            if (escada["min_x"] <= x <= escada["max_x"] and
                escada["min_y"] <= y <= escada["max_y"] and
                escada["min_z"] <= z <= escada["max_z"]):
                return True, escada["tipo"]
        return False, None
    
    def get_texto_zona(self, x, y, z):
        """Retorna a descrição da zona em que o jogador está."""
        for zona in self.zonas_texto:
            if (zona["min_x"] <= x <= zona["max_x"] and
                zona["min_y"] <= y <= zona["max_y"] and
                zona["min_z"] <= z <= zona["max_z"]):
                return zona["texto"]
        
        return self.max_text  # Texto padrão se não houver zona específica
    
    def obter_tipo_de_piso(self, x, y):
        """Verifica o tipo de piso na posição do jogador."""
        for plataforma in self.plataformas:
            if (plataforma["min_x"] <= x <= plataforma["max_x"] and 
                plataforma["min_y"] <= y <= plataforma["max_y"]):
                return plataforma["tipo"]
        return None
    
    def obter_elementos_na_area(self, x, y, z):
        """Retorna os elementos na área do jogador."""
        elementos_ativos = []
        for elemento in self.elementos:
            if (elemento["min_x"] <= x <= elemento["max_x"] and
                elemento["min_y"] <= y <= elemento["max_y"] and
                elemento["min_z"] <= z <= elemento["max_z"]):
                elementos_ativos.append(elemento["nome"])
        return elementos_ativos