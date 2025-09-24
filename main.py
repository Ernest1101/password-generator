import tkinter as tk
from tkinter import messagebox, StringVar
import random
import string

def generate_password():
    try:
        length = int(length_var.get())
        if length <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Ошибка", "Длина пароля должна быть положительным числом!")
        return

    chars = ""
    if use_upper.get():
        chars += string.ascii_uppercase
    if use_lower.get():
        chars += string.ascii_lowercase
    if use_digits.get():
        chars += string.digits
    if use_symbols.get():
        chars += "!@#$%^&*()_+-=[]{}|;:,.<>?"

    if exclude_ambiguous.get():
        ambiguous = "0O1lI"
        chars = ''.join(c for c in chars if c not in ambiguous)

    if not chars:
        messagebox.showwarning("Предупреждение", "Выберите хотя бы один тип символов!")
        return

    password = ''.join(random.choice(chars) for _ in range(length))
    password_output.set(password)

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_output.get())
    messagebox.showinfo("Готово", "Пароль скопирован в буфер обмена!")

# Создаём окно
root = tk.Tk()
root.title("🔐 Генератор паролей")
root.geometry("400x300")
root.resizable(False, False)

# Переменные
length_var = StringVar(value="12")
use_upper = tk.BooleanVar(value=True)
use_lower = tk.BooleanVar(value=True)
use_digits = tk.BooleanVar(value=True)
use_symbols = tk.BooleanVar(value=True)
exclude_ambiguous = tk.BooleanVar(value=False)
password_output = StringVar()

# Элементы интерфейса
tk.Label(root, text="Длина пароля:").pack(pady=(10, 0))
tk.Entry(root, textvariable=length_var, width=10).pack()

tk.Checkbutton(root, text="Заглавные буквы (A-Z)", variable=use_upper).pack(anchor="w", padx=20)
tk.Checkbutton(root, text="Строчные буквы (a-z)", variable=use_lower).pack(anchor="w", padx=20)
tk.Checkbutton(root, text="Цифры (0-9)", variable=use_digits).pack(anchor="w", padx=20)
tk.Checkbutton(root, text="Спецсимволы (!@#$...)", variable=use_symbols).pack(anchor="w", padx=20)
tk.Checkbutton(root, text="Исключить похожие символы (0, O, 1, l...)", variable=exclude_ambiguous).pack(anchor="w", padx=20)

tk.Button(root, text="Сгенерировать пароль", command=generate_password, bg="#4CAF50", fg="white").pack(pady=10)

tk.Entry(root, textvariable=password_output, width=50, justify="center", state="readonly").pack(pady=5)

tk.Button(root, text="Копировать", command=copy_to_clipboard).pack(pady=5)

# Запуск
root.mainloop()
