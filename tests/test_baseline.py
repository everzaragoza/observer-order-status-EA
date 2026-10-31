from order_status.customer_notifier import CustomerNotifier
from order_status.audit_observer import AuditObserver
from order_status.order_status import OrderStatus


def test_subscribed_observers_receive_status_updates():
    customer_notifier = CustomerNotifier()
    audit_observer = AuditObserver()
    order_status = OrderStatus("A-100")
    order_status.subscribe(customer_notifier)
    order_status.subscribe(audit_observer)

    order_status.set_status("SHIPPED")

    assert customer_notifier.messages == ["A-100:SHIPPED"]
    assert audit_observer.entries == [("A-100", "SHIPPED")]