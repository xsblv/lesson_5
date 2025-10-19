import os
from selene import browser, command, be, have
from test_data.user import User

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

    def select_gender(self, gender):
        browser.all('[name="gender"]').element_by(have.value(gender)).element(
            ".."
        ).element("label").click()


    def fill_phone_number(self, phone_number):
        browser.element('#userNumber').type(phone_number)
        return self

    def fill_birthdate(self, birthdate):
        browser.element('[id="dateOfBirthInput"]').perform(command.js.scroll_into_view)
        browser.element('[id="dateOfBirthInput"]').click()
        browser.element('.react-datepicker__month-select').should(be.visible)
        browser.element('.react-datepicker__year-select').should(be.visible)
        browser.element(".react-datepicker__month-select").all("option").element_by(have.text(birthdate["month"])).click()
        browser.element('.react-datepicker__year-select').click().element(f'[value = "{birthdate["year"]}"]').click()
        browser.element(f'.react-datepicker__day--0{f"{int(birthdate['day']):02d}"}:not(.react-datepicker__day--outside-month)').click()

    def fill_subjects(self, subject):
        browser.element('[id="subjectsInput"]').type(subject).press_enter()

    def fill_hobbies(self, hobby):
        for hobby in hobby:
            browser.all("label[for^='hobbies']").element_by(have.text(hobby)).click()

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

    def register_user(self, user: User):
        self.fill_student_name(user.first_name, user.last_name)
        self.fill_student_email(user.email)
        self.select_gender(user.gender)
        self.fill_phone_number(user.phone)
        self.fill_birthdate(user.birthdate)
        self.fill_subjects(user.subject)
        self.fill_hobbies(user.hobby)
        self.upload_file(os.path.abspath(user.file))
        self.fill_address(user.address)
        self.fill_state_and_city(user.state, user.city)
        self.submit_form()

    def should_have_registered(self, user: User):
        browser.element('.table').all('td').even.should(have.exact_texts(f"{user.first_name} {user.last_name}", user.email, user.gender, user.phone, f"{user.birthdate['day']} {user.birthdate['month']},{user.birthdate['year']}", user.subject,", ".join(user.hobby), user.file, user.address,
                             f"{user.state} {user.city}"))
        return self




