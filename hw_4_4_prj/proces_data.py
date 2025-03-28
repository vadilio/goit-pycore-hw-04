

def add_contact(args, contacts):
    # "add username phone". За цією командою бот зберігає у
    # пам'яті, наприклад у словнику, новий контакт.
    # Користувач вводить ім'я username та номер телефону phone,
    # обов'язково через пробіл.

    if len(args) > 1:
        name, phone = args
        contacts.append({'name': name, 'phone': phone})
        # contacts[name] = phone
        return "Contact added."
    return "Невірна команда: введіть Add Name Phone"


def change_contact(args, contacts):
    # "change username phone". За цією командою бот зберігає
    # в пам'яті новий номер телефону phone для контакту
    # username, що вже існує в записнику.
    if len(args) > 1:
        name, new_phone = args
        for contact in contacts:
            if contact["name"] == name:
                contact["phone"] = new_phone
                return (f"Номер телефона для {name} обновлен на {new_phone}")
        return f"Запись с именем {name} не найдена!"
    return "Невірна команда: введіть Change Name Phone"


def get_name_byphone(args, contacts):
    # "phone username" За цією командою бот виводить у консоль
    # номер телефону для зазначеного контакту username.
    if len(args) > 0:
        name = args
        for contact in contacts:
            if contact["name"] == name:
                return (f"Номер телефона для {name}: {contact["phone"]}")
        return f"Запис с іменем {name} не знайдена!"
    return "Невірна команда: введіть Phone username"


def get_all(args, contacts):
    # "all". За цією командою бот виводить всі збереженні контакти з
    # номерами телефонів у консоль.
    if contacts:
        for contact in contacts:
            return (f"Їм'я: {contact["name"]}, телефон: {contact["phone"]}")
    return f"Нема жлдного користувача"
