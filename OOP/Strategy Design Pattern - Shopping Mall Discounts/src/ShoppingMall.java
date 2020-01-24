public class ShoppingMall implements IShoppingMall {
    // Strategy Pattern is mostly a way to change the behaviour of an algorithm at runtime
    // Of course you can achieve this in many different ways (such as holding a value and using switch-case, but it wouldn't be as nice as Strategy Pattern).
    // we change the behaviour of an object at run time, client can also create its own strategy such as java comparator and our class would use it
    // https://stackoverflow.com/questions/25710295/differences-between-strategy-pattern-and-inheritance
    // some subclasses can share the same getDiscountdedPrice behaviour, in this case we would be needed to copy paste the code everywhere
    // to overcome the copy pasting strategy pattern can be used
    private DiscountStrategy discountStrategy;

    public ShoppingMall(DiscountStrategy discountStrategy) {
        this.discountStrategy = discountStrategy;
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
