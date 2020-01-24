public class Program {
    public static void main(String[] args) {
        IObserver observerOne = new StockObserver();
        IObserver observerTwo = new StockObserver();

        GoogleStock googleStock = new GoogleStock();
        googleStock.setPrice(1000);
        googleStock.register(observerOne);
        googleStock.register(observerTwo);

        // observers should be notified here
        googleStock.setPrice(1010);

        // unregister and test if it works
        googleStock.unregister(observerTwo);
        googleStock.setPrice(1040);

    }
}
