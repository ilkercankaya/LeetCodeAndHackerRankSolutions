public class ProfileManager {
    private static ProfileManager pm = null;
    int count = 0;
    private ProfileManager(){}

    public static ProfileManager getInstance(){
        if(pm == null){
            pm = new ProfileManager();
        }

        return pm;
    }

    public void incCount(){
        this.count += 1;
    }
}
