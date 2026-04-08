#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genera la guía de trabajo: Potencias y Raíces para Máximo (2° Medio)
Versión con símbolos matemáticos Unicode usando DejaVu Sans.
"""

from fpdf import FPDF
import os

# Rutas de fuentes DejaVu Sans
FONT_REGULAR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_ITALIC = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"  # No oblique available


class GuiaPDF(FPDF):
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=20)
        # Registrar fuente Unicode
        self.add_font("DS", "", FONT_REGULAR, uni=False)
        self.add_font("DS", "B", FONT_BOLD, uni=False)
        self.add_font("DS", "I", FONT_ITALIC, uni=False)

    def header(self):
        if self.page_no() == 1:
            return
        self.set_font("DS", "I", 8)
        self.set_text_color(130, 130, 130)
        self.cell(0, 8, "Guía de Potencias y Raíces — 2° Medio", align="C")
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("DS", "I", 8)
        self.set_text_color(130, 130, 130)
        self.cell(0, 10, f"Página {self.page_no()}/{{nb}}", align="C")

    def titulo_seccion(self, num, titulo):
        self.set_font("DS", "B", 14)
        self.set_fill_color(41, 128, 185)
        self.set_text_color(255, 255, 255)
        label = f"  SECCIÓN {num}: {titulo}" if num else f"  {titulo}"
        self.cell(0, 10, label, fill=True, new_x="LMARGIN", new_y="NEXT")
        self.ln(4)
        self.set_text_color(0, 0, 0)

    def subtitulo(self, texto):
        self.set_font("DS", "B", 11)
        self.set_text_color(41, 128, 185)
        self.cell(0, 7, texto, new_x="LMARGIN", new_y="NEXT")
        self.ln(2)
        self.set_text_color(0, 0, 0)

    def recuadro_recuerda(self, texto):
        self.set_font("DS", "B", 10)
        self.set_fill_color(255, 243, 205)
        self.set_draw_color(255, 193, 7)
        self.set_text_color(133, 100, 4)
        self.cell(0, 7, "  RECUERDA", fill=True, new_x="LMARGIN", new_y="NEXT")
        self.set_font("DS", "", 9)
        self.set_text_color(80, 60, 0)
        self.set_fill_color(255, 249, 230)
        self.multi_cell(0, 5, texto, fill=True)
        self.set_draw_color(0, 0, 0)
        self.set_text_color(0, 0, 0)
        self.ln(4)

    def recuadro_propiedad(self, titulo, texto):
        self.set_font("DS", "B", 10)
        self.set_fill_color(209, 236, 241)
        self.set_draw_color(41, 128, 185)
        self.set_text_color(21, 67, 96)
        self.cell(0, 7, f"  {titulo}", fill=True, new_x="LMARGIN", new_y="NEXT")
        self.set_font("DS", "", 9)
        self.set_text_color(0, 0, 0)
        self.set_fill_color(232, 248, 252)
        self.multi_cell(0, 5, texto, fill=True)
        self.set_draw_color(0, 0, 0)
        self.ln(3)

    def texto(self, contenido):
        self.set_font("DS", "", 10)
        self.multi_cell(0, 5.5, contenido)
        self.ln(2)

    def ejercicio(self, numero, enunciado):
        self.set_font("DS", "B", 10)
        self.set_text_color(192, 57, 43)
        self.cell(8, 6, f"{numero}.")
        self.set_font("DS", "", 10)
        self.set_text_color(0, 0, 0)
        self.multi_cell(0, 5.5, enunciado)
        self.ln(1)

    def lineas_respuesta(self, n=2):
        self.set_draw_color(200, 200, 200)
        for _ in range(n):
            y = self.get_y()
            self.line(self.l_margin, y, self.w - self.r_margin, y)
            self.ln(7)
        self.set_draw_color(0, 0, 0)
        self.ln(2)

    def dificultad(self, nivel):
        etiquetas = {1: "NIVEL BÁSICO", 2: "NIVEL INTERMEDIO", 3: "NIVEL AVANZADO"}
        colores = {1: (39, 174, 96), 2: (243, 156, 18), 3: (231, 76, 60)}
        c = colores[nivel]
        self.set_font("DS", "B", 9)
        self.set_fill_color(*c)
        self.set_text_color(255, 255, 255)
        self.cell(42, 6, f"  {etiquetas[nivel]}", fill=True, new_x="LMARGIN", new_y="NEXT")
        self.set_text_color(0, 0, 0)
        self.ln(3)


def generar_guia():
    pdf = GuiaPDF()
    pdf.alias_nb_pages()
    pdf.set_margins(15, 15, 15)

    # ════════════════════════════════
    # PORTADA
    # ════════════════════════════════
    pdf.add_page()
    pdf.ln(25)
    pdf.set_font("DS", "B", 28)
    pdf.set_text_color(41, 128, 185)
    pdf.cell(0, 12, "GUÍA DE TRABAJO", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(3)
    pdf.set_font("DS", "B", 22)
    pdf.set_text_color(44, 62, 80)
    pdf.cell(0, 10, "Potencias y Raíces", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(8)

    pdf.set_draw_color(41, 128, 185)
    pdf.set_line_width(1)
    y = pdf.get_y()
    pdf.line(50, y, pdf.w - 50, y)
    pdf.set_line_width(0.2)
    pdf.ln(10)

    pdf.set_font("DS", "", 14)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(0, 8, "Unidad 1: Números  |  2° Medio", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(5)
    pdf.set_font("DS", "", 12)
    pdf.cell(0, 8, "Alumno: Máximo", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(15)

    pdf.set_font("DS", "I", 10)
    pdf.set_text_color(120, 120, 120)
    pdf.multi_cell(0, 6,
        "Esta guía cubre las propiedades de potencias y raíces, su operatoria\n"
        "y resolución de problemas. Trabaja en orden, sección por sección.\n"
        "Cada sección aumenta en dificultad. No te saltes los recuadros\n"
        "de «Recuerda», son claves para lo que viene después.",
        align="C")
    pdf.ln(10)

    pdf.set_font("DS", "B", 11)
    pdf.set_text_color(44, 62, 80)
    pdf.cell(0, 7, "Contenidos de esta guía:", align="L", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("DS", "", 10)
    contenidos = [
        "1. Repaso de potencias y sus propiedades",
        "2. Raíces cuadradas, cúbicas y enésimas",
        "3. Propiedades de las raíces",
        "4. Conexión entre potencias y raíces (exponente racional)",
        "5. Operatoria con raíces (suma, resta, multiplicación, división)",
        "6. Racionalización",
        "7. Problemas de aplicación"
    ]
    for c in contenidos:
        pdf.cell(0, 6, f"    {c}", new_x="LMARGIN", new_y="NEXT")
    pdf.set_text_color(0, 0, 0)

    # ════════════════════════════════
    # SECCIÓN 1: REPASO DE POTENCIAS
    # ════════════════════════════════
    pdf.add_page()
    pdf.titulo_seccion("1", "REPASO DE POTENCIAS")

    pdf.recuadro_recuerda(
        "Una potencia es una forma abreviada de escribir una multiplicación repetida:\n"
        f"    aⁿ = a · a · a · … · a   (n veces)\n"
        "donde «a» es la base y «n» es el exponente.\n"
        f"Ejemplo: 3⁴ = 3 · 3 · 3 · 3 = 81"
    )

    pdf.subtitulo("Propiedades de las potencias (exponente entero)")

    pdf.recuadro_propiedad("1. Multiplicación de igual base",
        "aᵐ · aⁿ = aᵐ⁺ⁿ\n"
        "Se mantiene la base y se suman los exponentes.\n"
        "Ejemplo: 2³ · 2⁵ = 2³⁺⁵ = 2⁸ = 256")

    pdf.recuadro_propiedad("2. División de igual base",
        "aᵐ : aⁿ = aᵐ⁻ⁿ,  con a ≠ 0\n"
        "Se mantiene la base y se restan los exponentes.\n"
        "Ejemplo: 5⁷ : 5⁴ = 5⁷⁻⁴ = 5³ = 125")

    pdf.recuadro_propiedad("3. Potencia de una potencia",
        "(aᵐ)ⁿ = aᵐ·ⁿ\n"
        "Se mantiene la base y se multiplican los exponentes.\n"
        "Ejemplo: (2³)⁴ = 2³·⁴ = 2¹² = 4096")

    pdf.recuadro_propiedad("4. Potencia de un producto",
        f"(a · b)ⁿ = aⁿ · bⁿ\n"
        f"Ejemplo: (2 · 3)⁴ = 2⁴ · 3⁴ = 16 · 81 = 1296")

    pdf.recuadro_propiedad("5. Potencia de un cociente",
        f"(a/b)ⁿ = aⁿ / bⁿ,  con b ≠ 0\n"
        f"Ejemplo: (3/2)⁴ = 3⁴ / 2⁴ = 81/16")

    pdf.recuadro_propiedad("6. Exponente cero y exponente negativo",
        f"a⁰ = 1  (con a ≠ 0)\n"
        f"a⁻ⁿ = 1 / aⁿ\n"
        f"Ejemplo: 5⁰ = 1   |   2⁻³ = 1/2³ = 1/8")

    # Ejercicios Sección 1
    pdf.add_page()
    pdf.subtitulo("Ejercicios — Sección 1: Potencias")

    pdf.dificultad(1)
    pdf.ejercicio(1, "Calcula el valor de las siguientes potencias:")
    pdf.texto(
        f"a) 4³ =              b) (−2)⁵ =              c) (1/3)² =              d) 10⁰ =")
    pdf.lineas_respuesta(2)

    pdf.ejercicio(2, "Simplifica usando propiedades de potencias. Deja expresado como una sola potencia:")
    pdf.texto(
        f"a) 3⁴ · 3² =        b) 7⁸ : 7⁵ =          c) (5²)³ =             d) 2⁵ · 2⁻³ =")
    pdf.lineas_respuesta(2)

    pdf.ejercicio(3, "Calcula:")
    pdf.texto(
        f"a) (2/5)³ =          b) (−3)⁴ =             c) (2³ · 2⁴) : 2⁵ =   d) 6² · 6⁻² =")
    pdf.lineas_respuesta(2)

    pdf.dificultad(2)
    pdf.ejercicio(4, "Simplifica dejando el resultado como una sola potencia:")
    pdf.texto(
        f"a) (2³ · 2⁻¹)² =                    b) (5⁴ : 5²) · 5⁻¹ =")
    pdf.lineas_respuesta(2)

    pdf.ejercicio(5, "Verdadero o Falso. Justifica las falsas:")
    pdf.texto(
        f"a) ___ 2³ · 3³ = 6³\n"
        f"b) ___ (2³)² = 2⁵\n"
        f"c) ___ 4⁻² = −16\n"
        f"d) ___ a⁰ = 0, para todo valor de a"
    )
    pdf.lineas_respuesta(3)

    # ════════════════════════════════
    # SECCIÓN 2: RAÍCES
    # ════════════════════════════════
    pdf.add_page()
    pdf.titulo_seccion("2", "RAÍCES CUADRADAS, CÚBICAS Y ENÉSIMAS")

    pdf.recuadro_recuerda(
        "La raíz es la operación INVERSA de la potencia:\n"
        f"Si bⁿ = a, entonces b = raíz enésima de a.\n\n"
        f"Raíz cuadrada:  √a = x   si y solo si   x² = a   (x ≥ 0)\n"
        f"Raíz cúbica:    ∛a = x   si y solo si   x³ = a\n"
        f"Raíz enésima:  ⁿ√a = x   si y solo si   xⁿ = a"
    )

    pdf.subtitulo("Raíz cuadrada")
    pdf.texto(
        f"√a = b  significa que  b² = a  (con b ≥ 0)\n"
        f"Ejemplos:  √25 = 5  porque 5² = 25   |   √144 = 12  porque 12² = 144\n"
        f"OJO: √(−49) NO existe en ℝ (ningún número real al cuadrado da negativo)"
    )

    pdf.subtitulo("Raíz cúbica")
    pdf.texto(
        f"∛a = b  significa que  b³ = a\n"
        f"Ejemplos:  ∛8 = 2  porque 2³ = 8   |   ∛(−27) = −3  porque (−3)³ = −27\n"
        f"NOTA: La raíz cúbica SÍ acepta números negativos."
    )

    pdf.subtitulo("Raíz enésima")
    pdf.texto(
        f"ⁿ√a = x  significa que  xⁿ = a\n\n"
        "Condiciones importantes:\n"
        f"• Si n es PAR:  a debe ser ≥ 0 (no existe raíz par de negativo en ℝ)\n"
        f"• Si n es IMPAR:  a puede ser cualquier número real\n\n"
        f"Partes de una raíz: en ⁿ√a, «n» es el ÍNDICE y «a» es la CANTIDAD SUBRADICAL"
    )

    pdf.recuadro_recuerda(
        "Cuadrados perfectos útiles (¡memorízalos!):\n"
        f"1²=1    2²=4    3²=9    4²=16    5²=25    6²=36    7²=49    8²=64    9²=81    10²=100\n"
        f"11²=121    12²=144    13²=169    14²=196    15²=225\n\n"
        "Cubos perfectos útiles:\n"
        f"1³=1    2³=8    3³=27    4³=64    5³=125    6³=216    7³=343    8³=512    9³=729    10³=1000"
    )

    # Ejercicios Sección 2
    pdf.subtitulo("Ejercicios — Sección 2: Raíces")

    pdf.dificultad(1)
    pdf.ejercicio(1, "Calcula las siguientes raíces (sin calculadora):")
    pdf.texto(
        f"a) √81 =          b) √196 =         c) ∛125 =          d) ∛(−64) =\n"
        f"e) √0 =           f) √1 =           g) ∛1000 =         h) ⁴√16 ="
    )
    pdf.lineas_respuesta(2)

    pdf.ejercicio(2, "Indica si la raíz existe en los reales. Si existe, calcúlala:")
    pdf.texto(
        f"a) √(−25) =         b) ∛(−8) =          c) ⁴√(−81) =      d) ⁵√(−32) ="
    )
    pdf.lineas_respuesta(2)

    pdf.dificultad(2)
    pdf.ejercicio(3, "Determina el valor de x en cada caso:")
    pdf.texto(
        f"a) x² = 49    →  x = ?\n"
        f"b) x³ = −216  →  x = ?\n"
        f"c) x² = 225   →  x = ?\n"
        f"d) x⁴ = 81    →  x = ?"
    )
    pdf.lineas_respuesta(3)

    # ════════════════════════════════
    # SECCIÓN 3: PROPIEDADES DE RAÍCES
    # ════════════════════════════════
    pdf.add_page()
    pdf.titulo_seccion("3", "PROPIEDADES DE LAS RAÍCES")

    pdf.recuadro_propiedad("1. Raíz de un producto",
        f"ⁿ√(a · b) = ⁿ√a · ⁿ√b\n"
        "Se puede separar la raíz de un producto en el producto de las raíces.\n"
        f"Ejemplo: √324 = √(4 · 81) = √4 · √81 = 2 · 9 = 18")

    pdf.recuadro_propiedad("2. Raíz de un cociente",
        f"ⁿ√(a/b) = ⁿ√a / ⁿ√b,   con b ≠ 0\n"
        f"Ejemplo: √(49/25) = √49 / √25 = 7/5")

    pdf.recuadro_propiedad("3. Raíz elevada a su índice",
        f"(ⁿ√a)ⁿ = a\n"
        f"Es decir: (√5)² = 5   |   (∛7)³ = 7\n"
        f"También: ⁿ√(aⁿ) = a   (si n par, a ≥ 0)")

    pdf.recuadro_propiedad("4. Raíz de una raíz",
        f"ᵐ√( ⁿ√a ) = ᵐ·ⁿ√a\n"
        "Se multiplican los índices.\n"
        f"Ejemplo: √( ∛64 ) = ⁶√64")

    pdf.recuadro_propiedad("5. Ingreso/extracción de factor al subradical",
        f"b · ⁿ√a = ⁿ√(bⁿ · a)    (ingresar factor)\n"
        f"Ejemplo: 3√2 = √(3² · 2) = √(9·2) = √18\n\n"
        f"También al revés: √50 = √(25·2) = 5√2    (extraer factor)")

    pdf.recuadro_recuerda(
        "TRUCO para simplificar raíces cuadradas:\n"
        "1) Descomponer la cantidad subradical buscando cuadrados perfectos.\n"
        "2) Extraer la raíz de los cuadrados perfectos.\n"
        f"Ejemplo: √72 = √(36 · 2) = 6√2\n"
        f"Ejemplo: √200 = √(100 · 2) = 10√2"
    )

    # Ejercicios Sección 3
    pdf.subtitulo("Ejercicios — Sección 3: Propiedades de raíces")

    pdf.dificultad(1)
    pdf.ejercicio(1, "Usa la propiedad de raíz de un producto para calcular:")
    pdf.texto(
        f"a) √400 = √(___ × ___) =\n"
        f"b) √2025 = √(___ × ___ × ___) =\n"
        f"c) ∛(8 · 27) ="
    )
    pdf.lineas_respuesta(2)

    pdf.ejercicio(2, "Simplifica extrayendo factores del radical:")
    pdf.texto(
        f"a) √50 =           b) √72 =           c) √98 =           d) √300 =")
    pdf.lineas_respuesta(3)

    pdf.dificultad(2)
    pdf.ejercicio(3, "Ingresa el factor al subradical:")
    pdf.texto(
        f"a) 2√10 =         b) 5√3 =          c) 3∛4 =          d) 4√7 =")
    pdf.lineas_respuesta(2)

    pdf.ejercicio(4, "Calcula usando propiedades:")
    pdf.texto(
        f"a) √(48/3) =                 b) ∛(250/2) =\n"
        f"c) (√7)² =                   d) √( √256 ) ="
    )
    pdf.lineas_respuesta(3)

    # ════════════════════════════════
    # SECCIÓN 4: CONEXIÓN POTENCIAS - RAÍCES
    # ════════════════════════════════
    pdf.add_page()
    pdf.titulo_seccion("4", "CONEXIÓN POTENCIAS — RAÍCES")

    pdf.recuadro_recuerda(
        "CLAVE: Toda raíz puede escribirse como potencia de exponente fraccionario:\n\n"
        "    a ᵖ/q = ᑫ√(aᵖ)\n\n"
        "El DENOMINADOR del exponente → ÍNDICE de la raíz.\n"
        "El NUMERADOR del exponente → potencia a la que se eleva la base.\n\n"
        "Ejemplos:\n"
        "    a¹ᐟ² = √a             (raíz cuadrada)\n"
        "    a¹ᐟ³ = ∛a             (raíz cúbica)\n"
        "    a²ᐟ³ = ∛(a²)          (raíz cúbica de a²)\n"
        "    8¹ᐟ³ = ∛8 = 2\n"
        "    27²ᐟ³ = ∛(27²) = ∛729 = 9\n"
        "    (o bien: 27²ᐟ³ = (∛27)² = 3² = 9)"
    )

    pdf.subtitulo("Operaciones con potencias de exponente racional")
    pdf.texto(
        "Se aplican LAS MISMAS propiedades que con exponente entero:\n"
        "• Multiplicación (igual base):   aᵖ/q · aʳ/ˢ = aᵖ/q ⁺ ʳ/ˢ\n"
        "• División (igual base):           aᵖ/q : aʳ/ˢ = aᵖ/q ⁻ ʳ/ˢ\n"
        "• Multiplicación (igual exp.):   aᵖ/q · bᵖ/q = (a·b)ᵖ/q\n"
        "• Potencia de potencia:          (aᵖ/q)ʳ/ˢ = aᵖ·ʳ / q·ˢ"
    )

    # Ejercicios Sección 4
    pdf.subtitulo("Ejercicios — Sección 4: Exponente racional")

    pdf.dificultad(1)
    pdf.ejercicio(1, "Escribe como potencia de exponente racional:")
    pdf.texto(
        f"a) √5 =               b) ∛7 =               c) ⁴√3 =\n"
        f"d) ∛(x²) =             e) √(a³) =              f) ⁵√(2⁴) ="
    )
    pdf.lineas_respuesta(2)

    pdf.ejercicio(2, "Escribe como raíz:")
    pdf.texto(
        f"a) 9¹ᐟ² =              b) 8²ᐟ³ =              c) 16³ᐟ⁴ =            d) 32¹ᐟ⁵ =")
    pdf.lineas_respuesta(2)

    pdf.ejercicio(3, "Calcula el valor numérico:")
    pdf.texto(
        f"a) 25¹ᐟ² =             b) 8¹ᐟ³ =              c) 27²ᐟ³ =            d) 16³ᐟ⁴ =")
    pdf.lineas_respuesta(2)

    pdf.dificultad(2)
    pdf.ejercicio(4, "Simplifica dejando como una sola potencia:")
    pdf.texto(
        f"a) 5¹ᐟ² · 5¹ᐟ³ =                    b) 2³ᐟ⁴ : 2¹ᐟ⁴ =\n"
        f"c) (3²ᐟ⁵)⁵ᐟ² =                      d) 8⁻²ᐟ³ · 3⁻²ᐟ³ ="
    )
    pdf.lineas_respuesta(3)

    pdf.dificultad(3)
    pdf.ejercicio(5, "Expresa como una sola potencia y calcula si es posible:")
    pdf.texto(
        f"a) (4¹ᐟ² · 8¹ᐟ³) : 2 =\n"
        f"b) (27¹ᐟ³ · 9¹ᐟ²) / 3² ="
    )
    pdf.lineas_respuesta(4)

    # ════════════════════════════════
    # SECCIÓN 5: OPERATORIA CON RAÍCES
    # ════════════════════════════════
    pdf.add_page()
    pdf.titulo_seccion("5", "OPERATORIA CON RAÍCES")

    pdf.subtitulo("Suma y resta de raíces")
    pdf.recuadro_recuerda(
        "Solo se pueden SUMAR o RESTAR raíces que tengan el MISMO índice\n"
        "y la MISMA cantidad subradical (como términos semejantes en álgebra).\n\n"
        f"Ejemplo:  3√5 + 7√5 = (3+7)√5 = 10√5\n"
        f"Ejemplo:  4∛2 − ∛2 = (4−1)∛2 = 3∛2\n\n"
        f"CUIDADO: √2 + √3  NO se puede simplificar (subradical diferente)\n"
        f"CUIDADO: √9 + √16 = 3 + 4 = 7  (NO es √25 = 5)"
    )

    pdf.subtitulo("Multiplicación y división de raíces")
    pdf.texto(
        "Multiplicación (mismo índice):\n"
        f"  ⁿ√a · ⁿ√b = ⁿ√(a·b)\n"
        f"  Ejemplo: √3 · √12 = √(3·12) = √36 = 6\n\n"
        "División (mismo índice):\n"
        f"  ⁿ√a / ⁿ√b = ⁿ√(a/b)\n"
        f"  Ejemplo: √50 / √2 = √(50/2) = √25 = 5"
    )

    # Ejercicios Sección 5
    pdf.subtitulo("Ejercicios — Sección 5: Operatoria")

    pdf.dificultad(1)
    pdf.ejercicio(1, "Calcula las siguientes sumas y restas de raíces:")
    pdf.texto(
        f"a) 5√3 + 2√3 =\n"
        f"b) 8√7 − 3√7 =\n"
        f"c) 2∛5 + 6∛5 − ∛5 ="
    )
    pdf.lineas_respuesta(2)

    pdf.ejercicio(2, "Multiplica y simplifica:")
    pdf.texto(
        f"a) √5 · √20 =\n"
        f"b) √8 · √2 =\n"
        f"c) ∛4 · ∛16 ="
    )
    pdf.lineas_respuesta(2)

    pdf.dificultad(2)
    pdf.ejercicio(3,
        "Simplifica las raíces primero y luego opera "
        "(IMPORTANTE: a veces hay que simplificar para poder sumar):")
    pdf.texto(
        f"a) √12 + √27 =     [Pista: √12 = 2√3,  √27 = ?]\n"
        f"b) √50 − √18 =\n"
        f"c) √75 + √48 − √27 ="
    )
    pdf.lineas_respuesta(4)

    pdf.dificultad(3)
    pdf.ejercicio(4, "Resuelve las operaciones combinadas:")
    pdf.texto(
        f"a) √2 · (√8 + √18) =\n"
        f"b) (√3 + √5) · (√3 − √5) =\n"
        f"c) (2√3)² + √12 · √3 ="
    )
    pdf.lineas_respuesta(4)

    # ════════════════════════════════
    # SECCIÓN 6: RACIONALIZACIÓN
    # ════════════════════════════════
    pdf.add_page()
    pdf.titulo_seccion("6", "RACIONALIZACIÓN")

    pdf.recuadro_recuerda(
        "Racionalizar = eliminar la raíz del denominador de una fracción.\n"
        "Se multiplica numerador y denominador por una expresión conveniente.\n\n"
        f"Tipo 1:   a / √b   →   multiplica por √b/√b\n"
        f"Resultado:  a·√b / b\n\n"
        f"Tipo 2:   a / (b − √c)   →   multiplica por (b + √c)/(b + √c)\n"
        f"Se usa suma por diferencia: (b − √c)(b + √c) = b² − c"
    )

    # Ejercicios Sección 6
    pdf.subtitulo("Ejercicios — Sección 6: Racionalización")

    pdf.dificultad(1)
    pdf.ejercicio(1, "Racionaliza las siguientes fracciones:")
    pdf.texto(
        f"a) 1 / √3 =\n"
        f"b) 4 / √2 =\n"
        f"c) 6 / (3√5) ="
    )
    pdf.lineas_respuesta(4)

    pdf.dificultad(2)
    pdf.ejercicio(2, "Racionaliza usando el conjugado:")
    pdf.texto(
        f"a) 3 / (5 − √7) =\n"
        f"b) 2 / (√3 + √2) ="
    )
    pdf.lineas_respuesta(5)

    pdf.dificultad(3)
    pdf.ejercicio(3, "Racionaliza y simplifica:")
    pdf.texto(
        f"a) (√5 + 1) / (√5 − 1) =\n"
        f"b) 9 / (√3 + √2) ="
    )
    pdf.lineas_respuesta(5)

    # ════════════════════════════════
    # SECCIÓN 7: PROBLEMAS DE APLICACIÓN
    # ════════════════════════════════
    pdf.add_page()
    pdf.titulo_seccion("7", "PROBLEMAS DE APLICACIÓN")

    pdf.dificultad(1)
    pdf.ejercicio(1,
        f"El lado de un cuadrado mide √50 cm. "
        "Calcula el perímetro del cuadrado y expresa el resultado simplificado."
    )
    pdf.lineas_respuesta(3)

    pdf.ejercicio(2,
        f"El volumen de un cubo es 343 cm³. "
        "Determina la medida de su arista usando raíz cúbica."
    )
    pdf.lineas_respuesta(3)

    pdf.dificultad(2)
    pdf.ejercicio(3,
        f"Un rectángulo tiene un área de 6√2 cm² y su ancho mide √2 cm. "
        "Calcula la medida del largo del rectángulo."
    )
    pdf.lineas_respuesta(3)

    pdf.ejercicio(4,
        "Para calcular el tiempo (en segundos) que tarda un objeto en caer al suelo "
        f"desde una altura h (en metros), se usa la fórmula: t = √(h/5). "
        "Si un objeto cae desde 80 metros, calcula el tiempo que tarda en llegar al suelo. "
        "Racionaliza el resultado si es necesario."
    )
    pdf.lineas_respuesta(4)

    pdf.dificultad(3)
    pdf.ejercicio(5,
        f"La diagonal de un rectángulo mide √52 cm y uno de sus lados mide 4 cm. "
        "Determina: a) la medida del otro lado, b) el área del rectángulo, c) el perímetro. "
        "Usa el teorema de Pitágoras."
    )
    pdf.lineas_respuesta(5)

    pdf.ejercicio(6,
        "Simplifica la siguiente expresión y calcula su valor:\n"
        f"E = √48 − 2√27 + √75 − √12"
    )
    pdf.lineas_respuesta(5)

    # ════════════════════════════════
    # RESPUESTAS SELECCIONADAS
    # ════════════════════════════════
    pdf.add_page()
    pdf.titulo_seccion("", "RESPUESTAS SELECCIONADAS")
    pdf.set_font("DS", "I", 9)
    pdf.texto("(Usa estas respuestas para verificar tu trabajo. Intenta resolver antes de mirar.)")
    pdf.set_font("DS", "", 9)

    pdf.subtitulo("Sección 1")
    pdf.texto(
        f"Ej.1:  a) 64     b) −32     c) 1/9     d) 1\n"
        f"Ej.2:  a) 3⁶ = 729     b) 7³ = 343     c) 5⁶     d) 2² = 4\n"
        f"Ej.3:  a) 8/125     b) 81     c) 2² = 4     d) 1\n"
        f"Ej.5:  a) V     b) F: (2³)² = 2⁶ = 64     c) F: 4⁻² = 1/16     d) F: a⁰ = 1 si a ≠ 0"
    )

    pdf.subtitulo("Sección 2")
    pdf.texto(
        f"Ej.1:  a) 9   b) 14   c) 5   d) −4   e) 0   f) 1   g) 10   h) 2\n"
        f"Ej.2:  a) No existe en ℝ   b) −2   c) No existe en ℝ   d) −2\n"
        f"Ej.3:  a) x = 7 (o −7)   b) x = −6   c) x = 15 (o −15)   d) x = 3 (o −3)"
    )

    pdf.subtitulo("Sección 3")
    pdf.texto(
        f"Ej.2:  a) 5√2     b) 6√2     c) 7√2     d) 10√3\n"
        f"Ej.3:  a) √40     b) √75     c) ∛108     d) √112\n"
        f"Ej.4:  a) 4     b) 5     c) 7     d) ⁴√16 = 2"
    )

    pdf.subtitulo("Sección 4")
    pdf.texto(
        f"Ej.1:  a) 5¹ᐟ²   b) 7¹ᐟ³   c) 3¹ᐟ⁴   d) x²ᐟ³   e) a³ᐟ²   f) 2⁴ᐟ⁵\n"
        f"Ej.3:  a) 5   b) 2   c) 9   d) 8\n"
        f"Ej.4:  a) 5⁵ᐟ⁶   b) 2¹ᐟ² = √2   c) 3   d) 24⁻²ᐟ³"
    )

    pdf.subtitulo("Sección 5")
    pdf.texto(
        f"Ej.1:  a) 7√3     b) 5√7     c) 7∛5\n"
        f"Ej.2:  a) 10     b) 4     c) 4 (∛64 = 4)\n"
        f"Ej.3:  a) 5√3     b) 2√2     c) 6√3\n"
        f"Ej.4:  a) 4 + 6 = 10     b) 3 − 5 = −2     c) 12 + 6 = 18"
    )

    pdf.subtitulo("Sección 6")
    pdf.texto(
        f"Ej.1:  a) √3/3     b) 2√2     c) 2√5/5\n"
        f"Ej.2:  a) (5 + √7)/6     b) 2(√3 − √2)"
    )

    pdf.subtitulo("Sección 7")
    pdf.texto(
        f"Ej.1:  P = 4√50 = 20√2 cm\n"
        f"Ej.2:  arista = ∛343 = 7 cm\n"
        f"Ej.3:  largo = 6 cm\n"
        f"Ej.4:  t = √16 = 4 s\n"
        f"Ej.5:  a) 6 cm   b) 24 cm²   c) 20 cm\n"
        f"Ej.6:  E = 4√3 − 6√3 + 5√3 − 2√3 = √3"
    )

    # Guardar
    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                               "Guia_Potencias_Raices_Maximo.pdf")
    pdf.output(output_path)
    print(f"Guía generada exitosamente en: {output_path}")
    return output_path


if __name__ == "__main__":
    generar_guia()
