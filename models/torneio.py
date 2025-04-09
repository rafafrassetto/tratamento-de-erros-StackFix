import logging
from .partida import Partida

logger = logging.getLogger(__name__)

class Torneio:
    def __init__(self):
        self.times = set()
        self.partidas = []
        self.pontuacao = {}

    def adicionar_time(self, nome):
        if not nome or not nome.strip():
            logger.error("Erro: Nome inválido")
            print("❌ Erro: Nome inválido")
            return
        self.times.add(nome)
        self.pontuacao[nome] = 0
        print(f"✅ Time \"{nome}\" adicionado com sucesso!")

    def criar_partida(self, time1, time2, gols1, gols2):
        try:
            if time1 not in self.times or time2 not in self.times:
                raise ValueError("Time não existe")
            if gols1 < 0 or gols2 < 0:
                raise ValueError("Número inválido de gols")
            partida = Partida(time1, time2, gols1, gols2)
            self.partidas.append(partida)
            self._atualizar_pontos(time1, time2, gols1, gols2)
            print(f"✅ Partida entre \"{time1}\" e \"{time2}\" criada com sucesso!")
        except Exception as e:
            logger.error(f"Erro: {e}")
            print(f"❌ Erro: {e}")

    def _atualizar_pontos(self, time1, time2, gols1, gols2):
        if gols1 > gols2:
            self.pontuacao[time1] += 3
        elif gols1 < gols2:
            self.pontuacao[time2] += 3
        else:
            self.pontuacao[time1] += 1
            self.pontuacao[time2] += 1

    def jogar(self):
        return ResultadoTorneio(self.pontuacao, self.partidas)


class ResultadoTorneio:
    def __init__(self, pontuacao, partidas):
        self.pontuacao = pontuacao
        self.partidas = partidas

    def imprimirClassificacao(self):
        print("\nClassificação Final:")
        ranking = sorted(self.pontuacao.items(), key=lambda x: -x[1])
        for i, (time, pontos) in enumerate(ranking, 1):
            print(f"{i}. {time} ({pontos} pontos)")

    def imprimirResultados(self):
        print("\nResultados:")
        for partida in self.partidas:
            print(partida.resultado())
