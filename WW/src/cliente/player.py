class Player:
    # Lista para armazenar todos os jogadores
    players = []
    
    def __init__(self, charname, x=1, y=0, current_time=0):
        self.map = ""
        self.charname = charname
        self.x = x
        self.y = y
        self.beeping = 1
        self.pacifico = 0
        self.beacontime = 1250  # Valor fixo em vez de aleatório
        self.beacontimer = current_time  # Armazena o tempo fornecido externamente
    
    @classmethod
    def new_player(cls, charname, x, y, current_time=0):
        # Verifica se o jogador já existe
        for player in cls.players:
            if player.charname == charname:
                return
        
        # Cria um novo jogador e adiciona à lista
        new_player = cls(charname, x, y, current_time)
        cls.players.append(new_player)
    
    @classmethod
    def update_player(cls, name, x, y, map_name):
        # Atualiza a posição e mapa do jogador
        for player in cls.players:
            if player.charname == name:
                player.map = map_name
                player.x = x
                player.y = y
                break
    
    @classmethod
    def update_player2(cls, name, x, y, map_name, me, un):
        # Atualiza o jogador e também o jogador principal se for o mesmo
        for player in cls.players:
            if player.charname == name:
                player.map = map_name
                player.x = x
                player.y = y
                break
        
        if un == name:
            me.x = x
            me.y = y
    
    @classmethod
    def remove_player(cls, who, playertrack=""):
        # Remove um jogador da lista
        for i, player in enumerate(cls.players):
            if player.charname == who:
                if playertrack == who:
                    playertrack = ""
                cls.players.pop(i)
                return playertrack
        return playertrack
    
    @classmethod
    def beacon_loop(cls, current_time, mapname, me, p, un, playertrack=""):
        # Emite sons de beacon para os jogadores quando o timer expirar
        
        for player in cls.players:
            # Pula jogadores em mapas específicos
            if player.map == "t nel" or player.map == "quadro":
                continue
            
            # Verifica se é hora de emitir o beacon
            elapsed = current_time - player.beacontimer
            if (elapsed >= player.beacontime and 
                player.map == mapname and 
                player.beeping == 1 and 
                player.charname != un):
                
                # Reinicia o timer
                player.beacontimer = current_time
                
                # Reproduz o som apropriado
                if playertrack != player.charname:
                    if player.pacifico == 0:
                        p.play_2d("beacon.ogg", me.x, me.y, player.x, player.y, False)
                    elif player.pacifico == 1:
                        p.play_2d("bip.ogg", me.x, me.y, player.x, player.y, False)
                else:
                    p.play_2d("beacon2.ogg", me.x, me.y, player.x, player.y, False)
    
    @classmethod
    def get_player(cls, name):
        # Retorna o índice do jogador na lista
        for i, player in enumerate(cls.players):
            if player.charname == name:
                return i
        return -1
    
    @classmethod
    def get_player_instance(cls, name):
        # Retorna a instância do jogador pelo nome
        for player in cls.players:
            if player.charname == name:
                return player
        return None