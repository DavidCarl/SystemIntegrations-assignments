package classsetup;

import javax.xml.bind.annotation.XmlAccessType;
import javax.xml.bind.annotation.XmlAccessorType;
import javax.xml.bind.annotation.XmlElement;
import javax.xml.bind.annotation.XmlType;

@XmlAccessorType(XmlAccessType.FIELD)
@XmlType(name = "MathResult", propOrder = {
        "n1",
        "operator",
        "n2",
        "result"
})
public class MathResult {
    @XmlElement(required = true)
    protected double n1;
    @XmlElement(required = true)
    protected double n2;
    @XmlElement(required = true)
    protected String operator;
    @XmlElement(required = true)
    protected double result;

    public MathResult(double n1, double n2, String operator) {
        this.n1 = n1;
        this.n2 = n2;
        this.operator = operator;
        calculate();
    }

    public MathResult() {
    }

    private void calculate(){
        switch (operator){
            case "+":
                result = n1 + n2;
                break;
            case "-":
                result = n1 - n2;
                break;
            case "*":
                result = n1 * n2;
                break;
            case "/":
                if(n2 != 0.0){
                    result = n1 / n2;
                }else{
                    result = 0.0;
                }
                break;
            default:
                result = 0.0;
                break;
        }
    }

    public double getN1() {
        return n1;
    }

    public void setN1(double n1) {
        this.n1 = n1;
    }

    public double getN2() {
        return n2;
    }

    public void setN2(double n2) {
        this.n2 = n2;
    }

    public double getResult() {
        return result;
    }
}
