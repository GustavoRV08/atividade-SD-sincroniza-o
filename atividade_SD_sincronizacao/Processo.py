class Processo:
    def __init__(self, num, coord):
        self.id = num
        self.coordenador = coord
        self.ativo = True
        self.mensagensEnviadas = []
        self.mensagensRecebidas = []

    def enviar_election(self, origem):
        self.mensagensEnviadas.append(f"ELECTION P{origem+1}")
        return f'ELECTION P{origem+1}'

    def enviar_ok(self, origem):
        self.mensagensEnviadas.append(f"OK P{origem+1}")
        return f'OK P{origem+1}'

    def enviar_coordinator(self, origem):
        self.mensagensEnviadas.append(f"COORDINATOR P{origem+1}")
        return f'COORDINATOR P{origem+1}'

    def receber_mensagem(self, msg):
        self.mensagensRecebidas.append(msg)
        if msg[:11] == 'COORDINATOR':
            self.coordenador = int(msg[13:])
        return msg + f' P{self.id+1}'