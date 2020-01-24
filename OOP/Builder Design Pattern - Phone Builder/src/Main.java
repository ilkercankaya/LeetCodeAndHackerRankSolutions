public class Main {
    public static void main(String[] args) {
        Phone p = new PhoneBuilder().setCoreNumber(4).setId(101173).setModel("Note X").setResolution("4K").setYear(3000).build();
        p.use();
    }
}
