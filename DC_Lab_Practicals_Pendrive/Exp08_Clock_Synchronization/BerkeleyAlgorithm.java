import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Scanner;

public class BerkeleyAlgorithm {
    public static void berkeleyAlgo(String serverTime, String time1, String time2) {
        System.out.println("Server Clock = " + serverTime);
        System.out.println("Client Clock1 = " + time1);
        System.out.println("Client Clock2 = " + time2);

        SimpleDateFormat sdf = new SimpleDateFormat("mm:ss");
        sdf.setLenient(false);

        try {
            long s = sdf.parse(serverTime).getTime();
            long t1 = sdf.parse(time1).getTime();
            long t2 = sdf.parse(time2).getTime();

            long st1 = t1 - s;
            long st2 = t2 - s;
            System.out.println("t1 - s = " + st1 / 1000);
            System.out.println("t2 - s = " + st2 / 1000);

            long avg = (st1 + st2) / 2;
            System.out.println("(st1 + st2) / 2 = " + avg / 1000);

            long adjustedServer = s + avg;
            long adjT1 = avg - st1;
            long adjT2 = avg - st2;

            System.out.println("t1 adjustment = " + adjT1 / 1000);
            System.out.println("t2 adjustment = " + adjT2 / 1000);
            System.out.println("Synchronized Server Clock = " +
                    sdf.format(new Date(adjustedServer)));
            System.out.println("Synchronized Client1 Clock = " +
                    sdf.format(new Date(t1 + adjT1)));
            System.out.println("Synchronized Client2 Clock = " +
                    sdf.format(new Date(t2 + adjT2)));
        } catch (Exception e) {
            System.out.println("Invalid time. Enter time in mm:ss format.");
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter Server Time (mm:ss): ");
        String serverTime = scanner.nextLine();
        System.out.print("Enter Client 1 Time (mm:ss): ");
        String time1 = scanner.nextLine();
        System.out.print("Enter Client 2 Time (mm:ss): ");
        String time2 = scanner.nextLine();
        berkeleyAlgo(serverTime, time1, time2);
    }
}
