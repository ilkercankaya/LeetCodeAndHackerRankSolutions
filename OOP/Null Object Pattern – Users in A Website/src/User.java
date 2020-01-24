public class User extends IUser {

    public User(String username) {
        this.username = username;
    }

    @Override
    public boolean hasAccessToMyAccount() {
        return true;
    }
}
