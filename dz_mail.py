#I. Часть A. Функции

def normalize_addresses(email: str) -> str:
    return email.strip().lower()

def add_short_body(email: dict) -> dict:
    email["short_body"] = email["body"][:10] + "..."
    return email

def clean_body_text(body: str) -> str:
    return body.replace("\t", " ").replace("\n", " ").strip()

def build_sent_text(email: dict) -> str:
    return (
        f"Кому: {email['recipient']}, от {email['sender']}\n"
        f"Тема: {email['subject']}, дата: {email['date']}\n"
        f"{email['body']}"
    )

def check_empty_fields(subject: str, body:str) -> tuple[bool, bool]:
    is_subject_empty = not subject.strip()
    is_body_empty = not body.strip()
    return is_subject_empty, is_body_empty

def mask_sender_email(login: str, domain: str) -> str:
    return f"{login[:2]}***@{domain}"

def get_correct_email(email_list: list[str]) -> list[str]:
    correct_emails = []
    for email in email_list:
        email = email.strip().lower()

        if email.count("@") != 1:
            continue

        login, domain = email.split("@")

        if not login:
            continue

        if not domain or domain.startswith("."):
            continue

        if not (
           domain.endswith(".com")
            or domain.endswith(".ru")
            or domain.endswith(".net")
        ):
            continue

        correct_emails.append(email)

    return correct_emails

def create_email(sender: str, recipient: str, subject: str, body: str) -> dict:

    email = {
        "sender": sender,
        "recipient": recipient,
        "subject": subject,
        "body": body
    }
    return email

from datetime import date

def add_send_date(email: dict) -> dict:

    email["date"] = date.today().isoformat()
    return email

def extract_login_domain(address: str) -> tuple[str, str]:

    login, domain = address.split("@")
    return login, domain

#II. Часть B. Отправка письма

def sender_email(recipient_list: list[str], subject: str, message: str, *, sender="default@study.com") -> list[dict]:

#1. Проверить, что recipient_list не пустой:

    if not recipient_list:
        return []

#2. Проверить корректность email отправителя:

    sender_list = [sender]
    correct_sender_list = get_correct_email(sender_list)
    if not correct_sender_list:
            return []

    sender = correct_sender_list[0]

#2. Проверить корректность email получателя:

    recipient_list = get_correct_email(recipient_list)
    if not recipient_list:
        return []

#3. Проверить пустоту темы и тела письма:

    is_subject_empty, is_body_empty = check_empty_fields(subject, message)
    if is_subject_empty or is_body_empty:
        return []

#4. Исключить отправку самому себе:

    new_list = []

    for email in recipient_list:
            if email != sender:
                new_list.append(email)

    recipient_list = new_list


#5. Нормализовать: subject, body, recipient_list и sender:

    subject = clean_body_text(subject)
    message = clean_body_text(message)

    sender = normalize_addresses(sender)

    new_list = []

    for email in recipient_list:
       new_list.append(normalize_addresses(email))

    recipient_list = new_list


#6. Создать письмо для каждого получателя:

    emails = []

    for recipient in recipient_list:
        email = create_email(sender, recipient, subject, message)
        emails.append(email)


#7. Добавить дату отправки с помощью add_send_date():

    for email in emails:
        add_send_date(email)

#8. Замаскировать email отправителя с помощью extract_login_domain() и mask_sender_email():

    for email in emails:
        login, domain = extract_login_domain(email["sender"])
        email["sender"] = mask_sender_email(login, domain)

#9.Сохранить короткую версию в email["short_body"]:

    for email in emails:
        add_short_body(email)

#10.Сформировать итоговый текст письма функцией build_sent_text():
    for email in emails:
        email["sent_text"] = build_sent_text(email)

#11.Вернуть итоговый список писем:

    return emails