class Processo:
    def __init__(self, num, coord):
        self.id = num
        self.coordenador = coord
        self.ativo = True
        self.mensagensEnviadas = []
        self.mensagensRecebidas = []

    def enviar_election(self):
        self.mensagensEnviadas.append(f"ELECTION P{self.id+1}")
        return f'ELECTION P{self.id+1}'

    def enviar_ok(self):
        self.mensagensEnviadas.append(f"OK P{self.id+1}")
        return f'OK P{self.id+1}'

    def enviar_coordinator(self):
        self.mensagensEnviadas.append(f"COORDINATOR P{self.id+1}")
        return f'COORDINATOR P{self.id+1}'

    def receber_mensagem(self, msg):
        self.mensagensRecebidas.append(msg)
        if msg[:11] == 'COORDINATOR':
            print("entrou no if do receber_mensagem")
            self.coordenador = int(msg[13:])-1
        return msg + f' P{self.id+1}'