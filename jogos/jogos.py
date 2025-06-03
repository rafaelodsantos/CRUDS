import json
import os

arquivo = 'jogos.json'

def carregar_dados():
  if not os.path.exists(arquivo):
    return []
  with open(arquivo, 'r') as f:
    return json.load(f)
  
def salvar_jogos(jogos):
  with open(arquivo, 'w') as f:
    json.dump(jogos, f, indent = 4)

def gerar_novo_id(jogos):
  ids_usados = sorted([j['id'] for j in jogos])
  novo_id = 1
  for id_existente in ids_usados:
    if novo_id == id_existente:
      novo_id += 1
    else:
      break
  return novo_id

def criar_jogo():
  jogos = carregar_dados()
  novo_id = gerar_novo_id(jogos)
  nome = input('Digite o nome do jogo: ')
  categoria = input('Digite a categoria: ')
  jogos.append({'id':novo_id, 'nome':nome, 'categoria': categoria})
  salvar_jogos(jogos)
  print('Jogo Salvo com sucesso!')

def listar_jogos():
  jogos = carregar_dados()
  jogos_ordenados = sorted(jogos, key=lambda j: j['id'])
  if not jogos:
    print('Não há jogos registrados')
  for j in jogos_ordenados:
    print(f'{j['id']} - {j['nome']} ({j['categoria']})')

def atualizar_jogo():
  jogos = carregar_dados()
  id_alvo = int(input('ID do jogo para atualizar: '))
  for j in jogos:
    if j['id'] == id_alvo:
      j['nome'] = input(f'Novo nome (atual: {j['nome']}): ') or j['nome']
      j['categoria'] = input(f'Nova categoria (atual: {j['categoria']}): ') or j['categoria']
      salvar_jogos(jogos)
      print('Jogo atualizado com sucesso!')
      return
  print('Jogo não encontrado')

def deletar_jogo():
  jogos = carregar_dados()
  id_alvo = int(input('Digite o jogo que deseja deletar: '))
  novo_jogos = [j for j in jogos if j['id'] != id_alvo]
  if len(novo_jogos) != len(jogos):
    salvar_jogos(novo_jogos)
    print('Jogo apagado com sucesso!')
  else:
    print('Jogo não encontrado')

def menu():
  while True:
    print('\nMenu Avaliação de Jogos')
    print('1 - Criar Jogo')
    print('2 - Listar Jogo')
    print('3 - Atualizar Jogo')
    print('4 - Deletar Jogo')
    print('0 - Sair')

    opcao = input('Qual opção deseja selecionar: ')

    if opcao == '1':
      criar_jogo()
    if opcao == '2':
      listar_jogos()
    if opcao == '3':
      atualizar_jogo()
    if opcao == '4':
      deletar_jogo()
    if opcao == '0':
      print('Saindo...')
      break
    else:
      print('Opção iválida')

if __name__ == '__main__':
  menu()  