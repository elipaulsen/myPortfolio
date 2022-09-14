public class Timer {
    private long start;
    private long end;

    public void start() {
        start = System.nanoTime();
    }

    public void end() {
        end = System.nanoTime();
    }

    public double elapsedSeconds() {
        return (end - start) / Math.pow(10, 9);
    }
}
