import pytest
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


@pytest.mark.smoke
def test_producto_aparece_en_carrito(logged_in_page):
    """TC-09: Producto agregado desde inventario aparece en el carrito."""
    inventory = InventoryPage(logged_in_page)
    inventory.add_first_product_to_cart()

    cart = CartPage(logged_in_page)
    cart.navigate()

    assert cart.get_item_count() == 1


def test_eliminar_producto_del_carrito(logged_in_page):
    """TC-10: Eliminar un producto deja el carrito vacío."""
    inventory = InventoryPage(logged_in_page)
    inventory.add_first_product_to_cart()

    cart = CartPage(logged_in_page)
    cart.navigate()
    cart.remove_first_item()

    assert cart.get_item_count() == 0