import java.io.*;

class p34 {
	public static void main(String[] args) throws IOException {

		try
		{
			FileInputStream in = new FileInputStream("p33.java");
			FileOutputStream out = new FileOutputStream("output.txt");

			int c = in.read();
			while(c != -1)
			{
				out.write(c);
				c = in.read();
			}
		}
		finally{}

	}
}
