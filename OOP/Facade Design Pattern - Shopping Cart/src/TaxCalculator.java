public class TaxCalculator {
    private String state;

    public TaxCalculator(String state) {
        this.state = state;
    }

    public int calculateTax(){
        System.out.println("CALCULATING TAX WRT " + state);
        return state.hashCode() % 100;
    }
}
