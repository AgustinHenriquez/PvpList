from Stats import ataque_base, defensa_base, salud_base, cpm
import math


class Pokemon:

    def __init__(self, especie, nivel, iv_ataque, iv_defensa, iv_salud):
        self.especie = especie
        self.nivel = nivel
        self.iv_ataque = iv_ataque
        self.iv_defensa = iv_defensa
        self.iv_salud = iv_salud
        self.ataque_base = ataque_base(especie)
        self.defensa_base = defensa_base(especie)
        self.salud_base = salud_base(especie)
        self.ataque = self.calcular_ataque()
        self.defensa = self.calcular_defensa()
        self.salud = self.calcular_salud()
        self.pc = self.calcular_pc()
        self.pc_max_super = self

    def calcular_ataque(self):
        """Devuelve la estadistica de ataque de un pokemon en formato float"""
        multiplicador_pc = cpm(self.nivel)
        ataque = (self.ataque_base + self.iv_ataque) * multiplicador_pc
        return ataque

    def calcular_defensa(self):
        """Devuelve la estadistica de defensa de un pokemon en formato float"""
        multiplicador_pc = cpm(self.nivel)
        defensa = (self.defensa_base + self.iv_defensa) * multiplicador_pc
        return defensa

    def calcular_salud(self):
        """Devuelve la estadistica de salud de un pokemon en formato float"""
        multiplicador_pc = cpm(self.nivel)
        salud = (self.salud_base + self.iv_salud) * multiplicador_pc
        return salud

    def calcular_pc(self):
        """Devuelve los puntos de combate de un pokemon en formato int"""
        pc = self.ataque * math.sqrt(self.defensa) * math.sqrt(self.salud) / 10
        return math.floor(pc)

    def calcular_pc_max_super(self):
        """Devulve los puntos de combate maximos que puede alcanzar un pokemon para la liga super (1500PC max),
        en formato int"""
        ataque = self.ataque_base + self.iv_ataque
        defensa = self.defensa_base + self.iv_defensa
        salud = self.salud_base + self.iv_salud
        for nivel in range(2, 81):
            pc = ataque * math.sqrt(defensa) * math.sqrt(salud) * (cpm(nivel/2) ** 2) / 10
            pc_siguiente_nivel = ataque * math.sqrt(defensa) * math.sqrt(salud) * (cpm(nivel/2 + 0.5) ** 2) / 10
            if pc_siguiente_nivel > 1500:
                break
        return math.floor(pc)


