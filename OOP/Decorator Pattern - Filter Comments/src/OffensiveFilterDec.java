import java.util.ArrayList;
import java.util.Iterator;

public class OffensiveFilterDec extends FilterDecorator {
    private Filter filter;

    public OffensiveFilterDec(Filter filter) {
        this.filter = filter;
    }

    @Override
    protected void applyFilter() {
        filter.applyFilter();
        ArrayList<Comments> list = filter.getComments();
        list.removeIf(comments -> comments.getComment().contains("Fool"));
        list.removeIf(comments -> comments.getComment().contains("*"));
        list.removeIf(comments -> comments.getComment().contains("stupid"));
        this.comments = list;
    }

    @Override
    public ArrayList<Comments> getComments() {
        this.applyFilter();
        return this.comments;
    }
}
