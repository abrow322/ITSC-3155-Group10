import pytest
from Invoice import Invoice

@pytest.fixture()
def products():
    products = {'Pen': {'qnt': 10, 'unit price': 3.75, 'discount': 5},
                'Notebook': {'qnt': 5, 'unit price': 7.5, 'discount': 10}}
    return products

@pytest.fixture()
def invoice():
    invoice = Invoice()
    return invoice

@pytest.fixture()
def delivery_type():
    delivery_type = 2
    return delivery_type

def test_canCalculateTotalImpurePrice(products):
    invoice = Invoice()
    invoice.totalImpurePrice(products)
    assert invoice.totalImpurePrice(products) == 75

def test_canCalculateTotalDiscount(invoice, products):
    invoice.totalDiscount(products)
    assert invoice.totalDiscount(products) == 5.62

def test_canCalculateTotalPurePrice(invoice, products):
    invoice.totalPurePrice(products)
    assert invoice.totalPurePrice(products) == 69.38

def test_canCalculateTotalTime(invoice, products, delivery_type):
    invoice.totalTime(products, delivery_type)
    assert invoice.totalTime(products, delivery_type) == 30

def test_canCalculateDeliveryType(invoice):
    invoice.deliveryType(2)
    assert invoice.deliveryType(2) == 1
