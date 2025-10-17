import dataclasses


@dataclasses.dataclass

class User:
    first_name: str
    last_name: str
    email: str
    phone: str
    address: str
    gender: str
    birthdate: dict
    subject: str
    hobby: list
    file: str
    address: str
    state: str
    city: str

user = User(
        first_name='Test',
        last_name='Test',
        email='test@gmail.com',
        phone='7999999999',
        address='testAddress',
        gender='Female',
        birthdate={"day": "06", "month": "July", "year": 1989},
        state='Rajasthan',
        city='Jaipur',
        subject='English',
        hobby=["Sports","Reading","Music"],
        file='upload.txt')
