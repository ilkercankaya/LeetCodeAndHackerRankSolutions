public class FridayDiscount  implements DiscountStrategy {
    @Override
    public int applyDiscount(int originalPrice) {
        return (int) (originalPrice * 1.1);
    }
}
