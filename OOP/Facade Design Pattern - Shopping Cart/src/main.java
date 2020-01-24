public class main {
    public static void main(String[] args) {
        // Without Facade Pattern
//        String state = "Istanbul";
//        User u = new User(1, state);
//        TaxCalculator tax = new TaxCalculator(state);
//        CreditCard card = new CreditCard();
//        card.makePayment(tax.calculateTax());

        PaymentFacade payment = new PaymentFacade(new User(10,"New York City"));
        payment.makePayment();
    }
}
