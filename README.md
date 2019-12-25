# test_for_csssr

Скачайте файл test_link_name.py на свой компьютер.
Для запуска теста необходим Python версии не ниже 3.0

Затем нужно будет создать виртуальное окружение, выберете папку в которой планируете его разместить и выполните к командной строке все следующие команды:
python -m venv selenium_env

Затем активируем виртуальное окружение:
selenium_env\Scripts\activate.bat

В виртуальном окружение установим библиотеку Selenium иначе тест не будет работать:
pip install selenium==3.14.0

Теперь можем запустить наш тест:
test_link_name.py
