public class main {
    public static void main(String[] args) {

        System.out.println("USER WITH ID 0");
        IDBConnector connector = new DBConnectorProxy(0);
        System.out.println(connector.getEntry(7));
        System.out.println(connector.getEntry(3));
        System.out.println(connector.getEntry(1));


        System.out.println("USER WITH ID 3");
        IDBConnector connectorTwo = new DBConnectorProxy(3);
        System.out.println(connectorTwo.getEntry(7));
        System.out.println(connectorTwo.getEntry(3));
        System.out.println(connectorTwo.getEntry(1));
    }
}
