import java.util.ArrayList;

public abstract class Filter {
    protected ArrayList<Comments> comments;

    public Filter() {}

    public Filter(ArrayList<Comments> comments) {
        this.comments = comments;
    }

    protected abstract void applyFilter();

    public void setComments(ArrayList<Comments> comments) {
        this.comments = comments;
    }

    public ArrayList<Comments> getComments() {
        return comments;
    }
}
