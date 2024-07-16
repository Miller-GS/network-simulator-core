from network_simulator.link_layer.mac_address import MacAddress
from abc import ABC, abstractmethod

class Frame(ABC):
    def __init__(self, source_address: MacAddress, destination_address: MacAddress, data: bytes) -> None:
        self.source_address = source_address
        self.destination_address = destination_address
        self.data = data

    @abstractmethod
    def encode(self) -> bytes:
        """Encodes the frame into bytes"""

    @staticmethod
    @abstractmethod
    def decode(encoded_frame: bytes) -> 'Frame':
        """Decodes the bytes into a frame"""