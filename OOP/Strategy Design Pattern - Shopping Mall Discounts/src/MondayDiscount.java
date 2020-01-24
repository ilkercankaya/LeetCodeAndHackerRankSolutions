public class MondayDiscount implements DiscountStrategy {
    @Override
    public int applyDiscount(int originalPrice) {
        return (int) (originalPrice * 0.7);
    }
}
