public class HorseRace {
    public static double calculateExpectedTime(double averageSpeed, int numberOfHurdles) {
        double distance = 4000; // Distance in meters
        double time = 0; // Time in seconds

        // Convert averageSpeed from km/hr to m/s
        double averageSpeedMPS = averageSpeed * (1000.0 / 3600.0);

        // Calculate time taken to reach average speed
        double timeToReachAverageSpeed = (averageSpeedMPS / 2) / (distance / 2);
        time += timeToReachAverageSpeed;

        // Calculate time taken to cross each hurdle
        for (int i = 0; i < numberOfHurdles; i++) {
            double hurdleSpeedReductionMPS = (20.0 * 1000.0) / 3600.0; // Speed reduction in m/s
            double hurdleTime = 15.0 + (distance / (averageSpeedMPS - hurdleSpeedReductionMPS));
            time += hurdleTime;
        }

        // Calculate time taken for the last 500m with increased speed
        double increasedSpeedMPS = (averageSpeedMPS + (10.0 * 1000.0) / 3600.0);
        double timeForLast500m = (500.0 / increasedSpeedMPS);
        time += timeForLast500m;

        return time;
    }

    public static void main(String[] args) {
        double averageSpeed = 40; // Average speed in km/hr
        int numberOfHurdles = 10;

        double expectedTime = calculateExpectedTime(averageSpeed, numberOfHurdles);
        System.out.println("Expected time to complete the race: " + expectedTime + " seconds");
    }
}
