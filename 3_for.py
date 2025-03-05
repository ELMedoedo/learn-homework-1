"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

spis = [
    {
        "product": "iPhone 12",
        "items_sold": [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186],
    },
    {
        "product": "Xiaomi Mi11",
        "items_sold": [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316],
    },
    {
        "product": "Samsung Galaxy 21",
        "items_sold": [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247],
    },
]


def main():
    summarn_kolich, srednie_prodazhi, summarn_kolich_all, srednie_prodazhi_all = (
        0,
        0,
        0,
        0,
    )
    for i in range(len(spis)):
        slovar = spis[i]
        summarn_kolich = sum(slovar["items_sold"])
        print(
            "Суммарное количество продаж для", slovar["product"], "-->", summarn_kolich
        )
        srednie_prodazhi = summarn_kolich // len(slovar["items_sold"])
        print(
            "Среднее количество продаж для", slovar["product"], "-->", srednie_prodazhi
        )
        print("---------")
        summarn_kolich_all += summarn_kolich
        srednie_prodazhi_all += srednie_prodazhi
    print("Суммарное количество продаж:", summarn_kolich_all)
    print("Среднее количество продаж:", srednie_prodazhi_all)


if __name__ == "__main__":
    main()
