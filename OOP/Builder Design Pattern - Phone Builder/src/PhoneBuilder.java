public class PhoneBuilder {
    private int id;
    private String model;
    private int coreNumber;
    private String resolution;
    private int year;

    public PhoneBuilder setId(int id) {
        this.id = id;
        return this;
    }

    public PhoneBuilder setModel(String model) {
        this.model = model;
        return this;
    }

    public PhoneBuilder setCoreNumber(int coreNumber) {
        this.coreNumber = coreNumber;
        return this;
    }

    public PhoneBuilder setResolution(String resolution) {
        this.resolution = resolution;
        return this;
    }

    public PhoneBuilder setYear(int year) {
        this.year = year;
        return this;
    }

    public Phone build(){
        return new Phone(this.id, this.model, this.coreNumber, this.resolution, this.year);
    }
}
