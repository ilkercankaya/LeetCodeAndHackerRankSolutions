public class GoogleStock extends IStock {
    @Override
    public void notifyObservers() {
        for(IObserver observer : observers){
            observer.update(getPrice());
        }
    }
}
