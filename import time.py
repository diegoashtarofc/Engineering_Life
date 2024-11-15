import time
import pickle

# Função para exibir mensagens com delay 
def print_with_delay(message, delay=2): # print_with_delay define aqui o delay padrão como 2s)
    print(message) 
    print() # Define espaçamento entre as linhas de Output (Exibição)
    time.sleep(delay) 

# Função de animação de carregamento (Sem função usual, apenas para UIX)
def loading_animation():
    print("Aguarde, calculando", end="")
    for _ in range(3):  # Número de repetições do ciclo
        for _ in range(3):
            time.sleep(1)  # Pausa de 1 segundo entre um ponto e outro
            print(".", end="", flush=True)
        time.sleep(1) # Retorna 1 segundo para exibir nova contagem
        print("\b\b\b   \b\b\b", end="", flush=True) # Aplica os pontos em delay 1 por 1 e remove todos de imediato retornando ""
    print(". Pronto!") # Mensagem final após a animação de carregamento
    print()

# Funções para salvar e carregar dados ('filename' chama a biblioteca de dados armazenados em input)
def salvar_dados(dados, filename="dados.pkl"):
    with open(filename, 'wb') as f: # Salva os dados virtualmente
        pickle.dump(dados, f)

def carregar_dados(filename="dados.pkl"):
    with open(filename, 'rb') as f:
        return pickle.load(f)

# Boas-vindas
print_with_delay("Bem-Vindo(a) ao gabarito do Competidor!", 2)

# Informações sobre pontos
print_with_delay("Cada vitória vale 300 pontos,", 2)
print_with_delay("cada empate vale 150 pontos. 2000 pontos te fazem campeão!", 2)

# Coleta de dados do usuário
Nome = input("Nome: ")
time.sleep(1)
Idade = input("Idade: ")
time.sleep(1)
País = input("País: ")
print()
time.sleep(1)

# Resultados
vitorias = int(input("Vitórias: "))
time.sleep(1)
empates = int(input("Empates: "))
print()
time.sleep(2)

# Animação de carregamento
loading_animation()

# Cálculo de pontos
pontos = (vitorias * 300) + (empates * 150)
total = f"Sua pontuação é: {pontos}!"
print_with_delay(total, 3)

# Salvar dados
dados = {"Nome": Nome, "Idade": Idade, "País": País, "Pontos": pontos}
salvar_dados(dados)
print_with_delay("Dados salvos com sucesso!", 2)

# Verificação de vitória
if pontos >= 2000:
    print_with_delay("Você é o campeão!!!", 2)
else:
    print_with_delay("Infelizmente você perdeu.", 2)

# Carregar dados (exemplo de uso)
print_with_delay("Carregando dados salvos...", 2)
dados_carregados = carregar_dados()
print_with_delay(f"Dados carregados: {dados_carregados}", 2)