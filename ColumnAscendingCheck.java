// Write a program that checks if columns in a 2D array are in ascending order

public class ColumnAscendingCheck {

    public void checkColumnAscension(int[][] array) {
      // checks if parameter or array is empty
      if (array == null) {
        System.out.println("Parameter is empty - ending program!");
        return;
      } else if (array.length == 0) {
        System.out.print("Array is empty - ending program!");
        return;
      }
  
      for (int i = 0; i < array[0].length; i++) {
        // initalizes an isAscending variable to be true
        boolean isAscending = true;
        for (int j = 1; j < array.length; j++) {
          // if the current element is less than the previous, isAscending is false, iteration breaks
          if (array[j][i] < array[j - 1][i]) {
            isAscending = false;
            break;
          }
        }
        // different print statements dependent on if isAscending is true or false
        if (isAscending) {
          System.out.println("Column " + (i + 1) + " IS IN ascending order!");
        } else {
          System.out.println("Column " + (i + 1) + " IS NOT ascending order!");
        }
      }
    }
  
    public static void main(String[] args) {
      int[][] intArray = {
        {5, 7, 1},
        {9, 3, 2},
        {12, 6, 4}
          };
  
      ColumnAscendingCheck obj1 = new ColumnAscendingCheck();
      obj1.checkColumnAscension(intArray);
  
    }
  }