import java.util.ArrayList;

public abstract class SubjectAbstract implements ISubject {
    protected ArrayList<IObserver> observers;

    public SubjectAbstract(){
        // Creates an ArrayList to hold all observers
        observers = new ArrayList<IObserver>();
    }

    public void register(IObserver newObserver) {
        // Adds a new observer to the ArrayList
        observers.add(newObserver);
    }

    public void unregister(IObserver deleteObserver) {
        // Get the index of the observer to delete
        int observerIndex = observers.indexOf(deleteObserver);
        // Print out message (Have to increment index to match)
        System.out.println("Observer " + (observerIndex+1) + " deleted");
        // Removes observer from the ArrayList
        observers.remove(observerIndex);
    }
}
