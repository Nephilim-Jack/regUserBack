from django.test import TestCase
from .models import User
from django.contrib.auth.hashers import make_password, check_password

# Create your tests here.


class UserTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(**{
            'username': 'TestUser',
            'first_name': 'Test User First Name',
            'last_name': 'Test User Last Name',
            'email': 'test@example.com',
            'password': make_password('testUserPass')
        })

        user.profile.country = 'Test Country'
        user.profile.state = 'Test State'
        user.profile.city = 'Test City'
        user.profile.cep = 99999999
        user.profile.street = 'Test Street'
        user.profile.houseNumber = 99
        user.profile.complement = 'Test Complement'
        user.save()

    def test_profile_data(self):
        testUser = User.objects.get(username='TestUser')

        self.assertEqual(
            str(testUser.profile), 'TestUser',
            'Check if username is the repr of profile'
        )
        self.assertEqual(
            testUser.profile.country, 'Test Country',
            'Check if country is ok'
        )
        self.assertEqual(
            testUser.profile.houseNumber, 99,
            'Check if houseNumber is ok'
        )
        self.assertEqual(
            check_password('testUserPass', testUser.password), True,
            'Check if password is correctly encoded'
        )
