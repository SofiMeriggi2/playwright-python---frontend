# tests/test_checkout.py
import pytest
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.mark.smoke
def test_checkout_flujo_completo(logged_in_page):
    """TC-11: Flujo end-to-end — agregar producto y completar compra."""
    # Paso 1 — agregar producto al carrito
    inventory = InventoryPage(logged_in_page)
    inventory.add_first_product_to_cart()

    # Paso 2 — ir al carrito e iniciar checkout
    cart = CartPage(logged_in_page)
    cart.navigate()
    cart.go_to_checkout()

    # Paso 3 — completar formulario
    checkout = CheckoutPage(logged_in_page)
    checkout.fill_form("Sofi", "QA", "1900")
    checkout.continue_checkout()

    # Paso 4 — confirmar compra
    checkout.finish_checkout()

    assert checkout.get_confirm_header() == "Thank you for your order!"


def test_checkout_back_to_home(logged_in_page):
    """TC-11b: Botón Back Home redirige al inventario."""
    inventory = InventoryPage(logged_in_page)
    inventory.add_first_product_to_cart()

    cart = CartPage(logged_in_page)
    cart.navigate()
    cart.go_to_checkout()

    checkout = CheckoutPage(logged_in_page)
    checkout.fill_form("Sofi", "QA", "1900")
    checkout.continue_checkout()
    checkout.finish_checkout()
    checkout.back_to_home()

    assert logged_in_page.url.endswith("/inventory.html")


@pytest.mark.negative
def test_checkout_campo_vacio_first_name(logged_in_page):
    """TC-12: Formulario vacío muestra error de validación."""
    inventory = InventoryPage(logged_in_page)
    inventory.add_first_product_to_cart()

    cart = CartPage(logged_in_page)
    cart.navigate()
    cart.go_to_checkout()

    checkout = CheckoutPage(logged_in_page)
    checkout.fill_form("", "QA", "1900")
    checkout.continue_checkout()

    assert "First Name is required" in checkout.get_error_message()
    
@pytest.mark.negative
def test_checkout_campo_vacio_last_name(logged_in_page):
    """TC-13: Formulario con Last Name vacío muestra error de validación."""
    inventory = InventoryPage(logged_in_page)
    inventory.add_first_product_to_cart()

    cart = CartPage(logged_in_page)
    cart.navigate()
    cart.go_to_checkout()

    checkout = CheckoutPage(logged_in_page)
    checkout.fill_form("Sofi", "", "1900")
    checkout.continue_checkout()

    assert "Last Name is required" in checkout.get_error_message()

@pytest.mark.negative
def test_checkout_campo_vacio_postal_code(logged_in_page):
    """TC-14: Formulario con Postal Code vacío muestra error de validación."""
    inventory = InventoryPage(logged_in_page)
    inventory.add_first_product_to_cart()

    cart = CartPage(logged_in_page)
    cart.navigate()
    cart.go_to_checkout()

    checkout = CheckoutPage(logged_in_page)
    checkout.fill_form("Sofi", "QA", "")
    checkout.continue_checkout()

    assert "Postal Code is required" in checkout.get_error_message()