public class Droid {
    String name;
    int batteryLevel = 100;
  
    public Droid(String droidName) {
      name = droidName;
      batteryLevel = 100;
    }
  
    // This method returns 'null' as the name
    public String toString() {
      return "Hello, I am a droid and my name is: " + name;
    }
  
    public void performTask(String task) {
      System.out.println(name + " is performing task: " + task);
      batteryLevel -= 10;
    }
  
    public static void main(String[] args) {
      Droid codey = new Droid("Codey");
      System.out.println(codey);
      codey.performTask("fighting");
    }
  
  }