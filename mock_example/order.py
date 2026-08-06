from mock_example.notification import NotificationService


class OrderService:

    def __init__(self):
        self.notification = NotificationService()

    def create_order(self, email):

        print("Создаем заказ")

        self.notification.send_email(
            email,
            "Ваш заказ успешно оформлен"
        )

        return "ORDER_CREATED"