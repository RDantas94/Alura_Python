# Tela inicial:
# Título: Hashzap
# Botão: Iniciar Chat
# Quando clicar no botão:
# abrir um popup/modal/alerta
# Título: Bem vindo ao hashzap
# Caixa de Texto: Escreva seu nome no chat
# Botão: Entrar no chat
# Quando clicar no botão:
# fechar o popup
# Sumir com o título
# Sumir com o botão Iniciar Chat
# Carregar o chat
# Carregar o campo de enviar mensagem: "Digite sua mensagem"
# Botão Enviar
# Quando clicar no botão enviar
# Enviar a mensagem
# limpar a caixa de mensagem

# importar o flet
import flet as ft

# criar uma função principal para rodar o seu aplicativo


def main(pagina):
    texto = ft.Text("Hashzap")

    chat = ft.Column()

    nome_usuario = ft.TextField(label="Escreva seu nome")

    def enviar_mensagem_tunel(mensagem):
        tipo = mensagem["tipo"]
        if tipo == "mensagem":
            texto_mensagem = mensagem["texto"]
            usuario_mensagem = mensagem["usuario"]
            # adicionar a mensagem no chat
            chat.controls.append(
                ft.Text(f"{usuario_mensagem}: {texto_mensagem}"))
        else:
            usuario_mensagem = mensagem["usuario"]
            chat.controls.append(ft.Text(f"{usuario_mensagem} entrou no chat",
                                         size=12, italic=True, color=ft.colors.ORANGE_500))
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
        pagina.pubsub.send_all({"texto": campo_mensagem.value, "usuario": nome_usuario.value,
                                "tipo": "mensagem"})
        # limpar o campo de mensagem
        campo_mensagem.value = ""
        pagina.update()

    campo_mensagem = ft.TextField(
        label="Digite uma mensagem", on_submit=enviar_mensagem)
    botao_enviar_mensagem = ft.ElevatedButton(
        "Enviar", on_click=enviar_mensagem)

    def entrar_popup(evento):
        pagina.pubsub.send_all(
            {"usuario": nome_usuario.value, "tipo": "entrada"})
        # adicionar o chat
        pagina.add(chat)
        # fechar o popup
        popup.open = False
        # remover o botao iniciar chat
        pagina.remove(botao_iniciar)
        pagina.remove(texto)
        # criar o campo de mensagem do usuario
        # criar o botao de enviar mensagem do usuario
        pagina.add(ft.Row(
            [campo_mensagem, botao_enviar_mensagem]
        ))
        pagina.update()

    popup = ft.AlertDialog(
        open=False,
        modal=True,
        title=ft.Text("Bem vindo ao Hashzap"),
        content=nome_usuario,
        actions=[ft.ElevatedButton("Entrar", on_click=entrar_popup)],
    )

    def entrar_chat(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()

    botao_iniciar = ft.ElevatedButton("Iniciar chat", on_click=entrar_chat)

    pagina.add(texto)
    pagina.add(botao_iniciar)


ft.app(target=main, port=8000)

# deploy
