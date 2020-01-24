public class StockObserver implements IObserver {
    @Override
    public void update(int price) {
        System.out.println("An observer has been notified the price of the stock is now " + price);
    }
}
