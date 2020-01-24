import java.util.Date;

public class main {
    public static void main(String[] args) {
        ShipFactory rsf = new RandomShipFactory();
        System.out.println("RANDOM");
        System.out.println(rsf.generateShip(new Date().hashCode(), 100));
        System.out.println(rsf.generateShip(new Date().hashCode(), 100));
        System.out.println(rsf.generateShip(new Date().hashCode(), 100));
        System.out.println(rsf.generateShip(new Date().hashCode(), 100));
        System.out.println(rsf.generateShip(new Date().hashCode(), 100));
        System.out.println(rsf.generateShip(new Date().hashCode(), 100));

        ShipFactory bsf = new BalancedShipFactory();
        System.out.println("BALANCED");
        System.out.println(bsf.generateShip(new Date().hashCode(), 100));
        System.out.println(bsf.generateShip(new Date().hashCode(), 100));
        System.out.println(bsf.generateShip(new Date().hashCode(), 100));
        System.out.println(bsf.generateShip(new Date().hashCode(), 100));
        System.out.println(bsf.generateShip(new Date().hashCode(), 100));
        System.out.println(bsf.generateShip(new Date().hashCode(), 100));
    }
}
