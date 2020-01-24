public class Main {
    public static void main(String[] args) {
        System.out.println("Sunday Strategy");
        IShoppingMall shoppingMall = new ShoppingMall(new SundayDiscount());
        System.out.println(shoppingMall.getDiscountdedPrice(100));
        shoppingMall.setDiscountStrategy(new MondayDiscount());
        System.out.println("Monday Strategy");
        System.out.println(shoppingMall.getDiscountdedPrice(100));
        shoppingMall.setDiscountStrategy(new FridayDiscount());
        System.out.println("Friday Strategy");
        System.out.println(shoppingMall.getDiscountdedPrice(100));

        System.out.println("Friday Strategy");
        IShoppingMall mallNYC = new FridayShoppingMall();
        System.out.println(mallNYC.getDiscountdedPrice(100));

        System.out.println("Sunday Strategy");
        IShoppingMall mallToronto = new SundayShoppingMall();
        System.out.println(mallToronto.getDiscountdedPrice(100));

    }
}
