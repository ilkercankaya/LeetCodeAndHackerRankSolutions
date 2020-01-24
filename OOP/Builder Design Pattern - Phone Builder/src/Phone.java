public class Phone extends PhoneAbstract{
    public Phone(int id, String model, int coreNumber, String resolution, int year) {
        this.id = id;
        this.model = model;
        this.coreNumber = coreNumber;
        this.resolution = resolution;
        this.year = year;
    }

    @Override
    public void use() {
        System.out.println("ID");
        System.out.println(String.valueOf(this.id));
        System.out.println("Model");
        System.out.println(this.model);
        System.out.println("Core Number");
        System.out.println(String.valueOf(this.coreNumber));
        System.out.println("Resolution");
        System.out.println(this.resolution);
        System.out.println("Year");
        System.out.println(String.valueOf(this.year));
    }
}
