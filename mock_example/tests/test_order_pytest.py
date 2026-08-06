from unittest.mock import patch

from mock_example.order import OrderService


@patch("mock_example.order.NotificationService")
def test_create_order(mock_notification):

    mock_instance = mock_notification.return_value

    mock_instance.send_email.return_value = True

    service = OrderService()

    result = service.create_order("user@test.com")

    assert result == "ORDER_CREATED"

    mock_instance.send_email.assert_called_once_with(
        "user@test.com",
        "Ваш заказ успешно оформлен"
    )