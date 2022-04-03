from django.test import TestCase
import holomorphefrontend.taxhaven.views


class TaxHavenViewsTests(TestCase):
    def setUp(self):
        # Setup run before every test method.
        pass

    def tearDown(self):
        # Clean up run after every test method.
        pass

    def test_views_yes_gbp_seventeen_per_gbp_one_thousand_of_capital_above_gbp_two_thousands_with_a_maximum_duty_of_gbp_five_thousands(self):
        print("test_views_yes_gbp_seventeen_per_gbp_one_thousand_of_capital_above_gbp_two_thousands_with_a_maximum_duty_of_gbp_five_thousands")

        self.assertEqual(holomorphefrontend.taxhaven.views.yes_gbp_seventeen_per_gbp_one_thousand_of_capital_above_gbp_two_thousands_with_a_maximum_duty_of_gbp_five_thousands, "Yes, GBP £17 per GBP £1,000 of capital above GBP £2,000 with a maximum duty of GBP £5,000")
