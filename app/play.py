from engine import run

if __name__ == "__main__":
    time_out = 0
    turns = []
    turns_media = 0
    wins_percentage_behavior = {'impulsivo': 0, 'exigente': 0, 'cauteloso': 0, 'aleatorio': 0}
    most_behavior_wins = 0
    for i in range(300):
        temp = run()
        turns.append(temp['rounds'])
        a = temp['champion'].personality()
        if temp['champion'].personality() == 'impulsivo':
            wins_percentage_behavior['impulsivo'] += 1

        elif temp['champion'].personality() == 'exigente':
            wins_percentage_behavior['exigente'] += 1

        elif temp['champion'].personality() == 'cauteloso':
            wins_percentage_behavior['cauteloso'] += 1

        elif temp['champion'].personality() == 'aleatorio':
            wins_percentage_behavior['aleatorio'] += 1

        if temp['rounds'] == 'time out':
            time_out += 1

    for i in range(len(turns)):
        turns_media += turns[i]

    max_key = max(wins_percentage_behavior, key=wins_percentage_behavior.get)
    wins_percentage_behavior['impulsivo'] = f"{(wins_percentage_behavior['impulsivo'] * 100) / 300:.2f}%"
    wins_percentage_behavior['exigente'] = f"{(wins_percentage_behavior['exigente'] * 100) / 300:.2f}%"
    wins_percentage_behavior['cauteloso'] = f"{(wins_percentage_behavior['cauteloso'] * 100) / 300:.2f}%"
    wins_percentage_behavior['aleatorio'] = f"{(wins_percentage_behavior['aleatorio'] * 100) / 300:.2f}%"
    print(f"Quantas partidas terminam por time out (1000 rodadas)? --> {time_out}")
    print(f"Quantos turnos em média demora uma partida? --> {turns_media / len(turns):.2f}")
    print(f"Qual a porcentagem de vitórias por comportamento dos jogadores? --> {wins_percentage_behavior}")
    print(f"Qual o comportamento que mais vence? --> {max_key}")
