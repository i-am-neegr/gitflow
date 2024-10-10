# Gitflow + OOP hw1

в этом проекте есть 2 класса Product и Category<br><br>
Product: класс продукта, который имеет имя, описание, количество и цену - это его поля. Поля Product: name(str), description(str), price(float), quantity(int)<br><br>
Category: класс категории, который имеет имя описание, список продуктов, количество экземпляров класса в проекте и количество продуктов в категории Поля класса: name(str), description(str), products(list), count_category(int), count_products(int)<br><br>
так же есть функции в utils:
1. json_to_dict (конвертирует json в словарь)
2. fill_category (заполняет категорию по задоному словарю)
3. fill_categories (получает данные категорий и заполняет их)<br><br>
разница между 2 и 3 функцией в том что 3 обробатывает случай когда подается несколько словорей для заполнения класса


## Authors

- [@Artem Sergeev](https://github.com/i-am-neegr)