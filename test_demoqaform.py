import os

from pages.registration_form_page import RegistrationFormPage


def test_demoqaform(open_browser):
    registration_form_page = RegistrationFormPage()
    registration_form_page.open()
    registration_form_page.fill_student_name('Test', 'Testov')
    registration_form_page.fill_student_email('test@gmail.com')
    registration_form_page.select_gender()
    registration_form_page.fill_phone_number('7999999999')
    registration_form_page.fill_birthdate('06', '6', '1989')
    registration_form_page.fill_subjects('English')
    registration_form_page.fill_hobbies()
    registration_form_page.upload_file(os.path.abspath('resources/upload.txt'))
    registration_form_page.fill_address('testAddress')
    registration_form_page.fill_state_and_city('Rajasthan', 'Jaipur')
    registration_form_page.submit_form()
    registration_form_page.check_modal('Thanks for submitting the form')
    registration_form_page.assert_registered_student('Test Testov','test@gmail.com', 'Female', '7999999999', '06 July,1989', 'English', 'Sports, Reading, Music', 'upload.txt', 'testAddress', 'Rajasthan Jaipur')
    registration_form_page.close()
