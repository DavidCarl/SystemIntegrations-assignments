package rpc;

import entities.Car;

import java.util.List;

public class MessageHandler {
    private static String categories(List<Car> cars) {

        String message = "";
        for (Car car : cars) {
            if (!message.contains(car.getBrand())) {

                message += car.getBrand() + "\n";
            }

        }
        return message;
    }

    private static String pickCarBrand(String category, List<Car> cars) {
        String carList = "";
        for (Car car : cars) {
            if (car.getBrand().equals(category)) {
                carList += car.getModel() + "\n";
            }
        }
        if (!carList.isEmpty()) {
            carList += "please pick one of the cars";
        }
        return carList;
    }

    private static String chooseModel(String carChoice, List<Car> cars) {
        String carMessage = "";
        for (Car car : cars) {
            if (car.getModel().equals(carChoice)) {
                carMessage += car + "\nPlease pick a brand or model again!";
            }
        }
        return carMessage;
    }

    public String handleMessages(String message, List<Car> cars) {
        System.out.println("handler: " + message);
        String response = "";
        if(message.equals("getBrands")){
            response+=categories(cars);
        } else {
            if(pickCarBrand(message,cars).equals("")){
                if(chooseModel(message,cars).equals("")){
                    response+= "no such brand/model exists";
                }
            }
            if(!pickCarBrand(message,cars).equals("") && !chooseModel(message,cars).equals("")){
                response+= pickCarBrand(message,cars);
            } else {
                if(!pickCarBrand(message,cars).equals("")){
                    response+= pickCarBrand(message,cars);
                }
                if(!chooseModel(message,cars).equals("")){
                    response+= chooseModel(message,cars);
                }
            }
        }
        return response;
    }
}