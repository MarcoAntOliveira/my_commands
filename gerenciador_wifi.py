import subprocess
import sys


def criar_hotspot(ssid, senha):
    print(f"[*] Configurando Hotspot Wi-Fi: {ssid}...")

    # Comando para criar e ativar o ponto de acesso
    comando = [
        "sudo",
        "nmcli",
        "device",
        "wifi",
        "hotspot",
        "ifname",
        "wlan0",
        "ssid",
        ssid,
        "password",
        senha,
    ]

    try:
        # Executa o comando e captura a saída
        resultado = subprocess.run(comando, capture_output=True, text=True, check=True)
        print("[+] Hotspot criado com sucesso!")
        print(resultado.stdout)

        # Garante que vai reconectar sozinho no boot
        subprocess.run(
            [
                "sudo",
                "nmcli",
                "con",
                "modify",
                "Hotspot",
                "connection.autoconnect",
                "yes",
            ],
            check=True,
        )
        print("[+] Configurado para iniciar automaticamente no boot.")

    except subprocess.CalledProcessError as e:
        print(f"[-] Erro ao criar o hotspot: {e.stderr}", file=sys.stderr)


def desativar_hotspot():
    print("[*] Desativando Hotspot...")
    try:
        # Desativa a conexão chamada 'Hotspot'
        subprocess.run(["sudo", "nmcli", "connection", "down", "Hotspot"], check=True)
        print("[+] Hotspot desligado.")
    except subprocess.CalledProcessError as e:
        print(f"[-] Erro ao desligar o hotspot: {e.stderr}", file=sys.stderr)


if __name__ == "__main__":
    # Exemplo de uso:
    criar_hotspot("test", "0508")
