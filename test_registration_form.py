
from pages.registration_form import RegistrationFormPage
from user import user

def test_demoqaform(open_browser):
    registration_page = RegistrationFormPage()
    registration_page.open()
    registration_page.register_user(user)
    registration_page.should_have_registered(user)