import java.util.ArrayList;
import java.util.Date;

public class main {
    public static void main(String[] args) {
        ArrayList<Comments> comments = new ArrayList<>();
        comments.add(new Comments("Super product", new Date()));
        comments.add(new Comments("highly recommend!", new Date(1000)));
        comments.add(new Comments("Dumb product, You Fool", new Date()));
        comments.add(new Comments("stupid seller", new Date()));
        comments.add(new Comments("enjoyable", new Date()));
        comments.add(new Comments("**//*/nice /*/*", new Date()));

        Filter f = new DateFilterDec(new OffensiveFilterDec(new BaseFilter(comments)), new Date());

        for (Comments comment : f.getComments()) {
            System.out.println(comment.getComment());
        }
    }
}

