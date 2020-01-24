public abstract class Ship {
    protected String name;
    protected int power;

    public Ship(String name, int power) {
        this.name = name;
        this.power = power;
    }

    protected boolean canBeat(int ship) {
        return ship < this.power;
    }

    public String toString() {
        return name + " " + power;
    }
}
