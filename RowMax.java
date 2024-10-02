public class RowMax {

	public void findMax(int[][] array) {
		for (int i = 0; i < array.length; i++) {
			int max = Integer.MIN_VALUE;
			for (int j = 0; j < array[i].length; j++) {
				if (array[i][j] > max) {
					max = array[i][j];
				}
			}
			System.out.println("The max value in row " + (i + 1) + " is: " + max + "!");
		}
	}

  public static void main(String[] args) {
    int[][] intArray = {
      {5, 12, 9},
      {3, 7, 2},
      {6, 1, 4}
    };
    
    RowMax objOne = new RowMax();
    objOne.findMax(intArray);

  }
}