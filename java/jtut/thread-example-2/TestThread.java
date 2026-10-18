import java.io.*;

class RunnableDemo implements Runnable {
   private Thread t;
   private String threadName;
   
   RunnableDemo( String name) {
      threadName = name;
      System.out.println("Creating " +  threadName );
   }
   
   public void xrun() throws FileNotFoundException, IOException {
	FileInputStream f = new FileInputStream(threadName);
	int x = f.read();
	char c = (char)x;
	while( x != -1 )
	{
		System.out.println(threadName + " " + c);
		x = f.read();
		c = (char)x;
	}
	f.close();
   }
   public void run() {
      System.out.println("Running " +  threadName );
      try {
	xrun();
      } catch (Exception e) {
         System.out.println("Thread " +  threadName + " interrupted. "+ e.toString());
      }
      System.out.println("Thread " +  threadName + " exiting.");
   }
   
   public void start () {
      System.out.println("Starting " +  threadName );
      if (t == null) {
         t = new Thread (this, threadName);
         t.start ();
      }
   }
}

public class TestThread {

   public static void main(String args[]) throws IOException, FileNotFoundException {
      RunnableDemo R1 = new RunnableDemo("a.txt");
      R1.start();
      
      RunnableDemo R2 = new RunnableDemo("b.txt");
      R2.start();
   }   
}
