
#Crie um programa que pede ao usuário para digitar a largura e o comprimento de um retângulo e, 
#em seguida, calcula e exibe a área

# Função para solicitar um número válido ao usuário

def obter_numero(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            return valor # Retorna o valor se for um número
        except ValueError:
            print("Erro: por favor, insira apenas números.")

# Solicita a largura e o comprimento com validação
largura = obter_numero("Digite a largura: ")
comprimento = obter_numero("Digite o comprimento: ")

# Verifica se os valores são positivos
if largura > 0 and comprimento > 0:
    area = largura * comprimento
    print(f"A área do retangulo é: {area:.2f}")
else:
    print("A largura e o comprimento devem ser valores positivos.")
