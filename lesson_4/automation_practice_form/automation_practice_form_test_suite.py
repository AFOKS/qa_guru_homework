import os
import time

import automation_practice_form_po

class AutomationPracticeFormTestSuite:
    def __init__(self):
        self.automation_practice_form = automation_practice_form_po.AutomationPracticeFormPO("https://qa-guru.github.io/one-page-form/automation-practice-form.html")

    def setup(self):
        self.automation_practice_form.setup()
        self.tmp_file_name = self._create_tmp_file()

    def _create_tmp_file(self):
        file_path = os.path.abspath('test_file.jpg')
        with open(file_path, 'w') as file:
            file.write("Test")
        return file_path
    
    def test_form_positive01(self):
        self.automation_practice_form.fill_in_form(self.tmp_file_name, "Dmitry","Bugaev", "bugaev@example.com", "Male","1234567890",("1988", "4", "22"),("Maths", "English"), ("Sports", "Music"), "г. Санкт-Петербург, ул. Невский проспект, д 101", "NCR",  "Noida")
        self.automation_practice_form.assert_form(self.tmp_file_name, "Dmitry","Bugaev", "bugaev@example.com", "Male","1234567890",("1988", "4", "22"),("Maths", "English"), ("Sports", "Music"), "г. Санкт-Петербург, ул. Невский проспект, д 101", "NCR",  "Noida")
    # Изменил данные теста
    def test_form_positive02(self):
        self.automation_practice_form.fill_in_form(self.tmp_file_name, "Anna","Fedotova", "fed@as.ru", "Female","8005553555",("2000", "10", "01"),("Biology", "Civics"), ("Reading", "Music"), "г. Самосир, ул. Есенина, д 123", "Haryana",  "Panipat")
        self.automation_practice_form.assert_form(self.tmp_file_name, "Anna","Fedotova", "fed@as.ru", "Female","8005553555",("2000", "10", "01"),("Biology", "Civics"), ("Reading", "Music"), "г. Самосир, ул. Есенина, д 123", "Haryana",  "Panipat")

    def test_form_positive03(self):
        self.automation_practice_form.fill_in_form(self.tmp_file_name, "Криштиано","Рональндо", "cr7@test.com", "Male","8777777701",("1985", "2", "05"),("English", "Biology", "Economics", "Arts"), ("Sports", "Reading", "Music"), "г. Лиссабон, ул. Рональдо, д 7", "Uttar Pradesh",  "Merrut")
        self.automation_practice_form.assert_form(self.tmp_file_name, "Криштиано","Рональндо", "cr7@test.com", "Male","8777777701",("1985", "2", "05"),("English", "Biology", "Economics", "Arts"), ("Sports", "Reading", "Music"), "г. Лиссабон, ул. Рональдо, д 7", "Uttar Pradesh",  "Merrut")

    def test_form_positive04(self):
        self.automation_practice_form.fill_in_form(self.tmp_file_name, "Человек","Паук", "spiderman@hero.com", "Other","8567348990",("2005", "10", "01"),("Physics", "Biology", "Computer Science", "Arts",), ("Sports", "Reading", "Music"), "г. Нью-йорк, Бруклин", "NCR",  "Delhi")
        self.automation_practice_form.assert_form(self.tmp_file_name, "Человек","Паук", "spiderman@hero.com", "Other","8567348990",("2005", "10", "01"),("Physics", "Biology", "Computer Science", "Arts"), ("Sports", "Reading", "Music"), "г. Нью-йорк, Бруклин", "NCR",  "Delhi")

    def test_form_positive05(self):
        self.automation_practice_form.fill_in_form(self.tmp_file_name, "IRON","ЧЕЛОВЕК", "ironman@hero.ru", "Male","9999999999",("1990", "4", "07"),("Maths", "Physics", "Biology", "Computer Science", "Arts", "Economics"), ("Sports", "Music"), "г. Moscow, Вашингтон street", "Uttar Pradesh",  "Agra")
        self.automation_practice_form.assert_form(self.tmp_file_name, "IRON","ЧЕЛОВЕК", "ironman@hero.ru", "Male","9999999999",("1990", "4", "07"),("Maths", "Physics", "Biology", "Computer Science", "Arts", "Economics"), ("Sports", "Music"), "г. Moscow, Вашингтон street", "Uttar Pradesh",  "Agra")



    def tear_down(self):
        if os.path.exists(self.tmp_file_name):
            os.remove(self.tmp_file_name)
        self.automation_practice_form.tear_down()


test_suite = AutomationPracticeFormTestSuite()

# Запустил тесты в правильной последовательности

test_suite.setup() #создает каждый раз файл для прикрепеления
try:
    test_suite.test_form_positive01()
finally:
    test_suite.tear_down()
    print("\n✅ Тест №1 успешно пройден!!!")


test_suite.setup()
try:
    test_suite.test_form_positive02()
finally:
    test_suite.tear_down()
    print("\n✅ Тест №2 успешно пройден!!!")

test_suite.setup()
try:
    test_suite.test_form_positive03()
finally:
    test_suite.tear_down()
    print("\n✅ Тест №3 успешно пройден!!!")

test_suite.setup()
try:
    test_suite.test_form_positive04()
    time.sleep(5)
finally:
    test_suite.tear_down()
    print("\n✅ Тест №4 успешно пройден!!!")

test_suite.setup()
try:
    test_suite.test_form_positive05()
    time.sleep(5)
finally:
    test_suite.tear_down()
    print("\n✅ Тест №5 успешно пройден!!!")
