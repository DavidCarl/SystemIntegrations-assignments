package rmiserver;
/**
 *
 * @author Dora Di
 */
import java.rmi.Naming;
import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class RMIServer {
    /**
     * @param args the command line arguments
     */
    public static Registry registry;


    public static void main(String[] args) {
        try {
            System.out.println("RMI server localhost starts");

            // Create a server registry at default port 1099
            registry = LocateRegistry.createRegistry(1099);
            System.out.println("RMI registry created ");

            // Create engine of remote services, running on the server
            RMIInterface remoteCSV = new RMIcsv();
            RMIInterface remoteDB = new RMIdb();

            // Register the engine by the name, which later will be given to the clients
            Naming.rebind("//localhost/csv", remoteCSV);
            Naming.rebind("//localhost/db", remoteDB);

        } catch (Exception e) {
            System.err.println("Exception:" + e);
        }
    }
}