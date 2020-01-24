public class EnemyAdapter extends Enemy{
    private AlienRobot alienRobot;

    public EnemyAdapter(AlienRobot alienRobot) {
        this.alienRobot = alienRobot;
    }

    @Override
    public void attack() {
        System.out.println("Adapter bombShips");
        this.alienRobot.attackWithAI();
    }

    @Override
    public void killItself() {
        System.out.println("Adapter killItself");
        this.alienRobot.explodeAsap();
    }
}
