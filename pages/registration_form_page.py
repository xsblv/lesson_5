import os

from selene import browser, command, be, have


class RegistrationFormPage:

    def open(self):
        browser.open('/automation-practice-form')
        return self

    def fill_student_name(self, first_name, last_name):
        browser.element('#firstName').type(first_name)
        browser.element('#lastName').type(last_name)
        return self

    def fill_student_email(self, mail):
        browser.element('#userEmail').type(mail)
        return self

    def select_gender(self):
        browser.element('[for="gender-radio-2"]').click()
        return self


    def fill_phone_number(self, phone_number):
        browser.element('#userNumber').type(phone_number)
        return self

    def fill_birthdate(self, day, month, year):
        browser.element('[id="dateOfBirthInput"]').perform(command.js.scroll_into_view)
        browser.element('[id="dateOfBirthInput"]').click()
        browser.element('.react-datepicker__month-select').should(be.visible)
        browser.element('.react-datepicker__year-select').should(be.visible)
        browser.element('.react-datepicker__month-select').click().element(f'[value="{month}"]').click()
        browser.element('.react-datepicker__year-select').click().element(f'[value = "{year}"]').click()
        browser.element(f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)').click()
        return self

    def fill_subjects(self, subject):
        browser.element('[id="subjectsInput"]').type(subject).press_enter()
        return self

    def fill_hobbies(self):
        browser.element('[for="hobbies-checkbox-1"]').click()
        browser.element('[for="hobbies-checkbox-2"]').click()
        browser.element('[for="hobbies-checkbox-3"]').click()
        return self

    def upload_file(self, file):
        browser.element('#uploadPicture').set_value(os.path.abspath(file))
        return self

    def fill_address(self, address):
        browser.element('#currentAddress').type(address)
        return self

    def fill_state_and_city(self, state, city):
        browser.element('#state').perform(command.js.scroll_into_view)
        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(state)).click()
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(city)).click()
        return self

    def submit_form(self):
        browser.element('#submit').click()
        return self

    def check_modal(self, final_text):
        browser.element('#example-modal-sizes-title-lg').should(have.text(final_text))
        return self

    def assert_registered_student(self, full_name, email, gender, phone_number, birth_date, subject, hobbies, file, address, state_city):
        browser.element('.table').all('td').even.should(have.exact_texts(full_name, email, gender, phone_number, birth_date, subject, hobbies, file, address, state_city))
        return self

    def close(self):
        browser.element('#closeLargeModal').click
        return self
