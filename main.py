import flet as ft
import random
import string

def main(page: ft.Page):
    page.title = "🔐 Password Generator"
    page.padding = 30
    page.window_width = 500
    page.window_height = 550
    page.theme_mode = ft.ThemeMode.LIGHT

    password_output = ft.TextField(
        label="Ваш пароль",
        read_only=True,
        text_align=ft.TextAlign.CENTER,
        multiline=False,
        width=440,
        height=50,
        text_size=16,
        border_color="#2196f3",
        focused_border_color="#1976d2"
    )

    length_slider = ft.Slider(
        min=4,
        max=100,
        value=12,
        divisions=96,
        label="{value}",
        width=400
    )

    upper_check = ft.Checkbox(label="Заглавные буквы (A–Z)", value=True)
    lower_check = ft.Checkbox(label="Строчные буквы (a–z)", value=True)
    digits_check = ft.Checkbox(label="Цифры (0–9)", value=True)
    symbols_check = ft.Checkbox(label="Спецсимволы (!@#$%^&*...)", value=True)
    exclude_check = ft.Checkbox(label="Исключить похожие символы (0, O, 1, l...)", value=False)

    def copy_password(e):
        page.set_clipboard(password_output.value)
        page.snack_bar = ft.SnackBar(ft.Text("Пароль скопирован!"), open=True)
        page.update()

    def generate(e):
        length = int(length_slider.value)
        chars = ""
        if upper_check.value:
            chars += string.ascii_uppercase
        if lower_check.value:
            chars += string.ascii_lowercase
        if digits_check.value:
            chars += string.digits
        if symbols_check.value:
            chars += "!@#$%^&*()_+-=[]{}|;:,.<>?"

        if exclude_check.value:
            for c in "0O1lI":
                chars = chars.replace(c, "")

        if not chars:
            page.snack_bar = ft.SnackBar(ft.Text("Выберите хотя бы один тип символов!"), open=True)
            page.update()
            return

        password = ''.join(random.choice(chars) for _ in range(length))
        password_output.value = password
        page.update()

    page.add(
        ft.Text("Генератор надёжных паролей", size=24, weight=ft.FontWeight.BOLD),
        ft.Divider(height=20),
        ft.Column([
            ft.Text("Длина пароля:", size=14),
            length_slider
        ], spacing=5),
        ft.Divider(height=10),
        upper_check,
        lower_check,
        digits_check,
        symbols_check,
        exclude_check,
        ft.Divider(height=20),
        ft.ElevatedButton("Сгенерировать пароль", on_click=generate, width=220),
        ft.Divider(height=20),
        password_output,
        ft.ElevatedButton("Копировать", on_click=copy_password, width=220)
    )

ft.app(target=main)
