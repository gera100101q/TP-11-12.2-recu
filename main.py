import pygame
import sys
import math

# Inicialización de Pygame
pygame.init()

# Configuración de pantalla
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Mascota Virtual IPET 249 - Víbora de Python")

# Reloj de FPS
reloj = pygame.time.Clock()

# Paleta de Colores Institucionales y Python
BORDO = (128, 0, 32)
AMARILLO = (255, 215, 0)
ROJO = (220, 20, 60)
BLANCO = (255, 255, 255)
NEGRO = (20, 20, 20)
GRIS_OSCURO = (40, 40, 40)
PYTHON_AZUL = (48, 105, 152)
PYTHON_AMARILLO = (255, 212, 59)
VERDE = (50, 205, 50)

# Variables de Estado de la Mascota (0 a 100)
bateria = 100.0   # Carga de Café / Batería
codigo = 100.0    # Nivel de Código / Ánimo
salud = 100.0     # Limpieza de Bugs / Salud

# Fuentes
fuente_titulo = pygame.font.SysFont("Arial", 22, bold=True)
fuente_texto = pygame.font.SysFont("Arial", 16)
fuente_estado = pygame.font.SysFont("Arial", 18, bold=True)

def dibujar_escudo(x, y):
    """Dibuja el escudo institucional del IPET 249."""
    pygame.draw.polygon(pantalla, AMARILLO, [(x, y), (x + 70, y), (x + 70, y + 60), (x + 35, y + 85), (x, y + 60)])
    pygame.draw.polygon(pantalla, BORDO, [(x, y), (x + 70, y), (x + 70, y + 60), (x + 35, y + 85), (x, y + 60)], 3)
    
    # Texto del escudo
    texto_escudo = fuente_texto.render("249", True, BORDO)
    pantalla.blit(texto_escudo, (x + 20, y + 30))

def dibujar_vibora_python(x, y, estado):
    """Dibuja a la Víbora de Python con remera e identidad del IPET 249."""
    
    # Cuerpo enroscado de la víbora (segmentos)
    segmentos = [
        (x - 60, y + 100), (x - 30, y + 120), (x, y + 110), 
        (x + 30, y + 120), (x + 60, y + 100), (x + 80, y + 70),
        (x + 60, y + 40), (x + 20, y + 30)
    ]
    
    # Dibujar cuerpo (Capas alternadas Azul y Amarillo de Python)
    for i, pos in enumerate(segmentos):
        color_seg = PYTHON_AZUL if i % 2 == 0 else PYTHON_AMARILLO
        pygame.draw.circle(pantalla, color_seg, pos, 28)
        pygame.draw.circle(pantalla, NEGRO, pos, 28, 2)

    # Remera / Bufanda institucional en la base de la cabeza
    pygame.draw.rect(pantalla, BORDO, (x - 40, y - 10, 80, 40), border_radius=10)
    pygame.draw.rect(pantalla, AMARILLO, (x - 40, y + 10, 80, 10))
    # Detalle escudo bordado en la remera
    pygame.draw.rect(pantalla, AMARILLO, (x + 10, y, 16, 18))

    # Cabeza principal de la Víbora
    pygame.draw.ellipse(pantalla, PYTHON_AZUL, (x - 50, y - 90, 100, 90))
    pygame.draw.ellipse(pantalla, NEGRO, (x - 50, y - 90, 100, 90), 3)

    # Lengua bífida
    if estado == "bugs":
        # Lengua zigzag por error
        pygame.draw.lines(pantalla, ROJO, False, [(x, y), (x - 10, y + 15), (x + 10, y + 25)], 3)
    else:
        # Lengua bífida normal
        pygame.draw.line(pantalla, ROJO, (x, y), (x, y + 20), 3)
        pygame.draw.line(pantalla, ROJO, (x, y + 20), (x - 8, y + 30), 3)
        pygame.draw.line(pantalla, ROJO, (x, y + 20), (x + 8, y + 30), 3)

    # Ojos y Expresión según estado
    if estado == "cansado":
        # Ojos entornados/dormidos
        pygame.draw.line(pantalla, NEGRO, (x - 30, y - 50), (x - 10, y - 50), 4)
        pygame.draw.line(pantalla, NEGRO, (x + 10, y - 50), (x + 30, y - 50), 4)
    elif estado == "bugs":
        # Ojos en X (Error de Bug)
        pygame.draw.line(pantalla, ROJO, (x - 30, y - 60), (x - 10, y - 40), 4)
        pygame.draw.line(pantalla, ROJO, (x - 10, y - 60), (x - 30, y - 40), 4)
        pygame.draw.line(pantalla, ROJO, (x + 10, y - 60), (x + 30, y - 40), 4)
        pygame.draw.line(pantalla, ROJO, (x + 30, y - 60), (x + 10, y - 40), 4)
    else:
        # Ojos normales felices
        pygame.draw.circle(pantalla, BLANCO, (x - 20, y - 50), 12)
        pygame.draw.circle(pantalla, NEGRO, (x - 18, y - 50), 6)
        pygame.draw.circle(pantalla, BLANCO, (x + 20, y - 50), 12)
        pygame.draw.circle(pantalla, NEGRO, (x + 22, y - 50), 6)

    # Anteojos de Programador
    pygame.draw.circle(pantalla, NEGRO, (x - 20, y - 50), 18, 3)
    pygame.draw.circle(pantalla, NEGRO, (x + 20, y - 50), 18, 3)
    pygame.draw.line(pantalla, NEGRO, (x - 2, y - 50), (x + 2, y - 50), 3)

    # Auriculares Gaming Institucionales (Bordó y Amarillo)
    pygame.draw.rect(pantalla, BORDO, (x - 65, y - 65, 16, 35), border_radius=5)
    pygame.draw.rect(pantalla, BORDO, (x + 49, y - 65, 16, 35), border_radius=5)
    pygame.draw.arc(pantalla, BORDO, (x - 55, y - 110, 110, 70), 0, 3.14, 6)
    pygame.draw.rect(pantalla, AMARILLO, (x - 61, y - 55, 6, 18))
    pygame.draw.rect(pantalla, AMARILLO, (x + 55, y - 55, 6, 18))

def dibujar_barra(x, y, ancho, alto, valor, color, etiqueta):
    """Dibuja las barras de estado dinámicas."""
    pygame.draw.rect(pantalla, GRIS_OSCURO, (x, y, ancho, alto), border_radius=5)
    ancho_actual = int((valor / 100.0) * ancho)
    if ancho_actual > 0:
        pygame.draw.rect(pantalla, color, (x, y, ancho_actual, alto), border_radius=5)
    pygame.draw.rect(pantalla, BLANCO, (x, y, ancho, alto), 2, border_radius=5)
    texto = fuente_texto.render(f"{etiqueta}: {int(valor)}%", True, BLANCO)
    pantalla.blit(texto, (x, y - 22))

# Ciclo principal del juego
ejecutando = True
mensaje_accion = "¡Usa las teclas [C], [P] o [B] para interactuar!"

while ejecutando:
    # 1. Gestión de Desgaste Temporal
    bateria = max(0.0, bateria - 0.03)
    codigo = max(0.0, codigo - 0.02)
    salud = max(0.0, salud - 0.015)

    # 2. Eventos de Teclado
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_c:  # Tomar café
                bateria = min(100.0, bateria + 25.0)
                mensaje_accion = "¡Python tomó un Café de Sistemas! (+25% Batería)"
            elif evento.key == pygame.K_p:  # Programar
                codigo = min(100.0, codigo + 20.0)
                mensaje_accion = "¡Python ejecutó un script exitoso! (+20% Código)"
            elif evento.key == pygame.K_b:  # Depurar / Limpiar Bugs
                salud = min(100.0, salud + 30.0)
                mensaje_accion = "¡Python eliminó los Syntax Errors! (+30% Salud)"

    # 3. Determinación de Estado Visual
    if bateria < 30.0:
        estado_mascota = "cansado"
        estado_texto = "Estado: ¡Sin Batería / Cansado!"
    elif salud < 30.0:
        estado_mascota = "bugs"
        estado_texto = "Estado: ¡Error de Sintaxis / BUGS!"
    else:
        estado_mascota = "feliz"
        estado_texto = "Estado: Compilando a full (OK)"

    # 4. Renderizado Visual
    pantalla.fill(BORDO)  # Fondo institucional bordó

    # Marco de la interfaz
    pygame.draw.rect(pantalla, GRIS_OSCURO, (20, 20, 760, 560), border_radius=10)
    pygame.draw.rect(pantalla, AMARILLO, (25, 25, 750, 550), 3, border_radius=10)

    # Encabezado e Identidad Institucional
    dibujar_escudo(45, 40)
    titulo_1 = fuente_titulo.render("IPET 249 - Nicolás Copérnico", True, AMARILLO)
    titulo_2 = fuente_texto.render("Especialidad: Informática | Mascota Virtual: Python Copérnico", True, BLANCO)
    pantalla.blit(titulo_1, (130, 45))
    pantalla.blit(titulo_2, (130, 75))

    # Dibujar la Mascota
    dibujar_vibora_python(400, 260, estado_mascota)

    # Barras de Estado
    dibujar_barra(50, 480, 200, 20, bateria, AMARILLO, "Carga / Batería (C)")
    dibujar_barra(300, 480, 200, 20, codigo, VERDE, "Nivel de Código (P)")
    dibujar_barra(550, 480, 200, 20, salud, ROJO, "Limpia de Bugs (B)")

    # Estado y Mensajes de Control
    txt_estado = fuente_estado.render(estado_texto, True, AMARILLO)
    txt_instrucciones = fuente_texto.render("[C] Tomar Café  |  [P] Programar  |  [B] Limpiar Bugs", True, BLANCO)
    txt_feedback = fuente_texto.render(mensaje_accion, True, BLANCO)

    pantalla.blit(txt_estado, (250, 130))
    pantalla.blit(txt_instrucciones, (230, 525))
    pantalla.blit(txt_feedback, (200, 550))

    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
sys.exit()
