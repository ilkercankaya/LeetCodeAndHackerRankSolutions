public class Program {
    public static void main(String[] args) {
        WebSite mySite = new WebSite();
        mySite.addUser("John ");
        mySite.addUser("Rock ");

        // Here null pattern saves us the effort to do - if(mySite.getUser(2) != null)
        System.out.println(mySite.getUser(0).getUsername());
        System.out.println(mySite.getUser(1).getUsername());
        System.out.println(mySite.getUser(2).getUsername());
        System.out.println(mySite.getUser(27273).getUsername());

        // without null object pattern
//        if(mySite.getUser(27273) != null){
//            System.out.println(mySite.getUser(27273).getUsername());
//        }

    }
}
