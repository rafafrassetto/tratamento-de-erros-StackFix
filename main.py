import logging
from models.torneio import Torneio

# logs
logging.basicConfig(
    filename='log/erros.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def main():
    torneio = Torneio()

    # times
    torneio.adicionar_time("Brasil")
    torneio.adicionar_time("")  # ❌ Erro
    torneio.adicionar_time("Canadá")
    torneio.adicionar_time("Argentina")
    torneio.adicionar_time("Angola")

    # partidas
    torneio.criar_partida("Brasil", "Canadá", 1, 0)
    torneio.criar_partida("Argentina", "Angola", 0, 1)
    torneio.criar_partida("Brasil", "Argentina", -10, -2)  # ❌ Erro
    torneio.criar_partida("Brasil", "Argentina", 0, 2)
    torneio.criar_partida("Angola", "Canadá", 1, 1)
    torneio.criar_partida("Brasil", "Angola", 3, 2)
    torneio.criar_partida("Argentina", "Nigéria", 3, 3)  # ❌ Erro
    torneio.criar_partida("Argentina", "Canadá", 2, 4)

    # resultado final
    resultado = torneio.jogar()
    resultado.imprimirClassificacao()
    resultado.imprimirResultados()

if __name__ == "__main__":
    main()
