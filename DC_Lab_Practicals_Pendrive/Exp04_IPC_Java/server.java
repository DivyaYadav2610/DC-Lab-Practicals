import java.io.*;
import java.net.*;

public class server {
    public static void main(String[] args) {
        try {
            ServerSocket ss = new ServerSocket(6666);
            System.out.println("Server waiting for client...");
            Socket s = ss.accept();

            DataInputStream dis = new DataInputStream(s.getInputStream());
            int a = dis.readInt();
            int b = dis.readInt();

            System.out.println("Sum = " + (a + b));

            dis.close();
            s.close();
            ss.close();
        } catch (Exception e) {
            System.out.println(e);
        }
    }
}
