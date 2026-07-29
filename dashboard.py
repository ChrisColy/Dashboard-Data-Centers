# DASHBOARD SIMPLES - CRESCIMENTO DE DATA CENTERS

import tkinter as tk
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# ---------------- JANELA ----------------

janela = tk.Tk()
janela.title("Dashboard Data Centers")
janela.geometry("900x600")
janela.configure(bg="#1e1e1e")

# ---------------- TÍTULO ----------------

titulo = tk.Label(
    janela,
    text="Crescimento de Data Centers",
    font=("Arial", 20, "bold"),
    bg="#1e1e1e",
    fg="white"
)

titulo.pack(pady=20)

# ---------------- IMAGEM ----------------

# Coloque uma imagem chamada:
# datacenter.jpg
# na mesma pasta do código

imagem = Image.open("datacenter.jpg")
imagem = imagem.resize((400, 220))

foto = ImageTk.PhotoImage(imagem)

label_imagem = tk.Label(janela, image=foto)
label_imagem.pack(pady=10)

# ---------------- DADOS DO GRÁFICO ----------------

anos = [2021, 2022, 2023, 2024, 2025]
crescimento = [10, 18, 30, 45, 70]

# ---------------- GRÁFICO ----------------

figura, grafico = plt.subplots(figsize=(5, 3))

grafico.plot(anos, crescimento, marker="o")

grafico.set_title("Expansão de Data Centers")
grafico.set_xlabel("Ano")
grafico.set_ylabel("Quantidade")

canvas = FigureCanvasTkAgg(figura, master=janela)
canvas.draw()

canvas.get_tk_widget().pack(pady=20)

# ---------------- STATUS ----------------

status = tk.Label(
    janela,
    text="Status: Crescimento acelerado no setor",
    font=("Arial", 12),
    bg="#1e1e1e",
    fg="#00ff88"
)

status.pack()

# ---------------- EXECUTAR ----------------

janela.mainloop()