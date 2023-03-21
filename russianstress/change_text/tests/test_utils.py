from django.test import TestCase
from change_text.utils import add_stress

class AddStressTest(TestCase):

    def test_add_stress_returns_string_of_words(self):
        text = "В Москве состоялись переговоры между лидерами России и Китая."
        result = add_stress(text)
        print(result)

    def test_adds_stress_to_words(self):
        pass

    def test_func_keeps_punctuation(self):
        pass

    def test_func_preserves_original_spacing(self):
        pass
