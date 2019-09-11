package rmiserver;

import rmiserver.entity.User;

import java.rmi.Remote;
import java.rmi.RemoteException;
import java.util.List;

public interface RMIInterface extends Remote {
    public List<User> getUsers() throws RemoteException;

}
