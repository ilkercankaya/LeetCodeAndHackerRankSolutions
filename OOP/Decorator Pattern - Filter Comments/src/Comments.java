import java.util.Date;

public class Comments {
    private String comment;
    private Date d;

    public Comments(String comment, Date d) {
        this.comment = comment;
        this.d = d;
    }

    public String getComment() {
        return comment;
    }

    public Date getD() {
        return d;
    }

    public void setD(Date d) {
        this.d = d;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
}
