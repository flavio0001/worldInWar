import wx
from sound_manager import SoundManager
class GameFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="World in War", size=(400, 300))

        self.panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        # Título do jogo
        self.title_text = wx.StaticText(self.panel, label="The Endless War")
        vbox.Add(self.title_text, flag=wx.ALIGN_CENTER | wx.TOP, border=10)

        # Criando botões
        self.start_button = wx.Button(self.panel, label="Start Game")
        self.create_account_button = wx.Button(self.panel, label="Create Account")
        self.test_speakers_button = wx.Button(self.panel, label="Test Speakers")
        self.settings_button = wx.Button(self.panel, label="Settings")
        self.exit_button = wx.Button(self.panel, label="Exit The Game")

        # Adicionando botões ao layout
        for btn in [
            self.start_button,
            self.create_account_button,
            self.test_speakers_button,
            self.settings_button,
            self.exit_button,
        ]:
            vbox.Add(btn, flag=wx.ALIGN_CENTER | wx.TOP, border=10)

        self.panel.SetSizer(vbox)
        self.Center()

        # Lista de botões para navegação
        self.buttons = [
            self.start_button,
            self.create_account_button,
            self.test_speakers_button,
            self.settings_button,
            self.exit_button,
        ]
        self.current_index = 0

        # Foca no primeiro botão
        self.buttons[self.current_index].SetFocus()

        # Liga eventos de teclado ao painel
        self.panel.Bind(wx.EVT_CHAR_HOOK, self.on_key_press)

        # Liga eventos de clique nos botões
        self.start_button.Bind(wx.EVT_BUTTON, self.on_start_game)
        self.create_account_button.Bind(wx.EVT_BUTTON, self.on_create_account)
        self.test_speakers_button.Bind(wx.EVT_BUTTON, self.on_test_speaker)
        self.settings_button.Bind(wx.EVT_BUTTON, self.on_settings)
        self.exit_button.Bind(wx.EVT_BUTTON, self.on_exit_game)


        self.in_speaker_test = False

        # Criar e iniciar o gerenciador de som
        self.sound_manager = SoundManager()
        self.sound_manager.play_music("m1.ogg")


        # Evento para parar a música ao fechar a janela
        self.Bind(wx.EVT_CLOSE, self.on_close)

    def on_close(self, event):
        self.sound_manager.stop_music()
        event.Skip()

    def on_key_press(self, event):
        """Gerencia a navegação no menu com efeitos sonoros."""
        key_code = event.GetKeyCode()

        if self.in_speaker_test:
            if key_code == wx.WXK_LEFT:
                self.sound_manager.play_sound("menu", "left.ogg")
            elif key_code == wx.WXK_RIGHT:
                self.sound_manager.play_sound("menu", "right.ogg")
            elif key_code == wx.WXK_ESCAPE:
                self.exit_speaker_test()
                return

        previous_index = self.current_index  # Guarda o índice antes da mudança

        if key_code == wx.WXK_UP:
            self.current_index = (self.current_index - 1) % len(self.buttons)
        elif key_code == wx.WXK_DOWN:
            self.current_index = (self.current_index + 1) % len(self.buttons)
        elif key_code == wx.WXK_RETURN or key_code == wx.WXK_NUMPAD_ENTER:
            self.sound_manager.play_sound("menu", "enter.flac")  # Som de confirmação
            self.buttons[self.current_index].Command(wx.CommandEvent())  # Simula clique no botão
            return

        # Se o índice mudou, toca o som de navegação
        if self.current_index != previous_index:
            self.sound_manager.play_sound("menu", "menu.flac")

        self.buttons[self.current_index].SetFocus()

    def on_test_speaker(self, event):
        print("TEST mode of the speaker")
        self.sound_manager.stop_music()
        self.in_speaker_test = True
        self.title_text.SetLabel("Test speaker mode left | right | Esc to Exit")

    def exit_speaker_test(self):
        if not self.in_speaker_test:
            return
        print("back to the menu")
        self.in_speaker_test = False
        self.title_text.SetLabel("The Endless War")
        self.sound_manager.play_music("m1.ogg")

    def on_start_game(self, event):
        print("Starting Game...")

    def on_create_account(self, event):
        print("Creating Account...")


    def on_settings(self, event):
        print("Opening Settings...")

    def on_exit_game(self, event):
        print("Exiting Game...")
        self.Close()

    # Rodando a aplicação
if __name__ == "__main__":
    app = wx.App(False)
    frame = GameFrame()
    frame.Show()
    app.MainLoop()
