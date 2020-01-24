import java.util.ArrayList;

public class BaseFilter extends Filter {
    public BaseFilter(ArrayList<Comments> comments) {
        super(comments);
    }

    @Override
    protected void applyFilter() {
        // Does nothing
    }
}
