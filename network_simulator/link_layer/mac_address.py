class MacAddress:
    def __init__(self, mac_address: str) -> None:
        if not MacAddress.is_valid_mac_address(mac_address):
            raise ValueError(f"Invalid MAC address: {mac_address}")
        self.mac_address = mac_address.upper()

    @staticmethod
    def is_valid_mac_address(mac_address: str) -> bool:
        if len(mac_address) != 17:
            return False
        for i in range(0, 17):
            if i % 3 == 2 and mac_address[i] != ":":
                return False
            if i % 3 != 2 and (not mac_address[i].isalnum()):
                return False
        return True

    def __str__(self):
        return self.mac_address

    def __eq__(self, other: "MacAddress"):
        return self.mac_address == other.mac_address

    def __hash__(self):
        return hash(self.mac_address)
