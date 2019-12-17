package data;

import com.opencsv.CSVReader;
import entities.Car;

import java.io.FileReader;
import java.io.IOException;
import java.util.List;

public class CSVHandler {

    public void readCsv(List<Car> cars) throws IOException {
        CSVReader reader = new CSVReader(new FileReader(System.getProperty("user.dir") + "/src/main/resources/cars.csv"));
        List<String[]> myEntries = reader.readAll();

        for(String[] s : myEntries){
            cars.add(new Car(s[1],s[2],s[3]));

        }
    }
}
