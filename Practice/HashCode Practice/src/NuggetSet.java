import java.util.*;

public class NuggetSet<E> implements Set<E> {

    private int count = 0;
    private final List<E>[] buckets;

    public NuggetSet() {
        this(10);
    }

    public NuggetSet(int a) {
        buckets = new List[a];
        for (int i = 0; i < buckets.length; i++)
            buckets[i] = new LinkedList<>();
    }

    @Override
    public int size() {
        return count;
    }

    @Override
    public boolean isEmpty() {
        return count == 0;
    }

    @Override
    public boolean contains(Object o) {
        throw new UnsupportedOperationException();
    }

    @Override
    public Iterator<E> iterator() {
        throw new UnsupportedOperationException();
    }

    @Override
    public Object[] toArray() {
        throw new UnsupportedOperationException();
    }

    @Override
    public <T> T[] toArray(T[] a) {
        throw new UnsupportedOperationException();
    }

    @Override
    public boolean add(E e) {
        int hashCode = e.hashCode();
        int index = Math.abs(hashCode) % buckets.length;
        List<E> bucket = buckets[index];
        for (E elem : bucket) {
            if (elem.equals(e))
                return false;
        }
        bucket.add(e);
        return true;
    }

    @Override
    public boolean remove(Object o) {
        int hashCode = o.hashCode();
        int index = Math.abs(hashCode) % buckets.length;
        List<E> bucket = buckets[index];
        return bucket.remove(o);
    }

    @Override
    public boolean containsAll(Collection<?> c) {
        throw new UnsupportedOperationException();
    }

    @Override
    public boolean addAll(Collection<? extends E> c) {
        throw new UnsupportedOperationException();
    }

    @Override
    public boolean retainAll(Collection<?> c) {
        throw new UnsupportedOperationException();
    }

    @Override
    public boolean removeAll(Collection<?> c) {
        throw new UnsupportedOperationException();
    }

    @Override
    public void clear() {
        count = 0;
        for (int i = 0; i < buckets.length; i++)
            buckets[i] = new LinkedList<>();
    }

    public void debug() {
        int index = 0;
        for (List<E> bucket : buckets) {
            System.out.print(index + " > ");
            int elemCount = 0;
            for (E elem : bucket) {
                elemCount++;

                System.out.print(elem.toString() + " (" + elem.hashCode() + ")");
                if (elemCount <= bucket.size())
                    System.out.print(", ");
            }
            System.out.println();
            index++;
        }
    }

    public void analyze() {
        float numfilled = 0;

        for (List<E> bucket : buckets){
            if(!bucket.isEmpty()){
                numfilled++;
            }
        }
        float pct = (numfilled/buckets.length)*100;
        float avg = 100/ (float) buckets.length;
        if(avg<3 && pct >= 90) {
            System.out.println(buckets.length + ": " + pct + "%  || avg strings per bucket: " + avg);
        }
    }
}
