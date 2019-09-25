package classsetup;

import javax.xml.bind.annotation.XmlAccessType;
import javax.xml.bind.annotation.XmlAccessorType;
import javax.xml.bind.annotation.XmlElement;
import javax.xml.bind.annotation.XmlRootElement;
import javax.xml.bind.annotation.XmlType;

@XmlAccessorType(XmlAccessType.FIELD)
@XmlType(name = "", propOrder = {
        "n1", "operator","n2"
})
@XmlRootElement(name = "CalculatorRequest")
public class CalculatorRequest {

    @XmlElement(required = true)
    protected double n1;

    @XmlElement(required = true)
    protected String operator;

    @XmlElement(required = true)
    protected double n2;


    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }

    public double getN1() {
        return n1;
    }

    public double getN2() {
        return n2;
    }

    public void setN1(double n1) {
        this.n1 = n1;
    }

    public void setN2(double n2) {
        this.n2 = n2;
    }
}
