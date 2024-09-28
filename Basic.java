public class Basic {

	// a program that prints:
	// B a s i c
	// b A s i c
	// b a S i c
	// b a s I c
	// b a s i C
    public static void main(String[] args) {
	String[][] basic = {{"basic"}, {"basic"}, {"basic"}, {"basic"}, {"basic"}};
	for (String i = 0; i < basic.length; i++) {
	    System.out.println(basic[i]);
	}
    }

}
