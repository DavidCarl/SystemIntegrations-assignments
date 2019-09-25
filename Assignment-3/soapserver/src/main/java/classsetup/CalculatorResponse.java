package classsetup;

import javax.xml.bind.annotation.XmlAccessType;
import javax.xml.bind.annotation.XmlAccessorType;
import javax.xml.bind.annotation.XmlElement;
import javax.xml.bind.annotation.XmlRootElement;
import javax.xml.bind.annotation.XmlType;


@XmlAccessorType(XmlAccessType.FIELD)
@XmlType(name = "", propOrder = {
        "mathResult"
})
@XmlRootElement(name = "CalculatorResponse")
public class CalculatorResponse {

    @XmlElement(name = "MathResult", required = true)
    protected MathResult mathResult;

    public MathResult getResult() {
        return mathResult;
    }

    public void setResult(MathResult res) {
        this.mathResult = res;
    }
}
