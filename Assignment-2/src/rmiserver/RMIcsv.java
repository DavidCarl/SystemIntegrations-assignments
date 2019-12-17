package rmiserver;

import rmiserver.entity.User;

import java.io.*;
import java.rmi.RemoteException;
import java.util.ArrayList;
import java.util.List;

public class RMIcsv implements RMIInterface, Serializable {

    private String path = "users";
    private String row;

    public RMIcsv() throws RemoteException{
        super();
    }

    @Override
    public List<User> getUsers() throws RemoteException {
        List<User> users = new ArrayList();

        try {
            BufferedReader csvReader = new BufferedReader(new FileReader(path));
            while((row = csvReader.readLine()) != null){
                String[] csvData = row.split(",");
                users.add(new User(csvData[0], csvData[1]));
            }
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            return users;
        }
    }
}