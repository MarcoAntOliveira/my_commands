import NetworkManager
import uuid


def configurar_ap_profissional(ssid, senha):
    print(f"[*] Configurando AP '{ssid}' via D-Bus API...")

    # Define as configurações do Hotspot
    configuracao_conexao = {
        "connection": {
            "id": "Hotspot_Drone",
            "uuid": str(uuid.uuid4()),
            "type": "802-11-wireless",
            "autoconnect": True,
        },
        "802-11-wireless": {
            "ssid": ssid.encode("utf-8"),
            "mode": "ap",  # Modo Access Point
            "band": "bg",  # Banda 2.4GHz (use 'a' para 5GHz se sua Pi suportar)
        },
        "802-11-wireless-security": {"key-mgmt": "wpa-psk", "psk": senha},
        "ipv4": {
            "method": "shared"  # Compartilha a rede (ativa o DHCP para os clientes)
        },
        "ipv6": {"method": "ignore"},
    }

    try:
        # Adiciona a nova conexão ao NetworkManager
        NetworkManager.Settings.AddConnection(configuracao_conexao)
        print("[+] Configuração gravada no sistema!")

        # Encontra a placa Wi-Fi física (wlan0)
        wifi_dev = None
        for dev in NetworkManager.NetworkManager.GetDevices():
            if dev.Interface == "wlan0":
                wifi_dev = dev
                break

        if wifi_dev:
            # Ativa a conexão que acabamos de criar na placa wlan0
            # (Nota: Pode ser necessário buscar a conexão recém-criada para ativá-la)
            print("[*] Ativando placa de rede no modo AP...")
            # Para simplificar a ativação rápida sem recarregar objetos D-Bus,
            # você pode chamar o nmcli apenas para o 'up' se preferir:
            # subprocess.run(["nmcli", "con", "up", "Hotspot_Drone"])

    except Exception as e:
        print(f"[-] Falha na configuração via API: {e}")


if __name__ == "__main__":
    configurar_ap_profissional("Wi-Fi_Do_Drone", "123456789")
