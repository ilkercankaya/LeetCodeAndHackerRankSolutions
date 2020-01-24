public class RandomShipFactory implements ShipFactory {
    int offset = 50;

    @Override
    public Ship generateShip(int id, int power) {
        if(id % 2 == 0){
            return new BattleShip("Battle", power);
        }else if(id % 2 == 1){
            return new SupportShip("Support", power - offset);
        }else{
            return null;
        }
    }
}
