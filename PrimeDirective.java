import java.util.ArrayList;
class PrimeDirective {
  
  public static ArrayList<Integer> findPrimeInArray(int[] numArray) {
    ArrayList<Integer> numArrayList = new ArrayList<>();
    for (int i : numArray) {
      if (i / 1 == i && i / i == 1 && i % 2 != 0 && i % 3 != 0) {
        numArrayList.add(i);
      } 
    }
    return numArrayList;
  }
  
  public static void main(String[] args) {

    int[] numbers = {6, 29, 28, 33, 11, 100, 101, 43, 89};
    System.out.println("The prime numbers in your list are: " + findPrimeInArray(numbers));
  }  

}

// Task: Find a different way to construct the logic of 'findPrimeInArray'
