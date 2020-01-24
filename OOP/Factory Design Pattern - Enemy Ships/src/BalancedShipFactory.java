public class BalancedShipFactory implements ShipFactory {
    int battleShipCount = 0;
    int supportShipCount = 0;
    int offset = 50;
    @Override
    public Ship generateShip(int id, int power) {
        if(supportShipCount > battleShipCount){
            battleShipCount += 1;
            return new BattleShip("Battle", power);
        }else if(supportShipCount < battleShipCount){
            supportShipCount += 1;
            return new SupportShip("Support", power - offset);
        }
        if(id % 2 == 0){
            battleShipCount += 1;
            return new BattleShip("Battle", power);
        }else if(id % 2 == 1){
            supportShipCount += 1;
            return new SupportShip("Support", power - offset);
        }else{
            return null;
        }
    }
}
