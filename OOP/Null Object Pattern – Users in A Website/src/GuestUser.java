public class GuestUser extends IUser {
    // NULL OBJECT PATTERN
    // Handle Nulls with a default behaviour that should be consistent through out the whole app
    // This pattern is all about handling the null keyword in a way that removes all of those nasty if (object == null) checks from your code.
    // It also makes handling default values for null objects a breeze.
    public GuestUser() {
        this.username = "Guest";
    }

    @Override
    public boolean hasAccessToMyAccount() {
        // a guest does not have my account page
        return false;
    }
}
