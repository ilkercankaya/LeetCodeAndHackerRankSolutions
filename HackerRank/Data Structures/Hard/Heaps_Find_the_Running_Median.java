import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {


    public static PriorityQueue<Integer> leftMaxHeap = new PriorityQueue<>(Collections.reverseOrder());
    public static PriorityQueue<Integer> rightMinHeap = new PriorityQueue<>();


    private static final Scanner scanner = new Scanner(System.in);

    public static void addNumber(int x){
        if (leftMaxHeap.size() == 0 || x < leftMaxHeap.peek())
        leftMaxHeap.add(x);
        else
        rightMinHeap.add(x);

    }

    public static void balanceHeaps(){
        PriorityQueue<Integer> bigger = leftMaxHeap.size() > rightMinHeap.size() ? leftMaxHeap : rightMinHeap;

        PriorityQueue<Integer> smaller = leftMaxHeap.size() < rightMinHeap.size() ? leftMaxHeap : rightMinHeap;

        if(bigger.size() - smaller.size() >= 2){
                smaller.add(bigger.poll());
        }
    }

    public static double calculateMedian(){
        if (leftMaxHeap.size() == rightMinHeap.size()){
            return ((double) leftMaxHeap.peek() + rightMinHeap.peek()) / 2;
        } else if (leftMaxHeap.size() > rightMinHeap.size())
            return leftMaxHeap.peek();
            else
            return rightMinHeap.peek();

    }

    public static void runningMedian(int [] array){
         for (int i = 0; i < array.length; i++) {
            addNumber(array[i]);
            balanceHeaps();
            System.out.println(calculateMedian());
        }
    }

    public static void main(String[] args) {
        int n = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        int[] a = new int[n];

        for (int i = 0; i < n; i++) {
            int aItem = scanner.nextInt();
            scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");
            a[i] = aItem;
        }

        runningMedian(a);
        scanner.close();
    }
}
