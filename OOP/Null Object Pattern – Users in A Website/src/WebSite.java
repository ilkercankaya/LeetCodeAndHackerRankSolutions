import java.util.ArrayList;

public class WebSite {
    ArrayList<IUser> users;

    public WebSite() {
        this.users = new ArrayList<>();
    }
    public void addUser(String name){
        this.users.add(new User(name));
    }

    public IUser getUser(int id){
        if(id >= this.users.size()){
            return new GuestUser();
        }
        return users.get(id);
    }
}
