from faker import Faker

def generate_courier():
    fake = Faker()
    return {
        "login": fake.user_name(),
        "password": fake.password(),
        "firstName": fake.first_name()
    }

def generate_courier_missing_field(missing="login"):
    data = generate_courier()
    data.pop(missing, None)
    return data
