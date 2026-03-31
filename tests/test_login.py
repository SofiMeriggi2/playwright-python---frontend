# tests/test_login.py
import pytest
from pages.login_page import LoginPage
from data.messages import ErrorMessages


@pytest.mark.smoke
def test_login_exitoso(page):
    """TC-01: Usuario estándar puede loguearse correctamente."""
    login = LoginPage(page)
    login.navigate()
    login.login_as_standard()

    assert page.url.endswith("/inventory.html")


@pytest.mark.smoke
@pytest.mark.negative
def test_login_usuario_bloqueado(page):
    """TC-02: Usuario bloqueado ve mensaje de error específico."""
    login = LoginPage(page)
    login.navigate()
    login.login_as_locked()

    assert login.get_error_message() == ErrorMessages.LOCKED_USER


@pytest.mark.negative
def test_login_credenciales_invalidas(page):
    """TC-03: Credenciales incorrectas muestran mensaje de error."""
    login = LoginPage(page)
    login.navigate()
    login.login("usuario_falso", "password_falsa")

    assert login.get_error_message() == ErrorMessages.INVALID_CREDS


@pytest.mark.negative
def test_login_campos_vacios(page):
    """TC-04: Sin completar campos muestra error de validación."""
    login = LoginPage(page)
    login.navigate()
    login.login("", "")

    assert login.get_error_message() == ErrorMessages.USERNAME_REQUIRED