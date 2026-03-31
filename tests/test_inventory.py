import pytest
from pages.inventory_page import InventoryPage


@pytest.mark.smoke
def test_productos_visibles(logged_in_page):
    """TC-05: Se listan exactamente 6 productos."""
    inventory = InventoryPage(logged_in_page)

    assert inventory.get_product_count() == 6


def test_ordenar_por_precio_menor_mayor(logged_in_page):
    """TC-06: Ordenar por precio menor a mayor reordena la lista."""
    inventory = InventoryPage(logged_in_page)

    names_before = inventory.get_product_names()
    inventory.sort_by("lohi")
    names_after = inventory.get_product_names()

    assert names_before != names_after


@pytest.mark.smoke
def test_agregar_producto_al_carrito(logged_in_page):
    """TC-07: Agregar un producto muestra el badge en el carrito."""
    inventory = InventoryPage(logged_in_page)

    inventory.add_first_product_to_cart()

    assert inventory.cart_badge_is_visible()


def test_badge_carrito_se_actualiza(logged_in_page):
    """TC-08: El badge muestra el número correcto de productos."""
    inventory = InventoryPage(logged_in_page)

    inventory.add_first_product_to_cart()

    assert inventory.get_cart_badge_count() == 1