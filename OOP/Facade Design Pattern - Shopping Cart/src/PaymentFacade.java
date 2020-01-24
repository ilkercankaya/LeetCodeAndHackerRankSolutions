public class PaymentFacade {

//    A facade is an object that provides a simplified interface to a larger body of code, such as a class library. A facade can:
//    make a software library easier to use, understand and test, since the facade has convenient methods for common tasks;
//    make the library more readable, for the same reason;
//    reduce dependencies of outside code on the inner workings of a library, since most code uses the facade, thus allowing more flexibility in developing the system;
//    wrap a poorly designed collection of APIs with a single well-designed API.

    private String state;
    private User user;

    public PaymentFacade(User user) {
        this.state = user.getAdress();
        this.user = user;
    }

    public void makePayment(){
        TaxCalculator tax = new TaxCalculator(state);
        CreditCard card = new CreditCard();
        card.makePayment(user.getId(), tax.calculateTax());
    }
}
