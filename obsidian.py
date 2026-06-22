import flet as ft

def main(page: ft.Page):
    # Page settings
    page.title = "Obsidian Clicker"
    page.window.width = 600
    page.window.height = 400
    page.window.resizable = False
    page.window.maximizable = False
    page.window.icon = "img/icon.ico"

    page.fonts = {
        "Exo": "fonts/Exo-Medium.ttf",
        "Exo-Bold": "fonts/Exo-Bold.ttf",
        "Exo-Black": "fonts/Exo-Black.ttf"
    }
    page.theme = ft.Theme(font_family="Exo")

    def state_change(e):
        if enabledText.value == "Disabled":
            enable_clicker(e)
        else:
            disable_clicker(e)

    def enable_clicker(e):
        enabledText.value = "Enabled"
        enableButtonText.value = "Disable"
        page.update()

    def disable_clicker(e):
        enabledText.value = "Disabled"
        enableButtonText.value = "Enable"
        page.update()

    enabledText = ft.Text("Disabled", color="#ad8ed1", size=20)
    enableButtonText = ft.Text("Enable", color="#ad8ed1")
    enableButton = ft.OutlinedButton(content=enableButtonText, on_click=state_change, width=100, height=40)

    page.add(
        ft.Column(
            [
                enabledText,
                enableButton
            ],
        )
    )
    
ft.run(main)