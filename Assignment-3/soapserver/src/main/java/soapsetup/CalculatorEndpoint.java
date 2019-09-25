package soapsetup;

import classsetup.CalculatorRequest;
import classsetup.CalculatorResponse;
import classsetup.MathResult;
import org.springframework.ws.server.endpoint.annotation.Endpoint;
import org.springframework.ws.server.endpoint.annotation.PayloadRoot;
import org.springframework.ws.server.endpoint.annotation.RequestPayload;
import org.springframework.ws.server.endpoint.annotation.ResponsePayload;

@Endpoint
public class CalculatorEndpoint {

    private static final String NAMESPACE_URI = "https://www.howtodoinjava.com/xml/school";

    @PayloadRoot(namespace = NAMESPACE_URI, localPart = "CalculatorRequest")
    @ResponsePayload
    public CalculatorResponse getMathResult(@RequestPayload CalculatorRequest request) {
        CalculatorResponse response = new CalculatorResponse();
        response.setResult(new MathResult(request.getN1(), request.getN2(), request.getOperator()));

        return response;
    }
}
