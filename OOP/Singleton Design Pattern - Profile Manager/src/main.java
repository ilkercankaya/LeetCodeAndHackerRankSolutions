public class main {
    public static void main(String[] args) {
        ProfileManager pm = ProfileManager.getInstance();

        pm.incCount();
        System.out.println(pm.count);
        pm.incCount();
        System.out.println(pm.count);
        pm.incCount();
        System.out.println(pm.count);

        System.out.println("SHARED INSTANCE PROOF");
        pm = ProfileManager.getInstance();
        System.out.println(pm.count);
        pm.incCount();
        System.out.println(pm.count);

    }
}
