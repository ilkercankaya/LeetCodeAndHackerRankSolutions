public class User {
    private int id;
    private String adress;

    public User(int id, String adress) {
        this.id = id;
        this.adress = adress;
    }

    public String getAdress() {
        return adress;
    }

    public int getId() {
        return id;
    }
}
