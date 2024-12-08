class Customer:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deduct_balance(self, amount):
        """Списывает указанную сумму с баланса."""
        if amount > self.balance:
            print(f"Ошибка: недостаточно средств на счете {self.name}.")
        else:
            self.balance -= amount
            print(f"{amount} списано с баланса {self.name}. Текущий баланс: {self.balance}")

    def transfer_balance(self, amount, other_customer):
        """Передает указанную сумму другому пользователю."""
        if amount > self.balance:
            print(f"Ошибка: недостаточно средств для передачи {amount} от {self.name}. Текущий баланс: {self.balance}.")
            return
        self.balance -= amount
        other_customer.balance += amount
        print(f"{amount} передано от {self.name} к {other_customer.name}.")
        print(f"Текущий баланс {self.name}: {self.balance}")
        print(f"Текущий баланс {other_customer.name}: {other_customer.balance}")


def main():
    customer1 = Customer("Alice", 100.0)
    customer2 = Customer("Bob", 50.0)
    customer3 = Customer("Andrew", 0.0)

    print(f"Текущий баланс {customer1.name}: {customer1.balance}")
    print(f"Текущий баланс {customer2.name}: {customer2.balance}")

    amount_to_transfer = float(input("Введите сумму для передачи от Alice к Bob: "))

    customer1.transfer_balance(amount_to_transfer, customer2)

    amount_to_transfer = float(input("Введите сумму для передачи от Alice к Andrew: "))

    customer1.transfer_balance(amount_to_transfer, customer3)



if __name__ == "__main__":
    main()