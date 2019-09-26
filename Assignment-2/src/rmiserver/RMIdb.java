package rmiserver;

import rmiserver.entity.User;

import java.io.Serializable;
import java.rmi.RemoteException;
import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public class RMIdb implements RMIInterface, Serializable {

    private Connection connection;
    private String connectionURL = "jdbc:sqlserver://localhost:3306;" +
                                   "database=YourDBHere" +
                                   "user=YourUserHere" +
                                   "password=YourPasswordHere";


    public RMIdb()  throws RemoteException{
        super();
        try {
            connection = DriverManager.getConnection(connectionURL);
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    @Override
    public List<User> getUsers() throws RemoteException {
        List<User> users = new ArrayList();
        try {
            PreparedStatement stmt = connection.prepareStatement("SELECT * FROM users");
            ResultSet rs = stmt.executeQuery();
            while(rs.next()){
                users.add(new User(rs.getString("name"), rs.getString("email")));
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return users;
    }
}
