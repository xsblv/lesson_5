from selene import browser, be, have, command
import os

def test_demoqaform(open_browser):
    browser.element('#firstName').type('Test')
    browser.element('#lastName').type('Test')
    browser.element('#userEmail').type('test@gmail.com')
    browser.element('[for="gender-radio-2"]').click()
    browser.element('#userNumber').type('7999999999')
    browser.element('[id="dateOfBirthInput"]').click()
    browser.element('.react-datepicker__month-select').click().element('[value = "6"]').click()
    browser.element('.react-datepicker__year-select').click().element('[value = "1989"]').click()
    browser.element('.react-datepicker__day--006:not(.react-datepicker__day--outside-month)').click()
    browser.element('[id="subjectsInput"]').type('English').press_enter()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('[for="hobbies-checkbox-3"]').click()
    browser.element('#uploadPicture').set_value(os.path.abspath('upload.txt'))
    browser.element('#currentAddress').type('testAddress')
    browser.element('#state').perform(command.js.scroll_into_view)
    browser.element('#state').click().element('#react-select-3-option-3').click()
    browser.element('#city').click().element('#react-select-4-option-0').click()
    browser.element('#submit').click()
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.element('.table-responsive').all('tr').should(have.exact_texts('Label Values','Student Name Test Test','Student Email test@gmail.com', 'Gender Female', 'Mobile 7999999999', 'Date of Birth 06 July,1989', 'Subjects English', 'Hobbies Sports, Reading, Music', 'Picture upload.txt', 'Address testAddress', 'State and City Rajasthan Jaipur'))
    browser.element('#closeLargeModal').click


