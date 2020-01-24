public class DBConnecter implements IDBConnector {
    int userID = -1;
    int [] info;

    public DBConnecter(int id) {
        this.userID = id % 5;
    }

    @Override
    public boolean connectDB() {
        // imagine that the array is parsed through a DB
        this.info = new int[]{11, 12, 13, 15, 15};
        return true;
    }

    @Override
    public int getEntry(int id) {
        connectDB();
        return this.info[id % 5];
    }
}
