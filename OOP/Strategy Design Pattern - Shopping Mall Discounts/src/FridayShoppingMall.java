public class FridayShoppingMall implements IShoppingMall {
    private DiscountStrategy discountStrategy;

    public FridayShoppingMall() {
        this.discountStrategy = new FridayDiscount();
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
