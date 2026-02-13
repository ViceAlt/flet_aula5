import flet as ft

def main(page: ft.Page):
    page.title = "Game: Adivinhe a imagem"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

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
                    alignment=ft.MainAxisAlignment.CENTER
                )
            ]
        )
    )

ft.app(target=main)