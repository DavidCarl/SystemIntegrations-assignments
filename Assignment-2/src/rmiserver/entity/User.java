package rmiserver.entity;

import java.io.Serializable;

public class User implements Serializable {
    private String name;
    private String email;

    public User(String name, String email) {
        this.name = name;
        this.email = email;
    }

    public String getName() {
        return name;
    }

    public String getEmail() {
        return email;
    }

    @Override
    public String toString() {
        return "name: " + name + " Email: " + email;
    }
}
