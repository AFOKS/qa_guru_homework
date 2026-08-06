import unittest

from unittest.mock import patch

from mock_example.order import OrderService


class TestOrder(unittest.TestCase):

    @patch("mock_example.order.NotificationService")
    def test_create_order(self, mock_notification):

        mock_instance = mock_notification.return_value

        mock_instance.send_email.return_value = True

        service = OrderService()

        result = service.create_order("user@test.com")

        self.assertEqual(result, "ORDER_CREATED")

        mock_instance.send_email.assert_called_once_with(
            "user@test.com",
            "Ваш заказ успешно оформлен"
        )


if __name__ == "__main__":
    unittest.main()