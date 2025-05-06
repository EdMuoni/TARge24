class Container:
    """Container to transport orders."""

    def __init__(self, volume: int, orders: list[Order]):
        self.volume = volume
        self.orders = orders

    @property
    def volume_left(self):
        """
        Calculate and return remaining volume.
        """
        return self.volume - sum(map(lambda o: o.total_volume, self.orders))

    def add_order(self, order: Order) -> bool:
        """
        Add order to container if there is enough volume left.

        :param order: order to be added.
        :return: true if succeeded.
        """
        if self.volume_left >= order.total_volume:
            self.orders.append(order)
            return True
        return False


class ContainerAggregator:
    """Algorithm to prepare containers."""

    def __init__(self, container_volume: int):
        """
        Initialize Container Aggregator.

        :param container_volume: Volume of each container created by this aggregator.
        """
        self.container_volume = container_volume
        self.not_used_orders: list[Order] = []

    def prepare_containers(self, orders: tuple) -> dict:
        """
        Create containers and put orders to them.

        If order cannot be put to a container, it is added to self.not_used_orders list.

        :param orders: tuple of orders.
        :return: dict where keys are destinations and values are containers to that destination with orders.
        """
        result = {}
        for order in orders:
            if order.total_volume > self.container_volume:
                self.not_used_orders.append(order)
                continue
            containers = result.get(order.destination, [Container(self.container_volume, orders=[])])
            for container in containers:
                if container.add_order(order):
                    break
            else:
                containers.append(Container(self.container_volume, orders=[order]))
                result[order.destination] = containers
        return result

if __name__ == '__main__':
    # Your test code goes here
