import flet as ft
import math

def main(page: ft.Page):
    # Page settings
    page.title = "Obsidian Clicker"
    page.window.width = 400
    page.window.height = 400
    page.window.resizable = False
    page.window.maximizable = False
    page.padding = 0
    page.spacing = 0
    page.window.icon = "img/icon.ico"
    page.window.title_bar_hidden = True
    page.fonts = {
        "Exo": "fonts/Exo-Medium.ttf",
        "Exo-Bold": "fonts/Exo-Bold.ttf",
        "Exo-Black": "fonts/Exo-Black.ttf",
        "Ramabhadra": "fonts/Ramabhadra-Regular.ttf",
    }
    page.theme = ft.Theme(
        font_family="Exo",
        slider_theme=ft.SliderTheme(
            active_track_color="#ad8ed1",
            inactive_track_color="#252525",
            track_height=18,
            thumb_color="#ffffff",
            overlay_color=ft.Colors.with_opacity(0, "#ffffff"),
            active_tick_mark_color=ft.Colors.with_opacity(0, "#ffffff"),
            inactive_tick_mark_color=ft.Colors.with_opacity(0, "#ffffff"),
            padding=0,
        )
    )
    page.bgcolor = "#080808"

    def close(e):
        page.window.close()

    def minimize(e):
        page.window.minimized = True
        page.update()

    def toggle():
        if enabled:
            disable_clicker()
        else:
            enable_clicker()

    def enable_clicker():
        nonlocal enabled
        enabled = True
        enabledText.value = "Enabled"
        enabledText.color = "#080808"
        enable_button.style.bgcolor = "#ad8ed1"
        page.update()

    def disable_clicker():
        nonlocal enabled
        enabled = False
        enabledText.value = "Disabled"
        enabledText.color = "#ad8ed1"
        enable_button.style.bgcolor = "#080808"
        page.update()

    def on_lc_slider_change(e):
        v = math.floor(lc_slider.value)
        lc_value_text.value = f"{v} CPS"
        visible = v >= 15
        lc_high_cps_button.opacity = 1 if visible else 0
        lc_high_cps_button.disabled = not visible
        page.update()

    def on_rc_slider_change(e):
        v = math.floor(rc_slider.value)
        rc_value_text.value = f"{v} CPS"
        page.update()

    def show_tooltip():
        print()
    

    enabled = False
    enabledText = ft.Text("Disabled", color="#ad8ed1", font_family="Ramabhadra", size=10)
    lc_value_text = ft.Text("10 CPS", color="#ad8ed1", size=15, width=60)
    rc_value_text = ft.Text("10 CPS", color="#ad8ed1", size=15)

    enable_button = ft.OutlinedButton(
        content=enabledText,
        on_click=toggle,
        width=95,
        height=25,
        style=ft.ButtonStyle(
            side=ft.BorderSide(1, "#ad8ed1"),
            bgcolor="#080808",
            overlay_color=ft.Colors.with_opacity(0, "#ffffff"),
        ),
    )

    lc_high_cps_button = ft.IconButton(
        icon=ft.Icon(ft.Icons.WARNING, size=12),
        bgcolor="#500505",
        opacity=0,
        hover_color=ft.Colors.with_opacity(0, "#ffffff"),
        disabled=True,
        height=30,
        width=30,
        style=ft.ButtonStyle(
            padding=0,
            side=ft.BorderSide(1, "#BB5555"),
            shape=ft.RoundedRectangleBorder(radius=10),
            overlay_color=ft.Colors.with_opacity(0, "#ffffff"),
        ),
        on_hover=show_tooltip
    )

    lc_slider = ft.Slider(
        min=1,
        max=20,
        value=10,
        width=350,
        on_change=on_lc_slider_change
    )

    rc_slider = ft.Slider(
        min=1,
        max=20,
        value=10,
        width=350,
        on_change=on_rc_slider_change
    )

    left_click_cps = ft.Container(
        padding=ft.Padding(20, 0, 20, 5),
        content=ft.Column(
            spacing=5,
            controls=[
                ft.Row(
                    controls=[
                        ft.Text("Left Mouse Button - ", color="#ffffff", size=15),
                        lc_value_text,
                        ft.Row(
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                         
                            controls=[lc_high_cps_button],
                        ),
                    ],
                    spacing=0,
                ),
                ft.Row(
                    controls=[lc_slider],
                    alignment=ft.CrossAxisAlignment.CENTER,
                )
            ],
        ),
    )

    right_click_cps = ft.Container(
        padding=ft.Padding(20, 0, 20, 5),
        content=ft.Column(
            spacing=8,
            controls=[
                ft.Row(
                    controls=[
                        ft.Text("Right Mouse Button - ", color="#ffffff", size=15),
                        rc_value_text,
                    ],
                    spacing=0,
                ),
                ft.Row(
                    controls=[rc_slider],
                    alignment=ft.CrossAxisAlignment.CENTER,
                )
            ],
        ),
    )

    minimize_button = ft.IconButton(
        icon=ft.Icons.REMOVE,
        icon_color="#d4d4d4",
        icon_size=20,
        on_click=minimize,
        width=30,
        height=30,
        style=ft.ButtonStyle(
            padding=0,
            bgcolor=ft.Colors.with_opacity(0, "#ffffff"),
            overlay_color=ft.Colors.with_opacity(0.08, "#ffffff"),
            shape=ft.RoundedRectangleBorder(radius=5),
        ),
    )
 
    close_button = ft.IconButton(
        icon=ft.Icons.CLOSE,
        icon_color="#d4d4d4",
        icon_size=20,
        on_click=close,
        width=30,
        height=30,
        style=ft.ButtonStyle(
            padding=0,
            bgcolor=ft.Colors.with_opacity(0, "#ffffff"),
            overlay_color=ft.Colors.with_opacity(0.08, "#ffffff"),
            shape=ft.RoundedRectangleBorder(radius=5),
        ),
    )

    title_bar = ft.WindowDragArea(
        content=ft.Container(
            bgcolor="#1D1D1D",
            expand=True,
            content=ft.Column(
                controls=[
                    ft.Container(
                        padding=ft.Padding(10, 10, 10, 0),
                        content=ft.Row(
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            controls=[
                                ft.Row(
                                    spacing=8,
                                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                    controls=[
                                        ft.Image(src="img/icon.ico", width=30, height=30),
                                        ft.Text(
                                            spans=[
                                                ft.TextSpan("Obsidian", style=ft.TextStyle(size=20, color="#ad8ed1")),
                                                ft.TextSpan(" v1.0", style=ft.TextStyle(size=12, color="#666666",)),
                                            ]
                                        ),
                                        ft.Container(width=10),
                                        enable_button
                                    ],
                                ),
                                ft.Row(
                                    spacing=8,
                                    controls=[
                                        minimize_button, 
                                        close_button
                                    ],
                                ),
                            ],
                        ),
                    ),
                    ft.Divider(height=1, color="#ad8ed1", thickness=1, leading_indent=0, trailing_indent=0),
                ]
            )
        ),
    )

    root = ft.Container(
        expand=True,
        bgcolor="#0d0d0d",
        border=ft.Border.all(1),
        border_radius=7,
        content=ft.Column(
            spacing=10,
            controls=[
                title_bar,
                left_click_cps,
                right_click_cps,
            ]
        )
    )

    page.add(root)

ft.run(main)