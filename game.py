import flet as ft

def main(page: ft.Page):
    mensagem = ft.Text("Escolha a opção correta!")
    resposta_correta = "Tijolo"
    def verificar_resposta(e):
        if e.control.content == resposta_correta:
            mensagem.value = "Parabens"
        else:
            mensagem.value = "Resposta errada"
        page.update()


    page.title = "Game: Adivinhe a imagem"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = ft.Colors.BLACK

    page.add(
        
        ft.Column(
            controls=[
                ft.Text(
                    "Adivinhe a Imagem",
                    size=24,
                    weight="bold"
                ),
                ft.Image(
                    src="image/gato.jpg",
                    height=200,
                ),
                mensagem,
                ft.Row(
                    controls=[
                        ft.Button(
                            content="Gato",
                            on_click=verificar_resposta
                        ),
                        ft.Button(
                            content="Cachorro",
                            on_click=verificar_resposta
                        ),
                        ft.Button(
                            content="Tatu",
                            on_click=verificar_resposta
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Button(
                            content="Tijolo",
                            on_click=verificar_resposta,
                            color=ft.Colors.BLACK_12,
                            bgcolor=ft.Colors.BLACK_12,
                        ),
                
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

ft.app(target=main)