package rmiclient;

import java.rmi.*;
import java.util.ArrayList;
import rmiserver.*;
import rmiserver.entity.User;

public class RMIClient {

    public static void getService(String endpoint) throws Exception {
        // name =  rmi:// + ServerIP +  /EngineName;

        String name = "rmi://localhost/" + endpoint;

        // Create local stub, lookup in the registry searching for the remote engine - the interface with the methods we want to use remotely
        RMIInterface remoteEngine = (RMIInterface) Naming.lookup(name);

        // Send requests to the remote services the usual way, as if they are local
        ArrayList<User> result = (ArrayList<User>) remoteEngine.getUsers();

        printout(result);
    }

    public static void printout(ArrayList<User> users) {
        for (User u : users) {
            System.out.println(u);
        }
    }


    public static void main(String[] args) {
        try {
            getService("csv");
            getService("db");
        } catch (Exception e) {
            System.out.println("Exception: " + e);
        }
    }
}
