import java.io.*;
import java.net.*;
import java.util.*;

public class client {
    public static void main(String[] args) {
        Scanner userInput = new Scanner(System.in);
        try {
            Socket s = new Socket("localhost", 6666);
            DataOutputStream dout = new DataOutputStream(s.getOutputStream());

            System.out.print("Enter 1st no: ");
            int a = userInput.nextInt();
            System.out.print("Enter 2nd no: ");
            int b = userInput.nextInt();

            dout.writeInt(a);
            dout.writeInt(b);
            dout.flush();

            dout.close();
            s.close();
        } catch (Exception e) {
            System.out.println(e);
        }
    }
}
