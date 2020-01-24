import java.util.ArrayList;
import java.util.Date;

public class DateFilterDec extends FilterDecorator {
    private Filter filter;
    private Date date;
    public DateFilterDec(Filter filter, Date date) {
        this.filter = filter;
        this.date = date;
    }

    @Override
    protected void applyFilter() {
        ArrayList<Comments> list = this.filter.getComments();

        list.removeIf(comments -> Math.abs(comments.getD().getTime() - date.getTime()) > 1000);
        this.comments = list;

    }

    @Override
    public ArrayList<Comments> getComments() {
        applyFilter();
        return this.comments;
    }
}
