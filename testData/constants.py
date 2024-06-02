import random
import string


class Data:

    @staticmethod
    def generate_random_userName():
        initial = "RakeshTest"
        length = random.randint(3, 6)
        userName = initial + ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
        return userName

    @staticmethod
    def generate_random_firstName():
        initial_firstName = "Virat"
        length = random.randint(1, 3)
        firstName = initial_firstName + ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
        return firstName

    @staticmethod
    def generate_random_middleName():
        initial_middleName = "The King"
        length = random.randint(1, 3)
        middleName = initial_middleName + ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
        return middleName

    @staticmethod
    def generate_random_lastname():
        initial_lastName = "Kohli"
        length = random.randint(1, 3)
        lastName = initial_lastName + ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
        return lastName
