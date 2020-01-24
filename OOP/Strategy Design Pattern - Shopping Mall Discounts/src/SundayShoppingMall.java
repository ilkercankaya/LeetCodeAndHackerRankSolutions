public class SundayShoppingMall implements IShoppingMall {
    private DiscountStrategy discountStrategy;

    public SundayShoppingMall() {
        this.discountStrategy = new SundayDiscount();
    }

    @Override
    public void setDiscountStrategy(DiscountStrategy discountStrategy) {
        this.discountStrategy = discountStrategy;
    }

    @Override
    public int getDiscountdedPrice(int price){
        return this.discountStrategy.applyDiscount(price);
    }
}