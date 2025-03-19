import json

DUMP1090_JSON_PATH = "/run/dump1090-mutability/aircraft.json"

def get_local_adsb_data():
    try:
        with open(DUMP1090_JSON_PATH, "r") as f:
            data = json.load(f)

        if "aircraft" not in data or not data["aircraft"]:
            print("Nenhuma aeronave detectada no momento.")
            return

        print("Voos capturados:")
        for flight in data["aircraft"]:
            fgt = flight.get("flight", "N/A").upper()
            altitude = flight.get("altitude", "N/A")
            velocidade = flight.get("speed", "N/A")
            if fgt != "N/A":
                print(f"{fgt}, Altitude: {altitude} ft, Velocidade: {velocidade} nos")

    except Exception as e:
        print(f"Erro ao ler os dados do ADS-B: {e}")

if __name__ == "__main__":
    get_local_adsb_data()
