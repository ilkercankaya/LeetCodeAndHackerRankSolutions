public class DBConnectorProxy implements IDBConnector {
    // Proxy Design Pattern allows us to "Control and manage access to the object they are protecting."
    DBConnecter connector = null;

    int userID = -1;
    int [] info;

    public DBConnectorProxy(int id) {
        this.userID = id % 5;
    }


    @Override
    public boolean connectDB() {
        // Secure DB for banned users - assume user 3 is banned
        if(userID == 3){
            System.out.println("This User Is Not Allowed to Connect To DB");
            return false;
        }

        // Cache info here so that we dont make calls to the DB all the time
        if(connector == null){
            connector = new DBConnecter(this.userID);
            connector.connectDB();
            this.info = connector.info;
        }

        return true;
    }

    @Override
    public int getEntry(int id) {
        if(!connectDB())
            return -1;

        return this.info[id % 5];
    }
}
