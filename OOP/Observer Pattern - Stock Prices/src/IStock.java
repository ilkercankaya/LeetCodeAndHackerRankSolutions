public abstract class IStock extends SubjectAbstract {
    int price;

    public void setPrice(int price) {
        this.price = price;
        notifyObservers();
    }

    public int getPrice() {
        return price;
    }
}
