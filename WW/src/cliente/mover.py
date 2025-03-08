class Mover:
    def __init__(self, x=0, y=0, z=0, velocidade=1.0):
        """Inicializa a posição e velocidade do objeto."""
        self.x = x
        self.y = y
        self.z = z
        self.velocidade = velocidade  # Unidade de deslocamento por movimento

    def mover(self, direcao, tipo_movimento="andar"):
        """
        Move o objeto em uma direção específica.
        
        :param direcao: Direção do movimento ("norte", "sul", "leste", "oeste", etc.).
        :param tipo_movimento: Tipo de movimento ("andar", "voar", "rastejar", "nadar").
        """
        deslocamento = self.calcular_deslocamento(tipo_movimento)
        
        if direcao == "norte":
            self.y += deslocamento
        elif direcao == "sul":
            self.y -= deslocamento
        elif direcao == "leste":
            self.x += deslocamento
        elif direcao == "oeste":
            self.x -= deslocamento
        elif direcao == "noroeste":
            self.x -= deslocamento
            self.y += deslocamento
        elif direcao == "nordeste":
            self.x += deslocamento
            self.y += deslocamento
        elif direcao == "sudoeste":
            self.x -= deslocamento
            self.y -= deslocamento
        elif direcao == "sudeste":
            self.x += deslocamento
            self.y -= deslocamento
        elif direcao == "subir":
            self.z += deslocamento
        elif direcao == "descer":
            self.z -= deslocamento

        self.x = int(self.x)
        self.y = int(self.y)
        self.z = int(self.z)

        print(f"Movido para {self.x}, {self.y}, {self.z} via {tipo_movimento}")

    def calcular_deslocamento(self, tipo_movimento):
        """
        Define o deslocamento com base no tipo de movimento.
        Alguns movimentos podem ser mais rápidos/lentos.
        """
        if tipo_movimento == "andar":
            return self.velocidade
        elif tipo_movimento == "voar":
            return self.velocidade * 1.5
        elif tipo_movimento == "rastejar":
            return self.velocidade * 0.5
        elif tipo_movimento == "nadar":
            return self.velocidade * 0.8
        else:
            return self.velocidade

# Exemplo de uso
if __name__ == "__main__":
    objeto = Mover(10, 20, 0)
    objeto.mover("norte")
    objeto.mover("voar", "subir")
    objeto.mover("rastejar", "sudoeste")
