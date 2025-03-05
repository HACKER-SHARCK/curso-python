import time
import sys
import random
import os
from colorama import Fore, Style, init

# Inicializa colorama
init(autoreset=True)


def loading_animation(text, duration=3):
    """Muestra una animación de carga"""
    print(Fore.GREEN + text, end="", flush=True)
    for _ in range(duration * 4):
        time.sleep(0.25)
        print(Fore.GREEN + ".", end="", flush=True)
    print()


def fake_ip_scan():
    """Simula un escaneo de direcciones IP"""
    print(Fore.CYAN + "\nIniciando escaneo de redes...\n")
    for _ in range(10):
        ip = f"192.168.{random.randint(1, 255)}.{random.randint(1, 255)}"
        status = random.choice(
            ["[✓] Acceso permitido", "[X] Conexión fallida"])
        print(Fore.YELLOW + f"Escaneando {ip}... {status}")
        time.sleep(0.5)


def fake_hack():
    """Simula un ataque falso"""
    print(Fore.RED + "\nAccediendo a servidores gubernamentales...\n")
    loading_animation("Bypasseando firewalls", 4)
    loading_animation("Extrayendo archivos confidenciales", 4)

    print(Fore.GREEN + "\nArchivos encontrados:\n")
    files = ["Contratos_Secretos.pdf",
             "Agentes_Encubiertos.docx", "Misiles_Codigos.txt"]
    for file in files:
        print(Fore.GREEN + f"Descargando: {file}")
        time.sleep(1.5)


def fake_ddos():
    """Simula un ataque DDoS"""
    print(Fore.MAGENTA + "\nIniciando ataque DDoS en servidor...\n")
    for i in range(1, 101, 5):
        bar = "#" * (i // 2) + "-" * ((100 - i) // 2)
        print(Fore.MAGENTA + f"[{bar}] {i}%", end="\r")
        time.sleep(0.2)
    print(Fore.GREEN + "\nAtaque completado. Servidor caído.\n")


def main():
    os.system("cls" if os.name == "nt" else "clear")  # Limpia pantalla
    print(Fore.GREEN + Style.BRIGHT + "=== HACKER PRO TOOL ===\n")

    fake_ip_scan()
    fake_hack()
    fake_ddos()

    print(Fore.YELLOW + "\nHack completo. Eliminando rastros...")
    loading_animation("Borrando logs", 3)
    print(Fore.GREEN + "\n¡Trabajo terminado! Sistema seguro.")


if __name__ == "__main__":
    main()
