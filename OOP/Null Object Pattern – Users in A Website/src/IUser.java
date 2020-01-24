public abstract class IUser {
    public abstract boolean hasAccessToMyAccount();

    public String getUsername() {
        return username;
    }

    protected String username;
}
