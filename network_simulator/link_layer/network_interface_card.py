from network_simulator.link_layer.mac_address import MacAddress
from network_simulator.link_layer.frame import Frame
from abc import ABC, abstractmethod

class NetworkInterfaceCard(ABC):
    def __init__(self, mac_address: MacAddress) -> None:
        self.mac_address = mac_address

    @abstractmethod
    def send_frame(self, frame: Frame) -> None:
        """Sends a frame to the network"""
    
    @abstractmethod
    def receive_frame(self, frame: Frame) -> None:
        """Receives a frame from the network"""
