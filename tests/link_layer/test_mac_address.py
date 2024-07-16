import pytest
from network_simulator.link_layer.mac_address import MacAddress


def test_is_valid_with_valid_mac_address():
    assert MacAddress.is_valid_mac_address("aa:bb:cc:dd:ee:ff")


def test_is_valid_with_invalid_mac_address():
    assert not MacAddress.is_valid_mac_address("aa:bb:cc:dd:ee:ff:gg")


def test_constructor_with_valid_mac_address():
    mac_address = MacAddress("aa:bb:cc:dd:ee:ff")
    assert str(mac_address) == "AA:BB:CC:DD:EE:FF"


def test_constructor_with_invalid_mac_address():
    with pytest.raises(ValueError):
        MacAddress("aa:bb:cc:dd:ee:ff:gg")


def test_eq_with_equal_mac_addresses():
    mac_address1 = MacAddress("aa:bb:cc:dd:ee:ff")
    mac_address2 = MacAddress("aa:bb:CC:dd:ee:ff")
    assert mac_address1 == mac_address2


def test_eq_with_different_mac_addresses():
    mac_address1 = MacAddress("aa:bb:cc:dd:ee:ff")
    mac_address2 = MacAddress("aa:bb:cc:dd:ee:fe")
    assert mac_address1 != mac_address2
