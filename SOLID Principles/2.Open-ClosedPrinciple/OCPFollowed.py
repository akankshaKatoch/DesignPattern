from abc import ABC, abstractmethod

# Base class for Discount calculation
class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, price: float) -> float:
        pass

# Concrete strategy for regular customers
class RegularDiscount(DiscountStrategy):
    def apply_discount(self, price: float) -> float:
        return price * 0.95  # 5% discount

# Concrete strategy for premium customers
class PremiumDiscount(DiscountStrategy):
    def apply_discount(self, price: float) -> float:
        return price * 0.90  # 10% discount

# Context class that uses DiscountStrategy
class PriceCalculator:
    def __init__(self, discount_strategy: DiscountStrategy):
        self.discount_strategy = discount_strategy

    def calculate_price(self, price: float) -> float:
        return self.discount_strategy.apply_discount(price)

# Usage
if __name__ == "__main__":
    regular = PriceCalculator(RegularDiscount())
    premium = PriceCalculator(PremiumDiscount())

    print("Regular customer pays:", regular.calculate_price(100))
    print("Premium customer pays:", premium.calculate_price(100))