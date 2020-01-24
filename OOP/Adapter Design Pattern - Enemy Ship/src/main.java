public class main {
    public static void main(String[] args) {
        Enemy ship = new Enemy();

        ship.attack();
        ship.killItself();

        Enemy adapted = new EnemyAdapter(new AlienRobot());
        adapted.attack();
        adapted.killItself();
    }
}
