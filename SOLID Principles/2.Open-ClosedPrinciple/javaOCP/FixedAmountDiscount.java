
// FixedAmountDiscount.java
public class FixedAmountDiscount implements DiscountStrategy {
    private final double amount;

    public FixedAmountDiscount(double amount) {
        this.amount = amount;
    }

    @Override
    public double applyDiscount(double price) {
        return Math.max(0, price - amount);
    }
}