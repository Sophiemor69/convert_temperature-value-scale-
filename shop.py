def shop(*prices, **options):
    """
    *prices  — любое количество цен товаров
    **options — скидка (discount, %) и доставка (delivery)
    """
    # 1. Общая стоимость товаров
    total = sum(prices)

    # 2. Достаём параметры из kwargs (со значениями по умолчанию)
    discount_percent = options.get("discount", 0)
    delivery_cost = options.get("delivery", 0)

    # 3. Скидка через lambda
    apply_discount = lambda amount, percent: amount * (1 - percent / 100)
    discounted = apply_discount(total, discount_percent)

    # 4. Добавляем доставку
    final_total = discounted + delivery_cost

    # 5. Печатаем чек
    print("=" * 40)
    print("            ЧЕК")
    print("=" * 40)
    for i, price in enumerate(prices, 1):
        print(f"  Товар {i:>2}: {price:>8.2f} руб.")
    print("-" * 40)
    print(f"  Сумма без скидки:   {total:>8.2f} руб.")
    if discount_percent:
        saving = total - discounted
        print(f"  Скидка {discount_percent}%:       -{saving:>7.2f} руб.")
    print(f"  Доставка:           {delivery_cost:>8.2f} руб.")
    print("-" * 40)
    print(f"  ИТОГО К ОПЛАТЕ:     {final_total:>8.2f} руб.")
    print("=" * 40)

    return final_total


# Проверка
shop(120, 250, 80, discount=10, delivery=40)
