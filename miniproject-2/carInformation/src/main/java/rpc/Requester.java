package rpc;

import com.rabbitmq.client.AMQP;
import com.rabbitmq.client.Channel;
import com.rabbitmq.client.Connection;
import com.rabbitmq.client.ConnectionFactory;

import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.util.Scanner;
import java.util.UUID;
import java.util.concurrent.ArrayBlockingQueue;
import java.util.concurrent.BlockingQueue;
import java.util.concurrent.TimeoutException;

public class Requester implements AutoCloseable {

    private Connection connection;
    private Channel channel;
    private String requestQueueName = "car_queue";

    public Requester() throws IOException, TimeoutException {
        ConnectionFactory factory = new ConnectionFactory();
        factory.setHost("192.168.0.124");
        factory.setUsername("root");
        factory.setPassword("myPassword");
        connection = factory.newConnection();
        channel = connection.createChannel();
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        try (Requester start = new Requester()) {
            String response = start.call("getBrands");

            System.out.println(response);
            System.out.print("please type a car brand: ");
            while (true) {
                String input = scan.nextLine();
                response = start.call(input);
                System.out.println(response);
            }
        } catch (IOException | TimeoutException | InterruptedException e) {
            e.printStackTrace();
        }
    }

    public String call(String message) throws IOException, InterruptedException {
        final String corrId = UUID.randomUUID().toString();
        String replyQueueName = channel.queueDeclare().getQueue();
        AMQP.BasicProperties props = new AMQP.BasicProperties
                .Builder()
                .correlationId(corrId)
                .replyTo(replyQueueName)
                .build();
        channel.basicPublish("", requestQueueName, props, message.getBytes(StandardCharsets.UTF_8));
        final BlockingQueue<String> response = new ArrayBlockingQueue<>(1);
        String ctag = channel.basicConsume(replyQueueName, true, (consumerTag, delivery) -> {
            if (delivery.getProperties().getCorrelationId().equals(corrId)) {
                response.offer(new String(delivery.getBody(), StandardCharsets.UTF_8));
            }
        }, consumerTag -> {
        });
        String result = response.take();
        channel.basicCancel(ctag);
        return result;
    }

    @Override
    public void close() throws IOException {
        connection.close();
    }
}
