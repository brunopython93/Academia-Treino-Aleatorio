import random
from tkinter import *
from tkinter import ttk

lista_biceps = ["Rosca direta", "Rosca martelo", "Rosca alternada", "Rosca 21", "Rosca concentrada", "Rosca inversa", "Rosca scott", "Rosca spider", "Rosca com halteres", "Rosca com barra W", "Martelo com halteres", "Martelo com barra reta", "Supino fechado", "Curl com cabo", "Curl inclinado", "Curl na máquina", "Curl com elástico", "Curl com corda", "Curl na polia alta", "Curl na polia baixa", "Rosca 21 invertida", "Rosca com barra Z", "Rosca com pegada supinada", "Rosca com pegada pronada", "Rosca com pegada neutra", "Rosca concentrada inclinada", "Rosca na máquina de cabo", "Rosca na barra fixa", "Rosca aranha alternada", "Rosca drag curl", "Rosca com kettlebell", "Martelo com cabo", "Martelo inclinado", "Supino fechado com halteres", "Curl com barra olímpica", "Curl com anilha", "Curl inverso na máquina", "Curl no banco inclinado", "Curl no banco declinado", "Rosca com halteres alternada", "Rosca concentrada com halteres", "Rosca 21 com halteres", "Rosca com pegada martelo", "Rosca na barra fixa com pegada supinada", "Rosca na barra fixa com pegada pronada", "Rosca na barra fixa com pegada neutra", "Curl inverso com halteres", "Curl no banco inclinado com halteres", "Curl no banco Scott com halteres", "Curl Scott com barra"]

lista_triceps = ["Paralelas", "Supino fechado", "Tríceps testa", "Tríceps coice", "Tríceps corda", "Tríceps corda com pegada invertida", "Tríceps corda com pegada neutra", "Tríceps pulley unilateral", "Tríceps pulley bilateral", "Tríceps na polia alta em pé", "Tríceps na polia alta com barra reta", "Tríceps na polia alta com corda", "Tríceps na polia baixa com barra reta", "Tríceps na polia baixa com pegada invertida", "Tríceps na polia baixa com corda", "Dips entre bancos", "Dips no banco ou cadeira", "Dips no solo com rotação dos cotovelos ", "Copas de tríceps no banco inclinado", "Copas de tríceps no banco declinado", "Copas de tríceps no banco reto", "Copas de tríceps unilateral no banco inclinado", "Copas de tríceps unilateral no banco declinado", "Copas de tríceps unilateral no banco reto", "Copas de tríceps simultâneas com halteres no banco inclinado", "Copas de tríceps simultâneas com halteres no banco declinado", "Copas de tríceps simultâneas com halteres no banco reto", "Pulley invertido unilateral para o tríceps", "Pulley invertido bilateral para o tríceps", "Tríceps na barra fixa com pegada supinada", "Tríceps na barra fixa com pegada pronada", "Tríceps na barra fixa com pegada neutra", "Copas de tríceps simultâneas com halteres em pé", "Copas de tríceps unilateral em pé", "Copas de tríceps no banco Scott", "Copas de tríceps unilateral no banco Scott", "Tríceps corda unilateral na polia alta", "Tríceps corda bilateral na polia alta", "Pulley invertido unilateral com pegada neutra", "Pulley invertido bilateral com pegada neutra", "Tríceps no banco inclinado com halteres", "Tríceps no banco declinado com halteres", "Copas de tríceps simultâneas com halteres alternadas no banco inclinado", "Copas de tríceps simultâneas com halteres alternadas no banco declinado", "Copas de tríceps simultâneas com halteres alternadas no banco reto"]

lista_antebraco = ["Rosca de punho com barra", "Rosca de punho com halteres", "Flexão de punho com barra", "Flexão de punho com halteres", "Extensão de punho com barra", "Extensão de punho com halteres", "Pronação do antebraço", "Supinação do antebraço", "Rotação do antebraço com halteres", "Puxada de corda para antebraço", "Elevação lateral de punho com halteres", "Elevação frontal de punho com halteres", "Rotação do antebraço na polia alta", "Pronação do antebraço na polia baixa", "Supinação do antebraço na polia baixa", "Elevação frontal de punho na polia alta", "Elevação lateral de punho na polia alta", "Elevação frontal de punho na polia baixa", "Elevação lateral de punho na polia baixa", "Puxada de corda para antebraço na polia alta", "Puxada de corda para antebraço na polia baixa", "Flexão estática dos dedos com barra", "Flexão estática dos dedos com halteres", "Extensão estática dos dedos com barra", "Extensão estática dos dedos com halteres", "Punho em pronação no banco Scott", "Punho em supinação no banco Scott", "Punho em rotação no banco Scott", "Punho em flexão no banco Scott", "Punho em extensão no banco Scott", "Flexão de punho com elástico", "Extensão de punho com elástico", "Pronação do antebraço com elástico", "Supinação do antebraço com elástico", "Rotação do antebraço com elástico", "Elevação frontal de punho com elástico", "Elevação lateral de punho com elástico", "Puxada de corda para antebraço com elástico", "Flexão estática dos dedos com elástico", "Extensão estática dos dedos com elástico", "Punho em pronação no banco Scott com halteres", "Punho em supinação no banco Scott com halteres", "Punho em rotação no banco Scott com halteres", "Punho em flexão no banco Scott com halteres", "Punho em extensão no banco Scott com halteres"]

lista_ombro = ["Desenvolvimento com barra", "Desenvolvimento com halteres", "Elevação lateral com halteres", "Elevação frontal com halteres", "Elevação lateral na polia baixa", "Elevação frontal na polia baixa", "Elevação lateral na polia alta", "Elevação frontal na polia alta", "Desenvolvimento na máquina", "Desenvolvimento Arnold com halteres", "Desenvolvimento militar com barra", "Desenvolvimento sentado com halteres", "Desenvolvimento sentado na máquina", "Press militar com barra", "Press militar com halteres", "Elevação lateral em pé com halteres", "Elevação frontal em pé com halteres", "Elevação lateral inclinada com halteres", "Elevação frontal inclinada com halteres", "Remada alta com barra", "Remada alta com halteres", "Puxada de corda para ombros em pé", "Puxada de corda para ombros sentado", "Puxada de corda para ombros inclinado", "Puxada de corda para ombros unilateral em pé", "Puxada de corda para ombros unilateral sentado", "Puxada de corda para ombros unilateral inclinado", "Desenvolvimento com kettlebell unilateral em pé", "Desenvolvimento com kettlebell unilateral sentado", "Elevação lateral no cabo unilateral em pé", "Elevação frontal no cabo unilateral em pé", "Elevação lateral no cabo unilateral sentado", "Elevação frontal no cabo unilateral sentado", "Desenvolvimento na máquina Smith", "Desenvolvimento com barra na máquina Smith", "Elevação lateral na máquina", "Elevação frontal na máquina", "Desenvolvimento com halteres no banco inclinado", "Desenvolvimento com halteres no banco declinado", "Desenvolvimento com barra no banco inclinado", "Desenvolvimento com barra no banco declinado", "Elevação lateral com halteres no banco inclinado", "Elevação lateral com halteres no banco declinado", "Elevação frontal com halteres no banco inclinado", "Elevação frontal com halteres no banco declinado", "Pulley alto para ombros em pé", "Pulley alto para ombros sentado", "Pulley baixo para ombros em pé", "Pulley baixo para ombros sentado"]

lista_trapezio = ["Encolhimento de ombros com barra", "Encolhimento de ombros com halteres", "Encolhimento de ombros na máquina", "Encolhimento de ombros com cabo", "Elevação de ombros com halteres", "Elevação de ombros na máquina", "Elevação de ombros com cabo", "Remada alta com barra", "Remada alta com halteres", "Remada alta na máquina", "Puxada de corda para trapézio", "Puxada de corda na polia alta para trapézio", "Elevação lateral com halteres inclinado", "Elevação frontal com halteres inclinado", "Elevação lateral com halteres em pé", "Elevação frontal com halteres em pé", "Elevação lateral com halteres sentado", "Elevação frontal com halteres sentado", "Desenvolvimento com barra para trapézio", "Desenvolvimento com halteres para trapézio", "Desenvolvimento na máquina para trapézio", "Pulley alto para trapézio em pé", "Pulley alto para trapézio sentado", "Pulley baixo para trapézio em pé", "Pulley baixo para trapézio sentado", "Desenvolvimento Arnold para trapézio com halteres", "Encolhimento de ombros unilateral com halteres", "Elevação lateral unilateral com halteres inclinado", "Elevação frontal unilateral com halteres inclinado", "Elevação lateral unilateral com halteres em pé", "Elevação frontal unilateral com halteres em pé", "Elevação lateral unilateral com halteres sentado", "Elevação frontal unilateral com halteres sentado", "Remada alta unilateral com halteres", "Puxada de corda unilateral para trapézio", "Puxada de corda na polia alta unilateral para trapézio", "Desenvolvimento unilateral com halteres para trapézio", "Pulley alto unilateral para trapézio em pé", "Pulley alto unilateral para trapézio sentado", "Pulley baixo unilateral para trapézio em pé", "Pulley baixo unilateral para trapézio sentado", "Encolhimento de ombros na máquina Smith", "Encolhimento de ombros com barra no banco inclinado", "Encolhimento de ombros com barra no banco declinado", "Elevação de ombros na máquina Smith", "Elevação de ombros com halteres no banco inclinado", "Elevação de ombros com halteres no banco declinado"]

lista_costas = ["Puxada frontal com barra", "Puxada frontal com pegada supinada", "Puxada frontal com pegada pronada", "Puxada frontal na máquina", "Puxada frontal com corda", "Puxada frontal com halteres", "Puxada frontal com pegada larga", "Puxada frontal com pegada estreita", "Puxada frontal na polia alta", "Puxada frontal na polia baixa", "Remada curvada com barra", "Remada curvada com halteres", "Remada curvada na máquina", "Remada curvada na polia baixa", "Remada curvada unilateral com halteres", "Remada curvada unilateral na máquina", "Remada curvada T-bar", "Remada curvada no cabo", "Remada alta com barra", "Remada alta com halteres", "Remada alta na máquina", "Remada alta na polia baixa", "Remada alta unilateral com halteres", "Remada alta unilateral na máquina", "Pulldown na polia alta com barra em V", "Pulldown na polia alta com pegador reto", "Pulldown na polia alta com pegador em V invertido", "Pulldown na polia alta com corda", "Pulldown na polia alta unilateral com pegador reto", "Pulldown na polia baixa com barra em V", "Pulldown na polia baixa com pegador reto", "Pulldown na polia baixa com corda", "Pulldown na polia baixa unilateral com pegador reto", "Levantamento terra", "Levantamento terra sumô", "Hiperextensão lombar", "Superman", "Remada cavalinho", "Remada unilateral com halteres", "Remada unilateral na máquina", "Puxada alta para tríceps com corda", "Puxada alta para tríceps com barra reta", "Puxada alta para tríceps com pegador em V invertido", "Puxada alta para tríceps unilateral com pegador reto", "Puxada alta para tríceps unilateral com corda", "Puxada alta para bíceps com barra reta", "Puxada alta para bíceps com pegador em V invertido", "Puxada alta para bíceps com corda", "Puxada alta para bíceps unilateral com pegador reto", "Puxada alta para bíceps unilateral com corda"]

lista_peito = ["Supino reto com barra", "Supino reto com halteres", "Supino inclinado com barra", "Supino inclinado com halteres", "Supino declinado com barra", "Supino declinado com halteres", "Crossover", "Crossover inclinado", "Crossover declinado", "Flexão de braço tradicional", "Flexão de braço inclinada", "Flexão de braço declinada", "Flexão de braço diamante", "Flexão de braço com apoio na parede", "Mergulho entre bancos", "Mergulho assistido na máquina", "Pullover com halteres", "Pullover na máquina", "Pullover com barra", "Pullover unilateral com halteres", "Pullover unilateral na máquina", "Aperto de mãos no crossover", "Aperto de mãos no crossover inclinado", "Aperto de mãos no crossover declinado", "Peck deck (voador)", "Peck deck inclinado (voador)", "Peck deck declinado (voador)", "Dips no banco reto", "Dips no banco inclinado", "Dips no banco declinado", "Flexões explosivas (plyometric push-ups)", "Fondue no banco reto", "Fondue no banco inclinado", "Fondue no banco declinado", "Puxada peitoral na polia alta com pegador reto", "Puxada peitoral na polia alta com pegador em V invertido", "Puxada peitoral na polia alta unilateral com pegador reto", "Puxada peitoral na polia alta unilateral com pegador em V invertido", "Flexão de braço com aperto fechado", "Flexão de braço com aperto aberto", "Flexão de braço com aperto médio", "Supino inclinado com halteres alternados", "Supino declinado com halteres alternados", "Supino reto com halteres alternados", "Supino inclinado com barra em Smith", "Supino declinado com barra em Smith", "Supino reto com barra em Smith", "Crossover na máquina", "Crossover inclinado na máquina", "Crossover declinado na máquina"]

lista_quadriceps = ["Agachamento livre", "Agachamento Smith", "Agachamento hack", "Leg press horizontal", "Leg press 45º", "Avanço com barra", "Avanço com halteres", "Extensão de pernas na máquina", "Pistol squat", "Agachamento búlgaro", "Cadeira extensora", "Step-up com barra", "Step-up com halteres", "Salto com agachamento", "Caminhada lateral com elástico", "Afundo com barra", "Afundo com halteres", "Afundo na máquina Smith", "Afundo no Smith unilateral", "Sissy squat"]

lista_posterior = ["Stiff com barra", "Stiff com halteres", "Stiff na máquina", "Flexão de pernas deitado", "Flexão de pernas sentado", "Flexão de pernas em pé", "Flexão de pernas unilateral com halteres", "Flexão de pernas unilateral na máquina", "Flexão de pernas no cabo", "Levantamento terra", "Levantamento terra sumô", "Ponte de glúteos com barra", "Ponte de glúteos com halteres", "Ponte de glúteos na máquina", "Cadeira flexora", "Cadeira flexora unilateral", "Cadeira flexora inclinada", "Cadeira flexora inclinada unilateral", "Mesa flexora", "Mesa flexora unilateral"]

lista_panturrilha = ["Levantamento de panturrilha em pé", "Levantamento de panturrilha sentado", "Levantamento de panturrilha unilateral em pé", "Levantamento de panturrilha unilateral sentado", "Levantamento de panturrilha no leg press", "Panturrilha no Smith", "Panturrilha no hack", "Panturrilha no step", "Panturrilha no banco", "Panturrilha na máquina de adutora/abdução", "Panturrilha no cabo", "Salto de panturrilha em pé", "Salto de panturrilha com halteres", "Salto de panturrilha unilateral em pé", "Salto de panturrilha unilateral com halteres", "Elevação de panturrilha com apoio frontal", "Elevação de panturrilha com apoio traseiro", "Elevação de panturrilha com apoio inclinado", "Elevação de panturrilha com apoio declinado", "Elevação de panturrilha em escada"]

lista_adutor = ["Agachamento sumô", "Stiff com abertura lateral", "Levantamento terra sumô", "Abdução deitado na máquina", "Abdução sentado na máquina", "Abdução em pé na máquina", "Agachamento com abertura lateral", "Elevação lateral de pernas em pé", "Elevação lateral de pernas deitado", "Elevação lateral de pernas na máquina", "Agachamento com salto e abertura lateral", "Agachamento com banda elástica", "Cadeira adutora", "Cadeira adutora unilateral", "Cadeira adutora inclinada", "Cadeira adutora inclinada unilateral", "Mesa adutora", "Mesa adutora unilateral", "Mesa adutora inclinada"]

lista_abdutor = ["Abdução de pernas em pé", "Abdução de pernas deitado", "Abdução de pernas na máquina", "Agachamento com abertura lateral", "Elevação lateral de pernas em pé", "Elevação lateral de pernas deitado", "Elevação lateral de pernas na máquina", "Agachamento com salto e abertura lateral", "Agachamento com banda elástica", "Cadeira abdutora", "Cadeira abdutora unilateral", "Cadeira abdutora inclinada", "Cadeira abdutora inclinada unilateral", "Mesa abdutora", "Mesa abdutora unilateral", "Mesa abdutora inclinada", "Ponte com abdução de pernas", "Escalada lateral no step", "Passada lateral com elástico", "Prancha com abdução de pernas"]

lista_gluteo = ["Agachamento com Barra", "Levantamento Terra", "Agachamento Sumô", "Afundo com Barra", "Hip Thrust", "Cadeira Abdutora", "Cadeira Adutora", "Stiff", "Elevação de Quadril", "Agachamento Búlgaro", "Passada", "Agachamento Livre", "Caminhada Lateral com Elástico", "Kickback de Glúteo", "Ponte Glúteo com Peso", "Prensa 45°", "Abdução de Quadril em Pé", "Desenvolvimento Terra Romeno", "Glute Ham Raise", "Climber"]

lista_abdomen = ["Crunch", "Prancha", "Elevação de Pernas Suspensas", "Bicicleta no Ar", "Prancha Lateral", "Abdominal Infra no Solo", "Tesoura", "Prancha com Elevação de Braços Alternados", "Prancha com Rotação de Quadril", "V-Up", "Abdominal na Roda", "Prancha com Toque no Ombro", "Abdominal com Pernas Elevadas", "Prancha com Elevação de Perna", "Abdominal Lateral", "Prancha com Elevação de Braço e Perna", "Abdominal Canivete", "Prancha com Abdução de Perna", "Abdominal na Bola Suíça", "Prancha com Torção", "Abdominal no Banco Declinado", "Prancha com Deslize", "Abdominal no TRX", "Prancha com Elevação Alternada de Perna e Braço", "Abdominal na Corda"]

lista_lombar = ["Hiperextensão Lombar", "Superman", "Prancha Invertida", "Hiperextensão na Máquina", "Prancha Superman", "Hiperextensão em GHD", "Prancha com Elevação de Pernas", "Rotação de Tronco com Barra", "Hiperextensão com Rotação", "Prancha com Rotação de Quadril"]

lista_paravertebral = ["Hiperextensão Lombar", "Superman", "Prancha Invertida", "Hiperextensão na Máquina", "Prancha Superman", "Hiperextensão em GHD", "Prancha com Elevação de Pernas", "Rotação de Tronco com Barra", "Hiperextensão com Rotação", "Prancha com Rotação de Quadril"]

numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
tipos = ["ABDUTOR", "BÍCEPS", "TRÍCEPS", "ANTEBRAÇO", "OMBRO", "TRAPÉZIO", "COSTAS", "PEITO", "QUADRÍCEPS", "POSTERIOR", "PANTURRILHA", "ADUTOR", "GLÚTEO", "ABDÔMEN", "LOMBAR", "PARAVERTEBRAL"]
def btn_clicked():
    biceps = random.sample(lista_biceps, int(entry2.get()))
    ombro = random.sample(lista_ombro, int(entry5.get()))
    antebraco = random.sample(lista_antebraco, int(entry4.get()))
    triceps = random.sample(lista_triceps, int(entry3.get()))
    trapezio = random.sample(lista_trapezio, int(entry6.get()))
    costas = random.sample(lista_costas, int(entry7.get()))
    peito = random.sample(lista_peito, int(entry8.get()))
    quadriceps = random.sample(lista_quadriceps, int(entry9.get()))
    posterior = random.sample(lista_posterior, int(entry10.get()))
    panturrilha = random.sample(lista_panturrilha, int(entry11.get()))
    adutor = random.sample(lista_adutor, int(entry12.get()))
    abdutor = random.sample(lista_abdutor, int(entry1.get()))
    gluteo = random.sample(lista_gluteo, int(entry13.get()))
    abdomen = random.sample(lista_abdomen, int(entry14.get()))
    lombar = random.sample(lista_lombar, int(entry15.get()))
    paravertebral = random.sample(lista_paravertebral, int(entry16.get()))
    lista_tipos = [abdutor, biceps, triceps, antebraco, ombro, trapezio, costas, peito, quadriceps, posterior, panturrilha, adutor, gluteo, abdomen, lombar, paravertebral]
    for i, tipo in enumerate(lista_tipos):
        for j, item in enumerate(tipo):
            if len(tipo) != 0:
                if j == 0:
                    entry0.insert(INSERT, f"\n{tipos[i]}:\n{item}\n")
                else:
                    entry0.insert(INSERT, f"{item}\n")
def btn_clicked1():
    entry0.delete("0.0", "end")

window = Tk()
window.title("TREINO ALEATÓRIO")
window.geometry("1000x600")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 600,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    500.0, 300.0,
    image=background_img)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    766.0, 290.0,
    image = entry0_img)

entry0 = Text(
    font=("Helvetica", 12),
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry0.place(
    x = 563, y = 91,
    width = 406,
    height = 396)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked1,
    relief = "flat")

b0.place(
    x = 562, y = 525,
    width = 406,
    height = 40)

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    494.0, 313.0,
    image = entry1_img)

entry1 = ttk.Combobox(window, values = numeros)
entry1.set(0)
entry1.place(
    x = 473, y = 297,
    width = 42,
    height = 30)

entry2_img = PhotoImage(file = f"img_textBox2.png")
entry2_bg = canvas.create_image(
    228.5, 195.0,
    image = entry2_img)

entry2 = ttk.Combobox(window, values = numeros)
entry2.set(0)

entry2.place(
    x = 208, y = 179,
    width = 41,
    height = 30)

entry3_img = PhotoImage(file = f"img_textBox3.png")
entry3_bg = canvas.create_image(
    228.5, 234.0,
    image = entry3_img)

entry3 = ttk.Combobox(window, values = numeros)
entry3.set(0)

entry3.place(
    x = 208, y = 218,
    width = 41,
    height = 30)

entry4_img = PhotoImage(file = f"img_textBox4.png")
entry4_bg = canvas.create_image(
    228.5, 274.0,
    image = entry4_img)

entry4 = ttk.Combobox(window, values = numeros)
entry4.set(0)

entry4.place(
    x = 208, y = 258,
    width = 41,
    height = 30)

entry5_img = PhotoImage(file = f"img_textBox5.png")
entry5_bg = canvas.create_image(
    228.5, 313.0,
    image = entry5_img)

entry5 = ttk.Combobox(window, values = numeros)
entry5.set(0)

entry5.place(
    x = 208, y = 297,
    width = 41,
    height = 30)

entry6_img = PhotoImage(file = f"img_textBox6.png")
entry6_bg = canvas.create_image(
    228.5, 353.5,
    image = entry6_img)

entry6 = ttk.Combobox(window, values = numeros)
entry6.set(0)
entry6.place(
    x = 208, y = 338,
    width = 41,
    height = 29)

entry7_img = PhotoImage(file = f"img_textBox7.png")
entry7_bg = canvas.create_image(
    228.5, 393.5,
    image = entry7_img)

entry7 = ttk.Combobox(window, values = numeros)
entry7.set(0)
entry7.place(
    x = 208, y = 377,
    width = 41,
    height = 31)

entry8_img = PhotoImage(file = f"img_textBox8.png")
entry8_bg = canvas.create_image(
    228.5, 433.0,
    image = entry8_img)

entry8 = ttk.Combobox(window, values = numeros)
entry8.set(0)
entry8.place(
    x = 208, y = 417,
    width = 41,
    height = 30)

entry9_img = PhotoImage(file = f"img_textBox9.png")
entry9_bg = canvas.create_image(
    228.5, 473.0,
    image = entry9_img)

entry9 = ttk.Combobox(window, values = numeros)
entry9.set(0)
entry9.place(
    x = 208, y = 457,
    width = 41,
    height = 30)

entry10_img = PhotoImage(file = f"img_textBox10.png")
entry10_bg = canvas.create_image(
    494.0, 195.0,
    image = entry10_img)

entry10 = ttk.Combobox(window, values = numeros)
entry10.set(0)
entry10.place(
    x = 473, y = 179,
    width = 42,
    height = 30)

entry11_img = PhotoImage(file = f"img_textBox11.png")
entry11_bg = canvas.create_image(
    494.0, 234.0,
    image = entry11_img)

entry11 = ttk.Combobox(window, values = numeros)
entry11.set(0)
entry11.place(
    x = 473, y = 218,
    width = 42,
    height = 30)

entry12_img = PhotoImage(file = f"img_textBox12.png")
entry12_bg = canvas.create_image(
    494.0, 274.0,
    image = entry12_img)

entry12 = ttk.Combobox(window, values = numeros)
entry12.set(0)
entry12.place(
    x = 473, y = 258,
    width = 42,
    height = 30)

entry13_img = PhotoImage(file = f"img_textBox13.png")
entry13_bg = canvas.create_image(
    494.0, 353.5,
    image = entry13_img)

entry13 = ttk.Combobox(window, values = numeros)
entry13.set(0)
entry13.place(
    x = 473, y = 338,
    width = 42,
    height = 29)

entry14_img = PhotoImage(file = f"img_textBox14.png")
entry14_bg = canvas.create_image(
    494.0, 393.5,
    image = entry14_img)

entry14 = ttk.Combobox(window, values = numeros)
entry14.set(0)
entry14.place(
    x = 473, y = 377,
    width = 42,
    height = 31)

entry15_img = PhotoImage(file = f"img_textBox15.png")
entry15_bg = canvas.create_image(
    494.0, 433.0,
    image = entry15_img)

entry15 = ttk.Combobox(window, values = numeros)
entry15.set(0)
entry15.place(
    x = 473, y = 417,
    width = 42,
    height = 30)

entry16_img = PhotoImage(file = f"img_textBox16.png")
entry16_bg = canvas.create_image(
    494.0, 473.0,
    image = entry16_img)

entry16 = ttk.Combobox(window, values = numeros)
entry16.set(0)
entry16.place(
    x = 473, y = 457,
    width = 42,
    height = 30)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 29, y = 525,
    width = 486,
    height = 40)

window.resizable(False, False)
window.mainloop()