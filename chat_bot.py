import Levenshtein
import sys


def carregar_perguntas(arquivo):
    perguntas_respostas = {}
    with open(arquivo, "r", encoding="utf-8") as f:
        for linha in f:
            pergunta, resposta = linha.strip().split("|")
            perguntas_respostas[pergunta.lower()] = resposta
    return perguntas_respostas


def encontrar_resposta(pergunta, perguntas_respostas, limiar_distancia=5):
    menor_distancia = float("inf")
    melhor_resposta = ""
    for p, r in perguntas_respostas.items():
        distancia = Levenshtein.distance(pergunta, p)
        if distancia < menor_distancia:
            menor_distancia = distancia
            melhor_resposta = r
    if menor_distancia <= limiar_distancia:
        return melhor_resposta
    else:
        return "Pergunta não encontrada."


if __name__ == "__main__":
    perguntas_respostas = carregar_perguntas("perguntas.txt")

    if len(sys.argv) == 2:
        limiar_distancia = int(sys.argv[1])
        # Modo Jenkins: processar perguntas do arquivo perguntas_automaticas.txt
        with open("perguntas_automaticas.txt", "r", encoding="utf-8") as f:
            perguntas = [linha.strip() for linha in f]
        for pergunta in perguntas:
            resposta = encontrar_resposta(
                pergunta.lower(), perguntas_respostas, limiar_distancia
            )
            print(f"Pergunta: {pergunta}")
            print(f"Resposta: {resposta}")
    else:
        limiar_distancia = int(
            input(
                "Digite o limiar de distância para considerar uma pergunta semelhante:"
            )
        )
        # Modo interativo: processar perguntas do usuário
        while True:
            pergunta = input("Faça uma pergunta:").lower()
            if pergunta == "sair":
                break
            resposta = encontrar_resposta(
                pergunta, perguntas_respostas, limiar_distancia
            )
            print("Resposta:", resposta)
