from streamz import Stream

import random
import time


def parse_event(event):
    return event


def running_total(acc, event):

    customer = event["customer"]

    acc[customer] = (
        acc.get(customer, 0)
        + event["amount"]
    )

    return acc


def run_stream():

    print("\nStarting Streaming Pipeline\n")

    source = Stream()

    (
        source
        .map(parse_event)
        .accumulate(running_total, start={})
        .sink(print)
    )

    customers = [
        "Alice",
        "Bob",
        "Eve"
    ]

    for _ in range(10):

        event = {
            "customer": random.choice(customers),
            "amount": random.randint(10, 100)
        }

        print(f"\nEvent -> {event}")

        source.emit(event)

        time.sleep(1)