from order_status.analytics_observer import AnalyticsObserver
from order_status.customer_notifier import CustomerNotifier
from order_status.order_status import OrderStatus


def test_analytics_observer_added_without_changing_order_status():
    order_status = OrderStatus("A-100")
    analytics = AnalyticsObserver()
    order_status.subscribe(analytics)

    order_status.set_status("PAID")
    order_status.set_status("SHIPPED")
    order_status.set_status("PAID")

    assert analytics.status_counts == {"PAID": 2, "SHIPPED": 1}


def test_unsubscribed_observer_stops_receiving_updates():
    order_status = OrderStatus("A-100")
    notifier = CustomerNotifier()
    order_status.subscribe(notifier)
    order_status.set_status("PAID")

    order_status.unsubscribe(notifier)
    order_status.set_status("SHIPPED")

    assert notifier.messages == ["A-100:SHIPPED"[:0] + "A-100:PAID"]